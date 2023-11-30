import re
def liste_hashtags(tweet):
    """Renvoie la liste contenant tous les #"""
    hashtags = re.findall(r"#\w+", tweet)
    return hashtags


