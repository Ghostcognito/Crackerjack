# HMAC cracker
import random
import itertools

def randomLetters(lengthOfLetters):
    word = 'realign singularity polishing buffers'
    passWord = ''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8',
            '9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
            'P','Q','R','S','T','U','V','W','X','Y','Z','.',' ']
    listOfLetters=[]
    index = lengthOfLetters
    while index != 0:
        listOfLetters.append(alphabet[random.randint(0,62)])
        index = index-1
    return(''.join(listOfLetters))
    

def looprandom(numberOfTimes):
    lengthOfLetters = 4
    while numberOfTimes != 0:
        wordcheck = ""
        wordcheck = set(randomLetters(lengthOfLetters))
        numberOfTimes = numberOfTimes - 1
        print(''.join(wordcheck))
