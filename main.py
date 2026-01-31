import requests
import json
import time
import os

URL = "https://www.moltbook.com/api/v1/submolts/general?sort=new" # change for different submolts.
CHECK_INTERVAL = 15 # change for slower or faster checking, it's in seconds.
FILE_NAME = "posts.txt" # change for custom filename.

last_post_id = None

def save_data(posts):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for post in posts:
            f.write(json.dumps(post) + "\n")

def get_data():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

def monitor():
    global last_post_id
    
    current_posts = get_data().get("posts", [])
    current_ids = [p["id"] for p in current_posts]
    
    if not last_post_id in current_ids:
        
        save_data(current_posts)
        last_post_id = current_ids[0]
        return True
    
    return False
 

def main():

    print(f"Monitoring {URL}")
    counter = 0

    while True:
        
        if monitor():
            os.system("cls") # change to clear if using linux or mac.
            print(f"NEW POSTS - check {FILE_NAME}. {counter}")
            counter += 1
        
        time.sleep(CHECK_INTERVAL)
        

main()
