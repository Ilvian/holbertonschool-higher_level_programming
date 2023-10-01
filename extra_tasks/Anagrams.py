#!/usr/bin/python3
def are_anagrams(str1, str2):
    a = str1.replace(" ", "").lower()
    b = str2.replace(" ", "").lower()
    return sorted(a) == sorted(b)

if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("act", "cat"))
    print(are_anagrams("work", "rest"))
    print(are_anagrams("note", "tone"))
    print(are_anagrams("evil", "vile"))
    print(are_anagrams("dumbbell", "barbell"))
    print(are_anagrams("Moon starer", "Astronomer"))
    print(are_anagrams("The Morse Code", "Here come dots"))
