"""Command line interface for organizing Bear notes."""
import argparse
import json
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
    args = parser.parse_args()

    api = BearAPI()
    notes = api.get_notes()

    if args.by == "tag":
        categories = categorize_by_tag(notes)
    elif args.by == "title":
        categories = categorize_by_title(notes)
    else:
        categories = categorize_by_date(notes, date_key=args.date_key)

    print(json.dumps(categories, indent=2))


if __name__ == "__main__":
    main()
