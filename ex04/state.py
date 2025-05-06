import sys

def state(city):

    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
    capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver",}
    
    finder = False
    for c_key, c_values in capital_cities.items():
        if city == c_values:
            for s_key, s_values in states.items():
                if c_key == s_values:
                    print(s_key)
                    finder = True
                    break
    if finder == False:
        print("Unknow capital cities")
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        state(sys.argv[1])