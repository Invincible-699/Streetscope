import json  # lets python understand JSON files

# Step 1: open your trends.json file
with open("data/trends.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # Step 2: read the contents

# Step 3: print the title
print("🔥 StreetScope Trends 🔥")

# Step 4: go through every trend and show it
for trend in data["trends"]:
    print(f"- {trend['name']} ({trend['category']}) → Popularity: {trend['popularity']}")

