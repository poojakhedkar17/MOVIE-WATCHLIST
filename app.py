import datetime
import database

menu = """Please select one of the following options:
1. Add new movie
2. View upcoming movies.
3. View all movies.
4. Watch a movie.
5. View watched movies.
6. Add new user.
7. Search a movie.
8. Exit.

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
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%d-%m-%Y")
        print(f"{_id}: {title}\nRelease Date: {human_date}\n")
    print("------ \n")


def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username, movie_id)


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


def prompt_show_watched_movies():
    username = input("Username: ")
    watched_movies = database.get_watched_movies(username)
    if watched_movies:
        print_movie_list("Watched", watched_movies)
    else:
        print("This user has not watched any movies yet!")


def prompt_search_movie():
    search_term = input("Enter a part of movie name or movie name: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Movies Found!!",movies)
    else:
        print("Found no movies for this search term!!")


while (user_input := input(menu)) != "8":
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
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movie()
    else:
        print("Invalid input, Please try again!")
