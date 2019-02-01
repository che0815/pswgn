import string
import random
import numpy as np
import math

def createblock(blocklength):
    random.seed(a=None)
    chars =  string.ascii_uppercase + string.ascii_lowercase + string.digits + '=!§$%&?@€#ß'
    password = ''
    passwordlength = blocklength
    for c in range(passwordlength):
        password += random.choice(chars)
    return(password)

def chooseblocklength(blocklengths):
    random.seed(a=None)
    blength = random.choice(blocklengths)
    return(blength)

def entropy2(labels, base=None): # from: https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
    """ Computes entropy of label distribution. """
    n_labels = len(labels)

    if n_labels <= 1:
        return 0

    value,counts = np.unique(labels, return_counts=True)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)

    if n_classes <= 1:
        return 0

    ent = 0.

    # Compute entropy
    base = math.e if base is None else base
    for i in probs:
        ent -= i * math.log(i, base)

    return ent

def createpassword_step1(numofblocks, blocklengths):
    password = ''
    for ii in range(numofblocks):
        blocklengt = chooseblocklength(str(blocklengths))
        block = createblock(int(blocklengt))
        password += block
        if ii < numofblocks-1:
            password += '_'
    return(password)

def createpassword(numofblocks, blocklengths, bestoff):
    passlist = {}
    for ii in range(bestoff):
        aassi = createpassword_step1(numofblocks, blocklengths)
        passlist[entropy2(list(aassi))] = aassi
    return passlist[max(list(passlist.keys()))]    
