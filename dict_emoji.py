print("practis eof emoji : ")

message=input("> ")
words = message.split(" ")
emojis={
    ":)" : "😊",
    ":(" : "☹️"
}
op1=""
print(words)
for word in words:
    op1 += emojis.get(word,word) + " "
print(op1)