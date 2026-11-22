import json

print("-----------Python and JSON-----------")

asset = {
    "asset_number": "PUMP001",
    "DESCRIPTION": "Water Pump",
    "age": 8,
    "status": "OPERATING",
}

json_date = json.dumps(asset, indent=4)
print(json_date)

with open("asset.json", "w") as file:
    json.dump(asset, file, indent=4)

with open("asset.json", "r") as file:
    data = json.load(file)
    print(data)

print("---------End----------")

print("---------Assignment Start----------")
import json

assets = [
    {
        "assetnum": "PUMP1001",
        "description": "Water Pump",
        "age": 12,
        "status": "OPERATING"
    },
    {
        "assetnum": "MOTOR1002",
        "description": "Electric Motor",
        "age": 5,
        "status": "OPERATING"
    },
    {
        "assetnum": "GEN1003",
        "description": "Generator",
        "age": 15,
        "status": "DOWN"
    }
]

with open("assets.json", "w") as file:
    json.dump(assets, file, indent=4)

with open("assets.json", "r") as file:
    data = json.load(file)

for asset_object in data:
    print("assetnum:", asset_object["assetnum"])
    print("description:", asset_object["description"])
    print("age:", asset_object["age"])
    print("status:", asset_object["status"])
    if asset_object["age"] > 10:
        print("Priority: HIGH")
    elif asset_object["status"] == "DOWN":
        print("Priority: CRITICAL")

print("Assets written to assets.json")
print("---------End----------")

print("---------User input assignment Start----------")
asset_age = int(input("Enter age of Asset: "))
print("Asset Age:", asset_age);
print("-----------End----------")



