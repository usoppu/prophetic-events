#script to scrape and generate markdown files for site
#TODO check date formats, US/Rest of world

from lxml import html
import requests
import time
import operator

print ("starting")
envPath = "/home/uso/projects/prophetic-events/"
print ("path set to: ", envPath)

print("------------------------------")
page = requests.get('https://www.morningstarministries.org/events/all-events')
print("page:",page)
tree = html.fromstring(page.content)
print("tree:",tree)

#code = tree.xpath("(//span[@class='code' and (ancestor::article[contains(.,'AU')])]/text())[1]")
# events = tree.xpath("//div[@class='cbp-item']")
events = tree.xpath("//div[@class='cbp-item ']")
print("events:",events)
print("----------------------------------")

events_details = []
for event in events:
    event_title = event.xpath('.//a/b/text()')
    print("event_title:",event_title)
    event_image = event.xpath('.//img/@src')
    print("event_image:",event_image)
    event_link = event.xpath('.//a/@href')
    print("event_link:",event_link)
    event_date = event.xpath(".//span[@class='date-display-start']/text()")
    print("event_date:",event_date)
    event_location = "US"
    print("event_location:",event_location)
    event_location_details = "South Carolina"
    print("----------------------------------")
    event_details = {
        "title": event_title,
        "image": event_image,
        "link": event_link,
        "date": event_date,
        "location": event_location,
        "location_details": event_location_details,
    }
    events_details.append(event_details)

# print ("all events:",events_details)
# print("single:",events_details[0]["title"])

newlist = sorted(events_details, key=operator.itemgetter('date'))

for x in newlist:
    print(x["title"],x["date"])

# code = code[0]
# print("code:", code)
time.sleep(300)
