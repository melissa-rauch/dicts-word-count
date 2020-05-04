
def word_count(file_name):
    """Returns each word in given text and the number of times the word appears"""
    given_text = open(file_name)
    word_list = {}

    for line in given_text:
        words = line.rstrip().split()
        
        for word in words:
            word_list[word] = word_list.get(word, 0) + 1
    
    # return word_list               

    for key,value in word_list.items():
        
        print (f"{key} {value}")



word_count("twain.txt")  
