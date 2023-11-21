import Suppression_Caracteres_Speciaux
data = []

"""Création de la zone d'atterrissage"""
with open('aitweets.json', errors="ignore") as f:
    for line in f:
        line_sans_carac = Suppression_Caracteres_Speciaux.del_caractere_spe(line)
        data.append(line_sans_carac)
#print(data)




"""Analyse des sentiments de la publication"""
import Analyse_Des_Sentiments
sentiment = []
for i in range(len(data)):
    sentiment.append(Analyse_Des_Sentiments.analys_feeling(data[i]["TweetText"]))
#print(sentiment)




"""Liste des hashtags, et liste des mentions"""
import Liste_Hashtags
import Liste_Mentions
## Création de 2 listes contenant respectivement tous les hashtags et toutes les mentions de chaque publication

liste_hashtag = []
liste_mention = []
for i in range(len(data)) :
    liste_hashtag.append(Liste_Hashtags.liste_hashtags(data[i]["TweetText"]))
    liste_mention.append(Liste_Mentions.liste_mentions(data[i]['TweetText']))




"""TopK des hashtags""" 
import Top_K_Hashtags
dictK_hashtags = {} ## Initialisation d'un dictionnaire qui contiendra touts les différents hashtags avec leur nombre d'occurences
for elt in liste_hashtag : ## On parcoure notre liste contenant tous les hastags de chaque publication
    for h in elt : ## On parcoure les hashtags un à un des publications
        if h not in dictK_hashtags : ## On teste si le hashtags n'est pas déjà dans les clés du dictionnaire
            dictK_hashtags[h] = 1 ## Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
        else :
            dictK_hashtags[h] += 1 ## Sinon, on ajoute +1 à l'occurence du hashtag déjà existant

dictK_hashtags = dict(sorted(dictK_hashtags.items(), key = lambda item : item[1], reverse=True)) ## Trier le dictionnaire avec les hashtags par ordre décroissant

"""
k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des hashtags : "))
Top_K_Hashtags.topK_hashtags(k,dictK_hashtags)
"""




"""TopK des mentions"""
import Top_K_Mentions
dictK_mentions = {} ## Initialisation d'un dictionnaire qui contiendra toutes les différentes mentions avec leur nombre d'occurences
for elt in liste_mention : ## On parcoure notre liste contenant toutes les mentions de chaque publication
    for m in elt : ## On parcoure les mentions unes à unes des publications
        if m not in dictK_mentions : ## On teste si la mention n'est pas déjà dans les clés du dictionnaire
            dictK_mentions[m] = 1 ## Si oui, alors on créer une nouvelle clé dans le dictionnaire et on initialise son occurence à 1
        else :
            dictK_mentions[m] += 1 ## Sinon, on ajoute +1 à l'occurence de la mention déjà existante

dictK_mentions = dict(sorted(dictK_mentions.items(), key = lambda item : item[1], reverse=True)) ## Trier le dictionnaire avec les mentions par ordre décroissant


k = int(input("Donnes moi un nombre k afin que je t'affiche le top k des mentions : "))
Top_K_Mentions.topK_mentions(k,dictK_mentions)


