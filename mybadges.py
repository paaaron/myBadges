from bs4 import BeautifulSoup
import lxml
import requests
badgeCount = 0
 
# type in your acclaim badges url
# url = "https://www.youracclaim.com/user/robert-mapstead"
print("\nThis program lists your badges from the Acclaim Badges Platform \n")
name = input("Enter user name. Example: robert-mapstead >>> ")
url = "https://www.youracclaim.com/user/"+name
 
# Getting the webpage, creating a Response object.
response = requests.get(url)
 
# Extracting the source code of the page.
data = response.text
 
# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'lxml')
 
# Extracting all the <a> tags whose class name is 'result-title' into a list.
badges = soup.findAll('em', {'class': 'word-break'})
 
# Extracting text from the the <a> tags, i.e. class badges.
print()
print("Copy all of this text below for use in your resume, CV, or Social Media Profiles: \n")

fobj = open('badges.txt', 'a')
fobj.write(url+"\n")
print("\nmy Badges:")
for badge in badges:
    print(badge.text)
    with open('badges.txt','a') as f: 
      fobj.write(badge.text+"\n")
    badgeCount = badgeCount + 1

print()
print("Total Badges Earned: " + str(badgeCount))
with open('badges.txt','a') as f:
  fobj.write("totalBadges: "+str(badgeCount)+"\n")
print()
print("How many badges do you have?  https://bit.ly/uc-mybadges\n")
print("Source: "+url+"\n")

fobj.close()