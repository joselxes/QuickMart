
from queryGenerator import  *



def main():
    autoQuery=randQuery()
    autoQuery.saveQuery()
    print("An input file, for predictor.py has been created as 'test_query.txt'")



if __name__ == "__main__":
    main()



