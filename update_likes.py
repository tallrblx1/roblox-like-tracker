import urllib.request
import json

# Define your games with their acronyms and Universe IDs
GAMES = {
    "MTL": 10769008061,
    "MWT": 6529917434
}

output_data = {}

for key, universe_id in GAMES.items():
    url = f"https://games.roblox.com/v1/games/votes?universeIds={universe_id}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            upvotes = data['data'][0]['upVotes']
            output_data[key] = upvotes
            print(f"Successfully fetched {key} ({universe_id}) likes: {upvotes}")
    except Exception as e:
        print(f"Failed to fetch {key}: {e}")
        output_data[key] = 0

# Save both counts to likes.json
with open("likes.json", "w") as f:
    json.dump(output_data, f)
