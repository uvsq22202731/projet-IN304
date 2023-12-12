def Tweets_Utilisateur(data, utilisateur_cible):
    """Récupère tous les tweets d'un utilisateur spécifique."""
    tweets = []
    for entry in data:  # On parcourt chaque tweet un à un
        if entry["Utilisateur"] == utilisateur_cible:   # Si l'utilisateur recherché est trouvé
            tweets.append(entry["TweetText"])    # On ajoute le tweets à notre liste
    if len(tweets) == 0:
        return [], f"Aucun tweet trouvé pour l'utilisateur {utilisateur_cible}."    # Sinon on retourne ce message

    return tweets, None