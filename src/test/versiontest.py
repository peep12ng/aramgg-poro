import poro
from constant import MATCH_ID

m = poro.Match("KR", id=MATCH_ID)
season = m.version.split(".")[0]
count = m.version.split(".")[1]
version = f"{season}.{count}.1"

# print(poro.Champions(version).champions)
# print(poro.Items(version).items)
# print(poro.Perks(version).perks)
# print(poro.Spells(version).spells)
# pi = poro.ProfileIcons(version)

print(poro.PerkIcons("13.10.1").icons)