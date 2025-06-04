# Kstatus

A simple command-line tool for organizing notes stored in the [Bear](https://bear.app/) application. Notes can be grouped by tag, title, or date using the Bear API.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variables for the Bear API:
   - `BEAR_API_URL` - Base URL of the Bear API (defaults to `https://api.bear.app`).
   - `BEAR_API_TOKEN` - Personal access token used for authentication.

## Usage

Run the command-line tool from the project root:

```bash
python -m src.main --by tag          # group notes by their first tag
python -m src.main --by title        # group notes alphabetically by title
python -m src.main --by date --date-key modified   # group by modified date
```

The command prints categorized notes in JSON format.
