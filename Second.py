def check_asset_priority(asset_name, asset_age):

    print("Asset:", asset_name)

    if asset_age > 10:
        print("Priority: HIGH")

    elif asset_age > 5:
        print("Priority: MEDIUM")

    else:
        print("Priority: NORMAL")
    
    
    
    return asset_age


age = check_asset_priority("Water Pump", 12)
print(age)
age = check_asset_priority("Electric Motor", 8)
print(age)
age = check_asset_priority("Generator", 3)
print(age)

print("-------------------")


def create_workorder(asset_name, priority="MEDIUM"):

    print("Asset:", asset_name)
    print("Priority:", priority)


create_workorder("Water Pump")
create_workorder("Electric Motor", "HIGH")
print("-------------------")

status = "       OPERATING STATUS      "
print(status.upper())
print(status.lower())
print(status.capitalize())
print(status.title())
print(status.strip())
print(status.lstrip())
print(status.rstrip())
print("-------------------")

description = "Water pump leakage detected"

if "leak" in description.lower():
    print("Possible leakage issue detected")
else:
    print("No leakage keyword found")

print(description.find("Shreyuth") )
desc = description.replace("leakage", "leak")
print(desc)
desc_split = description.split(" ")
print(desc_split)
print(desc_split[0] )
print("-".join(description))
print("-------------------")

asset = "Water Pump"
age = 8
print(f"Asset is {asset} and age is {age}")
print("-------------------")

asset_statuses = [
    "OPERATING",
    "BREAKDOWN",
    "OPERATING",
    "DECOMMISSIONED",
    "BREAKDOWN"
]

print(asset_statuses)
print(set(asset_statuses))
print("-------------------")


asset_status = {"OPERATING", "BREAKDOWN", "DECOMMISSIONED", "OPERATING"}
asset_status.add("MAINTENANCE")
print(len(asset_status))
asset_status.remove("DECOMMISSIONED")
print(asset_status)
print("-------------------")


print("---------Start----------")
site_pune = {"PUMP1001", "MOTOR1002", "GEN1003"}
site_mumbai = {"PUMP1001", "COMP1004", "TRANS1005"}
print(site_pune | site_mumbai)
print(site_pune & site_mumbai)
print(site_pune - site_mumbai)
print(site_pune ^ site_mumbai)
print("---------End----------")


print("---------Using raise Start----------")
def validate_asset_age(age):
    if type(age) is str:
        raise TypeError("Asset age must be a number")
    elif age < 0:
        raise ValueError("Asset age cannot be negative")
      
    return "Asset age is valid"

try:
    print(validate_asset_age(-5))

except ValueError as error:
    print("Validation error:", error)
except TypeError as typeError:
    print("Type error:", typeError)

print("---------End----------")


print("---------Check Variable Type----------")
asset_age = "12"
print(type(asset_age))
print("---------End----------")


print("---------Practical Assignment----------")
assets = [
    {"name": "Pump-1001", "age": "12"},
    {"name": "Motor-1002", "age": "8"},
    {"name": "Generator-1003", "age": "abc"},
    {"name": "Compressor-1004", "age": "-5"},
    {"name": "Transformer-1005", "age": "6"}
]


for asset in assets:
    
    try:
        print(validate_asset_age(int(asset["age"])))
        print("Asset Name:", asset["name"])
        print("Asset Age:", asset["age"])
    except ValueError as error:
        print("Error:", error)

print("---------End----------")


print("---------Reading and Writing file Start----------")
file = open("assets.txt", "w")
file.write("asset_name,pump\n")
file.write("asset_age,12\n")
file.write("asset_number,12345\n")

file = open("assets.txt", "r")
print(file.read())
file.close()
print("---------End----------")

print("---------Reading and Writing file using with statement Start----------")

with open("assets.txt", "w") as file:
    file.write("asset_name,motor\n")
    file.write("asset_age,8\n")
    file.write("asset_number,67890\n")

with open("assets.txt","r") as file:
    print(file.read())

print("---------End----------")