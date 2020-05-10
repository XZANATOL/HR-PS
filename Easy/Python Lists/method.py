#Entering numbers of operations
N = int(input())
#list to be operated on
List = []
for i in range(N):
    #command input
    command = input().split()

    #check case
    if "insert" in command:
          List.insert(int(command[1]), int(command[2]))
    elif "print" in command:
        print(List)
    elif "remove" in command:
        if len(List) !=0:
            List.remove(int(command[1]))
    elif "append" in command:
        List.append(int(command[1]))
    elif "sort" in command:
           List.sort()
    elif "pop" in command:
       if len(List) !=0:
            List.pop()
    elif "reverse" in command:
        List.reverse()