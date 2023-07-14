# TwitterScraper
 This script allows you to scrape data from a Twitter profile using Selenium WebDriver and BeautifulSoup. It retrieves information such as the user's biography, follower count, following count, and likes count. The script utilizes the Chrome browser and requires users to provide their Chrome profile directory path to access their logged-in session on Twitter.

Technology Used:

Python: The programming language used to write the script.
Selenium: A Python library used to automate browser actions and interact with web elements.
BeautifulSoup: A Python library used for web scraping and parsing HTML content.
Instructions:
To use this scraper, please follow these steps:

Install the required dependencies: Selenium and BeautifulSoup.
Provide the path to your Chrome profile directory in the script's chrome_options.add_argument("user-data-dir=/path/to/your/chrome/profile") line.
Run the script and enter the desired Twitter username.
The script will retrieve the user's biography, follower count, following count, and likes count.
Note:

Ensure that you have the correct version of the ChromeDriver executable that matches your Chrome browser version.
Make sure you have the necessary permissions to access your Chrome profile directory.
