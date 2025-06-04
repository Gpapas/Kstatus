from collections import defaultdict
from typing import List, Dict


def categorize_by_tag(notes: List[Dict]) -> Dict[str, List[Dict]]:
    """Group notes by their first tag."""
    categories: Dict[str, List[Dict]] = defaultdict(list)
    for note in notes:
        tags = note.get("tags", [])
        key = tags[0] if tags else "untagged"
        categories[key].append(note)
    return categories


def categorize_by_title(notes: List[Dict]) -> Dict[str, List[Dict]]:
    """Group notes alphabetically by their title."""
    categories: Dict[str, List[Dict]] = defaultdict(list)
    for note in notes:
        title = note.get("title", "").strip()
        key = title[0].upper() if title else "?"
        categories[key].append(note)
    return categories


def categorize_by_date(notes: List[Dict], date_key: str = "created") -> Dict[str, List[Dict]]:
    """Group notes by a date field (created or modified)."""
    categories: Dict[str, List[Dict]] = defaultdict(list)
    for note in notes:
        date = note.get(date_key, "unknown")
        categories[str(date)].append(note)
    return categories
