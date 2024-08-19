
# Dota Match Data Downloader

Match history analysis for Valve Software's [Dota 2](dota2.com)

## Table of Contents

* [Introduction](#introduction)
* [Requirements](#requirements)
* [Usage](#usage)
* [API Documentation](#api-documentation)
* [Database Schema](#database-schema)

## Introduction

This project intends to be a framework for analysing match history data. It currently provides a python script to download Dota match data from the OpenDota API

## Requirements

* Python 3.11+
* `requests` library
* `pymongo` library
* MongoDB instance

## Usage

For using the downloader utility, follow either of the following:

### Docker

use `docker-compose up -d` to run the containarized version

### Python

1. Clone the repository: `git clone https://github.com/your-username/dota-match-data-downloader.git`
2. Install the required libraries: `pip install -r requirements.txt`
3. Create a MongoDB instance and add the connection string to the `app/utils/db.py` file
4. Run the script: `python app/utils/download.py`

## API Documentation

The script uses the OpenDota API to download match data. The API documentation can be found at [https://api.opendota.com](https://api.opendota.com).

## Database Schema

The script stores the match data in a MongoDB database. The database schema is as follows:

* `matches` collection:

  * `match_id`: unique identifier for the match
  * `player_slot`: player slot number
  * `radiant_win`: whether the radiant team won
  * `duration`: match duration
  * `game_mode`: game mode
  * `lobby_type`: lobby type
  * `hero_id`: hero ID
  * `start_time`: match start time
  * `version`: match version
  * `kills`: number of kills
  * `deaths`: number of deaths
  * `assists`: number of assists
  * `average_rank`: average rank
  * `leaver_status`: leaver status
  * `party_size`: party size
  * `hero_variant`: hero variant
