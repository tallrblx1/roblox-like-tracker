import urllib.request
import json

UNIVERSE_ID = 10769008061
url = f"https://games.roblox.com/v1/games/votes?universeIds={UNIVERSE_ID}"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        # The API returns a list under 'data', we want the upVotes of the first item
        upvotes = data['data'][0]['upVotes']
        
        output = {"likes": upvotes}
        with open("likes.json", "w") as f:
            json.dump(output, f)
        print(f"Successfully updated likes to: {upvotes}")
except Exception as e:
    print(f"Failed to fetch likes: {e}")
