from __future__ import print_function
import sys
import re
import os
import shutil
#import commands
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import web
import jinja2

def main():
    #count()
    print("hello")

def getWords():
    #print "Hello"
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage('credentials.txt')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1jq1EOegvSv25I8YsPsZwcwlI-aLn5ggCgcmEFtpjBs8'
    RANGE_NAME = 'A5:C'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    values = result.get('values', [])
    cards = []
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print(row)
            if len(row)>1:
                cards.append(FlashCard(row[0], row[1]))
                #print('%s, %s' % (row[0], row[1]))
    return cards

class FlashCard:
    def __init__(self, term, description):
        self.term = term
        self.description = description

def startMain():
    app = web.application(urls, globals())
    app.run()

jinja_environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            "%s/templates" % os.path.dirname(__file__)))

class MainPageHandler(object):
    def GET(self):
        web.header('Content-type', "text/html; charset=utf-8")
        template = jinja_environment.get_template('index.html')
        print("words: ", getWords())
        template_values = {'sync': False,
                           'cards': getWords() }
        return template.render(template_values)


urls = (r'/', MainPageHandler
        )

if __name__ == '__main__':
    startMain()
    #main()