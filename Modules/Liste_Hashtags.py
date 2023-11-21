import json
import re



def liste_hashtags(tweet) : ## on prend le tweet en argument
    temp = 0     ## Initialisation d'une variable temporaire qu'on utilisera pour traiter les hashtags
    liste_h = []      ## On initialise la liste qui va contenier les différents hashtags ou pas
    if "#" in tweet :     ## Tout d'abord, on vérifie la présence d'hashtags dans la publication
        split = tweet.split()     ## Si il y en a, alors on utilise .split() pour séparer les mots du tweet
        for elmnt in split :     ## On parcoure tous les mots du tweet
            if "#" in elmnt and elmnt[0] == "#" :    ## Premier cas, si il y a un # dans le mot, c'est un des hashtag du tweet (la 2ème condition ici sert à traiter les hashtags précédés d'aucun caractère avant donc le mot commence bien par un "#")
                for c in elmnt[1:] :     ## On parcoure la chaîne de caractère du hashtag
                    if (c not in list_min and c not in list_maj and c not in list_nb)  :    ## On teste si le caractère est un chiffre ou une lettre (miniscule ou majuscule) 
                        temp = 1     ## variable temporaire à 1 si un caractère remplit les conditions
                        hash = elmnt.split(c)     ## On sépare notre mot avec split() et comme argument le caractère spécial en question car on ne veut que l'hashtag pas de caractère spécial après
                        break    ## Ainsi on stoppe la boucle for quand on l'a trouvé 
                if temp == 1 and hash[0] != "#" : ## Si temp == 1 alors on est passé dans le if et on a split, la deuxième condition sert à ne pas prendre les hashtags tout seul sans mot après
                        liste_h.append(hash[0].lower()) ## On append donc le 1er élément de la liste (split) car notre hashtag n'est précédé par d'autres caractères donc le split se fera au premier chr spécial qui arrivera apres le hashtag 
                if temp != 1 and elmnt != "#…" : ## Sinon, je ne suis pas rentrer dans la liste càd pas de caractère spécial dans le mot contenant le hashtag
                    liste_h.append(elmnt.lower()) ## On l'append (à noter qu'on utilise lower() pour que les hashtags soit tous en miniscules et qu'on puisse les comparer facilement)
            elif "#" in elmnt and elmnt[0] != "#" : ## Deuxième cas, si le mot contient un "#" mais qu'il ne commence pas par ce dernier donc par un caractère spe tel que , ou par une parenthèse etc
                for c in elmnt : ## On parcoure chaque caractère du mot
                    if c == "#" : ## On teste si le caractère correspond au hashtag
                        i = elmnt.index(c) ## Si oui, alors je prends son indice dans le mot avec index()
                        hash2 = elmnt.split(elmnt[i-1]) ## Et je split au caractère juste avant pour le séparer du hashtag
                        break ## Je stoppe ma boucle si je l'ai trouvé 
                for h in hash2 : ## Ensuite je parcoure ma liste split pour faire comme dans le 1er cas càd dans spliter si le hashtag est suivi d'un caractère spécial que je ne veux pas
                    if "#" in h : ## On teste si l'élément dans ma liste corresponds au hashtag
                        for c in h : ## Si oui alors je parcours chaque caractère du mot 
                            if c not in list_min and c not in list_maj and c not in list_nb and c != "#" : ## Le if ici est pour savoir si le hashtag est suivi d'un caractère spécial, et on vérifie que ce caractère n'est pas un hashtag
                                temp = 2 ## Si oui, variable temp à 2
                                hash_final = h.split(c) ## Et je split au caractère spécial
                                break ## Je stoppe une fois le caractère trouvé
                        if temp == 2 : ## Si temp == 2 , alors je suis rentré dans le if
                            liste_h.append(hash_final[0].lower()) ## On append donc le 1er élément du split car notre hashtag n'est précédé par d'autres caractères donc le split se fera au premier chr spécial qui arrivera apres le hashtag
                        if temp != 2 : ## Sinon, je ne suis pas rentrer dans la liste càd pas de caractère spécial dans le mot contenant le hashtag
                            liste_h.append(h.lower()) ## On l'append normalement

    return liste_h 


list_nb = [str(i) for i in range(0,10)]  ## liste contenant les 10 premiers nombres 
list_maj = [chr(i) for i in range(65,91)]  ## liste contenant les 26 majuscules
list_min =  [chr(i) for i in range(97,123)] + ["-","_"]  ## liste contenant les 26 miniscules


