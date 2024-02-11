def reverse_words(sentence):

    words = sentence.split()

    reversed_words = [word[::-1] for word in words]#[::-1]


    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

sample_sentence = input("enter a sentence")
reversed_result = reverse_words(sample_sentence)

print(f"Original sentence: {sample_sentence}")
print(f"Reversed sentence: {reversed_result}")