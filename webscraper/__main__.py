
import siteScripts.timeout.scraper as timeoutScraper
import logging
from webscraper.models.landmark import Landmark

from webscraper.services.csv import saveLandmarksCSV


def main():
    # File to save landmarks
    f = "landmarks.csv"

    # Scrapers
    timeOutLandmarks = timeoutScraper.scrape()

    # Save Data
    saveLandmarksCSV(timeOutLandmarks, f)


if __name__ == '__main__':
    logging.config.fileConfig(fname="./logs/logging.conf",
                              disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    logger.info("Let's Begin")

    main()
