def topK_hashtags(k,dictK_hashtags) :
    """Renvoie les top K hashtags"""
    top = list(dictK_hashtags.items()) ## On créé une liste contenant les items du dictionnaire
    while k > len(top) : ## On teste si la valeur k donnée n'est pas supérieur au nombre d'hashtags que l'on a
        int(input(f"Désolé je ne peux pas t'imprimer le top {k} des hashtags car il n'y en a que {len(top)}, donne moi un nombre + petit : ")) ## Si k supérieur au nombre d'hashtags alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"Voici le top {k} des hashtags qui reviennent le + souvent : \n")
    for i in range(k) :
        print(f"- {i+1}) {top[i][0]} avec {top[i][1]} occurences.") ## On affiche le top K des hashtags avec le nombres d'occurences à chaque fois
