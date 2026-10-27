"""
Module 4 Project — Part 1: API Exploration
Explore 3 public APIs and document what you find.

Instructions:
- Fill in each TODO section
- Run the script to verify your code works
- Document your findings in comments and print statements
"""

import requests

BASE_URLS = {
    "jsonplaceholder": "https://jsonplaceholder.typicode.com",
    "pokeapi": "https://pokeapi.co/api/v2",
    "restcountries": "https://restcountries.com/v3.1",
}

# ============================================================
# API 1: JSONPlaceholder
# Documentation: https://jsonplaceholder.typicode.com/guide/
# ============================================================

def explore_jsonplaceholder():
    print("\n=== API 1: JSONPlaceholder ===")

    response = requests.get(f"{BASE_URLS["jsonplaceholder"]}/users")

    response.raise_for_status()

    users = response.json()

    print(f"Status Code: {response.status_code} {response.reason}")

    print(f"\nAll Users: {len(users)} ")
    print("===========================")

    for user in users:
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print("-------------------------")


    # TODO 2: GET posts by a specific user
    # Endpoint: GET /posts?userId=<number>
    # Print the count and first post title

    response = requests.get(f"{BASE_URLS["jsonplaceholder"]}/posts", params={"userId": 5})

    posts = response.json()

    print(f"    Count: {len(posts)}")
    if posts:
        print(f"    First title: {posts[0]['title']}")
    print("==============================")
    

    new_posts =  {
            "userId": 1,
            "title": "....",
            "body": "...."
        }
    response = requests.post(
    f"{BASE_URLS['jsonplaceholder']}/posts",
    json=new_posts
)

    response.raise_for_status()

    created_post = response.json()

    print(f"Status Code: {response.status_code}")
    print(f"Created Post ID: {created_post['id']}")
    
# ============================================================
# API 2: PokeAPI
# Documentation: https://pokeapi.co/docs/v2
# ============================================================

def explore_pokeapi():
    print("\n=== API 2: PokeAPI ===")

    response = requests.get(f"{BASE_URLS['pokeapi']}/pokemon/1")


    response.raise_for_status()

    pokemon = response.json()

    print(f"\nPokemon Name: {pokemon['name']}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")

    print("Abilities:")

    for ability in pokemon["abilities"]:
        print(f"  - {ability['ability']['name']}")

    print("==============================")
    
    type_url = pokemon["types"][0]["type"]["url"]

    response = requests.get(type_url)

    response.raise_for_status()

    pokemon_type = response.json()

    print(f"\nType Name: {pokemon_type['name']}")

    print("First 5 Pokémon of this type:")

    for poke in pokemon_type["pokemon"][:5]:
        print(f"  - {poke['pokemon']['name']}")

    print("==============================")

   
    # Top-level keys in the /pokemon response:

  # id: Unique identification number of the Pokémon (integer)
# name: Name of the Pokémon (string)
# height: Height of the Pokémon in decimeters (integer)
# weight: Weight of the Pokémon in hectograms (integer)
# abilities: List of the Pokémon's abilities (list of dictionaries)
# types: List of the Pokémon's types (list of dictionaries)
# stats: Base statistics such as HP, attack, and defense (list)
# moves: List of moves the Pokémon can learn (list)
# sprites: URLs for Pokémon images (dictionary)
# species: Name and URL of the Pokémon's species (dictionary)
# base_experience: Experience points earned when defeated (integer)
# order: Sorting order of the Pokémon (integer)


# ============================================================
# API 3: REST Countries
# Documentation: https://restcountries.com/#endpoints
# ============================================================

def explore_restcountries():
    print("\n=== API 3: REST Countries ===")

    # TODO 7: GET a country by name (try "Japan" or any country you like)
    # Endpoint: GET /name/<country_name>
    # Print: official name, capital, population, region

   
    response = requests.get(f"{BASE_URLS['restcountries']}/name/Japan")


    response.raise_for_status()

    countries = response.json()

    for country in countries:
        print(f"Official Name: {country['name']['official']}")
        print(f"Capital: {country['capital'][0]}")
        print(f"Population: {country['population']:,}")
        print(f"Region: {country['region']}")


    # TODO 8: GET all countries in a region (try "Europe" or "Asia")
    # Endpoint: GET /region/<region_name>
    # Print: count, first 10 country names alphabetically

    # TODO 9: Handle an error
    # Try a country name that doesn't exist
    # Handle the response gracefully (don't crash)


# ============================================================
# Run all explorations
# ============================================================

if __name__ == "__main__":
    explore_jsonplaceholder()
    explore_pokeapi()
    explore_restcountries()
    print("\n=== Exploration complete! ===")
