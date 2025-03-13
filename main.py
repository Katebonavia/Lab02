import re

import translator as tr

t = tr.Translator("dictionary.txt")

while(True):

    t.printMenu()

    t.loadDictionary()

    txtIn = input("Cosa vuoi fare? ")

    def validateInput(input):
        pattern = r"[a-zA-Z]"
        if re.match(pattern,input):
            pass
        else:
            raise Exception("Invalid input")


    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere? ")
        txtIn = input()
        validateInput(txtIn)
        t.handleAdd(txtIn)
        break
    if int(txtIn) == 2:
        print("Ok, quale parola devo tradurre? ")
        txtIn = input()
        validateInput(txtIn)
        t.handleTranslate(txtIn)
        break
    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare con wildcard? ")
        txtIn = input()
        t.handleWildCard(txtIn)
        break
    if int(txtIn) == 4:
        break