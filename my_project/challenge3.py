def solve(word):
    
    letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
                     'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                     'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    
    def substring_value(substring):
        return sum(letter_values[char] for char in substring)
    
   
    consonants = ''.join(char for char in word if char not in 'aeiou')
    
    
    substrings = consonants.split('a')  
    
    
    max_value = max(substring_value(substring) for substring in substrings)
    
    return max_value


print(solve("zodiacs"))  # Output: 26
print(solve("strength"))  # Output: 57
