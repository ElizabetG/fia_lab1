import random

# let's detect Moldavians on the moon. They will surely be a good source of income for moon HoReCa

mold1 = ['russian', 'vodka', 'mamaliga', 'manele', 'Independence Day']
mold2 = ['romanian', 'wine', 'sarmale', 'rock', 'Wine Day']
mold3 = ['moldavian', 'wine', 'sarmale', 'manele', 'Wine Day']
mold4 = ['romanian', 'wine', 'ciorba', 'pop', 'Romanian Language Day']
mold5 = ['moldavian', 'wine', 'sarmale', 'rock', 'Independence Day']
mold6 = ['russian', 'vodka', 'ciorba', 'pop', 'Wine Day']
mold7 = ['russian', 'vodka', 'ciorba', 'pop', 'Wine Day']

# differencesList = ['mother language', 'favorite drink', 'favorite food', 'favorite music', 'favorite holiday']
moldavians = [mold1, mold2, mold3, mold4, mold5, mold6, mold7]
molds = moldavians

# here we declare list of differences/questions which can be put; and double it in another variable
diff = ['mother language', 'favorite drink', 'favorite food', 'favorite music', 'favorite holiday']
diffP = ['mother language', 'favorite drink', 'favorite food', 'favorite music', 'favorite holiday']

# here we stock the answers that user gave
answers = []

# here we manage the question putting and the removing of the question from the list of possible questions
def question(choice):
    print('What is their ' + choice + '?')
    answer = input()
    diffP.remove(choice)
    return answer

# here we filter moldavians based on the answer of user
def filterOptions(answer):
    global molds
    moldsToRemove = []
    for mold in molds:
        if answer not in mold:
            moldsToRemove.append(mold)
    for moldToRemove in moldsToRemove:
        molds.remove(moldToRemove)

# here we will check which questions are useless to ask, like if remaining molds have common differences (e.g. both like wine)
def checkForUselessQuestions():
    global diffP
    result = set(molds[0])  
    for currSet in molds[1:]:  
        result.intersection_update(currSet)
    result = list(result) 
    if result:
        for item in result:
            index = molds[0].index(item)
            itemToRemove = diff[index]
            if itemToRemove in diffP:
                diffP.remove(itemToRemove)

# here we check if there are anymore questions to ask. if not, to print the final result
def checkForRemainingQuestions():
    if (len(diffP) == 0):
        printFinalResult()

# here we check if final answer is ready based on the remaining moldavians list
def isFinalAnswerReady():
    return len(molds) == 1

# we print intermediate/final results 
def printIntermediateAnswer():
    print('INTERMEDIATE Answer: Potential moldavians are: ')
    print(molds)

def printFinalResult():
    print('FINAL Answer: The corresponding moldavian(s) based on your answers: ')
    print(molds)
    print('P.S. Your answers were: ')
    print(answers)
    exit()

# we start the poll
def startPoll():
    global molds
    global diffP
    global answers
    for i in range(len(diffP)):
        answer = question(random.choice(diffP))
        answers.append(answer)
        filterOptions(answer)
        if isFinalAnswerReady():
            printFinalResult()
        else:
            checkForUselessQuestions()
            checkForRemainingQuestions()
            printIntermediateAnswer()

startPoll()