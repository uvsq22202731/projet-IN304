def Tweets_Utilisateur(data, utilisateur_cible):
    """Récupère tous les tweets d'un utilisateur spécifique."""
    tweets = []
    for entry in data:
        if entry["Utilisateur"] == utilisateur_cible:
            tweets.append(entry["TweetText"])
    if len(tweets) == 0:
        return [], f"Aucun tweet trouvé pour l'utilisateur {utilisateur_cible}."

    return tweets, None