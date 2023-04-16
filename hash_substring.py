# python3
# Egija Kokoreviča 	221RDB288

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    ievade = input("Ievdi F vai I:").rstrip()
    if "F" in ievade:
        file = input().rstrip()

        if "a" in file:
            print("You can't use file names with letter 'a'")
            return

        try:
            with open ("tests/"+file) as fp:
                pattern = fp.readline().rstrip()
                text = fp.readline().rstrip()

        except FileNotFoundError:
            print("Inprecision in the file name")
            return

    if "I" in ievade:  
        try:
                    
            pattern = input().rstrip()
            text = input().rstrip()

        except ValueError:
            print("Inprecision in input")
            return  
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    return pattern, text


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    n, m = len(text), len(pattern)
    if m > n:
        return []
    
    pattern_hash = hash(pattern)

    text_hashes = [hash(text[i:i+m]) for i in range(n-m+1)]

    result = [i for i, h in enumerate(text_hashes) if h == pattern_hash]

    result = [i for i in result if text[i:i+m] == pattern]
    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

