MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []


def add_movie():
    """Ask user for movie details and store them."""
    title = input("Enter the movie title: ").strip().title()
    director = input("Enter the movie director: ").strip().title()
    year = int(input("Enter the movie release year: "))

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movie():
    """Display all saved movies."""
    if not movies:
        print("No movies saved yet.")
        return

    for movie in movies:
        print_movie(movie)
        print("*" * 20)


def print_movie(movie):
    """Print details of a single movie dictionary."""
    print(f"\nTitle: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    """Find and display a movie by its title."""
    search_title = input("Enter movie title you're looking for: ").strip().title()
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)
            return
    print("Movie not found.")


# Map menu choices to functions 
user_option = {
    'a': add_movie,
    'l': show_movie,
    'f': find_movie
}


def menu():
    """Main menu loop."""
    selection = input(MENU_PROMPT).lower()

    while selection != "q":
        if selection in user_option:
            selected_function = user_option[selection]
            selected_function()
        else:
            print("Unknown command. Please try again!")

        selection = input(MENU_PROMPT).lower()


if __name__ == "__main__":
    menu()

    