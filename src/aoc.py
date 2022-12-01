from dotenv import load_dotenv
import argparse

from src.tasks.GetStars import GetStars
from src.tasks.SetupDay import SetupDay
from src.utils.date import get_date, get_year

load_dotenv()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v',
        '--verbosity',
        type=int,
        choices=[0, 1, 2, 3],
        default=2,
        help='How verbose should the logging be? Lower number means more logs. Default (2): warn and error only')
    parser.add_argument(
        '-y',
        '--year',
        type=int,
        default=get_year(),
        help='what year to get challenges for (default: current)')
    parser.add_argument(
        '-d',
        '--day',
        type=int,
        default=get_date(),
        help='what day to get challenges for (default: current)')
    parser.add_argument('-f', '--fetch', action='store_true', help='Fetch task and setup skeleton')
    parser.add_argument('-s', '--stars', action='store_true', help='Fetch stars and generate stars.md')
    args = parser.parse_args()
    if args.fetch:
        SetupDay(log_lvl=args.verbosity, year=args.year, day=args.day)
    if args.stars:
        GetStars(log_lvl=args.verbosity, year=args.year)
