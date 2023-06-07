from projectpart3.istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        with open(self.file_path, 'r') as file:
            movies = json.load(file)
        return movies

    def add_movie(self, title, rating, year, poster_url):
        movies = self.list_movies()
        movies[title] = {
            'title': title,
            'year': year,
            'rating': rating,
            'poster_url': poster_url,
        }
        with open(self.file_path, 'w') as file:
            json.dump(movies, file, indent=4)

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            with open(self.file_path, 'w') as file:
                json.dump(movies, file, indent=4)

    def update_movie(self, title, notes):
        movies = self.list_movies()
        if title in movies:
            movies[title]['notes'] = notes
            with open(self.file_path, 'w') as file:
                json.dump(movies, file, indent=4)


from storage_json import StorageJson

storage = StorageJson('../data.json')

# Test list_movies()
movies = storage.list_movies()
print(movies)

# Test add_movie()
storage.add_movie("The Shawshank Redemption", "1994", "9.3", "https://www.example.com/poster1.jpg")
storage.add_movie("Pulp Fiction", "1994", "8.9", "https://www.example.com/poster2.jpg")
movies = storage.list_movies()
print(movies)

# Test delete_movie()
storage.delete_movie("Pulp Fiction")
movies = storage.list_movies()
print(movies)

# Test update_movie()
storage.update_movie("The Shawshank Redemption", "A must-watch classic!")
movies = storage.list_movies()
print(movies)
