def square(number):
    if number > 64 or number < 1:
        raise ValueError ("square must be between 1 and 64")
    else:
        val = number -1 
        return 2**val
    
    


def total():
     return 2**64 -1
