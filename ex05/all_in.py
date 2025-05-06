import sys

def capital_city(state):
    # Dictionnaires d'états et capitales
    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
    capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}
    
    # Recherche si l'état correspond à une capitale
    for s_key, s_value in capital_cities.items():
        if state.lower() == s_value.lower():  # Comparaison insensible à la casse
            print(f"{s_value} is the capital of {list(states.keys())[list(states.values()).index(s_key)]}")
            return True  # Si on a trouvé, on renvoie True
    return False  # Si aucune capitale n'est trouvée

def state(city):
    # Dictionnaires d'états et capitales
    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
    capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}
    
    # Recherche si la ville est un état
    for s_key, s_value in states.items():
        if city.lower() == s_key.lower():  # Comparaison insensible à la casse
            print(f"{capital_cities[s_value]} is the capital of {s_key}")
            return True  # Si on a trouvé, on renvoie True
    return False  # Si aucune correspondance n'est trouvée

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # Séparer les éléments dans l'argument passé
        item_list = [item.strip() for item in sys.argv[1].split(",")]
        item_list = [item for item in item_list if item]  # Retirer les éléments vides
        for item in item_list:
            if not (state(item) or capital_city(item)):  # Vérifier si c'est un état ou une capitale
                print(f"{item} is neither a capital city nor a state")
