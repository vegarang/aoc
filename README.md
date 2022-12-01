## Utilities for [Advent of code](https://adventofcode.com/) in python

Inspired by [caderek/aocrunner](https://github.com/caderek/aocrunner), but not nearly as fancy. This just fetches the input for today

Setup using python 3.9

### Getting started:
Install dependencies from `requirements.txt` (preferrably in a [virtualenv](https://pypi.org/project/virtualenv/), see [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) if this is new to you):

```zsh
$ cd aoc
$ mkvirtualenv -p /path/to/python3.9 aoc
$ pip install -r requirements.txt
```

Then locate your session-token for AoC in cookies on [Advent of code](https://adventofcode.com/). Add this in a `.env`-file in the root of this project like this:

```.env
AOC_SESSION=53616c746[...]
```

Then, to set up skeleton for running AoC tasks, simply run `aoc.py`:

```zsh
$ python aoc.py
```

This will create a folder for the current year (e.g. `year2022`), with a folder for today (e.g. `day01`), with a `main.py` and `input.txt`.
The script always checks to see if files and/or folders already exists before doing anything, so if you want to re-fetch 
today's input you will have to rename or delete the file.

