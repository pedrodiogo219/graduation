#!/usr/bin/python

import threading
import time

class myThread (threading.Thread):
    def __init__ (self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.awake = False
        self.text = ''
        self.next = None
        self.finished = False

    def setNext(self, next):
        self.next = next

    def run(self):
        print(f'Thread {self.id} - Running')

        #roda enquanto nao terminou
        while not self.finished:
            #se eu nao devo acordar, volto a dormir
            if not self.awake:
                time.sleep(0.100)

            #se for minha vez de acordar
            else:
                #flag pra checar se eu achei alguma letra minuscula
                find = False
                for i in range (0, len(self.text)):
                    #quando achar a primera minuscula
                    #faz a troca e quebra o laço
                    if self.text[i].islower():
                        find = True
                        self.text = self.text[:i] + self.text[i].upper() + self.text[i+1:]
                        break

                #se eu fiz alguma troca, volto a dormir e acordo a proxima
                if find:
                    print(f'Thread#{self.id} --- {self.text}')
                    self.awake = False
                    self.next.wakeUp(self.text)
                #se nao fiz troca, o trabalho esta terminado
                else: 
                    self.finished = True
                    

        #agora que eu sei que ja terminei, aviso a proxima
        self.next.finished = True
        print(f'Thread#{self.id} - Exiting')
    
    #acorda a proxima thread
    def wakeUp(self, text):
        self.text = text
        self.awake = True

class Anel:
    def __init__(self, n):
        self.threads = [myThread(i) for i in range(0, n)]
        for i in range(0, n-1):
            self.threads[i].setNext(self.threads[i+1])
            self.threads[n-1].setNext(self.threads[0])


    def start(self, text):
        for t in self.threads:
            t.start()
        self.threads[0].wakeUp(text)

    def join(self):
        for t in self.threads:
            t.join()

def main():
    anel = Anel(3)

    text = input('Digite uma string:\n')
    
    anel.start(text)
    anel.join()
    print('exiting main')


main()