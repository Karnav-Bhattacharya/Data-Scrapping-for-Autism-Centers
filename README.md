# Data-Scrapping-for-Autism-Centers

This project is a web scraper designed to collect data about autism centers in India from the [Autism Connect directory](https://www.autismconnect.com/directory?country=India&state_name=&city=&category_id=64). The script extracts information such as the center's name, location, address, phone number, and email address, and saves it into a CSV file.

## Requirements

To run this project, you will need the following:

- Python 3.x
- Google Chrome
- ChromeDriver (ensure that the ChromeDriver version matches your installed version of Chrome)

## Installation

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/Karnav-Bhattacharya/Data-Scrapping-for-Autism-Centers.git
    cd autism-centers-scraper
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium beautifulsoup4 pandas
    ```

3. Download and install [ChromeDriver](https://sites.google.com/chromium.org/driver/), and ensure it is in your system PATH or specify the path directly in the script.

## Usage

1. Update the path to `chromedriver.exe` in the script if necessary:
    ```python
    service = Service(r'C:\Path\To\chromedriver.exe')
    ```

2. Run the script:
    ```sh
    python autism_centers_scraper.py
    ```

3. The script will scrape the data and save it to a CSV file named `Autism_centers.csv` in the project directory.

## Explanation

The script performs the following steps:

1. Navigates to the specified URL using Selenium.
2. Selects the option to show all results on one page.
3. Parses the page source with BeautifulSoup to extract the relevant data.
4. Collects the data into lists and processes them to handle multiple phone numbers and email addresses.
5. Saves the data into a CSV file using Pandas.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
