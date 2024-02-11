sentence = input("Enter a sentence: ")

words = sentence.split()

word_lengths = {word: len(word) for word in words}

print("Word lengths dictionary:")
print(word_lengths)