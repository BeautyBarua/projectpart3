import csv
from abc import ABC, abstractmethod
from movie_app import MovieApp
from storage_json import StorageJson
from typing import Dict

from istorage import IStorage


class StorageCsv(ABC):
    def __init__(self, filename):
        self._filename = filename

    @abstractmethod
    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        For example, the function may return:
        {
          "Titanic": {
            "rating": 9,
            "year": 1999
          },
          "..." {
            ...
          },
        }
        """
        pass

    @abstractmethod
    def add_movie(self, title, rating, year, poster):
        """
        Adds a new movie to the database.

        :param title: The title of the movie.
        :param rating: The rating of the movie.
        :param year: The year of the movie.
        :param poster: The URL of the movie poster.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Deletes a movie from the database.

        :param title: The title of the movie to delete.
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating, year, poster):
        """
        Updates the information of a movie in the database.

        :param title: The title of the movie to update.
        :param rating: The new rating of the movie.
        :param year: The new year of the movie.
        :param poster: The new URL of the movie poster.
        """
        pass


class StorageCsv(IStorage):
    def __init__(self, filename: str):
        self._filename = filename

    def list_movies(self) -> Dict[str, Dict[str, str]]:
        movies = {}

        with open(self._filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row.get('title', '')
                rating = row.get('rating', '')
                year = row.get('year', '')
                movies[title] = {'rating': rating, 'year': year}

        return movies

    def add_movie(self, title: str, rating: str, year: str, poster: str):
        with open(self._filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, rating, year, poster])

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            with open(self._filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'rating', 'year', 'poster'])
                for movie in movies.values():
                    writer.writerow([movie['title'], movie['rating'], movie['year'], movie['poster']])

    def update_movie(self, title, rating, year, poster):
        movies = self.list_movies()
        if title in movies:
            movies[title] = {'rating': rating, 'year': year, 'poster': poster}
            with open(self._filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['title', 'rating', 'year', 'poster'])
                for movie in movies.values():
                    writer.writerow([movie['title'], movie['rating'], movie['year'], movie['poster']])


# Test with JSON storage
json_storage = StorageJson('../data.json')
json_movie_app = MovieApp(json_storage)
json_movie_app.run()

# Test with CSV storage
csv_storage = StorageCsv('data.csv')
csv_movie_app = MovieApp(csv_storage)
csv_movie_app.run()
