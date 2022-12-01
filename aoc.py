from datetime import date
from pathlib import Path
import requests
import os
from dotenv import load_dotenv

DEBUG = 0
INFO = 1
WARN = 2
ERROR = 3


def get_date():
    return date.today().day


def get_year():
    return date.today().year


class Logger:
    def __init__(self, log_lvl=INFO):
        self.log_lvl = log_lvl

    def log(self, msg, lvl=INFO):
        if lvl >= self.log_lvl:
            print(msg)

    def debug(self, msg):
        self.log(msg=msg, lvl=DEBUG)

    def info(self, msg):
        self.log(msg=msg, lvl=INFO)

    def warn(self, msg):
        self.log(msg=msg, lvl=WARN)

    def error(self, msg):
        self.log(msg=msg, lvl=ERROR)

    def always_log(self, msg):
        self.log(msg=msg, lvl=99)


class SetupDay(Logger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date = get_date()
        self.year = get_year()
        self.setup_skeleton()
        self.load_input()
        self.log_todays_url()
        self.always_log('Done!')

    def get_root_path(self):
        return Path(Path(__file__).parent.resolve())

    def get_template_path(self):
        return Path(self.get_root_path(), 'template.py')

    def get_year_path(self):
        return Path(self.get_root_path(), f'year{self.year}')

    def get_today_path(self):
        return Path(self.get_year_path(), f'day{self.date:02}')

    def log_todays_url(self):
        url = f'https://adventofcode.com/{self.year}/day/{self.date}'
        self.always_log(f'For today\'s challenge, see: {url}')

    def make_year_folder(self):
        year_path = self.get_year_path()
        if year_path.exists() and year_path.is_dir():
            self.info('This years folder already exists, not creating')
        else:
            self.debug('Should make year folder now')
            Path.mkdir(year_path)

    def make_day_folder(self):
        today_path = self.get_today_path()
        if today_path.exists() and today_path.is_dir():
            self.warn('Today\'s folder exists, not creating')
        else:
            self.debug('Should make day folder now')
            Path.mkdir(today_path)

    def get_template(self):
        template_path = self.get_template_path()
        self.debug(f'reading template from {template_path}')
        with open(template_path, 'r') as f:
            template = f.read()
        return template

    def make_main_py_file(self):
        today_path = self.get_today_path()
        main_py_path = Path(today_path, 'main.py')
        if main_py_path.exists() and main_py_path.is_file():
            self.warn('Today\'s main.py already exists, not creating')
        else:
            self.debug('Making main.py now')
            Path.touch(main_py_path)
            self.debug('Writing template to main.py now')
            with open(main_py_path, 'w') as f:
                print(self.get_template(), file=f)

    def setup_skeleton(self):
        self.make_year_folder()
        self.make_day_folder()
        self.make_main_py_file()

    def fetch_input_content(self):
        url = f'https://adventofcode.com/{self.year}/day/{self.date}/input'
        session = os.getenv('AOC_SESSION', None)
        cookies = {
            'session': session
        }
        self.debug(f'Reading from {url} with session: {session}')
        r = requests.get(url, cookies=cookies)
        return r.text

    def load_input(self):
        today_path = self.get_today_path()
        input_path = Path(today_path, 'input.txt')
        if input_path.exists() and input_path.is_file():
            self.warn('Today\'s input already exists, not fetching')
            return

        self.debug('Should fetch input-file now')
        input_content = self.fetch_input_content()
        Path.touch(input_path)
        with open(input_path, 'w') as f:
            print(input_content, file=f)


if __name__ == '__main__':
    load_dotenv()
    SetupDay(log_lvl=WARN)
