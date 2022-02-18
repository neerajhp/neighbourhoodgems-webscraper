
import siteScripts.timeout.scraper as timeoutScraper
import logging
from decouple import config

from webscraper.utils.csv import saveLandmarksCSV


def main():
    # File to save landmarks
    f = "landmarks.csv"

    # Scrapers
    timeOutLandmarks = timeoutScraper.scrape()

    # Save Data
    saveLandmarksCSV(timeOutLandmarks, f)

    #Loop through entries in CSV
    #Insert entry into db


if __name__ == '__main__':
    
    # Configure logging
    logging.config.fileConfig(fname=config('LOGGING_CONFIG'),
                              disable_existing_loggers=False)
    logger = logging.getLogger(__name__)

    # Connect to DB

    # Start
    logger.info("Let's Begin")
    main()
