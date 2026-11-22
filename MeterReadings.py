
print("---------Asset Meter Details----------")

import base64
import requests
import urllib3
import matplotlib.pyplot as plt
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def appendlist(reading, date):  
    x.append(reading)
    y.append(date)
    
def chart_info(metername):
    plt.figure()
    plt.title(metername)
    plt.bar_label(plt.bar(y, x, width=.4), label_type='edge')
    plt.plot(y, x, marker='o', color='orange')
    plt.xlabel("Reading Date")
    plt.ylabel("Meter Reading")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show(block=False)

def clearlist():
    x.clear()
    y.clear()
    
while True:
    assetnum = input("Input Assetnum...")
    url = "https://<hostname>/maximo/api/os/MYASSET"
    username = "<username>"
    password = "<password>"
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
    print("Response Status Code:", response.status_code)
    data = response.json()
    for member in data["member"]:
        for assetmeter in member["assetmeter"]:
            if assetmeter["rolldownsource"] is None and "measurement" in assetmeter:
                for measure in assetmeter["measurement"]:
                    appendlist(measure["measurementvalue"], measure["measuredate"])
                chart_info(assetmeter["metername"])
                clearlist()
            elif "meterreading" in assetmeter:
                for meterred in assetmeter["meterreading"]:
                    appendlist(meterred["reading"], meterred["readingdate"])
                chart_info(assetmeter["metername"])
                clearlist()
            else:
                print(f"No readings found for meter: {assetmeter['metername']}")

        plt.show()
    print("---------Thanks----------")

