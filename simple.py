# Is a simple chatbot demonstration

import openai

# Setup to API
openai.api_key = "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"


# Define a function to intercat with the bot
def ask_chatbot(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=150,
    )
    return response['choices'][0]['text'].strip()


# Use the function to chat with the bot
try: 
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye!")
            break
        bot_response = ask_chatbot("You: " + user_input + "\nBot:")
        print(f"Bot: {bot_response}")
except:
    print("Something went wrong")