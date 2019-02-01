## Description: Super Basic Python Password Generator
Creates a password consiting of a number of blocks (numofblocks) which can/will have randomly chosen length (provided in blocklengths). The returned password has the highest entropy of the (bestoff) randomly generated ones.  
The password can consist of the possible symbols:
+ string.ascii_uppercase: __ABCDEFGHIJKLMNOPQRSTUVWXYZ__
+ string.ascii_lowercase: __abcdefghijklmnopqrstuvwxyz__
+ string.digits: __0123456789__
+ some symbols: __=!§$%&?@€#ß__

## Usage
```python
from paswgen import createpassword
numofblocks = 3
blocklengths = 12345
bestoff = 100
createpassword(numofblocks, blocklengths, bestoff)
```
```python
e6LjO_psf9_#xUE4
```
