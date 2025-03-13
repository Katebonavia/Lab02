import dictionary as dict

class Translator:

    def __init__(self, nomefiledict):
        self.dict_to_use = dict.Dictionary(nomefiledict)

    def printMenu(self):
        menu_scelte = ["1. Aggiungi nuova parola", "2. Cerca una traduzione",
                       "3. Cerca con wildcard", "4. Exit"]
        print("---------------------------------")
        print("   Translator Alien-Italian")
        print("---------------------------------")
        for i in range(len(menu_scelte)):
            print(menu_scelte[i])

    def loadDictionary(self):
        pass

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.dict_to_use.addWord(entry)


    def handleTranslate(self, query):
        self.dict_to_use.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        self.dict_to_use.translateWordWildCard(query)
        pass