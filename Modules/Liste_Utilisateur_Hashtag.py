import re
import Liste_Hashtags
def utilisateurs_mentionnant_hashtag(data, hashtag_specifique):
    """Renvoie tous les utilisateurs utilisant un hashtag"""
    utilisateurs_mentionnants = []
    for entry in data:
        hashtags_du_tweet = Liste_Hashtags.liste_hashtags(entry["TweetText"])
        hashtag_pattern = re.compile(fr"#{re.escape(hashtag_specifique)}\b", re.IGNORECASE)
        #  fr, permet d'ajouter des expressions python dans une chaîne de caractères
        #  {re.escape(hashtag_specifique)}, supprime tous les caractères spéciaux génant après le #
        #  \b, permet de garder qu'un seul mot, ça ne prend pas en compte la suite

        if any(hashtag_pattern.search(hashtag) for hashtag in hashtags_du_tweet):   #  Vérifier si le hashtag spécifique est présent dans la liste des hashtags du tweet
            utilisateurs_mentionnants.append(entry["Utilisateur"])

    return utilisateurs_mentionnants