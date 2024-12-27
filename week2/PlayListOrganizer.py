import csv

def read_csv_file(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []


def filter_by_genre(songs, genre):
    return [song for song in songs if song['genre'].lower() == genre.lower()]


def filter_by_duration(songs, max_duration):
    try:
        max_duration = float(max_duration)
        return [song for song in songs if float(song['duration']) <= max_duration]
    except ValueError:
        print("Error: Please enter a valid number for duration.")
        return []


def main():
    filename = "songs.csv"
    songs = read_csv_file(filename)

    if not songs:
        return

    while True:
        print("\n1. Filter by Genre")
        print("2. Filter by Maximum Duration")
        print("3. Show All Songs")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            genre = input("Enter genre: ")
            filtered = filter_by_genre(songs, genre)
            if filtered:
                print("\nFiltered Songs by Genre:")
                for song in filtered:
                    print(f"{song['title']} - {song['artist']} ({song['genre']} - {song['duration']} mins)")
            else:
                print("No songs found for the specified genre.")

        elif choice == "2":
            max_duration = input("Enter maximum duration: ")
            filtered = filter_by_duration(songs, max_duration)
            if filtered:
                print("\nFiltered Songs by Duration:")
                for song in filtered:
                    print(f"{song['title']} - {song['artist']} ({song['genre']} - {song['duration']} mins)")
            else:
                print("No songs found within the specified duration.")

        elif choice == "3":
            print("\nAll Songs:")
            for song in songs:
                print(f"{song['title']} - {song['artist']} ({song['genre']} - {song['duration']} mins)")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
