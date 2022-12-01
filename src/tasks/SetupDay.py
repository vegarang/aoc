from pathlib import Path

from src.utils.Logger import Logger
from src.utils.aoc_request import fetch_aoc_content
from src.utils.paths import get_day_path, get_root_path, get_template_path, get_year_path


class SetupDay(Logger):
    def __init__(self, year, day, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root_path = None
        self.day = day
        self.year = year
        self.setup_skeleton()
        self.load_input()
        self.log_todays_url()
        self.always_log('Done!')

    def get_root_path(self):
        if not self.root_path:
            self.debug(f'setting root-path: {self.root_path}')
            self.root_path = get_root_path()
        return self.root_path

    def get_year_path(self):
        return get_year_path(year=self.year)

    def get_today_path(self):
        return get_day_path(year=self.year, day=self.day)

    def log_todays_url(self):
        url = f'https://adventofcode.com/{self.year}/day/{self.day}'
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
        template_path = get_template_path()
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
        url = f'https://adventofcode.com/{self.year}/day/{self.day}/input'
        r = fetch_aoc_content(url=url, log_lvl=self.log_lvl)
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