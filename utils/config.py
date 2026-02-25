from dotenv import load_dotenv
import os
import joblib


load_dotenv(override=True)

# .env variables
APP_NAME = os.getenv('APP_NAME')
VERSION = os.getenv('VERSION')

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_FOLDER_PATH = os.path.join(BASE_DIR, "Models")

# Models
preprocessor = joblib.load(os.path.join(MODELS_FOLDER_PATH, 'preprocessor.pkl'))
xgboost_model = joblib.load(os.path.join(MODELS_FOLDER_PATH, 'xgb_model.pkl'))
best_threshold = 0.8966
