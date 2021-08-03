#!/home/bruhh/current_build/blog/scripts/venv/bin/python

# donna is going to help us automate the writing of file name and the content.

# make it working in the most broke way possible
# name of the file, takes today date to write the name.
import argparse
import os
from datetime import datetime

import frontmatter


START_DATE = datetime(year=2021, month=7, day=13)


def format_title(title: str) -> str:
    title = '"' + title + '"'
    return title


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create new file and add content')
    parser.add_argument('--title', dest='title', type=str, required=True, help='title of the file')
    parser.add_argument('--ext', dest='ext', default='markdown', type=str, help='extension of the file')
    parser.add_argument('--cat', dest='category', type=str, default='competitive-programming', help='category of the post')
    parser.add_argument('--day', dest='day', action='store_true')
    args = parser.parse_args()

    # today's date in YYYY-MM-DD format
    now = datetime.now()
    today_date = now.strftime('%Y-%m-%d')

    # title
    title = args.title
    title = '-'.join(title.lower().split())

    day_num = (now - START_DATE).days

    if args.day:
        filename = '-'.join((today_date, f'day-{day_num}', title))
    else:
        filename = '-'.join((today_date, title))
    filename = filename + '.' + args.ext

    title = args.title.title()

    if args.day:
        title = f'Day {day_num}: {title}'

    if os.path.exists(filename):
        raise FileExistsError(f'{filename} already exists. Please choose different title.')

    # write new content in the file
    with open(filename, 'w') as f:
        f.write('---\n')
        metadata = {
            'layout': 'post',
            'title': format_title(title),
            'date': f'{today_date} +0530',
            'categories': args.category,
        }
        for k, v in metadata.items():
            f.write(f'{k}: {v}\n')
        f.write('---\n')
