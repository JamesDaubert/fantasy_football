import os.path
import requests
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from domain.player import Player

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
TEAMS_SHEET = "1GzkNwRVeWhWKO1aT_gKqCnGgJOfAYRYSnWIubEfJ4hE"
SAMPLE_RANGE_NAME = "Team 1!A2:E"


def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
#   creds = None
#   # The file token.json stores the user's access and refresh tokens, and is
#   # created automatically when the authorization flow completes for the first
#   # time.
#   if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#   # If there are no (valid) credentials available, let the user log in.
#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file(
#           "credentials.json", SCOPES
#       )
#       creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())

  try:
    # service = build("sheets", "v4", credentials=creds)

    # # Call the Sheets API
    # sheet = service.spreadsheets()
    # result = (
    #     sheet.values()
    #     .get(spreadsheetId=TEAMS_SHEET, range=SAMPLE_RANGE_NAME)
    #     .execute()
    # )
    # values = result.get("values", [])

    # if not values:
    #   print("No data found.")
    #   return

    # print("Team, Name, Position:")
    # for row in values:
    #   # Print columns A and E, which correspond to indices 0 and 4.
    #   print(f"{row[0]}, {row[1]}, {row[2]}")
    # # Now let's scrape pro football reference and get these items

    URL = "https://www.pro-football-reference.com/years/2023/fantasy.htm"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    result = {}
    table = soup.find('table', id='fantasy')
    # print(table)
    body = table.find('tbody')
    row_1 = body.find('tr')
    data = row_1.find_all('td')
    name = data[0].find('a').contents[0]
    team = data[1].find('a')["title"]
    position = data[2].text
    player = Player(name, team, position)
    print(player)
    # for i, d in enumerate(data[0]):
    #     print(i, d)
    # print(data[])
    # name = data[0]
    # print(name)
    # for row in body.find('tr'):
    #     print(row)
    #     data = row.find('td')
    #     print(data)
    # for row in soup.table.find_all('tr'):
    #     print(row)
    #     row_header = row.th.get_text()
    #     print(row_header)
    #     row_cell = row.td.get_text()
    #     result[row_header] = row_cell    
    # print(result)
    # print(results.prettify())


  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()