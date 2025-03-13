class Dictionary:
    def __init__(self, nomefile):
        self.nomefile = nomefile

    def addWord(self, word):
        readfile = open(self.nomefile, 'r')
        word_list = word.split(" ")
        print(word_list)
        lines_dict = [line for line in readfile]
        word_exist = False
        for i in range(len(lines_dict)):
            if lines_dict[i].split(" ")[0].__eq__(word.lower().split(" ")[0]):
                lines_dict[i] = lines_dict[i].rstrip()+word.removeprefix(word.split(" ")[0])+'\n'
                print(lines_dict[i])
                word_exist=True
                i+=1
        if word_exist.__eq__(False):
            lines_dict.append('\n'+word)
        writefile = open(self.nomefile, 'w')
        for line in lines_dict:
            writefile.write(f"{line}")

    def translate(self, word):
        readfile = open(self.nomefile, 'r')
        word_lowcase = word.lower()
        for line in readfile:
            if line.__contains__(word_lowcase):
                print(line.removeprefix(word+' '))


    def translateWordWildCard(self, word):
        word_split = list(word)
        index_qm = word_split.index('?')
        del word_split[index_qm]
        print(word_split)
        print(index_qm)
        readfile = open(self.nomefile, 'r')
        lines_dict = [line.rstrip() for line in readfile]
        for line in lines_dict:
            if len(list(line.split(' ')[0]))==len(list(word)):
                lett_first_word = list(line.split(' ')[0])
                del lett_first_word[index_qm]
                if lett_first_word==word_split:
                    print(line)

