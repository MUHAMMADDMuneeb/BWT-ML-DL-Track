class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # Getter methods
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_pages(self):
        return self.pages
    
    # Setter methods
    def set_title(self, title):
        self.title = title
    
    def set_author(self, author):
        self.author = author
    
    def set_pages(self, pages):
        self.pages = pages

    # Class method to calculate reading time
    def calculate_reading_time(pages):
        # Assuming average words per page is 300
        words_per_minute=250
        words_per_page = 300
        total_words = pages * words_per_page
        try:
            reading_time = total_words / words_per_minute
        except ZeroDivisionError:
            print("Error: Reading speed cannot be zero. Please provide a valid reading speed.")
            return 0
        return  reading_time
    
class Ebook(Book):
    def __init__(self, title, author, pages, format):
        # """
        # Initialize a new Ebook instance.

        # :param title: str: The title of the ebook.
        # :param author: str: The author of the ebook.
        # :param pages: int: The number of pages in the ebook.
        # :param format: str: The format of the ebook (e.g., 'PDF', 'EPUB').
        # """
        super().__init__(title, author, pages)
        self.format = format

    def get_format(self):
        # """
        # Get the format of the ebook.

        # :return: str: The format of the ebook.
        # """
        return self.format

    def set_format(self, format):
        # """
        # Set the format of the ebook.

        # :param format: str: The new format of the ebook.
        # """
        self.format = format

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)


        # Using getter and setter methods
print("Title:", book.get_title())
book.set_title("The Great Gatsby: Revised Edition")
print("New Title:", book.get_title())

        # Calculate reading time
reading_time = Book.calculate_reading_time(book.get_pages())
print(f"Estimated Reading Time: {reading_time:.2f} minutes")

        # Create an instance of Ebook
ebook = Ebook("1984", "George Orwell", 328, "EPUB")
        # Using getter and setter methods for Ebook
print("Format:", ebook.get_format())
ebook.set_format("PDF")
print("New Format:", ebook.get_format())       

