# Property Scraper

This is a Python script that scrapes a specific Rightmove URL for new rental properties every 5 minutes, and sends a WhatsApp message for each new property found to a specific group. It stores found properties in a txt within the same directory.

## Requirements
- Python 3
- pywhatkit
- requests
- BeautifulSoup

## Usage
1. Install the required packages by running the following command in your terminal: 
```
pip install pywhatkit requests bs4
```

2. Set the URL of the Rightmove website you want to scrape in the `url` variable.

3. Set the WhatsApp group ID you want to send messages to in the `groupID` variable.

4. Run the script in your terminal:
```
python Rightmove_Whatsapp.py
```
5. Log onto https://web.whatsapp.com/


The script will continue to run until it is stopped manually. It will check for new properties every 5 minutes.

If a new property is found, the script will send a message to the specified WhatsApp group. If a property has already been found before, it will not be sent again.

The initial properties are stored in a text file (`properties.txt`), so that the script can check for new properties each time it runs.

## Disclaimer
This script is for educational purposes only. Use at your own risk.
