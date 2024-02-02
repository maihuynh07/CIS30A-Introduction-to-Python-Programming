import re   # import re module which is utilities for working with regular expressions 

# function: checking name if it is all alpha then return true, else return false
def invalidName(name):
    try:
        assert (re.sub("[ .]","",name)).isalpha()   # name should be all alpha a-z or A-Z or whitespace or dot
    except:
        return False
    else:
        return True

# function: checking address if it is only alpha or digit (whitespace and comma and dot are allowed) then return true, else return false
def invalidAddress(mailAddress):
    try:
        assert (re.sub("[,. ]","",mailAddress)).isalnum()
    except:
        return False
    else:
        return True
# function: checking emailAddress if its format is true then return true, else return false
def invalidEmail(emailAddress):
    try:
        assert re.match(r'^[\w\W]+@{1}[\w\W]+[.]{1}[\w\W]+$',emailAddress)    # email format should be something@abc.xyz
    except:
        return False
    else:
        return True