import pyodbc
import logging
from decouple import config

from webscraper.models.landmark import Landmark



# LOGGER
logger = logging.getLogger(__name__)

# CONSTANTS
SERVER = config('SERVER')
DATABASE = config('DATABASE')
USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

def connect():
    """ Connect to SQL Database"""
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD)
    cursor = cnxn.cursor()


def insertLandmark(landmark: Landmark, table: str, cursor):
    """Insert Landmark entity into SQL table """
    
