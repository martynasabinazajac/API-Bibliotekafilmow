import random


class Movie:
    def __init__(self, title, publication_date, genre, number_of_play):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre
        self.number_of_play = number_of_play

    def __str__(self):
        return f"{self.title} (publication date:{self.publication_date})"

    def play(self):
        self.number_of_play = self.number_of_play + 1
        return f"Number of plays for {self.title}: {self.number_of_play}"

    def search_options(self):
        return f"title:{self.title}, publication date:{self.publication_date}, genre:{self.genre}, number of play:{self.number_of_play}"


class TV_series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}."

    def search_options(self):
        return f"title:{self.title}, publication date:{self.publication_date}, genre:{self.genre}, number of play:{self.number_of_play}, S{self.season_number:02d}E{self.episode_number:02d}"


movies = [
    Movie(
        title="Hen hen tam", publication_date="2014", genre="comedy", number_of_play=11
    ),
    Movie(
        title="A ulu lu lu", publication_date="2021", genre="horror", number_of_play=19
    ),
    TV_series(
        title="Simpson",
        publication_date="2019",
        genre="comedy",
        number_of_play=1,
        episode_number=1,
        season_number=3,
    ),
    TV_series(
        title="Adi",
        publication_date="2011",
        genre="comedy",
        number_of_play=9,
        episode_number=3,
        season_number=9,
    ),
]


def show_list(list):
    list.sort(key=lambda x: x.title)
    for x in list:
        print(x)
    return "Done"


def show_list_number_of_plays(list):
    for x in list:
        print(x.play())


def get_series(list, list2):
    for x in list:
        if isinstance(x, TV_series) == True:
            list2.append(x)
        list2.sort(key=lambda x: x.title)
    for x in list2:
        print(x)
    return "Done!"


def get_movie(list, list2):
    for x in list:
        if isinstance(x, Movie) == True and isinstance(x, TV_series) == False:
            list2.append(x)
            list2.sort(key=lambda x: x.title)
    for x in list2:
        print(x)
    return "Done!"


def search(list):
    search_option = str(input("Enter title:"))
    for x in list:
        if x.title == search_option:
            print(x.search_options())


def generate_views(list):
    y = random.choice(list)
    print(y)
    rr = random.randint(1, 100)
    x = y.number_of_play + rr
    print(x)


def generate_views_10(quantity, list):
    for _ in range(quantity):
        generate_views(list)


def top_titles(list):
    list.sort(key=lambda x: x.number_of_play, reverse=True)
    top_values = list[:quantity2]
    for x in top_values:
        print(x)


if __name__ == "__main__":
    get_movies_series = []
    get_movies = []
    show_list(movies)
    show_list_number_of_plays(movies)
    print('\nList of "TV_series:')
    get_series(movies, get_movies_series)
    print("\n------------------------------------------------------\nList of movies:")
    get_movie(movies, get_movies)
    print(
        "\n------------------------------------------------------\nInformation about searched movie:"
    )
    search(movies)
    print("\n------------------------------------------------------\nLucky choice:")
    generate_views(movies)
    print(
        "\n------------------------------------------------------\nLucky choice for more than one record:"
    )
    quantity = int(input("Enter quantity:"))
    generate_views_10(quantity, movies)
    print("\n------------------------------------------------------\nTop titles:")
    quantity2 = int(input("Enter quantity:"))
    top_titles(movies)
