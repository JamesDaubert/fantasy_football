import enum
import heapq
import json
import os.path
import requests
import numpy
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from domain.team import Team
from domain.player import Player

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
TEAMS_SHEET = "1GzkNwRVeWhWKO1aT_gKqCnGgJOfAYRYSnWIubEfJ4hE"
SHEETS_AND_RANGES = ["Team 1!A2:E", "Team 2!A2:E", "Team 3!A2:E", "Team 4!A2:E", "Team 5!A2:E", "Team 6!A2:E",
                     "Team 7!A2:E", "Team 8!A2:E", "Team 9!A2:E", "Team 10!A2:E", "Team 11!A2:E", "Team 12!A2:E"]


def main():
    # Generate player table
    player_table = {}
    URL = "https://www.pro-football-reference.com/years/2023/fantasy.htm"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find('table', id='fantasy')
    body = table.find('tbody')

    for row in body.find_all('tr'):
        data = row.find_all('td')
        if not data:
            continue
        name = data[0].find('a').contents[0]
        # print(name)
        if not data[1].find('a'):
            team = '2TM'
        else:
            team = data[1].find('a')["title"]
        position = data[2].text
        fantasy_points = data[25].text
        player_table[name] = Player(name, team, position, fantasy_points)
    print("Player dictionary created with ", len(player_table), " players!")

    # Generate google auth creds
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    league = {}
    try:
        service = build("sheets", "v4", credentials=creds)

        # Next, grab all the teams from our league, and initialize the teams, with totals
        sheet = service.spreadsheets()
        for i, s in enumerate(SHEETS_AND_RANGES):
            team_num = i + 1
            result = (
                sheet.values()
                .get(spreadsheetId=TEAMS_SHEET, range=s)
                .execute()
            )
            values = result.get("values", [])

            if not values:
                print("No data found.")
                return

            # print(team_num)
            new_team = Team(str(team_num))
            for row in values:
                name = row[1]
                player = player_table[name]
                if player.is_qb():
                    new_team.set_qb(player)
                if player.is_rb():
                    new_team.add_rb(player)
                if player.is_wr():
                    new_team.add_wr(player)
                if player.is_flex():
                    new_team.set_flex(player)
            league[new_team.name] = new_team
        print("League generated!")
    except HttpError as err:
        print(err)
    
    settings = {}
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    # Exception handling if bad json in settings

    """
    Define the input
    Choose a probability distribution
    Simulate the input by sampling from the probability distribution
    Perform a deterministic calculation of the simulated input
    Summarize the results
    """
    num_simulations = settings['num_simulations']  # need to grab from settings.json
    avg = settings['avg'] 
    std_dev = settings['std_dev'] / float(10)
    num_teams = 12
    # for _ in range(num_simulations):


    schedule = {}
    schedule[1] = [[6, 5], [11, 7], [4, 3], [2, 12], [1, 9], [8, 10]]
    schedule[2] = [[6, 11], [5, 10], [4, 7], [2, 3], [1, 12], [8, 9]]
    schedule[3] = [[6, 4], [5, 11], [2, 7], [1, 3], [8, 12], [9, 10]]
    schedule[4] = [[6, 2], [5, 4], [11, 10], [1, 7], [8, 3], [9, 12]]
    schedule[5] = [[6, 1], [5, 2], [11, 4], [8, 7], [9, 3], [12, 10]]
    schedule[6] = [[6, 8], [5, 1], [11, 2], [4, 10], [9, 7], [12, 3]]
    schedule[7] = [[6, 9], [5, 8], [11, 1], [4, 2], [12, 7], [3, 10]]
    schedule[8] = [[6, 12], [5, 9], [11, 8], [4, 1], [2, 10], [3, 7]]
    schedule[9] = [[6, 3], [5, 12], [11, 9], [4, 8], [2, 1], [7, 10]]
    schedule[10] = [[6, 7], [5, 3], [11, 12], [4, 9], [2, 8], [1, 10]]
    schedule[11] = [[6, 10], [5, 7], [11, 3], [4, 12], [2, 9], [1, 8]]
    schedule[12] = [[6, 5], [11, 7], [4, 3], [2, 12], [1, 9], [8, 10]]
    schedule[13] = [[6, 11], [5, 10], [4, 7], [2, 3], [1, 12], [8, 9]]
    schedule[14] = [[6, 4], [5, 11], [2, 7], [1, 3], [8, 12], [9, 10]]
    schedule[15] = [[6, 2], [5, 4], [11, 10], [1, 7], [8, 3], [9, 12]]
    # TODO: Refactor this to fit with league settings, add wins/losses, points for.
    # Simulate a season
    average_placement = [0 for _ in range(12)]
    for _ in range(num_simulations):
        for week in range(1, 16):
            this_weeks_schedule = schedule[week]
            # print("week", week)
            # print("schedy", this_weeks_schedule)
            percent_projections_for_teams = abs(numpy.random.normal(avg, std_dev, num_teams).round(2))
            # print('%', percent_projections_for_teams)
            team_totals = [0]
            for i, p in enumerate(percent_projections_for_teams):
                weekly_avg = league[str(i+1)].get_weekly_score()
                team_totals.append(weekly_avg * percent_projections_for_teams[i])
            # print(team_totals)
            for matchup in this_weeks_schedule:
                # print("matchy", matchup)
                home = matchup[0]
                away = matchup[1]
                home_score = team_totals[home]
                away_score = team_totals[away]
                home_name = str(home)
                away_name = str(away)
                if home_score > away_score:
                    # print(home_name, " wins")
                    league[home_name].win(home_score)
                    league[away_name].lose(away_score)
                elif home_score == away_score:
                    # print('tie', home, away)
                    league[home_name].tie(home_score)
                    league[away_name].tie(away_score)
                else:
                    # print(away, " wins")
                    league[away_name].win(away_score)
                    league[home_name].lose(home_score)
            
        standings = []

        # win = 1000 points
        for team_name in league.keys():
            team = league[team_name]
            wins = team.wins
            total_points = wins * 1000 + team.points_for
            # print(total_points)
            heapq.heappush(standings, (-total_points, team_name))
            # print(standings)

        final_standings = []
        place = 1
        while standings:
            cur = heapq.heappop(standings)
            # print(cur)
            final_standings.append(cur[1])
            average_placement[int(int(cur[1]) - 1)] += place
            place +=1
    final_standings = []
    for i, p in enumerate(average_placement):
        average_placement[i] = p / 1000
    print(average_placement)
    final_final = []
    for i, p in enumerate(average_placement):
        heapq.heappush(final_final, (p, i))
    # while final_standings:
    #     final_final.append(heapq.heappop(final_standings))
    THE_FINAL_STANDINGS = []
    for i, t in enumerate(final_final):
        THE_FINAL_STANDINGS.append(t[1]+1)
    print(THE_FINAL_STANDINGS)
    l = 0
    r = 11
    bracket = []
    while l < r:
        bracket.append([THE_FINAL_STANDINGS[l], THE_FINAL_STANDINGS[r]])
        l+=1
        r-=1
    print(bracket)
    # print(average_placement)
    # Generate standings


if __name__ == "__main__":
    main()