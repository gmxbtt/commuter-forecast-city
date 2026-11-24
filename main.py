#!/usr/bin/env python3
"""One-line weather forecast for Zembla, a city that isn't.

Writes the forecast to /output/entry.txt (UTF-8, one line, <=140 chars).
"""

import os

FORECAST = (
    "Zembla: light snow falling upwards, 4\u00b0C \u2014 buses on time, "
    "umbrellas useless, but your coffee stays warm all the way to work."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
