import string
import random

def createblock(blocklength):
    random.seed(a=None)
    chars =  string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ''
    passwordlength = blocklength
    for c in range(passwordlength):
        password += random.choice(chars)
    return(password)

def chooseblocklength(blocklengths):
    random.seed(a=None)
    blength = random.choice(blocklengths)
    return(blength)

def createpassword(numofblocks, blocklengths):
    password = ''
    for ii in range(numofblocks):
        blocklengt = chooseblocklength(str(blocklengths))
        block = createblock(int(blocklengt))
        password += block
        if ii < numofblocks-1:
            password += '_'
    return(password)
