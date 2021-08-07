#!/home/bruhh/current_build/blog/scripts/venv/bin/python

# donna is going to help us automate the writing of file name and the content.

# make it working in the most broke way possible
# name of the file, takes today date to write the name.
import argparse
import os
import re
from datetime import datetime

import frontmatter

START_DATE = datetime(year=2021, month=7, day=13)


def format_title(title: str) -> str:
    title = '"' + title + '"'
    return title


def create_new_file(args: argparse.Namespace) -> None:
    # today's date in YYYY-MM-DD format
    now = datetime.now()
    today_date = now.strftime("%Y-%m-%d")

    # title
    title = args.title
    title = "-".join(title.lower().split())

    # number of days elapsed from START_DATE
    no_of_days = (now - START_DATE).days

    if args.day:
        filename = "-".join((today_date, f"day-{no_of_days}", title))
    else:
        filename = "-".join((today_date, title))
    filename = filename + "." + args.ext

    title = args.title.title()

    if args.day:
        title = f"Day {no_of_days}: {title}"

    if os.path.exists(filename):
        raise FileExistsError(f"{filename} already exists. Please choose different title.")

    # write new content in the file
    with open(filename, "w") as f:
        f.write("---\n")
        metadata = {
            "layout": "post",
            "title": format_title(title),
            "date": f"{today_date} +0530",
            "categories": args.category,
        }
        for k, v in metadata.items():
            f.write(f"{k}: {v}\n")
        f.write("---\n")


def update_current_file(args: argparse.Namespace) -> None:
    filename = args.filename

    # checks
    # - the new file to be create is not already present
    # Check if the given file is present
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"{filename} doesn't exists")

    now = datetime.now()
    today_date = now.strftime("%Y-%m-%d")

    no_of_days = (now - START_DATE).days

    # update the date
    # format : year-month-day-{file-name}.markdown
    *_, name = filename.split("-", maxsplit=3)

    pattern = r"(day)\-\d+(\-.*)"
    # subsitute
    name = re.sub(pattern, f"\\1-{no_of_days}\\2", name)

    new_filename = "-".join((today_date, name))

    if os.path.exists(new_filename):
        raise FileNotFoundError(f"{new_filename} already exists. Cannot update.")

    os.rename(filename, new_filename)

    # if 'Day X' is also present then update that also
    post = frontmatter.load(new_filename)
    metadata = post.metadata
    content = post.content

    # title pattern
    tpattern = r"(Day)\s\d+(\: .*)"
    metadata["title"] = re.sub(tpattern, f"\\1 {no_of_days}\\2", metadata["title"])

    metadata["date"] = f"{today_date} +0530"
    metadata["title"] = format_title(metadata["title"])
    # write new content in the file
    with open(new_filename, "w") as f:
        f.write("---\n")
        for k, v in metadata.items():
            f.write(f"{k}: {v}\n")
        f.write("---\n")
        f.write(content)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create new file and add content")

    subparsers = parser.add_subparsers(dest="subparser_name")

    # create subparser
    create = subparsers.add_parser("create", help="create new post")
    create.add_argument("--title", dest="title", type=str, required=True, help="title of the file")
    create.add_argument("--ext", dest="ext", default="markdown", type=str, help="extension of the file")
    create.add_argument("--cat", dest="category", type=str, default="competitive-programming", help="category of the post")
    create.add_argument("--day", dest="day", action="store_true")

    # update subparser
    upd = subparsers.add_parser("upd", help="update the post date to today")
    upd.add_argument("filename", type=str, help="name of file to be updated")
    return parser


def main() -> None:
    parser = create_parser()

    args = parser.parse_args()

    if args.subparser_name == "create":
        create_new_file(args)
    elif args.subparser_name == "upd":
        update_current_file(args)


if __name__ == "__main__":
    main()
