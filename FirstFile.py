# Lesson 1
asset_number = "PUMP1001"       
asset_description = "Water Pump"     
site = "PUNE01"       
purchase_cost = 50000
status = "OPERATING"   

print(asset_number)
print(asset_description)
print(site)
print(purchase_cost)
print(status)


#Lesson 2
asset_name = "Water Pump"
asset_age = 8
maintenance_required = True

if asset_age>5:
    print("Maintenance Inspection Required")
    if maintenance_required == True:
        print("Asset needs immediate maintenance attention")
else:
    print("Asset is Within Age Limit")
    
    
for i in range(5):
    print(i)
    
    
assets = [
    {"name": "Water Pump", "age": 8},
    {"name": "Electric Motor", "age": 12},
    {"name": "Generator", "age": 3},
    {"name": "Compressor", "age": 15}
]

for asset in assets:

    print("Asset:", asset["name"])

    if asset["age"] > 10:
        print("Priority: HIGH")

    elif asset["age"] > 5:
        print("Priority: MEDIUM")

    else:
        print("Priority: NORMAL")

    print("-------------------")
    
    
asset = {
    "asset_number": "PUMP1001",
    "description": "Water Pump",
    "age": 8,
    "status": "OPERATING",
    "criticality": "HIGH"
}

print(asset["asset_number"])
print(asset["description"])
print(asset["age"])
print("-------------------")

asset = {
    "asset_number": "PUMP1001",
    "status": "OPERATING"
}

asset["status"] = "BREAKDOWN"

print(asset["status"])
print("-------------------")

asset["maintenance_required"] = True
print(asset)
print("-------------------")

assets = [
    {"name": "Pump-1001", "age": 12, "status": "OPERATING"},
    {"name": "Motor-1002", "age": 8, "status": "OPERATING"},
    {"name": "Generator-1003", "age": 3, "status": "BREAKDOWN"},
    {"name": "Compressor-1004", "age": 15, "status": "OPERATING"},
    {"name": "Transformer-1005", "age": 6, "status": "OPERATING"}
]

for asset in assets:
    asset["name"]="AT001"
    asset["age"]=4
    asset["ststu"]="BREAKDOWN"
    
print(assets)
print("-------------------")