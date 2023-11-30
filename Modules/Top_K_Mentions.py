def topK_mentions(k,dictK_mentions) :
    """Renvoie les top K mentions"""
    top = list(dictK_mentions.items()) ## On créé une liste contenant les items du dictionnaire
    while k > len(top) : ## On teste si la valeur k donnée n'est pas supérieur au nombre de mentions que l'on a
        int(input(f"Désolé je ne peux pas t'imprimer le top {k} des mentions car il n'y en a que {len(top)}, donne moi un nombre + petit : ")) ## Si k supérieur au nombre de mentions alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"Voici le top {k} des mentions qui reviennent le + souvent : \n")
    for i in range(k) :
        print(f"- {i+1}) {top[i][0]} avec {top[i][1]} occurences.") ## On affiche le top K des mentions avec le nombres d'occurences à chaque fois

