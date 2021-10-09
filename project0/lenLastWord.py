def lengthOfLastWord(s):
    words = s.split()
    last = words[-1]
    return len(last)
