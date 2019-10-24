
#Cheering up -Example
#The starting letters of words prefer prefix an
an_letters="aefhilmnorsxAEFHILMNORSX"
#inputting the word
word=raw_input("I will cheer you!, Enter a word:")
#The frequency of cheering, input as int
times=int(input("Enthusiasm Level(1-10):"))
#Using while loop
#initializing counter
#i=0
#while i<len(word):
#    char=word[i]
#    if char in an_letters:
#        print("Give me an",char+"!",char)
#    else:
#        print("Give me a",char+"!",char)
#    i+=1
#print("What does that spell?")
#for i in range(times):
#    print(word,"!!!")

#Code with for loop
for char in word:
    if char in an_letters:
        print("Give me an",char,"!",char)
    else:
        print("Give me a",char,"!",char)
        
print("What does that spell?")
for i in range(times):
    print(word,"!!!")