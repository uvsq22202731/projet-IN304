def liste_mentions(tweet) :
    temp = 0
    liste_m = []
    if "@" in tweet :
        split = tweet.split()
        for elmnt in split :
            if "@" in elmnt and elmnt[0] == "@" :
                for c in elmnt[1:] :
                    if c not in list_maj and c not in list_min and c not in list_nb :
                        temp = 1
                        mention = elmnt.split(c)
                        break
                if temp == 1 and mention[0] != "@" :
                    liste_m.append(mention[0])
                if temp != 1 and elmnt != "@…" :
                    liste_m.append(elmnt)
            elif "@" in elmnt and elmnt[0] != "@" :
                for c in elmnt :
                    if c == "@" :
                        i = elmnt.index(c)
                        mention2 = elmnt.split(elmnt[i-1])
                        break
                for m in mention2 :
                    if "@" in m :
                        for c in m :
                            if c not in list_min and c not in list_maj and c not in list_nb and c != "@" :
                                temp = 2
                                ment_final = m.split(c)
                                break
                        if temp == 2 :
                            liste_m.append(ment_final[0])
                        if temp != 2 :
                            liste_m.append(m)
                        
    return liste_m

list_nb = [str(i) for i in range(0,10)]  ## liste contenant les 10 premiers nombres 
list_maj = [chr(i) for i in range(65,91)]  ## liste contenant les 26 majuscules
list_min =  [chr(i) for i in range(97,123)] + ["-","_"]  ## liste contenant les 26 miniscules