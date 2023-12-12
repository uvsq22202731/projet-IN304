import re
def liste_hashtags(tweet):
    """Renvoie la liste contenant tous les #"""
    hashtags = re.findall(r"#\w+", tweet)   # re.findall trouve tous les hashtags de la forme # +un seul mot
    return hashtags


