from pathlib import Path

root_path = None


def get_root_path():
    return Path(Path(__file__).parent.parent.parent.resolve())


def get_year_path(year):
    return Path(get_root_path(), f'year{year}')


def get_day_path(year, day):
    return Path(get_year_path(year=year), f'day{day:02}')


def get_template_path():
    return Path(get_root_path(), 'template.py')


def get_stars_md_path(year):
    return Path(get_year_path(year=year), 'stars.md')
