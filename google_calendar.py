from __future__ import print_function
from datetime import datetime
from datetime import *
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from emailsender import * 
from dotenv import load_dotenv
import os
import time

meals = queryDB()

load_dotenv(".env")

RECIEVER = os.environ.get("GMAIL_RECIEVER")

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

 
def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    # creates one hour event tomorrow 10 AM IST
    #service = get_calendar_service()

    
    length = 0
 
    print(meals)
    for i in meals: 
        d = datetime.now().date()
        tomorrow = datetime(d.year, d.month, d.day, 17)
        start = (tomorrow + timedelta(days=length)).isoformat()
        end = (tomorrow + timedelta(days=length)).isoformat()
        events = {
        "summary": i,
        "description": 'Dinner',
        "start": {
            "dateTime": start,
            "timeZone": 'Europe/London'
        },
        "end": {
            "dateTime": end,
            "timeZone": 'Europe/London'
        },
        "attendees": [
            {
            "email": RECIEVER,
            # Other attendee's data...
            },
        ],
        }

        length += 1

        event_result = service.events().insert(calendarId='primary', body=events).execute()

        print("created event")
        print(event_result['id'])
        time.sleep(10)
if __name__ == '__main__':
   main()

