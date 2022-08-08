def frequency_analysis(text):
    """Count the frequency of each letter in the text"""
    freq = {}
    frequency = list('etaoinshrdlcumwfgypbvkjxqz')
    result = text
    for letter in text:
        freq[letter] = freq.get(letter, 0) + 1
    
    freq = sorted(freq, key=freq.get, reverse=True)
    for letter in freq:
        result = result.replace(letter, frequency.pop())
    return "".join(result)

def caesar_shift(text, shift=3):
    """Shift the text by a number of letters"""
    result = []
    text = text.upper()
    for letter in text:
        if letter.isalpha():
            result.append(chr((ord(letter) + shift - 65) % 26 + 65))
    return "".join(result)

def uncaesar_shift(text, shift=3):
    """Shift the text by a number of letters"""
    result = []
    text = text.upper()
    for letter in text:
        result.append(chr((ord(letter) - shift - 65) % 26 + 65))
    return "".join(result)

text = "This is a cool sentence that should be converted nicely123"
print(caesar_shift(text))
print(frequency_analysis(caesar_shift(text)))