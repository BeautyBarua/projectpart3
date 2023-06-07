from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
        Returns a list of all movies.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the storage.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The rating of the movie.
            poster (str): The URL of the movie poster.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Deletes a movie from the storage.

        Args:
            title (str): The title of the movie to delete.
        """
        pass

    @abstractmethod
    def update_movie(self, title, notes):
        """
        Updates the notes for a movie.

        Args:
            title (str): The title of the movie to update.
            notes (str): The new notes for the movie.
        """
        pass
