## Utilities for [Advent of code](https://adventofcode.com/) in python

Inspired by [caderek/aocrunner](https://github.com/caderek/aocrunner), but not nearly as fancy. This just fetches the input for today and generates a _very_ basic skeleton for todays task. Has flags for selecting another day (or year) if needed. Can also generate a .md of which stars you've gotten so far in a given year. 

Set-up using python 3.9

### Getting started:
Install dependencies from `requirements.txt` (preferably in a [virtualenv](https://pypi.org/project/virtualenv/), see [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) if this is new to you):

```zsh
  cd aoc
  mkvirtualenv -p /path/to/python3.9 aoc
  pip install -r requirements.txt
```

Then locate your session-token for AoC in cookies on [Advent of code](https://adventofcode.com/). Add this in a `.env`-file in the root of this project like this:

```.env
  AOC_SESSION=53616c746[...]
```

Then, to set up skeleton for running AoC tasks, simply run `aoc.py`:

```zsh
  python src/aoc.py --f
```

This will create a folder for the current year (e.g. `year2022`), with a folder for today (e.g. `day01`), with a `main.py` and `input.txt`.
The script always checks to see if files and/or folders already exists before doing anything, so if you want to re-fetch 
today's input you will have to rename or delete the file.

You can override year and day using parameters, and generate a markdown-file showing what tasks you've managed for a given year

For more info, see help-text: 

```zsh
  python src/aoc.py --help
```

```
usage: aoc.py [-h] [-v {0,1,2,3}] [-y YEAR] [-d DAY] [-f] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -v {0,1,2,3}, --verbosity {0,1,2,3}
                        How verbose should the logging be? Lower number means
                        more logs. Default (2): warn and error only
  -y YEAR, --year YEAR  what year to get challenges for (default: current)
  -d DAY, --day DAY     what day to get challenges for (default: current)
  -f, --fetch           Fetch task and setup skeleton
  -s, --stars           Fetch stars and generate stars.md
```

