import urllib.request
import json

# Using the direct path endpoint that works cleanly
UNIVERSE_ID = 10769008061
url = f"https://games.roblox.com/v1/games/{UNIVERSE_ID}/votes"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        upvotes = data['upVotes']
        
        output = {"likes": upvotes}
        with open("likes.json", "w") as f:
            json.dump(output, f)
        print(f"Successfully updated likes to: {upvotes}")
except Exception as e:
    print(f"Failed to fetch likes: {e}")
