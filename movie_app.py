from storage_json import StorageJson


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()

        if movies:
            print("List of movies:")
            for movie_id, movie_data in movies.items():
                title = movie_data.get('title', '')
                year = movie_data.get('year', '')
                rating = movie_data.get('rating', '')
                print(f"Movie ID: {movie_id}")
                print(f"Title: {title}")
                print(f"Year: {year}")
                print(f"Rating: {rating}")
                print("---------------------")
        else:
            print("No movies in the database.")

    def _command_movie_stats(self):
        movies = self._storage.list_movies()

        # Compute average rating
        ratings = [float(movie['rating']) for movie in movies.values() if 'rating' in movie]
        average_rating = sum(ratings) / len(ratings)
        print("Average rating in the database:", average_rating)

        # Compute median rating
        sorted_ratings = sorted(ratings)
        if len(sorted_ratings) % 2 == 0:
            median_index_1 = len(sorted_ratings) // 2
            median_index_2 = median_index_1 - 1
            median_rating = (sorted_ratings[median_index_1] + sorted_ratings[median_index_2]) / 2
        else:
            median_index = len(sorted_ratings) // 2
            median_rating = sorted_ratings[median_index]
        print("Median rating in the database:", median_rating)

        # Find the best movie(s) by rating
        best_rating = max(ratings, default=0)
        best_movies = [movie.get('title', '') for movie in movies.values() if
                       'rating' in movie and float(movie.get('rating', 0)) == best_rating]
        print("Best movie(s) by rating:")
        if best_movies:
            for movie in best_movies:
                print(movie)
            print("Rating:", best_rating)
        else:
            print("No movie with the highest rating.")

        # Find the worst movie(s) by rating
        worst_rating = min(ratings, default=0)
        worst_movies = [movie.get('title', '') for movie in movies.values() if
                        'rating' in movie and float(movie.get('rating', 0)) == worst_rating]
        print("Worst movie(s) by rating:")
        if worst_movies:
            for movie in worst_movies:
                print(movie)
            print("Rating:", worst_rating)
        else:
            print("No movie with the lowest rating.")

    def _generate_website(self):
        movies = self._storage.list_movies()
        movie_html = ""

        for movie in movies.items():
            title, movie_data = movie  # Unpack the tuple into title and movie_data

            movie_html += "<li class='movie-grid'>\n"
            movie_html += f"<div class='list-movies-title'>\n"
            movie_html += f"<img class='movie-poster' src='{movie_data['poster_url']}'>\n"

            movie_html += f"<div>{movie_data['title']}</div>\n"
            movie_html += f"<div>{movie_data['year']}</div>\n"

            movie_html += f"</div>\n"
            movie_html += "</li>\n"

        print(movie_html)

        with open('../index_template.html', 'r') as f:
            template_content = f.read()

        replace_content = template_content.replace("__TEMPLATE_MOVIE_GRID__", movie_html)
        replace_txt = replace_content.replace("__TEMPLATE_TITLE__", "Beauty's movie app")
        print(replace_txt)

        with open("../index.html", 'w') as file:
            file.write(replace_txt)

        print("Website was generated successfully.")

    def _command_exit_program(self):
        movies = self._storage.list_movies()
        print("Bye!")
        exit()

    def run(self):
        while True:
            # Print menu
            print("1. List Movies")
            print("2. Movie Statistics")
            print("3. Generate Website")
            print("4. Exit")

            # Get user command
            command = input("Enter a command (1-4): ")

            # Execute command
            if command == "1":
                self._command_list_movies()
            elif command == "2":
                self._command_movie_stats()
            elif command == "3":
                self._generate_website()
            elif command == "4":
                self._command_exit_program()
                break
            else:
                print("Invalid command. Please try again.")


# Create an instance of the StorageJson class
storage = StorageJson('../data.json')

# Print the list of movies
print(storage.list_movies())

# Add a new movie
storage.add_movie("Movie Title", 2023, 7.5, "https://example.com/movie_poster.jpg")

# Print the updated list of movies
print(storage.list_movies())

# Update an existing movie
storage.update_movie("movie_id", {
    "title": "Updated Movie Title",
    "year": 2023,
    "rating": 8.0,
    "poster_url": "https://example.com/updated_movie_poster.jpg"
})

# Print the updated list of movies
print(storage.list_movies())

# Delete a movie
storage.delete_movie("movie_id")

# Print the updated list of movies
print(storage.list_movies())
