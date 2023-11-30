import re
def liste_mentions(tweet):
    """Renvoie la liste contenant tous les @"""
    mentions = re.findall(r"@\w+", tweet)
    return mentions