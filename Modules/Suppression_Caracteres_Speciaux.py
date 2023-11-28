import re

def del_caractere_spe(txt):
    """Supprime les caractères spéciaux, type émojis"""
    new_text = re.sub(r'[^a-zA-Z0-9\s@#(){}[]', '', txt)
    #  [^...] correspond à la recherche de tous les élément compris dans les crochets, les autres seront supprimés
    #  a-zA-z0-9 correspond à tout l'alphabet de a à z avec les majuscules ainsi que les chiffres de 0 à 9
    #  \s correspond à tous les espacement, tabulation, saut de ligne, etc..
    #  et le reste c'est les caractères que l'on supprime pas 
    return(new_text)

