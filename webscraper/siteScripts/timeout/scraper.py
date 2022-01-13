import requests
from bs4 import BeautifulSoup
import siteScripts.timeout.urls as urls
from models.landmark import Landmark
import logging

# Get logger
logger = logging.getLogger(__name__)

# Get All
# Restaurants


def getBestRestaurantsNames():
    """Scrapes Timeout article The Best Restaurants in Melbourne' and returns list of names of first 50 results.
        Names are split by whitespace and are stored as string list. """

    restaurantNames = []

    # Go to URL
    page = requests.get(urls.TIMEOUT_MELB_BEST_RESTAURANTS_LIST)
    # Pass to Parser
    soup = BeautifulSoup(page.content, "html.parser")

    # Get list of article titles
    articleContainer = soup.find_all("div", class_="_zoneFirst_abr0c_5")[0]
    articleTitles = articleContainer.find_all("h3")

    # Strip titles of ranking and split name by whitespace
    for article in articleTitles:
        text = article.text
        restaurantNames.append(text.split()[1:])

    logger.info("Number of articles gathered %d" % len(restaurantNames))

    return restaurantNames


def getRestaurantArticle():
    """Takes a restaurant name and returns article contents"""


def parseToLandmark():
    """Takes contents of article and returns Landmark object"""


# Cafes
# Bars
# Events/Things-to-do
def scrape():
    getBestRestaurantsNames()
