import re
import Liste_Mentions
def Tweets_Mentionnant_Utilisateur(data, utilisateur_mentionne):
    """Renvoie les tweets ou l'utilisateur donné est mentionné"""
    tweets_mentionnant = []
    for entry in data:  # On parcourt tous les tweets
        mentions_du_tweet = Liste_Mentions.liste_mentions(entry["TweetText"])   # On prends les différentes mentions du tweet dans une liste
        mention_pattern = re.compile(fr"@{utilisateur_mentionne}\b", re.IGNORECASE) # re.compile recherche une mention dans le tweet de la forme @'nom de l'utilisateur que l'on cherche'
        if mention_pattern.search(entry["TweetText"]) or utilisateur_mentionne.lower() in map(str.lower, mentions_du_tweet):    # si l'utilisateur spécifique est mentionné soit directement dans le texte du tweet, soit parmi les mentions extraites du texte du tweet
            tweets_mentionnant.append(entry["TweetText"])   # On ajoute ce tweet à notre liste des tweets

    return tweets_mentionnant