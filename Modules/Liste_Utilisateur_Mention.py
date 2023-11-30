import re
import Liste_Mentions
def Tweets_Mentionnant_Utilisateur(data, utilisateur_mentionne):
    """Renvoie les tweets ou l'utilisateur donné est mentionné"""
    tweets_mentionnant = []

    for entry in data:
        # Utiliser la fonction liste_mentions pour extraire toutes les mentions dans le texte du tweet
        mentions_du_tweet = Liste_Mentions.liste_mentions(entry["TweetText"])

        # Utiliser une expression régulière pour rechercher la mention dans le texte du tweet
        mention_pattern = re.compile(fr"@{utilisateur_mentionne}\b", re.IGNORECASE)
        if mention_pattern.search(entry["TweetText"]) or utilisateur_mentionne.lower() in map(str.lower, mentions_du_tweet):
            tweets_mentionnant.append(entry["TweetText"])

    return tweets_mentionnant