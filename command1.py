#Demonstration of commandline Arguments.


from sys import *
def main():
    print("total no of arguments are : ",len(argv))
    print("name of application : ",argv[0])
    print("first argument : ",argv[1])
    print("second argument : ",argv[2])
    print("third argument : ", argv[3])
if __name__ == "__main__":
    main()
    
    
    #python command1.py 12 hello 21 
