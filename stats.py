def get_num_words(text):
    split_text = text.split()
    return len(split_text)


def get_num_chars(text):
    chars = {}
    for char in text:
        lc = char.lower()
        if lc not in chars.keys():
            chars[lc] = 1
        else:
            chars[lc] += 1
    return chars


def sort_chars(inval):
    output = []
    chars_count = get_num_chars(inval)
    for k, v in chars_count.items():
        if k.isalpha():
            output.append({"char": k, "num": v})
    x = lambda x: x["num"]
    output.sort(key=x, reverse=True)
    return output
