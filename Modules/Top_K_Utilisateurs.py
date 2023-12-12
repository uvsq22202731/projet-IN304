def Publications_par_Utilisateurs(data):
    """Compte le nombre de publications par utilisateur."""
    publications_par_utilisateur = {}
    for i in data:  # On parcourt tous les tweets
        utilisateur = i["Utilisateur"]
        if utilisateur in publications_par_utilisateur:     # Si utilisateur est déjà dans notre dictionnaire on ajoute 1 au nombres de publicationd
            publications_par_utilisateur[utilisateur] += 1
        else:
            publications_par_utilisateur[utilisateur] = 1   # Sinon on initialise à 1 son nombre de tweet

    return publications_par_utilisateur


def Top_K_Users(publications_par_utilisateur, k):
    """Renvoie les k meilleurs utilisateurs en fonction du nombre de publications."""
    sorted_publications = sorted(publications_par_utilisateur.items(), key=lambda x: x[1], reverse=True)    # Tri le nombre de publications par utilisateurs de façon décroissante

    return sorted_publications[:k]