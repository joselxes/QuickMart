import os
import sys
from queryGenerator import  *



def main():
    autoQuery=randQuery()
    autoQuery.saveQuery()
    batcmd=('python3 predictorStressTest.py < test_query.txt ')
    result  = os.popen(batcmd).readlines()
    varCount=0
    while result[0][:-1]== autoQuery.solution:
        print(autoQuery.solution, varCount)
        autoQuery=randQuery()
        autoQuery.saveQuery()
        result  = os.popen(batcmd).readlines()
        varCount+=1



if __name__ == "__main__":
    main()



