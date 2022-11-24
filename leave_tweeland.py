# heavily based on https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/0d1587147d3bf8338b5fea2b4e5bb56d37f5c2b6/Follows-Lookup/followers_lookup.py
# added csv writer and pagination
# jean-marc couffin, 2022

import requests
import os
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAH" # your bearer token

current_folder = os.path.dirname(os.path.abspath(__file__))

filepath = os.path.join(current_folder, "followers.csv")
# filepath = os.path.join(current_folder, "following.csv")



def create_url():
    # Replace with user ID below
    user_id = 101010101010101010101 # your tweeter user id
    return "https://api.twitter.com/2/users/{}/followers".format(user_id)
    # return "https://api.twitter.com/2/users/{}/following".format(user_id)


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FollowingLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def add_to_csv(data):
    # fix data encoding
    data = json.dumps(data, ensure_ascii=False)
    data = json.loads(data)
    with open(filepath, "a", encoding="utf-8") as f:
        for user in data["data"]:
            f.write(user["name"] + "," + user["username"] + "," + user["id"])
            f.write("\n")

def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    add_to_csv(json_response)
    return json_response["meta"]["next_token"]


if __name__ == "__main__":
    next_token = main()
    while next_token:
        url = create_url() + "?pagination_token=" + next_token
        json_response = connect_to_endpoint(url)
        add_to_csv(json_response)
        next_token = json_response["meta"]["next_token"]
