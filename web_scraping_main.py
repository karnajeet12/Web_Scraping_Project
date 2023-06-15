# used requests and bs4 (for beautiful soup) libraries for web scraping

import requests
from bs4 import BeautifulSoup as bs
import instaloader

choice = input(
    "Enter the Platform from which you want to download the profile picture: \n G -> GitHub \n I -> Instagram \n")

if choice == "I" or choice == "i":
    insta = instaloader.Instaloader()
    insta_profile_pic = input("Enter Instagram Username: ")
    insta.download_profile(insta_profile_pic, profile_pic_only=True)


elif choice == "G" or choice == "g":
    github_user = input("Enter github Username: ")
    url = "https://github.com/"+github_user
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    github_profile_image = soup.find('img', {'alt': 'Avatar'})['src']
    print(github_profile_image)

else:
    print("You entered the wrong choice")
