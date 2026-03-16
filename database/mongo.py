from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# get URI
MONGO_URI = os.getenv("MONGO_URI")

# create client
client = MongoClient(MONGO_URI)

# select database
db = client["health_monitoring_db"]

# collections
patient_groups = db["patient_groups"]
thresholds = db["thresholds"]
escalation_paths = db["escalation_paths"]
compliance = db["compliance"]

# test connection
try:
    client.admin.command("ping")
    print("MongoDB connection successful")
except Exception as e:
    print("MongoDB connection failed:", e)