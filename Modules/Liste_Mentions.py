import re
def liste_mentions(tweet):
    """Renvoie la liste contenant tous les @"""
    mentions = re.findall(r"@\w+", tweet)   # re.findall trouve toutes les mentions de la forme @ +un seul mot
    return mentions