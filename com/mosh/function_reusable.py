def emojis(message):
    words = message.split(" ")
    dictionary = {
        ":)": "😀",
        ":(": "🥲",
        ":3": "😺"
    }
    output = ""
    for word in words:
        output += dictionary.get(word, word) + " "
    return output


user_message = input("> ")
print(emojis(user_message))

