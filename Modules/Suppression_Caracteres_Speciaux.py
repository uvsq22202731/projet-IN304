import json
import re


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

data = []

