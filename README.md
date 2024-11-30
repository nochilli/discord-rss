# Discord RSS Feed Notifier

## Overview

This code reads a RSS feed and sends a message to a given Discord webhook after filtering the articles from a whitelist. Users and roles can be pinged to notify them about the new content. This project can be used to track various RSS feeds or you can create your own feed using [morss.it](https://morss.it) and get updated whenever any site you choose posts a new article.

## Features

- Easy to understand code
- Choose which articles get sent
- Customisable refresh rate
- Customisable message body

## Requirements

Before you begin, ensure you have the following software installed:

- [Python](https://python.org) 3 or above

## Dependencies

This program uses three python modules

- `time`              – Time related functions
- `requests`          – HTTPS POST and GET commands
- `feedparser`        – Reads the RSS feed and parses it into an object


   Install them (if not already installed):

```bash
pip install time requests feedparser
```

## Installation

Clone the repository:

```bash
git clone https://github.com/nochilli/discord-rss.git
```

## Setup 

1. Add feed and webhook URLs in `discord.py` 
2. Edit `options.py` if you want local settings or `online_options.py` if you want to have the settings online
3. Change the value in line 6 in `main.py` to `"offline"` and skip steps 3 - 5 if you're not using the online settings file
4. `options_url` should be changed to the RAW link of the `online_options.py` file
5. Do this by uploading `online_options.py` after editing it, to any raw text hosting service or a public GitHub repo and paste it's raw link  
```py
options_url = "https://raw.githubusercontent.com/nochilli/discord-rss/refs/heads/main/online_options.py"
```
## Customisation

### Changing the refresh rate:

- Go to line 10 in `main.py` and change the value.
```py
refreshrate = 10  # Refresh rate in minutes
```
### Changing the message contents

- Change the value of line 74 in `discord.py`
```py
content = f""">>> {pings}\n# [{data.title}](<{data.link}>)\n------------\n{data.description}""" # Discord message body
```
`pings` contains both user and role mentions.

`data` is the feed object

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---