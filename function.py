def frequency_analysis(text):
    """Count the frequency of each letter in the text"""
    freq = {}
    result = []
    frequency = list('etaoinshrdlcumwfgypbvkjxqz')
    for letter in text:
        freq[letter] = freq.get(letter, 0) + 1
    


text = "fasdfuyasdfhsdngdfjghsdfgysfdbvxcmnbhjcvbgyfdtuyiwerweoqrtpsdfgsdfkgljdbxcmnvbmxcbjdfguytewruyqiuqwieo"
print(frequency_analysis(text))