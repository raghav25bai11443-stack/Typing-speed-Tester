import time
import datetime
import threading
from typing import Self

class tester:
    def __init__(self, paragraph): # type: ignore
        self.correctWords = []
        self.incorrectWords = {}
        self.typedwords = []
        self.totalWords = []
        self.input = None
        self.paragraph = paragraph
        self.accuracy = 0
        self.time = 0
        self.wordPermin = 0
        self.run()

    def clock(self):
        while len(self.typedWords) == 0:
            self.time += 1
            time.sleep(1)

    def run(self):
        threading.Thread(target=self.clock).start()
        threading.Thread(target=self.testspeed).start()

    def testSpeed(self):
        print('\n\n'+self.paragraph+'\n\n')
        self.inpu = str(input('\t\n'+'start typing\n\n'))
        self.totalWords = self.paragh.split(' ')
        self.typedWords = self.input.split(' ')

        try:
            for i in range(len(self.typedwords)):
                if(self.typedwords[i] == self.totalWords[i]):
                    self.correctwords.append(self.typedWords[i])
                else:
                    self.incorrectWords.append(self.typedWords[i])

        except Exception as e:
            print(e)

        
        self.accuracy = len(self.correctwords/len(self.totalWords)) * 100
        self.wordPerMin = len(self.typedWords) / (self.time / 60)

        print('\n\nResult :--')
        print(f'Accuracy: -- {self.accuracy}')
        print(f'Word per minute: -- {self.wordPerMin}')
        print(f'Time taken: -- {self.time} seconds')
        print(f'Correct words: -- {self.correctWords}')
        print(f'Incorrect words: -- {self.incorrectWords}')
    