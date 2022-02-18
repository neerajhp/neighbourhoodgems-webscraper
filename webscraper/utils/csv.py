import csv
import logging
from typing import List
from webscraper.models.landmark import Landmark


# LOGGER
logger = logging.getLogger(__name__)


def checkFile(filename: str):

    # if .csv file doesn't exist, create one
    # try to read from desired file, to check if one exists
    try:
        with open(filename, 'r', newline='') as csvfile:
            logger.info("%s exists" % filename)
    # if desired file doesn't exist, create it with the write ('w') or
    # append 'a' mode
    except:
        with open(filename, 'a', newline='') as csvfile:
            logger.info("%s file created" % filename)


def checkHeaders(filename, fields):
    """Check if header exists in csv file object"""

    # if .csv file doesn't contain Headers, populate it with Headers
    # read first row in file, to check if some Headers exists
    with open(filename, 'r') as csvfile:
        try:
            reader = csv.reader(csvfile)
            row1 = next(reader)
            logger.info("Headers Exist")
            logger.info(row1)
    # if no Headers exists, create Headers with the help of the
    # previously declared and initialized fields array
        except:
            with open(filename, 'w', encoding='UTF8', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                logger.info("Writing Headers")


def saveLandmarksCSV(landmarks: List[Landmark], filename: str):
    """Takes an array of landmarks and saves to specified CSV file"""

    # Check if file exists
    checkFile(filename)

    # Check if header exists else
    header = ['Type', 'Name', 'Coordinates', 'Location',
              'Rating', 'Images', 'Tags', 'Source', 'Description']
    checkHeaders(filename, header)

    # Write to file
    with open(filename, 'a', encoding='UTF8', newline='') as f:

        writer = csv.writer(f)

        for landmark in landmarks:
            writer.writerow([landmark.type, landmark.name, landmark.coords, landmark.location,
                            landmark.rating, landmark.image, landmark.tags, landmark.source, landmark.description])
