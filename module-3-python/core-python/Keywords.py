import keyword

print(keyword.kwlist)
def check_keyword(word):
    if word in keyword.kwlist:
        print(f"{word} is a keyword in Python.")
    else:
        print(f"{word} is not a keyword in Python.")
