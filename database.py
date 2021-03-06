import couchdb
import random
couch = couchdb.Server("http://admin:test@125.125.125.125:5984/")


class EngTime():
    def __init__(self):

        self.verbs = couch["verbs"]
        self.words = couch["technicalwords"]
        self.everydaywords = couch["everydaywords"]
        self.adjectives = couch["adjectives"]
        self.vocabulary = couch["vocabulary"]
        self.nouns = couch["nouns"]

    def addVerb(self,verb1,verb2,verb3,translate,verb_type,ex1,ex1t,ex2,ex2t,ex3,ex3t):
        cntrlverb = self.controlVerb(verb1)
        if not cntrlverb:
            doc = {"verb1":verb1.lower(),
                   "verb2":verb2.lower(),
                   "verb3":verb3.lower(),
                   "translate":translate.lower(),
                   "type":verb_type,
                   "ex1":ex1,
                   "ex1translate":ex1t,
                   "ex2":ex2,
                   "ex2translate":ex2t,
                   "ex3":ex3,
                   "ex3translate":ex3t}
            self.verbs.save(doc)
            return True
        else:
            return False


    def RandomVerbs(self,type):
        main_list = []
        database = couch["verbs"]
        for doc in database.find({"selector":{"type":type}}):
            main_list.append([doc["verb1"],
                   doc["verb2"],
                   doc["verb3"],
                   doc["translate"],
                   doc["type"],
                   doc["ex1"],
                   doc["ex1translate"],
                   doc["ex2"],
                   doc["ex2translate"],
                   doc["ex3"],
                   doc["ex3translate"]])
        rnd = random.randint(0,len(main_list)-1)
        res_dict ={"verb1":main_list[rnd][0],
                   "verb2":main_list[rnd][1],
                   "verb3":main_list[rnd][2],
                   "translate":main_list[rnd][3],
                   "type":main_list[rnd][4],
                   "ex1":main_list[rnd][5],
                   "ex1translate":main_list[rnd][6],
                   "ex2":main_list[rnd][7],
                   "ex2translate":main_list[rnd][8],
                   "ex3":main_list[rnd][9],
                   "ex3translate":main_list[rnd][10]}
        return res_dict

    def controlVerb(self,verb):
        database = couch["verbs"]
        for doc in database.find({"selector":{"verb1":verb.lower()}}):
            return True
        return False

    def GameRegularVerb(self):
        try:
            onegame = self.RandomVerbs("regular")
            twogame = self.RandomVerbs("regular")
            treegame = self.RandomVerbs("regular")
            fourgame = self.RandomVerbs("regular")

            doc ={"verb":onegame['verb1'],
                  "real":onegame['translate']}

            secimlistem =[onegame['translate'],
                          twogame['translate'],
                          treegame['translate'],
                          fourgame['translate']]
            a = 0
            while True:
                a +=1
                rnd = random.randint(0,len(secimlistem)-1)
                doc["t"+str(a)] = str(secimlistem[rnd])
                secimlistem.pop(rnd)
                if len(secimlistem) ==0:
                    break
            return doc
        except:
            docx={}
            return docx

    def GameirRegularVerb(self):
        try:
            onegame = self.RandomVerbs("irregular")
            twogame = self.RandomVerbs("irregular")
            treegame = self.RandomVerbs("irregular")
            doc ={"verb":onegame['verb1'],
                  "t1":onegame['translate'],
                  "t2":twogame['translate'],
                  "t3":treegame['translate']}
            return doc
        except:
            docx={}
            return docx

    def addWord(self,word,translate,ex1,ex1t):
        doc = {"word":word.lower(),
               "translate":translate.lower(),
               "ex1":ex1,
               "ex1translate":ex1t}
        self.words.save(doc)
        return True

    def RandomWord(self):
        main_list = []
        database = couch["technicalwords"]
        for i in database:
            for doc in database.find({"selector":{"_id":i}}):
                main_list.append([ doc["word"],
                                   doc["translate"],
                                   doc["ex1"],
                                   doc["ex1translate"]])
        rnd = random.randint(0,len(main_list)-1)
        res_dict ={"word":main_list[rnd][0],
                   "translate":main_list[rnd][1],
                   "ex1":main_list[rnd][2],
                   "ex1t":main_list[rnd][3]}
        return res_dict

    def controlWord(self,word):
        for doc in self.words.find({"selector":{"word":word.lower()}}):
            return True
        return False

    def addEveryDayWord(self,word,translate,ex1,ex1t):
        doc = {"word":word.lower(),
               "translate":translate.lower(),
               "ex1":ex1,
               "ex1translate":ex1t}
        self.everydaywords.save(doc)
        return True

    def RandomEveryDayWord(self):
        main_list = []
        for i in self.everydaywords:
            for doc in self.everydaywords.find({"selector":{"_id":i}}):
                main_list.append([ doc["word"],
                                   doc["translate"],
                                   doc["ex1"],
                                   doc["ex1translate"]])
        rnd = random.randint(0,len(main_list)-1)
        res_dict ={"word":main_list[rnd][0],
                   "translate":main_list[rnd][1],
                   "ex1":main_list[rnd][2],
                   "ex1t":main_list[rnd][3]}
        return res_dict

    def controlEveryDayWord(self,word):
        for doc in self.everydaywords.find({"selector":{"word":word.lower()}}):
            return True
        return False

    def addAdjectives(self,adjectives,translate,ex1,ex1t):
        if not self.controlAdjectives(adjectives):
            doc = {"adjectives":adjectives.lower(),
                   "translate":translate.lower(),
                   "ex1":ex1,
                   "ex1translate":ex1t}
            self.adjectives.save(doc)
            return True
        else:
            return False

    def RandomAdjectives(self):
        main_list = []
        for i in self.adjectives:
            for doc in self.adjectives.find({"selector":{"_id":i}}):
                main_list.append([ doc["adjectives"],
                                   doc["translate"],
                                   doc["ex1"],
                                   doc["ex1translate"]])
        rnd = random.randint(0,len(main_list)-1)
        res_dict ={"adjectives":main_list[rnd][0],
                   "translate":main_list[rnd][1],
                   "ex1":main_list[rnd][2],
                   "ex1t":main_list[rnd][3]}
        return res_dict

    def controlAdjectives(self,adjectives):
        for doc in self.adjectives.find({"selector":{"adjectives":adjectives.lower()}}):
            return True
        return False

    def addVocabulary(self,vocabulary,translate,ex1,ex1t):
        if not self.controlVocabulary(vocabulary):
            doc = {"vocabulary":vocabulary.lower(),
                   "translate":translate.lower(),
                   "ex1":ex1,
                   "ex1translate":ex1t}
            self.vocabulary.save(doc)
            return True
        else:
            return False

    def RandomVocabulary(self):
        main_list = []
        for i in self.vocabulary:
            for doc in self.vocabulary.find({"selector":{"_id":i}}):
                main_list.append([ doc["vocabulary"],
                                   doc["translate"],
                                   doc["ex1"],
                                   doc["ex1translate"]])
        rnd = random.randint(0,len(main_list)-1)
        res_dict ={"vocabulary":main_list[rnd][0],
                   "translate":main_list[rnd][1],
                   "ex1":main_list[rnd][2],
                   "ex1t":main_list[rnd][3]}
        return res_dict

    def controlVocabulary(self,vocabulary):
        for doc in self.vocabulary.find({"selector":{"vocabulary":vocabulary.lower()}}):
            return True
        return False

    def addNouns(self,nouns,translate,ex1,ex1t):
        if not self.controlNouns(nouns):
            doc = {"nouns":nouns.lower(),
                   "translate":translate.lower(),
                   "ex1":ex1,
                   "ex1translate":ex1t}
            self.nouns.save(doc)
            return True
        else:
            return False

    def RandomNouns(self):
        main_list = []
        for i in self.nouns:
            for doc in self.nouns.find({"selector":{"_id":i}}):
                main_list.append([ doc["nouns"],
                                   doc["translate"],
                                   doc["ex1"],
                                   doc["ex1translate"]])
        rnd = random.randint(0,len(main_list)-1)
        res_dict ={"nouns":main_list[rnd][0],
                   "translate":main_list[rnd][1],
                   "ex1":main_list[rnd][2],
                   "ex1t":main_list[rnd][3]}
        return res_dict

    def controlNouns(self,nouns):
        for doc in self.nouns.find({"selector":{"nouns":nouns.lower()}}):
            return True
        return False
