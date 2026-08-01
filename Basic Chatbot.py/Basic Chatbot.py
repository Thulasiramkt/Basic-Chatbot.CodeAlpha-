def get_bot_response(user_input: str) -> tuple[str, bool]:
    """Processes user input and returns (bot_response, should_exit)."""
    # Clean input: remove surrounding whitespace and convert to lowercase
    cleaned_input = user_input.strip().lower()

    # Define synonyms for common intents
    greetings = {"hello", "hi", "hey", "hello bot", "hey bot"}
    farewells = {"bye", "goodbye", "exit", "quit"}

    if not cleaned_input:
        return "Bot: Please say something!", False

    if cleaned_input in greetings:
        return "Bot: Hi there!", False

    elif "how are you" in cleaned_input:
        return "Bot: I'm fine, thanks!", False

    elif "your name" in cleaned_input or cleaned_input == "what is your name":
        return "Bot: My name is Python Bot.", False

    elif cleaned_input in farewells:
        return "Bot: Goodbye!", True

    else:
        return "Bot: Sorry, I don't understand.", False


def main():
    print("===== Basic Chatbot =====")
    print("Type 'bye', 'exit', or 'quit' to exit.\n")

    while True:
        try:
            user_input = input("You: ")
            response, should_exit = get_bot_response(user_input)
            print(response)

            if should_exit:
                break
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break


if __name__ == "__main__":
    main()