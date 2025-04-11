# Simple Book Recommendation Chatbot in Python

# Sample book dataset (title, author, genre)
books = [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopia"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
    {"title": "The Martian", "author": "Andy Weir", "genre": "Sci-Fi"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction"}
]

def recommend_books(preferred_genre):
    # Filter books by the user's preferred genre
    recommendations = [book for book in books if book["genre"].lower() == preferred_genre.lower()]
    return recommendations if recommendations else None

def chatbot():
    print("Hello! I'm your Book Recommendation Bot. Let's find you a book!")
    
    while True:
        # Ask for user input
        print("\nWhat genre do you like? (e.g., Fantasy, Dystopia, Romance, Sci-Fi, Fiction)")
        print("Type 'exit' to quit.")
        user_input = input("> ").strip()

        # Check if user wants to exit
        if user_input.lower() == "exit":
            print("Goodbye! Happy reading!")
            break

        # Get recommendations based on genre
        suggestions = recommend_books(user_input)

        # Provide feedback to the user
        if suggestions:
            print("\nHere are some books you might like:")
            for book in suggestions:
                print(f"- {book['title']} by {book['author']} ({book['genre']})")
        else:
            print(f"Sorry, I don’t have any books in the '{user_input}' genre yet. Try another!")

# Start the chatbot
if __name__ == "__main__":
    chatbot()