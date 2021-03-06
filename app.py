from flask import Flask, jsonify, request

import database
import database as db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'

desc_word = "word"
desc_translate = "translate"
desc_sentence1 = "sentence1"
desc_sentence1Trans = "sentence1translate"
desc_sentence2 = "sentence2"
desc_sentence2Trans = "sentence2translate"
desc_image = "image"


@app.route('/test', methods=['POST'])
def test():
    return "test"


@app.route('/addVerb', methods=['POST'])
def addVerb():
    verb1 = request.form["verb1"]
    verb2 = request.form["verb2"]
    verb3 = request.form["verb3"]
    translate = request.form[desc_translate]
    verbtype = request.form["verbtype"]
    ex1 = request.form["ex1"]
    ex1trans = request.form["ex1translate"]
    ex2 = request.form["ex2"]
    ex2trans = request.form["ex2translate"]
    ex3 = request.form["ex3"]
    ex3trans = request.form["ex3translate"]
    ET = database.EngTime()
    result = ET.addVerb(verb1,verb2,verb3,translate,
                        verbtype,ex1,ex1trans,ex2,ex2trans,ex3,ex3trans)
    if result:
        return "ok"
    else:
        return "kayıt var"

@app.route('/randomverb',methods=['POST'])
def randomverb():
    verb_type = request.form["type"]
    ET = database.EngTime()
    result = ET.RandomVerbs(verb_type)
    return result

@app.route('/controlverb',methods=['POST'])
def controlverb():
    verb = request.form["verb"]
    ET = database.EngTime()
    result = ET.controlVerb(verb)
    if result:
        return "var"
    else:
        return "yok"

@app.route('/gameRegularVerb',methods=['POST'])
def gameRegularVerb():
    ET = database.EngTime()
    return ET.GameRegularVerb()

@app.route('/gameirRegularVerb',methods=['POST'])
def gameirRegularVerb():
    ET = database.EngTime()
    return ET.GameirRegularVerb()

@app.route('/addWord', methods=['POST'])
def addWord():
    word = request.form["word"]
    translate = request.form["translate"]
    ex1 = request.form["ex1"]
    ex1trans = request.form["ex1t"]
    ET = database.EngTime()
    result = ET.addWord(word,translate,ex1,ex1trans)
    if not result:
        return "ex"
    else:
        return "ok"

@app.route('/randomWord',methods=['POST'])
def randomWord():
    ET = database.EngTime()
    result = ET.RandomWord()
    return result

@app.route('/controlWord',methods=['POST'])
def controlWord():
    word = request.form["word"]
    ET = database.EngTime()
    result = ET.controlWord(word)
    if result:
        return "var"
    else:
        return "yok"

@app.route('/addEveryDayWord', methods=['POST'])
def addEveryDayWord():
    word = request.form["word"]
    translate = request.form["translate"]
    ex1 = request.form["ex1"]
    ex1trans = request.form["ex1t"]
    ET = database.EngTime()
    result = ET.addEveryDayWord(word,translate,ex1,ex1trans)
    if not result:
        return "ex"
    else:
        return "ok"

@app.route('/randomEveryDayWord',methods=['POST'])
def randomEveryDayWord():
    ET = database.EngTime()
    result = ET.RandomEveryDayWord()
    return result

@app.route('/controlEveryDayWord',methods=['POST'])
def controlEveryDayWord():
    word = request.form["word"]
    ET = database.EngTime()
    result = ET.controlEveryDayWord(word)
    if result:
        return "var"
    else:
        return "yok"

@app.route('/addAdjectives', methods=['POST'])
def addAdjectives():
    adjectives = request.form["adjectives"]
    translate = request.form["translate"]
    ex1 = request.form["ex1"]
    ex1trans = request.form["ex1t"]
    ET = database.EngTime()
    result = ET.addAdjectives(adjectives,translate,ex1,ex1trans)
    if not result:
        return "ex"
    else:
        return "ok"

@app.route('/randomAdjectives',methods=['POST'])
def randomAdjectives():
    ET = database.EngTime()
    result = ET.RandomAdjectives()
    return result

@app.route('/controlAdjectives',methods=['POST'])
def controlAdjectives():
    adjectives = request.form["adjectives"]
    ET = database.EngTime()
    result = ET.controlAdjectives(adjectives)
    if result:
        return "var"
    else:
        return "yok"

@app.route('/addVocabulary', methods=['POST'])
def addVocabulary():
    vocabulary = request.form["vocabulary"]
    translate = request.form["translate"]
    ex1 = request.form["ex1"]
    ex1trans = request.form["ex1t"]
    ET = database.EngTime()
    result = ET.addVocabulary(vocabulary,translate,ex1,ex1trans)
    if not result:
        return "ex"
    else:
        return "ok"

@app.route('/randomVocabulary',methods=['POST'])
def randomVocabulary():
    ET = database.EngTime()
    result = ET.RandomVocabulary()
    return result

@app.route('/controlVocabulary',methods=['POST'])
def controlVocabulary():
    vocabulary = request.form["vocabulary"]
    ET = database.EngTime()
    result = ET.controlVocabulary(vocabulary)
    if result:
        return "var"
    else:
        return "yok"

@app.route('/addNouns', methods=['POST'])
def addNouns():
    nouns = request.form["nouns"]
    translate = request.form["translate"]
    ex1 = request.form["ex1"]
    ex1trans = request.form["ex1t"]
    ET = database.EngTime()
    result = ET.addNouns(nouns,translate,ex1,ex1trans)
    if not result:
        return "ex"
    else:
        return "ok"

@app.route('/randomNouns',methods=['POST'])
def randomNouns():
    ET = database.EngTime()
    result = ET.RandomNouns()
    return result

@app.route('/controlNouns',methods=['POST'])
def controlNouns():
    nouns = request.form["nouns"]
    ET = database.EngTime()
    result = ET.controlNouns(nouns)
    if result:
        return "var"
    else:
        return "yok"


if __name__ == '__main__':
    app.run()
