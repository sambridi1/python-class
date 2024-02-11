sentence="perfect ? he is the perfect . perfect"
print("the original sentence is: "+sentence)
sentence_list=sentence.split()
dict_2 = {}
for word in sentence_list:
    count_value = sentence.count(word)
    dict_2[word] = count_value
#dict1={word:sentence.count(word) for word in sentence_list}
print(dict_2)