import requests

payload = {
    "name": "Alanto",
    "destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"],
    "business": True,
    "distances": [
        "Munich - Munich: 0",
        "Munich - Kinganru: 3",
        "Munich - Facenianorth: 7",
        "Munich - SantaTiesrie: 4",
        "Munich - Mitling: 1",
        "Kinganru - Facenianorth: 2",
        "Kinganru - SantaTiesrie: 1",
        "Kinganru - Mitling: 1",
        "Facenianorth - SantaTiesrie: 5",
        "Facenianorth - Mitling:  3",
        "SantaTiesrie - Mitling: 2",
    ],
}

res = requests.post("http://127.0.0.1:8001/calculate", json=payload)
if res.status_code == 404:
    print(f"Calculate - {res.status_code} - route not found")
else:
    print(f"Calculate - {res.status_code} - {res.json()}")

res = requests.get("http://127.0.0.1:8001/business-trips")
if res.status_code == 404:
    print(f"Business trips - {res.status_code} - route not found")
else:
    print(f"Business trips - {res.status_code} - {res.json()}")
