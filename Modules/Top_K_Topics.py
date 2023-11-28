import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models
from gensim.models import LdaModel
import Publications_par_Topics
def topics(text, num_topics=1):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    # Create dictionary and corpus
    dictionary = corpora.Dictionary([lemmatized_words])
    corpus = [dictionary.doc2bow(lemmatized_words)]

    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary)

    all_topic_words = []  # Nouvelle liste pour stocker les mots clés de tous les sujets

    topic_distribution = lda_model[corpus[0]]

    for topic_id, topic_weight in topic_distribution:
        top_words = lda_model.show_topic(topic_id)
        words = [word[0] for word in top_words]
        freq = [word[1] for word in top_words]
        topic_words = [f"{word} ({weight:.2f})" for word, weight in zip(words, freq)]
        all_topic_words.extend(topic_words)  # Ajouter les mots clés à la liste

    return all_topic_words


def get_top_k_topics(all_results, k):
    topic_counts = Publications_par_Topics.nb_publications_par_topic(all_results)

    # Trier les topics par ordre décroissant du nombre de publications
    sorted_topics = sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)

    # Sélectionner les K premiers topics
    top_k_topics = sorted_topics[:k]

    return top_k_topics