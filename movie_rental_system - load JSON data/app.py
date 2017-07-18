from movie import Movie
from user import User
import json

user = User("Isha")


user.add_movie("Harry Potter", "Fantasy")
user.add_movie("Iron Man", "Sci-Fi")

#User.save_to_file()
#user = User.load_from_file('Isha')
#with open("Movie.txt", 'w') as f:
 #   json.dump(user.json(), f)

with open("Movie.txt", 'r') as file:
    json_data = json.load(file)
    user =  User.load_from_json(json_data)
    print(user.json())