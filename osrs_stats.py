import urllib, json, pprint

url = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=556"

response = urllib.urlopen(url)
data = json.loads(response.read())

# pprint.pprint(data)

# print(data['item']['name'])
# print("Description: " + data['item']['description'])
# print("Price: " + str(data['item']['current']['price']))

ign = "Filipino"
url = "http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=" + urllib.quote_plus(ign)

response1 = urllib.urlopen(url)
data1 = response1.read()
# print(data1.strip().split())

skills = ["Overall", "Attack", "Defence", "Strength", "Hitpoints", "Ranged", "Prayer", "Magic", "Cooking",
            "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining",
            "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecraft", "Hunter", "Construction"]

data = [x for x in [data1.strip().split()[i].split(',') + [i] for i in range(len(skills))]]
# print(data)

print("Username: " + ign)
for i in range(len(skills)):
    print(skills[i] + ": " + data[i][1])

# Suggestions:
# OSRS STAT ANALYSIS TOOL
# Compare players
# %/exp til next/X level
#  - level/exp goals


# Sort skills from highest to lowest
# Sorts by level, then exp, then alphabetically
print("\nSkills high to low")
htl = sorted(data, key=lambda x: (-int(x[1]), -int(x[2]), skills[x[3]]))
for i in htl:
    print(skills[i[3]] + ": " + i[1])
