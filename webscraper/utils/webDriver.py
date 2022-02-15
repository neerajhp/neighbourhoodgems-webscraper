from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setupWebDriver():
    chromeOptions = Options()
    # chromeOptions.add_argument("--headless")

    return webdriver.Chrome(options=chromeOptions)
