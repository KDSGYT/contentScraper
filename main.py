#!/usr/bin/env python3
print("Hello, World!")
# This is a simple Python script that prints "Hello, World!" to the console.
# It serves as a basic example of how to run a Python script.
# To run this script, use the command: python3 main.py
# Ensure you have Python 3 installed on your system.
# You can modify this script to perform other tasks as needed.

# For example, you can add more print statements or define functions.

import instaloader as ig
import os
import webbrowser
USERNAME = os.getenv('INSTA_USERNAME')
PASSWORD = os.getenv('INSTA_PASSWORD')

print(f"Logging in as {USERNAME}")

L = ig.Instaloader(download_videos=True, download_pictures=False)

browser = webbrowser.get('brave %s')
# browser.open("google.com")

# login to Instagram
try:
    L.login(USERNAME, PASSWORD)
    # L.interactive_login(USERNAME)
    print("Login successful!")

# implementing the login having issue with authentication: password was entered correctly however login with browser is reqired. Stopping coding for now since there is redundant error showing wrong password. 

except Exception as e:
    print("Login failed. Login with Browser.")
#     # Extract the URL from the error message if present
    print("Please login manually in the browser")

# L.test_login()

hashtag = "funny"  # Replace with your desired hashtag
for post in ig.Hashtag.from_name(L.context, hashtag).get_posts():
    # print a list of posts with the specified hashtag 
    print(f"Post: {post.shortcode}, Likes: {post.likes}, Comments: {post.comments}, Video: {post.is_video}")
    if post.is_video:
        L.download_post(post, target=f"#{hashtag}")

        