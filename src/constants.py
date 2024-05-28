from os import environ
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = environ["API_KEY"]
API_SECRET = environ["API_SECRET"]
ADMIN_TOKEN = environ["ADMIN_TOKEN"]
STORE_URL = environ["STORE_URL"]

headers = {"Content-Type": "application/json", "X-Shopify-Access-Token": ADMIN_TOKEN}
