from projectpart3.storage_json import StorageJson
from projectpart3.movie_app import MovieApp


def main():
    # Create a StorageJson object
    storage = StorageJson('../data.json')

    # Create a MovieApp object with the StorageJson object
    app = MovieApp(storage)

    # Run the app
    app.run()


# Execute the main function
if __name__ == "__main__":
    main()
