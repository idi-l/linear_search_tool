def linear_search(data, target):
    """
    Recherche linéaire : retourne l'index si trouvé, sinon -1.
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1
