# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)

#USER DEFINED EXCEPTIONS
class Error(Exception):
    """BASE calss for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raise when the input value is too small"""
    pass
