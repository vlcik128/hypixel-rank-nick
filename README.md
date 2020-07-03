# hypixel-rank-nick
Python script that returns player's rank and guild tag based on nickname using Hypixel API.

# Installation/requirements
To install, download the .py file and set there your Hypixel API key in it. <br /><br />

Your API keys belongs here: `API_KEY = "enter-your-api-key-here"` <br />
To obtain one, join the lobby and type: `/api new`. There are not any other methods to obtain it, except for this. <br /><br />

**!!!** You have to have installed `requests` package. If you have not, open command prompt (or terminal) and execute: `pip install requests` 

# How to use? 
1.  Run the script. (Cmd/terminal: `python hypixel_rank_nick.py`)
1.  Enter the nick of player, you want to check. (Or nicks, if you want to check more players at once (max 57). Separate them using spaces: ` `)
1.  You'll see for each player a paragraph with informations. 
1.  Last paragraph are your API key usage stats: 
    *  QPM - Queries past minute. 
    *  TQ - Total queries (life-time) sent by the owner of the API key.


