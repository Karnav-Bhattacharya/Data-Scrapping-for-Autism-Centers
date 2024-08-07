from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.autismconnect.com/directory?country=India&state_name=&city=&category_id=64"
service = Service(r'C:\Program Files\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    driver.get(url)

    element_select_all = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "limit"))
    )
    print("All- option found")
    All_select = Select(element_select_all)
    All_select.select_by_visible_text("All")
    print("All- option selected")

    time.sleep(5)  # Wait for the page to load

    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")

    # Initialize lists to store data
    autism_center_name = []
    all_locations = []
    all_addresses = []
    all_phno = []
    all_emails = []

    list_of_center = soup.find_all(class_='mt-25 mb-20')
    for center in list_of_center:
        autism_center_name.append(center.text.strip())

    print(f"Found {len(list_of_center)} centers")
    print("List of centers created successfully")

    center_containers = soup.find_all("div", class_="search-details")
    for container in center_containers:
        all_p_tags = container.find_all("p")
        location = all_p_tags[0].get_text(strip=True) if len(all_p_tags) > 0 else None
        all_locations.append(location)

        address = all_p_tags[1].get_text(strip=True) if len(all_p_tags) > 1 else None
        all_addresses.append(address)

        phone_numbers = [a_tag.get_text(strip=True) for a_tag in container.find_all("a", href=True) if a_tag['href'].startswith("tel:")]
        all_phno.append(phone_numbers if phone_numbers else None)

        emails = [a_tag.get_text(strip=True) for a_tag in container.find_all("a", href=True) if a_tag['href'].startswith("mailto:")]
        all_emails.append(emails if emails else None)

    print(f"Found {len(all_locations)} locations")
    print("List of locations created successfully")
    print(f"Found {len(all_addresses)} addresses")
    print("List of addresses created successfully")
    print(f"Found {len(all_phno)} phone numbers")
    print("List of phone numbers created successfully")
    print(f"Found {len(all_emails)} email addresses")
    print("List of email addresses created successfully")

finally:
    driver.quit() #This is most important here.

# Processing lists for DataFrame creation
def process_list(lst):
    processed_list = []
    for item in lst:
        if isinstance(item, list):
            if len(item) == 0:
                processed_list.append(None)
            elif len(item) == 1:
                processed_list.append(item[0])
            else:
                processed_list.append(','.join(map(str, item)))
        else:
            processed_list.append(item)
    return processed_list

data = {
    'Center Name': process_list(autism_center_name),
    'Location': process_list(all_locations),
    'Address': process_list(all_addresses),
    'Phone Numbers': process_list(all_phno),
    'Email Address': process_list(all_emails)
}

df = pd.DataFrame(data)
df.to_csv('Autism_centers.csv', index=False)
print(df)
