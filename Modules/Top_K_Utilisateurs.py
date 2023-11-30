def Publications_par_Utilisateurs(data):
    """Compte le nombre de publications par utilisateur."""

    publications_par_utilisateur = {}

    for i in data:
        utilisateur = i["Utilisateur"]
        if utilisateur in publications_par_utilisateur:
            publications_par_utilisateur[utilisateur] += 1
        else:
            publications_par_utilisateur[utilisateur] = 1

    return publications_par_utilisateur


def Top_K_Users(publications_par_utilisateur, k):
    """Renvoie les k meilleurs utilisateurs en fonction du nombre de publications."""
    sorted_publications = sorted(publications_par_utilisateur.items(), key=lambda x: x[1], reverse=True)

    return sorted_publications[:k]