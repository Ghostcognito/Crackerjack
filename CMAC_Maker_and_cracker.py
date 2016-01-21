# HMAC maker
# HMAC cracker
import random

def randomLetters(lengthOfLetters):
    """This is how the random alphanumeric characters are genarated"""
    word = 'realign singularity polishing buffers'
    passWord = ''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8',
            '9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
            'P','Q','R','S','T','U','V','W','X','Y','Z','.',' ']
    listOfLetters=[]
    index = lengthOfLetters
    while index != 0:
        listOfLetters.append(alphabet[random.randint(0,63)])
        index = index-1
    return(''.join(listOfLetters))
    

def loopRandom(numberOfTimes):
    """This function genarates the crack key, a good length is 4"""
    lengthOfLetters = 4
    crackKey = []
    while numberOfTimes != 0:
        crackKey.append(randomLetters(lengthOfLetters))
        numberOfTimes = numberOfTimes - 1
    return(crackKey)

hmac_blocksize=16

def strToNum(inp):
    """Takes a sequence of bytes and makes a number"""
    out=0
    for i in inp:
        out=out<<8
        out^=ord(i)
        #print "\t", out
    return(out)

def numToStr(inp):
    """Take a number and make a sequence of bytes in a string"""
    out=""
    while inp!=0:
        out=chr(inp & 255)+out
        #print "\t", inp
        inp=inp>>8
        #print "\t",  out
    return(out)

def cueh_hash_1(inp):
    """ CUEH Hash Function v 1.0
    Returns 16 bit hash of any string input or stringable input
    """
    inp=str(inp) #Make sure we have a string
    if len(inp)%2!=0: inp+=" " #Pad it if we need to
    val=0 #Our accumulator
    for pos in range(0,len(inp),2): #Now in twos...
        i=inp[pos]
        j=inp[pos+1]
        #print ("\tEncoding",i,j)
        val^=ord(i)  #XOR first char onto lowest 8 bits
        val^=(ord(j)<<8)  #and second char onto highest 8 bits
        #print ("\t\t",val)
    #print ("\t",val)
    return(val)
     
def cueh_hmac_1(key, message):
    """Outputs a hash-based digest of the message and secret key combo"""
    key=str(key)
    message=str(message)
    if len(key)>hmac_blocksize/8:
        key=numToStr(cueh_hash_1(key)) #Keys are shortened to blocksize
    while len(key)<hmac_blocksize/8:
        key+=" " #Keys are padded with spaces if they're too short
        #print("0x%x"%cueh_hash_1(key+message))
    return(cueh_hash_1(key+message))

def testRunner():
    """The answer for this as it stands now should be 7194"""
    # You can change the secretKey and authedMessage to any of the key message
    # pairs in the crackerJack mathod to check that it in fact works

    authedMessage="detatch porpoise"
    secretKey="FnO "
    out=cueh_hmac_1(secretKey,authedMessage)
    print("%d|%s"%(out, authedMessage))

def crackerJack(x):
    """This will test if the randomly genarated values for the amount y at a
    leanth x will match to make the cueh_hash of a given message
    x sould be how many times you would like it to try.
    A good value is 100000"""
    # the hmac corresponds to the values once the hash has been carried out
    # with the secretKey.
    # hmac1 corresponds to message1 and so on so forth
    hmac1 = 7194
    message1 = "This is a test of the emergency broadcast system."
    hmac2 = 25193
    message2 = "power up gigamatrix server"
    hmac3 = 21084
    message3 = "install toaster updates"
    hmac4 = 25136
    message4 = "realign singularity polishing buffers"
    hmac5 = 14382
    message5 = "enhance undulation"
    hmac6 = 23900
    message6 = "detatch porpoise"

    # Change hmac and message here to the ones you want to test

    listOfKeys=[]
    for i in loopRandom(x):
        y = cueh_hmac_1(i,message6)
        if y == hmac6:
            listOfKeys.append(i)
    return(listOfKeys)


        
