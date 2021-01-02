# yacache - Yet Another Cache

yacache is yet another python cache. This library allows for caching function results in whatever type they were initially returned. This is meant to be fast, optional, and, most importantly, retain all docstrings unlike some other caching libs.

### Installation
 Simply:
```sh
pip install yacache
```

### Usage
Simply:
```py
from yacache import cache

@cache
def testFunc( arg1=None ):
    ''' 
    Test func
    
    Args:
        arg1 (str, None): first argument
    
    Returns:
        bool
    '''
    return isinstance( arg1, str )
```

License
----

MIT
