import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Handle SSL/TLS for Mongo just like app.py
if MONGO_URI:
    client = MongoClient(
        MONGO_URI,
        server_api=ServerApi('1'),
        connect=False,
        tlsCAFile=certifi.where()
    )
    
    # Extract DB name logic from app.py
    db_name = "voice_agent_db"
    if "/" in MONGO_URI.split("@")[-1]:
         extracted = MONGO_URI.split("@")[-1].split("/")[1].split("?")[0]
         if extracted: db_name = extracted
         
    db = client.get_database(db_name)
    
    print(f"Connected to DB: {db_name}")
    
    forms = list(db.form_builders.find())
    print(f"Found {len(forms)} forms.")
    
    for f in forms:
        print(f"\nApp: {f.get('app_name')}")
        print(f"ID: {f.get('_id')}")
        print("Fields:")
        for field in f.get('fields', []):
            print(f"  - Label: '{field.get('label')}' | Name: '{field.get('name')}' | Type: '{field.get('type')}'")
        print("-" * 30)

else:
    print("MONGO_URI not found in .env")
