def  vowels(s):
    count=0
    vowel = "aeiouAEIOU"
    for i in s:
        if i in vowel:
            count +=1
    return count
if __name__ == '__main__':
    print(vowels("aeiou"))
    print(__name__)
