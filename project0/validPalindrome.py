def validPalindrome(s):
    words = s.split()

    word_proc = ""
    for word in words:
        word_proc = word_proc + word.lower()

    word_back = ""
    length = len(word_proc)
    for i in range(length):
        word_back = word_back + word_proc[length-i-1]

    return(word_proc == word_back)