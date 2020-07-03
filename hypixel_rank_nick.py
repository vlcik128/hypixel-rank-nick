# hypixel_rank_nick.py - Python script that returns player's rank and guild tag based on nickname using Hypixel API.
# Copyright (C) MMXX  vlcik128

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import requests

API_KEY = "enter-your-api-key-here"
PLAYERS = input("> ").split(" ")

if len(PLAYERS) > 57:
    print("\nYou can check max 57 players!") # This prevents you from exceeding the API limit of 120 requests.
    exit()


def replace_all_color_codes(string):
    string = string.replace("0", "")
    string = string.replace("§", "")
    string = string.replace("1", "")
    string = string.replace("2", "")
    string = string.replace("3", "")
    string = string.replace("4", "")
    string = string.replace("5", "")
    string = string.replace("6", "")
    string = string.replace("7", "")
    string = string.replace("8", "")
    string = string.replace("9", "")
    string = string.replace("a", "")
    string = string.replace("b", "")
    string = string.replace("c", "")
    string = string.replace("d", "")
    string = string.replace("e", "")
    string = string.replace("f", "")
    return string  # I'm too lazy to do regexs xd


print()
for PLAYER in PLAYERS:
    data = requests.get("https://api.hypixel.net/player?key=" + API_KEY + "&name=" + PLAYER).json()
    if data["player"] is None:
        print(PLAYER + " doesn't exist. (or is NICKED if found ingame)\n")
    else:
        gdata = requests.get(
            "https://api.hypixel.net/guild?key=" + API_KEY + "&player=" + data["player"]["uuid"]).json()

        rank: str
        # From Carcroft's tutorial
        if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
            rank = data["player"]["rank"]
        elif "newPackageRank" in data["player"]:
            rank = data["player"]["newPackageRank"]
        elif "packageRank" in data["player"]:
            rank = data["player"]["packageRank"]
        else:
            rank = "Non-Donor (DEFAULT)"
        # From Carcroft's tutorial

        # Getting guild tag here
        TAG: str
        if "guild" in gdata and gdata["guild"] is not None and "tag" in gdata["guild"]:
            tag = gdata["guild"]["tag"]
            tag_color: str
            if "tagColor" in gdata["guild"]:
                tag_color = gdata["guild"]["tagColor"]
            else:
                tag_color = "GREY"
            TAG = "[" + gdata["guild"]["tag"] + "]\n  - Guild tag color: " + tag_color
        else:
            TAG = ""
        # Getting guild tag here

        # todo: Make this code more efficient using some defs.
        if rank == "Non-Donor (DEFAULT)":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                print(data["player"]["displayname"] + " " + TAG)
        elif rank == "VIP":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                print("[VIP] " + data["player"]["displayname"] + " " + TAG)
        elif rank == "VIP_PLUS":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                print("[VIP+] " + data["player"]["displayname"] + " " + TAG)
        elif rank == "MVP":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                print("[MVP] " + data["player"]["displayname"] + " " + TAG)
        elif rank == "MVP_PLUS":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                if "monthlyPackageRank" in data["player"] and data["player"]["monthlyPackageRank"] == "SUPERSTAR":
                    print("[MVP++] " + data["player"]["displayname"] + " " + TAG)
                else:
                    print("[MVP+] " + data["player"]["displayname"] + " " + TAG)
                if "rankPlusColor" in data["player"]:
                    print("  - Plus color: " + data["player"]["rankPlusColor"])
                else:
                    print("  - Plus color: RED")
        elif rank == "YOUTUBER":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
                if PLAYER == "Technoblade":
                    print("  - Plus color: AQUA")
            else:
                print("[YOUTUBE] " + data["player"]["displayname"] + " " + TAG)
        elif rank == "ADMIN":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                print("[ADMIN] " + data["player"]["displayname"] + " " + TAG)
        elif rank == "MODERATOR":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                print("[MOD] " + data["player"]["displayname"] + " " + TAG)
        elif rank == "HELPER":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                print("[HELPER] " + data["player"]["displayname"] + " " + TAG)
        elif rank == "NONE":
            if "prefix" in data["player"]:
                print(replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                print("Well, " + data["player"][
                    "displayname"] + " has got NONE rank in Hypixel API. I don't know exactly what does this mean.")
        else:
            if "prefix" in data["player"]:
                print(
                    replace_all_color_codes(data["player"]["prefix"]) + " " + data["player"]["displayname"] + " " + TAG)
                print("  - Permissions of " + replace_all_color_codes(
                    data["player"]["prefix"]) + " prefix are based on " + rank + " rank. ")
            else:
                print(data["player"]["displayname"] + " " + TAG)
        print()

# Prints stats of your API key usage. 
kdata = requests.get("https://api.hypixel.net/key?key=" + API_KEY).json()
if kdata["success"]:
    print("\n\n    API key stats:\n    VALID,QPM=" + str(kdata["record"]["queriesInPastMin"] + 2) + ",TQ=" + str(
        kdata["record"]["totalQueries"] + 2) + ",LIMITPM=120")
