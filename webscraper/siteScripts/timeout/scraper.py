
import requests
import logging
import re
from typing import Dict, List
from bs4 import BeautifulSoup
import siteScripts.timeout.urls as urls
import siteScripts.settings.timeout as settings
from models.landmark import Landmark
from webscraper.siteScripts.timeout.urls import TIMEOUT_MELB_RESTAURANTS

# LOGGER
logger = logging.getLogger(__name__)


def getBestRestaurants():
    """Scrapes Timeout article 'The Best Restaurants in Melbourne' and returns array of first 50 restaurant names and the urls to articles for restaurants."""

    restaurantURLS = []

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
        # Remove Timeout ranking from title to get restaurant name
        nameArray = text.lower().split()[1:]
        # Construct URL from name
        restaurantName = ' '.join(nameArray).title()
        url = getURLFromName(TIMEOUT_MELB_RESTAURANTS, nameArray)
        restaurantURLS.append({'name': restaurantName, 'url': url})

    logger.info("Number of articles gathered %d" % len(restaurantURLS))

    return restaurantURLS


def articleToLandmark(restaurant: Dict[str, str]):
    """Takes a restaurant url and returns timeout article contents"""

    # TODO Refactor out
    html = getPageHTML(restaurant["url"])

    # Get Article from page
    article = html.find("article", class_="listing")

    # Get Location
    location = article.find("span", class_="flag--location")
    if location == None:
        location = "Could not get location from article"
    else:
        location = re.sub("\n+\s{2,}", "", location.text.strip())

    #  Get Images
    images = []
    imageTags = article.find_all("img")
    for img in imageTags:
        images.append(img.get("data-srcset"))

    # Get Rating
    rating = article.find("meta", itemprop="ratingValue")
    if rating == None:
        rating = "Could not get rating from article"

    # Get Description
    description = article.find("div", itemprop="reviewBody").text
    if description == None:
        description = "Could not get description from article"

    # Get Tags
    tags = [article.find("span", class_="flag--primary_category").text,
            article.find("span", class_="flag--sub_category").text]

    return Landmark("Restaurant", {'lat': 0.0, 'lng': 0.0}, location, restaurant["name"], rating, images, description, tags, {"outlet": "Timeout", "url": restaurant["url"]})


def getPageHTML(url: str):
    """Gets html content from page and return through BS4 parser"""
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


def getCoords():
    """Takes landmark name and suburb and returns coordinates"""


def getURLFromName(base: str, name: List[str]):
    """Takes string array representing restaurant name and returns timeout url"""
    # Create Timeout URL
    return base + '-'.join(name)

# Cafes
# Bars
# Events/Things-to-do


def scrape():

    landmarks = []

    if(settings.articles['BEST_RESTAURANTS']):
        restaurants = getBestRestaurants()

        for restaurant in restaurants:
            # get landmark from article
            restaurantLandmark = articleToLandmark(restaurant)
            restaurantLandmark.printLandmark()
            landmarks.append(restaurantLandmark)
