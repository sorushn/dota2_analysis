import datetime
import logging
import os
import time
from sys import stdout

import requests
from tqdm import tqdm

import db as db_utils

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logFormatter = logging.Formatter(
    "%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
consoleHandler = logging.StreamHandler(stdout)  # set streamhandler to stdout
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

API = "https://api.opendota.com/api"


def download_match_history(player_id: str):
    url = f"{API}/players/{player_id}/matches"
    response = requests.get(url)
    if response.status_code == 200:
        logger.debug(
            f"Downloaded match history for player {player_id}, {len(response.json())} matches")
        return response.json()
    else:
        raise Exception


def download_match(match_id: str):
    url = f"{API}/matches/{match_id}"
    response = requests.get(url)
    if response.status_code == 200:
        logger.debug(f"Downloaded match {match_id}")
        return response.json()
    else:
        raise Exception


def download_all_matches(player_id: str, match_history: list = [], player_db=None, match_db=None, rate_limit_per_min=60, rate_limit_per_day=2000):

    if player_db is None:
        player_db = db_utils.get_database().player
    if match_db is None:
        match_db = db_utils.get_database().match
    if match_history == []:
        match_history = download_match_history(player_id)
        player_db.insert_many(match_history)

    start_time = datetime.datetime.now()
    match_count = 0

    for match in tqdm(match_history, desc="Downloading matches"):
        if "match_id" not in match:
            continue
        if match["game_mode"] != 22:
            continue
        if match_db.find_one({"match_id": match["match_id"]}):
            continue

        match_count += 1
        elapsed_time = datetime.datetime.now() - start_time

        if match_count >= rate_limit_per_day and elapsed_time.total_seconds() >= 60 * 60 * 24:
            break

        if elapsed_time.total_seconds() >= 60:
            break

        try:
            match = download_match(match["match_id"])
        except Exception as e:
            logger.debug(f"{e}, error downloading match {match['match_id']}")
        match_db.insert_one(match)
        time.sleep(60/rate_limit_per_min)


if __name__ == "__main__":
    download_all_matches('124219753')
