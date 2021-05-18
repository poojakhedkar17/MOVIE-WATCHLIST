from database import fetch_entries, add_entry, create_table

menu = """Please select one of the following options:
1. Add new movie
2. View upcoming movies.
3. View all movies.
4. Watch a movie.
5. View watched movies.
6. Exit

Your Input: """

Welcome = """Welcome to the movie watching app"""


# def prompt_new_entry():
#     date = input("Enter a date:")
#     content = input("Enter the content:")
#     add_entry(date, content)
#
#
# def view_entries(entries):
#     for entry in entries:
#         print(f"Date : {entry[1]}\nContent : {entry[0]}\n\n")


print(Welcome)
create_table()

while (user_input := input(menu)) != "6":
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input, Please try again!")
