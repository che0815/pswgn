## Description: Super Basic Python Password Generator
Creates a password consiting of a number of blocks (numofblocks) which can/will have randomly chosen length (provided in blocklengths). The returned password has the highest entropy of the (bestoff) randomly generated ones.

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
