import logging
from pdb import Restart
import re
from typing import Dict, List
from unittest.mock import NonCallableMagicMock
from bs4 import BeautifulSoup
import siteScripts.timeout.urls as urls
import siteScripts.settings.timeout as settings
from models.landmark import Landmark
from webscraper.siteScripts.timeout.urls import TIMEOUT_MELB_BEST_RESTAURANTS_LIST, TIMEOUT_MELB_RESTAURANTS

# LOGGER
logger = logging.getLogger(__name__)


def getBestRestaurants(driver):
    """Scrapes Timeout article 'The Best Restaurants in Melbourne' and returns array of first 50 restaurant names and the urls to articles for restaurants."""

    restaurantURLS = []

    html = getPageHTML(driver, TIMEOUT_MELB_BEST_RESTAURANTS_LIST)

    # Get list of article titles
    articleContainer = html.find_all("div", class_="_zoneFirst_abr0c_5")[0]
    articleTitles = articleContainer.find_all("h3")

    # Strip titles of ranking and split name by whitespace
    for article in articleTitles:
        text = article.text
        text = re.sub("[^a-zA-Z0-9\s]+", "", text)
        # Remove Timeout ranking from title to get restaurant name
        nameArray = text.lower().split()[1:]
        # Construct URL from name
        restaurantName = ' '.join(nameArray).title()
        url = getURLFromName(TIMEOUT_MELB_RESTAURANTS, nameArray)
        restaurantURLS.append({'name': restaurantName, 'url': url})

    logger.info("Number of articles gathered %d" % len(restaurantURLS))

    return restaurantURLS


def articleToLandmark(driver, restaurant: Dict[str, str]):
    """Takes a restaurant url and returns timeout article contents"""

    # TODO Refactor out
    html = getPageHTML(driver, restaurant["url"])

    # Get Article from page
    article = html.find("article", class_="listing")
    if article == None:
        return None

    # Get Location
    location = article.find("span", class_="flag--location")
    if location == None:
        location = "Could not get location from article"
    else:
        location = re.sub("\n+\s{2,}", "", location.text.strip())

    #  Get Images
    images = []
    imageHTMLTags = article.find_all("img")
    for img in imageHTMLTags:
        images.append(img.get("data-srcset"))

    # Get Rating
    articleRating = article.find("meta", itemprop="ratingValue")
    if articleRating == None:
        landmarkRating = "Could not get rating from article"
    else:
        landmarkRating = articleRating.get("content")

    # Get Description
    articleDescription = article.find("div", itemprop="reviewBody")
    if articleDescription == None:
        landmarkDescription = "Could not get description from article"
    else:
        landmarkDescription = articleDescription.text

    # Get Tags
    landmarkTags = []
    articleTags = [article.find("span", class_="flag--primary_category"),
                   article.find("span", class_="flag--sub_category")]
    for tag in articleTags:
        if tag != None:
            landmarkTags.append(tag.text)

    return Landmark("Restaurant", {'lat': 0.0, 'lng': 0.0}, location, restaurant["name"], landmarkRating, images, landmarkDescription, landmarkTags, {"outlet": "Timeout", "url": restaurant["url"]})


def getPageHTML(driver, url):
    """Gets html content from page and return through BS4 parser"""
    driver.get(url)
    return BeautifulSoup(driver.page_source, "html.parser")


def getCoords():
    """Takes landmark name and suburb and returns coordinates"""


def getURLFromName(base: str, name: List[str]):
    """Takes string array representing restaurant name and returns timeout url"""
    # Create Timeout URL
    return base + '-'.join(name)

# Cafes
# Bars
# Events/Things-to-do


def scrape(driver):

    landmarks = []

    if(settings.articles['BEST_RESTAURANTS']):
        restaurants = getBestRestaurants(driver)

        for restaurant in restaurants:
            # get landmark from article
            restaurantLandmark = articleToLandmark(driver, restaurant)
            if restaurantLandmark == None:
                pass
            else:
                restaurantLandmark.printLandmark()
                landmarks.append(restaurantLandmark)
