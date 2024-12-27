import csv

def write_songs_you_want_in_the_future():
    try:
        filename = "suggestions.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Song Name"])  # Header

            while True:
                song = input("Enter the song name you want in the future (or type 'mnawer' to finish): ")
                if song.lower() == 'mnawer':
                    break
                writer.writerow([song])

        print(f"Songs have been saved in '{filename}'")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    write_songs_you_want_in_the_future()
