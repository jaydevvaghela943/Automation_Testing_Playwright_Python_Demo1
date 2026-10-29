import json


with open("config/settings.json") as f:

    settings = json.load(f)

BASE_URL = settings["base_url"]

BROWSER = settings["browser"]

HEADLESS = settings["headless"]

TIMEOUT = settings["timeout"]