import json
import re
from textblob import TextBlob

def del_caractere_spe(lastline):
    """Supprime les caractères spéciaux, type émojis"""
    last = json.loads(lastline)  # On lit notre ligne en tant que fichier json, ce qui la convertit en dictionnaire
    lastsanscarac = last["TweetText"].encode('utf8','ignore')  # On prend le tweet et on l'encode en UTF8 en ignorant les autres caractères
    convertstr = lastsanscarac.decode('utf8')  # On decode notre texte sans smileys, en utf 8
    c = convertstr.replace("\n\n"," ").replace("\n","")  # On retire tous les sauts de ligne, si c'est deux saut de ligne d'affilé on met un espace sinon non
    texte_nettoye = re.sub(r'[^\w\s.,!?;:()"\'@#/-]', '', c)  # On garde seulement tous les alphabet, ainsi que certains caractères spéciaux
    #  [^...] correspond à la recherche de tous les élément compris dans les crochets, les autres seront supprimés
    #  \w correspond à tous les caractères des différents alphabet
    #  \s correspond à tous les espacement, tabulation, saut de ligne, etc..
    #  Le reste de l'expression correspond au caractère que l'on veut garder
    last['TweetText'] = texte_nettoye  # On remplace le texte du tweet par celui sans caractère spéciaux
    return last

## Extraire la liste des hashtags de la publication :

def liste_hashtags(tweet) : ## on prend le tweet en argument
    """Fonctions prenant en argument la liste des tweet, et qui renvoie la liste de tous les hashtags de tous les tweets."""
    temp = 0     ## Initialisation d'une variable temporaire qu'on utilisera pour traiter les hashtags
    liste_h = []      ## On initialise la liste qui va contenier les différents hashtags ou pas
    if "#" in tweet :     ## Tout d'abord, on vérifie la présence d'hashtags dans la publication
        split = tweet.split()     ## Si il y en a, alors on utilise .split() pour séparer les mots du tweet
        for elmnt in split :     ## On parcoure tous les mots du tweet
            if "#" in elmnt and elmnt[0] == "#" :    ## Premier cas, si il y a un # dans le mot, c'est un des hashtag du tweet (la 2ème condition ici sert à traiter les hashtags précédés d'aucun caractère avant donc le mot commence bien par un "#")
                for c in elmnt[1:] :     ## On parcoure la chaîne de caractère du hashtag
                    if (c not in list_min and c not in list_maj and c not in list_nb)  :    ## On teste si le caractère est un chiffre ou une lettre (miniscule ou majuscule) 
                        temp = 1     ## variable temporaire à 1 si un caractère remplit les conditions
                        hash = elmnt.split(c)  ## On sépare notre mot avec split() et comme argument le caractère spécial en question car on ne veut que l'hashtag pas de caractère spécial après
                        break    ## Ainsi on stoppe la boucle for quand on l'a trouvé 
                if temp == 1 and hash[0] != "#" :  ## Si temp == 1 alors on est passé dans le if et on a split, la deuxième condition sert à ne pas prendre les hashtags tout seul sans mot après
                        liste_h.append(hash[0].lower())  ## On append donc le 1er élément de la liste (split) car notre hashtag n'est précédé par d'autres caractères donc le split se fera au premier chr spécial qui arrivera apres le hashtag 
                if temp != 1 and elmnt != "#…" :  ## Sinon, je ne suis pas rentrer dans la liste càd pas de caractère spécial dans le mot contenant le hashtag
                    liste_h.append(elmnt.lower())  ## On l'append (à noter qu'on utilise lower() pour que les hashtags soit tous en miniscules et qu'on puisse les comparer facilement)
            elif "#" in elmnt and elmnt[0] != "#" :  ## Deuxième cas, si le mot contient un "#" mais qu'il ne commence pas par ce dernier donc par un caractère spe tel que , ou par une parenthèse etc
                for c in elmnt :  ## On parcoure chaque caractère du mot
                    if c == "#" :  ## On teste si le caractère correspond au hashtag
                        i = elmnt.index(c)  ## Si oui, alors je prends son indice dans le mot avec index()
                        hash2 = elmnt.split(elmnt[i-1])  ## Et je split au caractère juste avant pour le séparer du hashtag
                        break  ## Je stoppe ma boucle si je l'ai trouvé 
                for h in hash2 :  ## Ensuite je parcoure ma liste split pour faire comme dans le 1er cas càd dans spliter si le hashtag est suivi d'un caractère spécial que je ne veux pas
                    if "#" in h :  ## On teste si l'élément dans ma liste corresponds au hashtag
                        for c in h : ## Si oui alors je parcours chaque caractère du mot 
                            if c not in list_min and c not in list_maj and c not in list_nb and c != "#" :  ## Le if ici est pour savoir si le hashtag est suivi d'un caractère spécial, et on vérifie que ce caractère n'est pas un hashtag
                                temp = 2  ## Si oui, variable temp à 2
                                hash_final = h.split(c)  ## Et je split au caractère spécial
                                break  ## Je stoppe une fois le caractère trouvé
                        if temp == 2 :  ## Si temp == 2 , alors je suis rentré dans le if
                            liste_h.append(hash_final[0].lower())  ## On append donc le 1er élément du split car notre hashtag n'est précédé par d'autres caractères donc le split se fera au premier chr spécial qui arrivera apres le hashtag
                        if temp != 2 :  ## Sinon, je ne suis pas rentrer dans la liste càd pas de caractère spécial dans le mot contenant le hashtag
                            liste_h.append(h.lower())  ## On l'append normalement

    return liste_h 



## Extraire la liste des mentions de la publication :

def liste_mentions(tweet) :  ## On prend le tweet en argument
    """Fonctions prenant en argument la liste des tweet, et qui renvoie la liste de toutes les mentions de tous les tweets."""
    temp = 0  ## On initialise temp à 0
    liste_m = []  ## On initialise une liste vide, qui va contenir les différentes mentions
    if "@" in tweet :  ## On vérifie s'il y a des @ dans le tweet
        split = tweet.split()  ## On utilse .split pour séparer chaque mots du tweet
        for elmnt in split :  ## On parcourt tous les mots du tweet
            if "@" in elmnt and elmnt[0] == "@" :  ## Si il y a un arobase dans le mot
                for c in elmnt[1:] :  ## On parcourt lettre par lettre le mot
                    if c not in list_maj and c not in list_min and c not in list_nb :  ## Si c n'est pas une lettre, une majuscule ou un chiffre
                        temp = 1  ## temp égal à 1
                        mention = elmnt.split(c)  ## On sépare notre mot quand on a trouvé notre @
                        break  ## On sort de la boucle une fois la mention trouvée
                if temp == 1 and mention[0] != "@" :  ## Si on a trouvé un @ met qu'il n'y a pas de nom à la suite
                    liste_m.append(mention[0])  ## On append le premier element de notre liste split
                if temp != 1 and elmnt != "@…" :  ## Si il n'y a pas de caractères spéciaux dans le @
                    liste_m.append(elmnt)  ## On l'append
            elif "@" in elmnt and elmnt[0] != "@" :  ## Si notre element contient un @ mais qu'il commence par un . , (), etc... 
                for c in elmnt :  ## On parcourt chaque caractère de l'element
                    if c == "@" :  ## Si on trouve une mention
                        i = elmnt.index(c)  ## i est égal à l'index d'où se trouve l'arobase
                        mention2 = elmnt.split(elmnt[i-1])  ## On split au caractère juste avant pour le séparer du @
                        break  ## On sort de la boucle
                for m in mention2 :  ## Ensuite on parcourt notre mention pour spliter si jamais la mention est suivi d'un caractère indésirables
                    if "@" in m :  ## Si on trouve l'@
                        for c in m :  ## Si oui je parcourt chaque caractère du mot
                            if c not in list_min and c not in list_maj and c not in list_nb and c != "@" :  ## Si le caractère est un caractère spécial
                                temp = 2  ## temp est égale à 2 si c'est un caractère spécial
                                ment_final = m.split(c)  ## On split au caractère spécial
                                break  ## On sort de la boucle
                        if temp == 2 :  ## Si temp est égale à 2
                            liste_m.append(ment_final[0])  ## On ajoute à la liste final au premier caractère de notre split pour ne pas avoir le caractère spécial
                        if temp != 2 :  ## sinon
                            liste_m.append(m)  ## On ajoute simplement la mention 
                        
    return liste_m  ## On renvoie la liste contenant toutes les mentions de chaque tweet


## Analyser le sentiment du tweet :

def analys_feeling(tweet) :
    """Fonction qui permet d'analyser les sentiments d'un tweet"""
    sentiment = ""  ## On créer la variable sentiment contenant une chaîne de caractère vide
    tweet_blob = TextBlob(tweet)  ## tweet_blob contient le tweet avec la class textblob appliquée
    polarity = tweet_blob.sentiment.polarity  ## Polarity contient le tweet analysé par textblob avec sa polarité
    if round(polarity,2) > (0.00) :  ## si l'arrondi de la polarité est au dessus de 0
        sentiment += "+"  ## On met le sentiment du tweet à +
    elif round(polarity,2) < (0.00) :  ## si l'arrondi de la polarité est en dessous de 0
        sentiment += "-"  ## On met le sentiment du tweet à -
    else :
        sentiment += "0"  ## Si la polarité est neutre on met le sentiment du tweet à 0
    return sentiment  ## On renvoie le sentiment du tweet



def topK_hashtags(k) :
    """Fonction qui prends un argument K (entier) et renvoie les K hashtags les plus utilisées dans la liste de tweets"""
    top = list(dictK_hashtags.items()) ## On créé une liste contenant les items du dictionnaire
    while k > len(top) : ## On teste si la valeur k donnée n'est pas supérieur au nombre d'hashtags que l'on a
        int(input(f"Désolé je ne peux pas t'imprimer le top {k} des hashtags car il n'y en a que {len(top)}, donne moi un nombre + petit : ")) ## Si k supérieur au nombre d'hashtags alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"Voici le top {k} des hashtags qui reviennent le + souvent : \n")
    for i in range(k) :
        print(f"- {i+1}) {top[i][0]} avec {top[i][1]} occurences.") ## On affiche le top K des hashtags avec le nombres d'occurences à chaque fois




def topK_mentions(k) :
    """Fonction qui prends un argument K (entier) et renvoie les K utilsateurs les plus mentionnés dans la liste de tweets"""
    top = list(dictK_mentions.items()) ## On créé une liste contenant les items du dictionnaire
    while k > len(top) : ## On teste si la valeur k donnée n'est pas supérieur au nombre de mentions que l'on a
        int(input(f"Désolé je ne peux pas t'imprimer le top {k} des mentions car il n'y en a que {len(top)}, donne moi un nombre + petit : ")) ## Si k supérieur au nombre de mentions alors on renvoie un message d'erreur et on demande au user d'en rentrer un autre
    print(f"Voici le top {k} des mentions qui reviennent le + souvent : \n")
    for i in range(k) :
        print(f"- {i+1}) {top[i][0]} avec {top[i][1]} occurences.") ## On affiche le top K des mentions avec le nombres d'occurences à chaque fois




"""Programme principal"""



data = []

with open('aitweets.json') as f:
    for line in f:
        line_sans_carac = del_caractere_spe(line)
        data.append(line_sans_carac)
#print(data)


list_nb = [str(i) for i in range(0,10)]  ## liste contenant les 10 premiers nombres 
list_maj = [chr(i) for i in range(65,91)]  ## liste contenant les 26 majuscules
list_min =  [chr(i) for i in range(97,123)] + ["-","_"]  ## liste contenant les 26 miniscules + les tirets et les tirets du bas


## Création de 2 listes contenant respectivement tous les hashtags et toutes les mentions de chaque publication

liste_hashtag = []
liste_mention = []
for i in range(len(data)) :
    liste_hashtag.append(liste_hashtags(data[i]["TweetText"]))
    liste_mention.append(liste_mentions(data[i]['TweetText']))


## TopK des hashtags 

dictK_hashtags = {} ## Initialisation d'un dictionnaire qui contiendra touts les différents hashtags avec leur nombre d'occurences
for elt in liste_hashtag : ## On parcoure notre liste contenant tous les hastags de chaque publication
    for h in elt : ## On parcoure les hashtags un à un des publications
        if h not in dictK_hashtags : ## On teste si le hashtags n'est pas déjà dans les clés du dictionnaire
            dictK_hashtags[h] = 1 ## Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
        else :
            dictK_hashtags[h] += 1 ## Sinon, on ajoute +1 à l'occurence du hashtag déjà existant

dictK_hashtags = dict(sorted(dictK_hashtags.items(), key = lambda item : item[1], reverse=True)) ## Trier le dictionnaire avec les hashtags par ordre décroissant

'''

k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des hashtags : "))
topK_hashtags(k)
'''


## TopK des mentions :

dictK_mentions = {} ## Initialisation d'un dictionnaire qui contiendra toutes les différentes mentions avec leur nombre d'occurences
for elt in liste_mention : ## On parcoure notre liste contenant toutes les mentions de chaque publication
    for m in elt : ## On parcoure les mentions unes à unes des publications
        if m not in dictK_mentions : ## On teste si la mention n'est pas déjà dans les clés du dictionnaire
            dictK_mentions[m] = 1 ## Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
        else :
            dictK_mentions[m] += 1 ## Sinon, on ajoute +1 à l'occurence de la mention déjà existante

dictK_mentions = dict(sorted(dictK_mentions.items(), key = lambda item : item[1], reverse=True)) ## Trier le dictionnaire avec les mentions par ordre décroissant

'''

k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des mentions : "))
topK_mentions(k)

'''


## Sentiments de tous les tweets

liste_sentiments = []
for i in range(len(data)) :
    liste_sentiments.append(analys_feeling(data[i]["TweetText"]))
#print(liste_sentiments)