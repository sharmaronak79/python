def emojiconverter(message):
    words=message.split(" ")
    emoji_dict={
        ":)":"😊",
        ":(":"☹️",
        ";)":"😉"
    }
    op= ""
    for word in words:
        op+=emoji_dict.get(word,word) + " "
    return op



print("welcome to return value with function and dictionary of emoji")
message=input("> ")
print(emojiconverter(message))