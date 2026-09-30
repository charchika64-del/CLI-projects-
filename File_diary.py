from datetime import datetime
from pathlib import Path

print("Type 1 to write entry.")
print("Type 2 to read entry.")
print("Type 3 to exit.")


def get_free_filename(base_name):
    # Add .txt to the base name
    candidate = base_name + ".txt"
    path = Path(candidate)
    # Keep changing name while file exists
    while path.is_file():#True if file already exists
        # Fresh time inside the loop
        now = datetime.now()
        time_part = now.strftime("%H-%M-%S")
        candidate = base_name + "_" + time_part + ".txt"
        path = Path(candidate)   # update the thing we check
    # Return the free name
    return candidate


while True:
    try:
        num = int(input("Enter a number "))

        if num == 1:
            opening = input("Say something to diary: ")
            now = datetime.now()
            entry_date = now.strftime("%B %d, %Y\n%A\n")#September 29,2026 (newline) tuesday
            entry = input("Write body: ")
            closing = input("Say bye to diary: ")

            base_name = now.strftime("%b%d,%Y")
            final_name = get_free_filename(base_name)   # store the return

            with open(final_name, "a") as diary:
                diary.write(" \n")
                diary.write(entry_date)
                diary.write(f"{opening}\n")
                diary.write(f"{entry}\n")
                diary.write(f"{closing}\n")
                diary.write(" \n")

            print(f"[Saved as {final_name}]")

        elif num == 2:
            try:
                print("[Don't add extension. .txt will be added automatically.]")
                filename = input("Enter the file of your diary entry: ")
                filename = filename + ".txt"
                with open(filename, "r") as diary:
                    content = diary.read()
                print(content)
            except FileNotFoundError:
                print("This file does not exist.")
                continue
            except ValueError:
                print("Type a file name.")
                continue

        elif num == 3:
            print("Exited")
            break

        else:
            print("Type 1,2 or 3")
            continue

    except ValueError:
        print("Type a number.")
        continue
