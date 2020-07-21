# Grubhub Menu Webscraper
### This program allows you to scrape the menu of a restaurant from grubhub given a valid url

### Works using Python 3

### Dependencies:
* #### Selenium (needed to get javascript generated HTML)
  * Python Installation:
    * run `pip install selenium`
  * Chrome Driver Installation:
    * Mac OS X Instructions: http://jonathansoma.com/lede/foundations-2017/classes/more-scraping/selenium/
    * Driver Download: https://chromedriver.chromium.org/downloads
* #### BeautifulSoup:
  * run `pip install beautifulsoup4`

### Intructions:
1. Install dependencies listed above
2. Clone project (make sure that both the PY file and the JSON file are included)
3. Run the Python script with Python 3
4. You should be met with the text 'Grubhub Link?', this is where you paste the url
    * An example of a valid url is: https://www.grubhub.com/restaurant/insomnia-cookies-76-pearl-st-new-york/295836 (this is also the location that was scraped for the example data in the 'data.json' file of this repository)

### Troubleshooting:
1. The JSON file is empty/missing options or information
    * The PY script has `time.sleep()` statements to account for the page loading. It's possible that the page wasn't completely loaded before the HTML code was sent to Python. Increase the time of the sleep statements to account for slower internet.
2. File Not Found Error
    * More than likely, the file 'data.json' is missing from the directory that the Python script is in.
3. Chrome driver errors
    * Check that the driver was installed to the correct location. Also, make sure the driver is for the same version of chrome that you have installed
