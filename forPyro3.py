def isAlphabet(string):
    if len(string) != 1:
        return False
    else:
        if string.isalpha():
            return True
        else:
            return False


s = input("Enter an Alphabet: ")

if isAlphabet(s):
    print("your input is a valid English ALphabet")
else:
    print("your input is either invalid length or not an english alphabet")
