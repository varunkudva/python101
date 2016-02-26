#!/usr/bin/python -tt

def example_list():
    L = []
    for i in range(int(raw_input())): 
        command = raw_input().split()
        if command[0] == "insert":
            L.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print L
        elif command[0] == "remove":
            L.remove(int(command[1]))
        elif command[0] == "append":
            L.append(int(command[1]))
        elif command[0] == "sort":
            L.sort()
        elif command[0] == "pop":
            L.pop()        
        elif command[0] == "reverse":
            L.reverse()
            print L 
        else:
            none

           
def example_tuple():
    x = tuple(int (i) for i in (raw_input().split()))
    print hash(x)



        
if __name__ == '__main__':
   #example_list()
   example_tuple() 

