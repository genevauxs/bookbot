def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    text_lower_list = list(text.lower())
    text_lower_unique = set(text_lower_list)
    return_dict = {}
    for id in text_lower_unique:
        return_dict[id] = text_lower_list.count(id)
    return return_dict

def get_sorted_num_char(dictionary):
    return_lst = []
    for char in dictionary:
        return_lst.append({"char" : char, "num" : dictionary[char]})
    return sorted(return_lst, key= lambda x: x["num"], reverse=True)
