from webbrowser import Chrome
import siteScripts.timeout.scraper as timeoutScraper
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setupWebDriver():
    chromeOptions = Options()
    # chromeOptions.add_argument("--headless")

    return webdriver.Chrome(options=chromeOptions)


def main():
    driver = setupWebDriver()
    timeoutScraper.scrape(driver)
    driver.quit()


if __name__ == '__main__':
    logging.config.fileConfig(fname="./logs/logging.conf",
                              disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    logger.info("Let's Begin")

    main()
