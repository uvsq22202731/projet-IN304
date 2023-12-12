def nb_publications_par_topic(all_results):
    """Renvoie le nombre de publications par topics"""
    topic_counts = {}
    for result in all_results:  # On parcourt tous les tweets
        if result:
            best_topic = result[0]
            topic_name = best_topic.split(' (')[0]  # On prend le premier topics de chaque tweet
            
            if topic_name is not None:  # Si le topic n'est pas NULL
                if topic_name in topic_counts:
                    topic_counts[topic_name] += 1  # Si le topic n'est pas nouveau on incrémente son nombre d'itération
                else:
                    topic_counts[topic_name] = 1    # Sinon on l'initialise à 1

    # Trier le dictionnaire par ordre décroissant des valeurs (nombre de publications)
    sorted_topic_counts = dict(sorted(topic_counts.items(), key=lambda x: x[1], reverse=True))

    return sorted_topic_counts
