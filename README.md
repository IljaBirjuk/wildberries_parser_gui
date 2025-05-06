# Wildberries Product Parser (GUI)

This is a Python application that parses product data from [wildberries.ru](https://www.wildberries.ru) based on a search query and saves the result into a CSV file.

The script uses a graphical user interface (GUI) for easy interaction — just type your keyword (e.g. "платье", "кроссовки") and it will collect product data across multiple pages.

## Features

- Search for any product (e.g. shoes, dresses, coats)
- Parses:
  - Product title
  - Price (in RUB)
  - Number of reviews
  - Average rating
  - Direct link to product page
- Saves data to CSV
- Handles multiple pages
- Logs errors into errors.log
- Easy-to-use GUI

## How to Run

1. Make sure Python 3.10+ is installed
2. No external libraries are required (only standard modules)
3. Run the script:
```bash
python wb_gui_parser.py
