import re
def utilisateurs_mentionnes_par_utilisateur(data, utilisateur_specifique):
    """Renvoie les utilisateurs mentionnés par l'utilisateur specifique"""
    utilisateurs_mentionnes = set()    #  Création d'un set afin d'éliminer les doublons
    for entry in data:
        if re.search(fr'\b{re.escape(utilisateur_specifique)}\b', entry["TweetText"], flags=re.IGNORECASE):    #  Vérifie si l'utilisateur spécifique est mentionné dans le tweet
            utilisateurs_mentionnes.add(entry["Utilisateur"])   #  Ajoute l'utilisateur du tweet à la liste
    return list(utilisateurs_mentionnes)    #  Retourne la liste des utilisateurs mentionnés