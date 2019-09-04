from random import *
import json
import requests
from time import time

def getRatio():
    ratio =  0.0
    for i in range(1,1000001):
        ratio += pow(-1,i+1)/float((2*i-1))
    return ratio

def getPi(factor):
    return 4*factor

def execLocal():
    timer1 = time()
    temp = getPi(getRatio())
    timer2 = time()
    print 'Pi value:\t',temp ,'latency:\t', timer2-timer1

def main():
    while 1:
        print 'Select a option:'
        print '1)\tExecute pi local calculation'
        print '2)\tExecute latency test'
        print '3)\tExit'
        option = input('Give me a number: ')
        if int(option) == 1:
            execLocal()
            break
        elif int(option) == 2:
            print '\tC/S model latency'+'\t'+'Local model latency'
            for i in range (10):
                #execute the local calculation
                btime2 = time()
                getPi(getRatio())
                etime2 = time()
                latency2 =  etime2 - btime2 
                #execute the C/S calculation
                btime1 = time()
                #request the ratio to the url of new project
                res = requests.get('http://www.practice3icc.appspot.com/').json()['value']
                getPi(res)
                etime1 = time()
                latency1 =etime1 - btime1
                #print 'C/S model latency: ', latency1, '\n','local model latency: ', latency2
                print i+1,'\t',latency1, '\t\t', latency2
            break    
        else:
            print 'Exit'
            break

if __name__ == "__main__":
    main()
