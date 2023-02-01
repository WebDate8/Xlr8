import random

words = []
counter = 0
answ = "s"
word = 0

print("Welcome ☠️ .\nIt's a wordlist generetor made by Xlr8.")

while answ == "s":
    answ = str.lower(input("1-Do you want to generete a wordlist?(S/N): "))
    if answ != "s":
        print ("•You chosen to do not make a wordlist, stopping the scrip.")
        break
    print("2-You chosen to generete a wordlist.\nTo stop adding words type -0.")
    while word != "-0":
        counter += 1
        word = input("•Type a word: ")
        if word == "-0":
            print("•You chosen to stop adding words.")
            break
        else:
            words.append(word)
    senhas = int(input("3-How many words do you want to generete? "))
    dig = int(input("4-How many caracteres do you want? "))
    wordlist = []
    list1 = []
    list2 = []
    list1 = words
    list2 = words
    words.sort
    list1.sort(reverse=True)
    list2.reverse
    for w in range(senhas):
        word = random.choice(words)+random.choice(list1)
        while len(word) < dig:
            word += random.choice(list2)
        wordlist.append(word)
    file = open("words.txt", "w")
    for i in wordlist:
        file.write(i)
        file.write("\n")
        file.close
    print ("•Wordlist gerada com sucesso. \n -~-~-> XLR$ <-~-~-")
    break
