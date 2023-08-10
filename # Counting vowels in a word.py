# Counting vowels in a word

def count_vowel_letters(word):
    vowels = 'aeiou'
    count_vowel = [letter for letter in word if letter.lower() in vowels]
    return count_vowel

word = input()
result = count_vowel_letters(word) # Takes and considers the vowels
count_of_words = len(result) # It counts the vowels that were taken
print("The number of vowels in your word are:", count_of_words)