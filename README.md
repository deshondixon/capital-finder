# LAB 16 - Class 401d20

## Capital Finder

#### *Author:* DeShon Dixon

---

## Overview

- Serverless function handles two kinds of queries.

- Prints a welcome message to the user, explaining the Madlib process and command line interactions.

- Serverless function handles GET http request with a given country name that responds with a string with the form The capital of X is Y.
- 
- E.g./capital-finder?country=Chile generates a http response of The capital of Chile is Santiago.

---

## Setup

- Create repo on desktop
- Create virtual environment: 
*python3.11 -m venv .venv*
- Activate environment: 
*source .venv/bin/activate*
- Install pywatch: 
*pip install pytest-watch*
- Clone repo: *https://github.com/deshondixon/capital-finder.git*