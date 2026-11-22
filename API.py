
print("---------Asset Meter Details----------")

import base64
import requests
import urllib3
import matplotlib.pyplot as plt

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

assetnum = input("Input Assetnum...")
url = "https://localhost:9443/maximo/api/os/MYASSET"
username = "maxadmin"
password = "maxadmin"
auth_token = base64.b64encode(f"{username}:{password}".encode()).decode("ascii")
headers = {"Accept": "application/json", "maxauth": auth_token}
params = {
    "oslc.select": "*",
    "oslc.where": f"ASSETNUM=\"{assetnum}\"",
    "lean": "1",
    "_dropnulls": "0"
}

response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=15,
    verify=False,
)
x = []
y = []
w = 0.4
print("Response Status Code:", response.status_code)
data = response.json()
for member in data["member"]:
    # print("Asset Number:", member["assetnum"])
    # print("Description:", member["description"])
    for assetmeter in member["assetmeter"]:
#        print("Meter Name:", assetmeter["metername"])
        if assetmeter["rolldownsource"] is None:
            for measure in assetmeter["measurement"]:
                # print("Meter Reading:", measure["measurementvalue"])
                # print("Reading Date:", measure["measuredate"])
                x.append(measure["measurementvalue"])
                y.append(measure["measuredate"])
            plt.figure()
            plt.title(assetmeter["metername"])
            plt.bar(y, x)
            plt.xlabel("Reading Date")
            plt.ylabel("Meter Reading")
            plt.xticks(rotation=20)
            plt.show(block=False)
        else:
            for meterred in assetmeter["meterreading"]:
                #print("Meter Reading:", meterred["reading"])
                #print("Reading Date:", meterred["readingdate"])
                x.append(meterred["reading"])
                y.append(meterred["readingdate"])
            plt.figure()
            plt.title(assetmeter["metername"])
            plt.bar(y, x)
            plt.xlabel("Reading Date")
            plt.ylabel("Meter Reading")
            plt.xticks(rotation=20)
            plt.show(block=False)

    plt.show()
print("---------Thanks----------")

