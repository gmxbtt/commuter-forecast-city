# Charm the Commuter: Forecast a City That Isn't

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather, 140 characters at most, for a city that does not exist.

## The forecast

> Zembla: light snow falling upwards, 4°C — buses on time, umbrellas useless, but your coffee stays warm all the way to work.

123 characters. Zembla is invented; the snow falls the wrong way up, the
buses are somehow on time, and the one thing the commuter can count on is
warm coffee.

## Why this line

A forecast first, a joke second: the city is named up front, the weather
is the whole point, and the register stays that of a broadcast bulletin —
temperature, transport, one practical tip — only bent. The bent bits are
small and concrete (snow rising, a useless umbrella) so the line reads in
one breath at a rainy bus stop, and it ends on the commuter's side: the
coffee stays warm all the way to work.

## How it works

`main.py` writes the forecast to `/output/entry.txt` — a single UTF-8 line,
no trailing newline, well inside the 140-character cap.

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

- Competition: [Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
- License: MIT
