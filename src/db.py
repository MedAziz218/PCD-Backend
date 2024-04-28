from config import mongo_uri
import mongoengine as mg
from models import PowerConsumptionLog
mongo_connection = None
try :
    print("[app] Attempting to connecting to db")
    mg.connect("energy-sense", host=mongo_uri)
    mongo_connection = mg.get_connection("default")
    print("[app] pinging database")
    PowerConsumptionLog.objects().count()
    print("[app] Successfully connected to MongoDB database")
except Exception :
    print("[app] Error: Failed to connect to MongoDB. Check your internet connection or try again later.")
    quit()

