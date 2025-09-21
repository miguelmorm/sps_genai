
import requests

# Base URL for local FastAPI server
BASE = "http://127.0.0.1:8000"

# Test the /similarity/ endpoint with two input texts
resp_sim = requests.post(f"{BASE}/similarity/", json={
    "text1": "king",
    "text2": "queen"
})
print("Similarity Response:", resp_sim.json())

# Test the /entities/ endpoint with one input text
resp_ent = requests.post(f"{BASE}/entities/", json={
    "text": "Barack Obama was born in Hawaii and served as President of the United States."
})
print("Entities Response:", resp_ent.json())
