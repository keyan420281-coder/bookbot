def get_num_words(text):
    num = text.split()
    return len(num)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered_c = c.lower()
        if lowered_c in chars:
            chars[lowered_c] +=1
        else:
            chars[lowered_c] = 1
    return chars

def sort_on(item):
    return item["num"]

def sort_chars(chars):
    result = []
    for char, count in chars.items():
       result.append({"char": char, "num": count}) 

    
    result.sort(key=sort_on, reverse=True)
    return result