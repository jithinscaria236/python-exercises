# Program to print list elements and display sentence
try:
    sentence_list  = ["hi", "this", "is" , "jithin"]
    sentence = ""
    i = 0
    for value in sentence_list:
        if i == 0:
            sentence = sentence + value
        else:
            sentence = sentence + " " + value
        i = i + 1
    print(sentence)

    print("Enter a sentence")
    input_txt = input()
    input_txt_list = input_txt.split()
    print("Sentence list is:")
    print(input_txt_list)
except Exception as error:
    print(f"Error occured inside the program\n:Please find the error details:{error}")
