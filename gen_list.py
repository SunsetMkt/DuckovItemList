import csv
import json

i18nTable = {}

with open("ChineseSimplified.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    print(fieldnames)
    for row in reader:
        i18nTable[row["key"]] = row["value"]


def getI18n(key):
    return i18nTable.get(key, key).replace("\\?", "?")


with open("ItemAssetsCollection.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    entries = data["m_Structure"]["entries"]

plainList = ""

templateLine = "* `displayName` (`id`): `description` (`name`, `displayQuality`, `quality`, `priceEach`, `maxStackCount`)\n"
plainList += templateLine

for i in entries:
    metaData = i["metaData"]
    line = (
        f"* {getI18n(metaData['displayName'])} ({metaData['id']}): {getI18n(metaData['description'])}"
        + f" ({metaData['name']}, {metaData['displayQuality']}, {metaData['quality']}, {metaData['priceEach']}, {metaData['maxStackCount']})"
        + "\n"
    )
    plainList += line

with open("list.txt", "w", encoding="utf-8") as f:
    f.write(plainList)
