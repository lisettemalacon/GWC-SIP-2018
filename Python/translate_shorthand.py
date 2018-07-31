answer = input()

def translate_shorthand(dictionary):
    for key, value in sorted(dictionary.items()):
        if answer in key:
            print(value)

shorthand = {
"omg" : "oh my gawd",
"l8r" : "later",
"ttyl" : "talk to you later",
"g9" : "good night",
"gg" : "good game",
"wtf" : "what the fark",
"w/e" : "whatever"
}
translate_shorthand(shorthand)
