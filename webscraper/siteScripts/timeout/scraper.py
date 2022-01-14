
import requests
import logging
import re
from bs4 import BeautifulSoup
import siteScripts.timeout.urls as urls
import siteScripts.settings.timeout as settings
from models.landmark import Landmark
from webscraper.siteScripts.timeout.urls import TIMEOUT_MELB_RESTAURANTS

# LOGGER
logger = logging.getLogger(__name__)


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
        text = re.sub("[^a-zA-Z0-9\s]+", "", text)
        restaurantNames.append(text.split()[1:])

    logger.info("Number of articles gathered %d" % len(restaurantNames))

    return restaurantNames


def getRestaurantArticle(name):
    """Takes a restaurant url and returns timeout article contents"""

    url = getURLFromName(name)
    print(url)
    # Go to URL
    page = None
    while page == None:
        page = requests.get(url)
    # TODO Error Handling
    # Pass to Parser
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find("article", class_="listing")

    # Get Location
    location = content.find("span", class_="flag--location")
    if location == None:
        location = "Could not get location from article"
    else:
        location = re.sub("\n+\s{2,}", "", location.text.strip())

    # Get Images

    # Get Rating
    rating = content.find("meta", itemprop="ratingValue")
    if rating == None:
        rating = "Could not get rating from article"

    # Get Description
    description = content.find("div", itemprop="reviewBody").text
    if description == None:
        description = "Could not get description from article"

    # Get Tags
    tags = [content.find("span", class_="flag--primary_category").text,
            content.find("span", class_="flag--sub_category").text]

    return Landmark("Restaurant", {'lat': 0.0, 'lng': 0.0}, location, ' '.join(name), rating, [], description, tags, "Timeout")


def getCoords():
    """Takes landmark name and suburb and returns coordinates"""


def parseToLandmark():
    """Takes contents of timeout article and returns Landmark object"""


def getURLFromName(name):
    """Takes restaurant name array and returns url"""
    # Create Timeout URL
    return TIMEOUT_MELB_RESTAURANTS + '-'.join(name)

# Cafes
# Bars
# Events/Things-to-do


def scrape():

    landmarks = []

    if(settings.articles['BEST_RESTAURANTS']):
        names = getBestRestaurantsNames()

        for name in names:
            article = getRestaurantArticle(name)
            article.printLandmark()
            landmarks.append(article)
