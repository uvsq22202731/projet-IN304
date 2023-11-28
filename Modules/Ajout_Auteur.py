import json
import Suppression_Caracteres_Speciaux
import random
def verification_structure(fichier):
    with open('atterissage.json','w'):  #  On ouvre notre fichier zone d'atterissage
        pass
    tweet_keys = ["id", "AuthorLocation", "CreatedAt", "RetweetCount",  #  On créer une liste avec les différentes clés de notre fichier json
                     "TweetLanguage", "TweetText"]
    with open(fichier,'r', encoding='utf-8') as f:  #  On ouvre notre fichier en mode read
        lignes=f.readlines()    #  on ajoute chacunes des lignes à lignes
    with open('atterissage.json','a',encoding='utf-8') as atterissage:  # On ouvre notre fichier en mode append pour pouvoir écrire dedans
        for ligne in lignes:
            tweet=json.loads(ligne)    #  On ouvre notre ligne 
            for keys in tweet:
                if keys in tweet_keys:
                    tweet[keys]=Suppression_Caracteres_Speciaux.del_caractere_spe(tweet[keys])  #  On supprime les caractères spéciaux de notre ligne
            tweet['Utilisateur']=random.randint(0,100)  #  On ajoute un nombre aléatoire entre 0 et 100 pour l'utilisateur du tweet
            json.dump(tweet,atterissage,ensure_ascii=False)
            atterissage.write('\n')    #  On écrit dans notre fichier le fichier sans caractères spé
        tweet['Utilisateur']=random.randint(0,100)  #  On créer un utilisateur avec un nombre aléatoire entre 0 et 100
        json.dump(tweet,atterissage,ensure_ascii=False)
        atterissage.write('\n')     #  On écrit dans notre fichier les utilisateurs qui ont crée les tweets
