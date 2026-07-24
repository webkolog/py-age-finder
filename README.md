# PY Age Finder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
**Version:** 1.0

**Created Date:** 2026-07-22

**Last Updated:** 2026-07-22

**Compatibility:** Python 3.x

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

**PY Age Finder** is a precise, lightweight Python 3 script designed to calculate a person's exact age via the command line. Unlike simple calendar-year subtractions, this utility checks whether the birth day and month have actually arrived in the current year, ensuring an accurate real-age result.

## Features
- Accurately tracks precise age considering months and days.
- Zero external package dependencies (uses Python's built-in `datetime`).
- Fast and clean interactive command-line interface (CLI).

## Installation

### Prerequisites
Make sure you have Python 3.x installed on your system. You can check your version by running:
```bash
python --version

```

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/webkolog/py-age-finder.git
cd py-age-finder

```

## Usage

Simply run the script using Python:

```bash
python age_finder.py

```

### How it Works

1. The program prompts you to enter your birth day (1-31), month (1-12), and year.
2. It fetches the current system date using `datetime.now()`.
3. It performs a logical check: if the current month/day is behind the birth month/day, it subtracts 1 from the calculated year difference to reflect your true age.
4. Outputs the final accurate age directly to the console.

## Code Preview

```python
from datetime import datetime

# Get day, month and year information
birth_day = int(input("Enter your birth day (1-31): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_year = int(input("Enter your birth year: "))

# Current date
today = datetime.now()

# Calculate the approximate difference in years
age = today.year - birth_year

# Month and day check:
# If the birth month hasn't arrived yet, or if we are in the birth month but the day hasn't arrived yet, we subtract 1 from the age
if (today.month < birth_month) or (today.month == birth_month and today.day < birth_day):
    age -= 1

print("Your real age:", age)

```

## Dependencies

This project operates purely on core Python standard libraries and requires no third-party installations or libraries.

## License

This PY Age Finder script is open-source software licensed under the [MIT license](https://mit-license.org/).

```text
MIT License

Copyright (c) 2026 Ali Candan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements (such as adding GUI support, localization, or time-zone handling), please feel free to open an issue or submit a pull request on the GitHub repository.

## Support

For any questions or support regarding the PY Age Finder, you can refer to the project's GitHub repository issues or contact the author.
