import pywhatkit as pw
import requests
from bs4 import BeautifulSoup
import os.path
import time
import datetime

print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)

# URL of the website to scrape
url = 'https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=OUTCODE%5E293&maxBedrooms=3&minBedrooms=3&radius=3.0&propertyTypes=&mustHave=student&dontShow=&furnishTypes=&keywords='

# File to store the initial properties
file_path = 'properties.txt'

# Check if the file exists
if os.path.isfile(file_path):
    # Load the initial properties from the file
    with open(file_path, 'r') as f:
        initial_props = [tuple(line.strip().split('\t')) for line in f.readlines()]
    first_time_running = False
else:
    initial_props = []
    first_time_running = True

# Check for new properties every 5 minutes
while True:
    new_props = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    props = soup.find_all('div', class_='propertyCard')
    
    # Extract new properties
    for prop in props:
        name = prop.find('a', class_='propertyCard-link').text.strip().replace('\n', '')
        address = prop.find('address', class_='propertyCard-address').text.strip().replace('\n', '').replace(' ', '')
        try:
            price = prop.find('div', class_='propertyCard-price').text.strip().replace('\n', '')
        except AttributeError:
            price = 'Price Not Available'
        link = 'https://www.rightmove.co.uk' + prop.find('a', class_='propertyCard-link')['href']
        link = link.replace('\n', '')
        link = link.split("~")[0]
        link = link.split("#")[0]
        if (name, address, price, link) not in initial_props:
            new_props.append((name, address, price, link))
    
    # Send a WhatsApp message for each new property
    for prop in new_props:
        message = f'New property found:\nName: {prop[0]}\nAddress: {prop[1]}\nPrice: {prop[2]}\nLink: {prop[3]}'
        if not first_time_running:
            pw.sendwhatmsg_to_group_instantly("KZrWwMQH6MfEJuYbxjNRqC", message, wait_time=60, tab_close=True)
        print(message)
    
    # Update the list of initial properties
    initial_props += new_props
    
    # Save the updated list of initial properties to the file
    with open(file_path, 'w') as f:
        for prop in initial_props:
            f.write('\t'.join(prop) + '\n')
    
    # Wait for 5 minutes before checking for new properties again
    time.sleep(300)
