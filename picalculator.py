from random import *
import json
import requests
from time import time

def getRatio():
    ratio =  0.0
    for i in range(1,13000001):
        ratio += pow(-1,i+1)/float((2*i-1))
    return ratio

def getPi(factor):
    return 4*factor

def main():
    
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

if __name__ == "__main__":
    main()
