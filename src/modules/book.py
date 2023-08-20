"""Book Object"""
from utils import get_db


class Book:
    def __init__(
        self,
        title: str,
        author_fn: str,
        author_ln: str,
        publisher: str,
        pages: int,
        pub_year: int,
        tags: list[str],
        read: bool,
        reading: bool,
        isbn: str,
        translator: str = "",
        orig_pub_year: int = 0,
        notes: str = "",
    ):
        self.title: str = title
        self.author_fn: str = author_fn
        self.author_ln: str = author_ln
        self.publisher: str = publisher
        self.translator: str | None = translator if translator != "" else None
        self.pages: int = pages
        self.pub_year: int = pub_year
        self.orig_pub_year: int | None = orig_pub_year if orig_pub_year != 0 else None
        self.tags: list[str] = tags
        self.read: bool = read
        self.reading: bool = reading
        self.isbn: str = isbn
        self.notes: str | None = notes if notes != "" else None

    def to_dict(self) -> dict:
        book_id = len(get_db()) + 1
        return {
            "id": book_id,
            "title": self.title,
            "author_fn": self.author_fn,
            "author_ln": self.author_ln,
            "translator": self.translator,
            "publisher": self.publisher,
            "pages": self.pages,
            "publication_year": self.pub_year,
            "original_publication_year": self.orig_pub_year,
            "tags": self.tags,
            "read": self.read,
            "reading": self.reading,
            "isbn": self.isbn,
            "notes": self.notes,
        }

    def __str__(self):
        if self.translator is None:
            return f"{self.title} - {self.author_ln}, {self.author_fn}"
        return f"{self.title} - {self.author_ln}, {self.author_fn} (Trns. {self.translator})"

    def display(self):
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author_fn} {self.author_ln}")
        if self.translator is not None:
            print(f"Translator: {self.translator}")
        print(f"Publisher: {self.publisher}")
        print(f"Pages: {self.pages}")
        if self.orig_pub_year is not None:
            print(
                f"Publication Year: {self.pub_year} (Orig. Published {self.orig_pub_year})"
            )
        else:
            print(f"Publication Year: {self.pub_year}")
        print(f"Tags: {self.tags}")
        print(f"Read: {self.read}")
        print(f"Reading: {self.reading}")
        print(f"ISBN: {self.isbn}")
        print(f"Notes: {self.notes}\n")
