import datetime
import database

menu = """Please select one of the following options:
1. Add new movie
2. View upcoming movies.
3. View all movies.
4. Watch a movie.
5. View watched movies.
6. Exit

Your Input: """

Welcome = """Welcome to the movie watching app"""

print(Welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release Date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print(f"{heading} movies:")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%d-%m-%Y")
        print(f"Movie name : {movie[0]}\nRelease Date: {human_date}\n")
    print("------ \n")


def prompt_watch_movie():
    title = input("Enter the movie title you have watched: ")
    database.watch_movie(title)


while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        watched_movies = database.get_watched_movies()
        print_movie_list("Watched", watched_movies)
    else:
        print("Invalid input, Please try again!")
