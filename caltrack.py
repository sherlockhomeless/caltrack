#!/usr/bin/env python3

from auth import *
import caldav

PATH_CREDS = "credentials.secret"
URL = "https://selfhostgang.dynv6.net/radicale/"

def get_client(url: str, creds: (str, str)) -> caldav.Principal:
    client = caldav.DAVClient(url=url, username=creds[0], password=creds[1])
    principo = client.principal()
    return principo

def read_calendars():
    creds = read_credentials(PATH_CREDS)
    principal = get_client(URL, creds)
    print(principal.calendars())
    

if __name__ == '__main__':
    read_calendars()
