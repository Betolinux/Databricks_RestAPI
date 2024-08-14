import requests


# Constants
DATABRICKS_INSTANCE = "<Databricks url"
# Example https://adb-XXXXXXXXXXX.15.azuredatabricks.net
API_VERSION = "2.0"
IP_ACCESS_LIST_ID = "<your-ip-access-list-id>"
TOKEN = "<Token>"

# URL for the API endpoint
#url = f"{DATABRICKS_INSTANCE}/api/{API_VERSION}/ip-access-lists/{IP_ACCESS_LIST_ID}"
url = f"{DATABRICKS_INSTANCE}/api/{API_VERSION}/ip-access-lists/"

# Headers for the request
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_ip_access_list_details():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()  # Return the response JSON if successful
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    ip_access_list_details = get_ip_access_list_details()
    if ip_access_list_details:
        print(ip_access_list_details)
