# def func_x(x):
#     y=x**2+5*x+3
#     return y
# numbers=[1,2,3,4,5,6,7,8,9,10]
# map_example=list(map(func_x,numbers))
# print(map_example)



# def upper_words(sentence):
#     return sentence.title()
#     # print(x)
    
# sample_sentence = input("enter a sentence")
# splitted_list=sample_sentence.split(" ")
# map_example=list(map(upper_words,splitted_list))
# final_sentence = ' '.join(map_example)
# print(final_sentence)



# euta sentence dine and first word lai upper garne second lai title feri 3rd lai upper and so on 
def upper_words(sentence,index):
    if(index%2==0):
        result_word=sentence.upper()
    else:
        result_word= sentence.title()
    return result_word
    
sample_sentence = "this is the world where we live and sleep"
result=[upper_words(word,index) for index, word in enumerate(sample_sentence.split())]
complete_sentence = ' '.join(result)
print(complete_sentence)