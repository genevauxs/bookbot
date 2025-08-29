def generate_output(path, word_count, list_of_char):
    print(f"============ BOOKBOT ============ \n" +
          f"Analyzing book found at {path}...\n" + 
          f"----------- Word Count ----------\n"+
          f"Found {word_count} total words\n"+
          f"--------- Character Count -------")
    for char_tuple in list_of_char:
        if char_tuple["char"].isalpha():
            print(f"{char_tuple['char']}: {char_tuple['num']}")
    print(f"============= END ===============")
