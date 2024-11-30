import requests, time

    # options_url = URL to the file with settings (for online settings only)
    # feed_url    = URL of the RSS feed
    # webhook_url = URL of the Discord Webhook
options_url = "https://raw.githubusercontent.com/...../...../refs/heads/main/online_options.py"
feed_url    = "http://feeds.bbci.co.uk/news/rss.xml"
webhook_url = "https://discord.com/api/webhooks/123/webhook"


class dsc:
    def __init__(self, webhook, username, avatar_url, feed):
        self.webhook    = webhook
        self.username   = username
        self.avatar_url = avatar_url
        self.feed       = feed
        
    # GET the settings from the online source
    def init_settings(source):
        wh   = webhook_url
        feed = feed_url
        global whitelist, mentions, roles
        
        if source == "online":                              # Get settings from online file 
            r = requests.get(options_url).text.split(";")
            whitelist  = eval(r[0])
            username   = eval(r[1])
            avatar_url = eval(r[2])
            mentions   = eval(r[3])
            roles      = eval(r[4])

        else:                                               # Get settings from local file
            import options

            whitelist  = options.whitelist
            username   = options.username
            avatar_url = options.avatar_url
            mentions   = options.mentions
            roles      = options.roles

        return wh, username, avatar_url, feed
    
    # Filter through articles and send only whitelisted articles that are not older than 10 minutes
    def filter(self, s):
        sent = list(s)
        for entry in self.feed.entries:
            for allowed in whitelist:
                if (allowed.lower() in entry.title.lower() and allowed.lower() not in sent):
                    sent.append(allowed.lower())
                    print(f"""[{time.asctime()}] {entry.title}""")
                    self.sendmsg(entry)
                    
        return sent

    # POST the message to the Discord Webhook
    def sendmsg(self, data):
        headers = {"Content-Type": "application/json"}
        pings   = ""
        
        for user in mentions:
            titles = user[1]
            id     = user[0]
            for m in range(len(titles)):
                if whitelist[titles[m]].lower() in data.title.lower():
                    pings += f"""<@{id}> """
                    
        for role in roles:
            titles = role[1]
            id     = role[0]
            for m in range(len(titles)):
                if whitelist[titles[m]].lower() in data.title.lower():
                    pings += f"""<@&{id}> """

        content = f""">>> {pings}\n# [{data.title}](<{data.link}>)\n------------\n{data.description}""" # Discord message body
        payload = {
            "username": self.username,
            "content": content,
            "avatar_url": self.avatar_url,
        }
        
        return requests.post(url=self.webhook, headers=headers, json=payload)