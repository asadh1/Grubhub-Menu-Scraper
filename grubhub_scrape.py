from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import json


def get_item(browser, id):
    """ given an id, scrape a menu item and all of its options """
    button = browser.find_element_by_id(id)
    browser.execute_script("arguments[0].click();", button)
    time.sleep(1)

    innerHTML = browser.page_source
    html = BeautifulSoup(innerHTML, 'html.parser')

    _options = {}
    options = html.find_all('div', class_='menuItemModal-options') # menuItemModal-choice-option-description
    for option in options:
        name = option.find(class_='menuItemModal-choice-name').text
        choices = option.find_all('span', class_='menuItemModal-choice-option-description')
        if ' + ' in choices[0].text:
            _choices = {choice.text.split(' + ')[0]:choice.text.split(' + ')[1] for choice in choices}
        else:
            _choices = [choice.text for choice in choices]
        _options[name] = _choices
    return _options

def get_menu(url):
    """ given a valid grubhub url, scrape the menu of a restaurant """
    print('Running...')
    chrome_options = Options()
    # To disable headless mode (for debugging or troubleshooting), comment out the following line:
    chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    time.sleep(10)
    innerHTML = browser.page_source

    html = BeautifulSoup(innerHTML, 'html.parser')

    menu = html.find(class_="menuSectionsContainer");
    if menu is None:
        print('menu fail')
        get_menu(url)
        return
    # Categories
    cats = menu.find_all('ghs-restaurant-menu-section')
    cats = cats[1:]

    cat_titles = [cat.find('h3', class_='menuSection-title').text for cat in cats]
    cat_items = [[itm.text for itm in cat.find_all('a', class_='menuItem-name')] for cat in cats]
    prices = [[p.text for p in cat.find_all('span', class_='menuItem-displayPrice')] for cat in cats]

    ids = []
    for cat in cats:
        cat_ids = []
        items = cat.find_all('div', class_='menuItem-inner')
        for item in items:
            cat_ids.append(item.get('id'))
        ids.append(cat_ids)

    full_menu = {}
    for ind, title in enumerate(cat_titles):
        all_items = []
        for ind2, itm_name in enumerate(cat_items[ind]):
            item = {}
            item['name'] = itm_name
            item['price'] = prices[ind][ind2]
            item['options'] = get_item(browser, ids[ind][ind2])
            all_items.append(item)
        full_menu[title] = all_items
    path = '/'.join(os.path.realpath(__file__).split('/')[:-1])
    with open(f'{path}/data.json', 'w') as f:
        json.dump(full_menu, f, indent=4)
    print('[Finished]')
get_menu(input('Grubhub Link?  '))
#example link: 'https://www.grubhub.com/restaurant/insomnia-cookies-76-pearl-st-new-york/295836'
