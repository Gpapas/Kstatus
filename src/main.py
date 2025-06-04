"""Command line interface for organizing Bear notes."""
import argparse
import json
import sys
import requests
from .bear_api import BearAPI
from .organizer import (
    categorize_by_tag,
    categorize_by_title,
    categorize_by_date,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize Bear notes")
    parser.add_argument(
        "--by",
        choices=["tag", "title", "date"],
        default="tag",
        help="Categorization method",
    )
    parser.add_argument(
        "--date-key", default="created", help="Date field to use when --by date"
    )
    parser.add_argument(
        "--output",
        help="Path to file where JSON output will be written",
    )
    args = parser.parse_args()

    api = BearAPI()
    try:
        notes = api.get_notes()
    except requests.exceptions.HTTPError:
        print("failed to fetch notes")
        sys.exit(1)

    if args.by == "tag":
        categories = categorize_by_tag(notes)
    elif args.by == "title":
        categories = categorize_by_title(notes)
    else:
        categories = categorize_by_date(notes, date_key=args.date_key)

    result_json = json.dumps(categories, indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(result_json)
    else:
        print(result_json)


if __name__ == "__main__":
    main()
