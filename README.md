# fantasy_football
Maybe this will help me win my league...


### About
This app runs a Monte Carlo simulation for a 12-team fantasy football league. It draws data from pro-football-reference.com, and a pre-defined
set of teams from Google Sheets. The fantasy teams are simplified from what you may see in a real league: there are only 7 offensive players.

Settings for the simulation are read in from a settings.json file in the directory. This file can be edited to tweak standard deviation, and in
the future could even be used to pick the type of distribution used (uniform, normal).

The schedule is also the same for each simulation, and the simulation could be further "randomized" by making the schedule randomly generated
during each simulation. 

The output of this simulation is a bracket with the most likely playoff matchups, printed to your command line, and written
to your Google Sheet in a new worksheet with a randomly generated UUID

### Running the sim

#### Pre-requisites

**Google Auth**

Follow this guide to enable this app to read and write to your sheets account by creating a Google Cloud Project.
 https://developers.google.com/workspace/guides/get-started. You will need to enable `Google Sheets API` in the *Enabled APIs & services* tab. 

#### Running sim

To run the sim, use the following command in your Terminal: `<path-to-python>/python3 <path-to-code-directory>/fantasy_football/quickstart.py

On the first runtime, you should be asked to allow this app to access your Google Cloud Project you configured above. After that, a token
should be reused on subsequent runs.

### Further improvements

There are several improvements that can be made to this SIM.

1. The simulation itself could be improved to offer more randomized distributions.
2. The application could allow you to supply your own Google creds, so that you could pull in your own league.
3. More details could be provided on execution, like "best finish" or "worst finish"
4. Rosters could be expanded, with BYE weeks taken into account, and bench players used to fill in gaps. Obviously there is still no waiver wire system, but that could conceivably be written in as well with enough time.