import os
from pathlib import Path
from dotenv import load_dotenv

### Load environment variables from .env file
load_dotenv()
STRAVA_CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
STRAVA_REFRESH_TOKEN = os.getenv("STRAVA_REFRESH_TOKEN")
STRAVA_ACCESS_TOKEN = os.getenv("STRAVA_ACCESS_TOKEN")
STRAVA_USER_AUTHORIZATION_CODE = os.getenv("STRAVA_USER_AUTHORIZATION_CODE")

### Constants
BASE_URL = 'https://www.strava.com/api/v3'
TOKEN_URL = 'https://www.strava.com/oauth/token'

# Token store
TOKEN_FILE = Path("./tmp/strava_token.json")

# Strava data store
DATA_PATH = f"{os.getenv("DATA_DIR", "./data")}/"  # Default to ./data/ if not set
os.makedirs(DATA_PATH, exist_ok=True)

STREAM_PATH = f"{DATA_PATH}{os.getenv('STREAM_DIR_NAME', 'streams')}/"
os.makedirs(STREAM_PATH, exist_ok=True)

ATHLETE_DATA = Path(f"{DATA_PATH}{os.getenv('ATHLETE_DETAILS_FILE_NAME', 'athlete_details')}.json")
ATHLETE_ACTIVITIES = Path(f"{DATA_PATH}{os.getenv('ATHLETE_ACTIVITIES_FILE_NAME', 'athlete_activities')}.json")