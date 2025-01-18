# Define a dictionary to store information about your favorite book
favorite_book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction"
}

# Retieve the genre using the dictionary method
book_genre = favorite_book.get("genre")

# Print the genre
print("The genre of my favorite book is:", book_genre)