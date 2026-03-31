import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "../model/xgb_pipeline.pkl")
)

print("📦 MODEL PATH:", MODEL_PATH)
print("📂 EXISTS:", os.path.exists(MODEL_PATH))

MODEL_VERSION = "1.0.0"
APP_NAME = "Clinical AI Prediction API"