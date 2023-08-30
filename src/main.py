from modules.book import Book
from utils import bool_input, int_input, get_db, list_input, rev_bool_input, update_db


class App:
    def __init__(self):
        print("Welcome to Jaden's Book Registry!")
        self.main_loop()

    def main_loop(self):
        while True:
            print("Please select one of the following options: (Enter 0 to exit)\n")
            print("1) Display all books.")
            print("2) Search for a book.")
            print("3) Add a new book.\n")
            i = int_input("", 0, 3)
            print("")

            match i:
                case 1:
                    stage = self.display_all()
                case 2:
                    stage = self.search()
                case 3:
                    stage = self.add_book()
                case _:
                    stage = False

            if stage is False:
                print("Exiting...")
                break

    @staticmethod
    def dict_to_book(d: dict) -> Book:
        """
        :param d: dictionary returned by json.load()
        :return: Book Object
        """

        return Book(
            d.get("title"),
            d.get("author_fn"),
            d.get("author_ln"),
            d.get("publisher"),
            d.get("pages"),
            d.get("publication_year"),
            d.get("tags"),
            d.get("read"),
            d.get("reading"),
            d.get("isbn"),
            d.get("translator"),
            d.get("original_publication_year"),
            d.get("notes"),
        )

    @staticmethod
    def get_book_details() -> Book:
        book: Book | None = None

        while True:
            # Title
            t = input("What is the title of this book? ")
            # Author
            a_fn = input("What is the author's first name? ")
            a_ln = input("What is the author's last name? ")
            # Translator
            translator_yn = bool_input("Was this work translated? ")
            if translator_yn:
                translator = input("Who was the translator? ")
            else:
                translator = None
            # Publisher
            pub = input("Who was the publisher? ")
            # Pages
            pgs = int_input("How many pages are in this book? ", 1)
            # Publication Year
            pub_yr = int_input("When was this book published? ", 1400, 2030)
            og_pub_yr = int_input(
                "When was this book originally published? (Leave blank if same as above.) ",
                1,
            )
            if og_pub_yr == "":
                og_pub_yr = None
            # Tags
            tags = list_input("Tags (Separate with spaces): ", " ")
            # Read Status
            read = bool_input("Have you read this book? ")
            reading = bool_input("Are you currently reading this book? ")
            # ISBN
            isbn = input("What is the full ISBN number? (Include dashes) ")
            # Notes
            notes = input("Any additional notes? (Leave blank if none) ")
            if notes == "":
                notes = None

            print("You have entered the following:")
            print(
                f"""
                        Title: {t}
                        Author: {a_ln}, {a_fn}
                        Translator: {translator}
                        Publisher: {pub}
                        Pages: {pgs}
                        Published: {pub_yr}
                        Originally Published: {og_pub_yr}
                        Tags: {tags}
                        Read: {read}
                        Reading: {reading}
                        ISBN: {isbn}
                        Notes: {notes}         
                    """
            )
            print("Is this correct?")

            response = bool_input("")
            if response is True:
                return Book(
                    t,
                    a_fn,
                    a_ln,
                    pub,
                    pgs,
                    pub_yr,
                    tags,
                    read,
                    reading,
                    isbn,
                    translator,
                    og_pub_yr,
                    notes,
                )

    @staticmethod
    def edit_book(book: Book):
        book.display()
        edit = bool_input("Would you like to edit this entry? ")
        if edit is False:
            return

        while True:
            data_to_edit = input("What would you like to edit? ")
            match data_to_edit.lower():
                case "ti" | "title":
                    val = input("Input new title: ")
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["title"] = val
                    update_db(db)
                case "a" | "author":
                    fn = input("Author's First Name: ")
                    ln = input("Author's Last Name: ")
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["author_fn"] = fn
                            d["author_ln"] = ln
                    update_db(db)
                case "tr" | "translator":
                    translator_yn = bool_input("Does this book have a translator? ")
                    if translator_yn:
                        val = input("Translator: ")
                    else:
                        val = None
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["translator"] = val
                    update_db(db)
                case "pu" | "pub" | "publisher":
                    val = input("Input new publisher: ")
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["publisher"] = val
                    update_db(db)
                case "pa" | "pgs" | "pages":
                    val = int_input("How many pages? ", 1)
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["pages"] = val
                case "pub yr" | "publication":
                    val = int_input("When was this book published? ", 1400)
                    og_val = int_input(
                        "When was this book originally published? (Leave blank if same) ",
                        1400,
                    )
                    if og_val == "":
                        og_val = None
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["publication_year"] = val
                            d["original_publication_year"] = og_val
                    update_db(db)
                case "tag" | "tags":
                    val = list_input("Input new tags: ", " ")
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["tags"] = val
                    update_db(db)
                case "read":
                    val = bool_input("Have you read this book? ")
                    if val is False:
                        reading_val = bool_input(
                            "Are you currently reading this book? "
                        )
                    else:
                        reading_val = False
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["read"] = val
                            d["reading"] = reading_val
                    update_db(db)
                case "isbn":
                    val = input("Input corrected isbn: ")
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["isbn"] = val
                    update_db(db)
                case "notes":
                    val = input("Input notes: ")
                    db = get_db()
                    for d in db:
                        if d.get("isbn") == book.isbn:
                            d["notes"] = val
                    update_db(db)
            if bool_input("Would you like to edit anything else? ") is False:
                return

    def display_all(self) -> bool:
        """
        Displays a list of all books in database.
        """
        data: list[dict] = get_db()
        books = []
        for d in data:
            books.append(self.dict_to_book(d))

        for i, b in enumerate(books, start=1):
            print(f"{i}) {b}")
        print()  # Generate new line after last book entry

        i = int_input("Select a book: (Enter 0 to return to main menu) ", 0, len(books))
        if i == 0:
            return True
        else:
            book = books[i - 1]

        self.edit_book(book)

        return rev_bool_input("Would you like to exit? ")

    def search(self):
        pass

    def add_book(self) -> bool:
        book: Book = self.get_book_details()
        db: list[dict] = get_db()

        for d in db:
            if d.get("isbn") == book.isbn:
                i = bool_input(
                    f"{book.title} already in database. Would you still like to proceed? "
                )
                if i is False:
                    print("Returning to Main Menu...")
                    return True
                break

        db.append(book.to_dict())
        db.sort(key=lambda x: x["title"].lower())
        db.sort(key=lambda x: x["author_ln"].lower())
        update_db(db)

        return rev_bool_input("Would you like to exit? ")


def main():
    App()


if __name__ == "__main__":
    main()
