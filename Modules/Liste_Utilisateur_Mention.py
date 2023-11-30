import re
import Liste_Mentions
def Tweets_Mentionnant_Utilisateur(data, utilisateur_mentionne):
    """Renvoie les tweets ou l'utilisateur donné est mentionné"""
    tweets_mentionnant = []
    for entry in data:
        mentions_du_tweet = Liste_Mentions.liste_mentions(entry["TweetText"])
        mention_pattern = re.compile(fr"@{utilisateur_mentionne}\b", re.IGNORECASE)
        if mention_pattern.search(entry["TweetText"]) or utilisateur_mentionne.lower() in map(str.lower, mentions_du_tweet):    # si l'utilisateur spécifique est mentionné soit directement dans le texte du tweet, soit parmi les mentions extraites du texte du tweet
            tweets_mentionnant.append(entry["TweetText"])

    return tweets_mentionnant