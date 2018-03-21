# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

def encode(input):
    if not input:
        return ""

    result = ""
    currentChar = input[0]
    currentCount = 0

    for i,char in enumerate(input,1):
        if char == currentChar:
            currentCount +=1
        else:
            result += str(currentCount) + currentChar
            currentChar = char
            currentCount = 1
    result += str(currentCount) + currentChar

    return result

def decode(input):
    count = 0
    result = ""

    for char in input:
        if char.isdigit():
            count = count*10 + int(char)
        else:
            result += char * count
            count = 0
    
    return result

    




print(encode("AAAABBBCCDAA"))
print(decode("4A3B2C1D2A"))