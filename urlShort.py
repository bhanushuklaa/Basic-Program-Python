import pyshorteners

s = pyshorteners.Shortener
url = "https://thehackerish.com/best-hacking-websites-for-ethical-hackers/"

print(s.tinyurl.short(url))
