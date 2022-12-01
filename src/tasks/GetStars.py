import os

from src.utils.Logger import Logger
from src.utils.aoc_request import fetch_aoc_content
from src.utils.paths import get_stars_md_path

md_start = '''
## Overview for {}:

| Day | Star 1 | Star 2 |
| --- | ------ | ------ |'''

md_row = '| {} | {} | {} |'

class GetStars(Logger):
    def __init__(self, year, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.year=year
        self.leaderboard_id = os.getenv('LEADERBOARD_ID', None)
        self.member_id = os.getenv('MEMBER_ID', None)
        self.leaderboard = {}
        self.stars = {}
        self.name = None

        self.fetch_leaderboard()
        self.parse_leaderboard()
        self.generate_stars_md()

    def get_leaderboard_url(self):
        if self.leaderboard_id is None:
            raise Exception('Cannot fetch leaderboard without LEADERBOARD_ID in .env')
        self.debug(f'fetching leaderboard: {self.leaderboard_id}')
        return f'https://adventofcode.com/{self.year}/leaderboard/private/view/{self.leaderboard_id}.json'

    def fetch_leaderboard(self):
        r = fetch_aoc_content(url=self.get_leaderboard_url(), log_lvl=self.log_lvl)
        self.leaderboard = r.json()

    def bool_to_symbol(self, expr):
        return u'✅' if expr else u'❌'

    def parse_leaderboard(self):
        member_id = os.getenv('MEMBER_ID', None)
        if member_id is None:
            self.warn('MEMBER_ID not in .env, generating stars for owner of leaderboard')
            member_id = self.leaderboard['owner_id']
        current_leaderboard = self.leaderboard['members'][member_id]
        self.name = current_leaderboard['name']
        stars = {}
        for day, stars_in_day in current_leaderboard['completion_day_level'].items():
            stars[day] = {
                'first': self.bool_to_symbol('1' in stars_in_day),
                'second': self.bool_to_symbol('1' in stars_in_day)
            }
        self.stars = stars

    def generate_stars_md(self):
        with open(get_stars_md_path(year=self.year), 'w') as f:
            print(md_start.format(self.name), file=f)
            for day, stars in self.stars.items():
                print(md_row.format(day, stars.get('first', u'❌'), stars.get('second', u'❌')), file=f)
