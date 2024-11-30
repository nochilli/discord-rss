import feedparser, time
from discord import dsc

    # use dsc.init_settings("offline") if you're using options.py 
    # use dsc.init_settings("online") for online settings sync
webhook, username, avatar_url, feed_url = dsc.init_settings("online")

sent = ""; prev = ""; x = 1

refreshrate = 10                                # Refresh rate in minutes

feed = feedparser.parse(feed_url)
hook = dsc(webhook, username, avatar_url, feed)

print(f"""[{time.asctime()}] Got {len(feed.entries)} articles from {"".join(feed_url.split("//")[1]).split("/")[0]}""")

while 1:
    feed = feedparser.parse(feed_url)
    
    if feed.entries != prev:                    # skip if feed hasn't been updated
        sent = list(hook.filter(sent))
        prev = feed.entries
        time.sleep(2)
    else:
        print(f"""[{time.asctime()}] No New Articles""")
    
    x += 1
    time.sleep(refreshrate * 60)

    if x == (18 * 60 / refreshrate):            # Reset sent messages list once in 18h
        sent = ""
        x = 1