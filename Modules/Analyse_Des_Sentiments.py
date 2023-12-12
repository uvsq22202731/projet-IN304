from textblob import TextBlob

def analys_feeling(tweet) :
    """Analyse les sentiments de la publications grâce au module textblob"""
    sentiment = ""
    tweet_blob = TextBlob(tweet)
    polarity = tweet_blob.sentiment.polarity
    if round(polarity,2) > (0.00) :
        sentiment += "+"
    elif round(polarity,2) < (0.00) : 
        sentiment += "-"
    else :
        sentiment += "0"
    return sentiment    # Renvoie un sentiment -,0,+ en fonction des sentiments de la publication