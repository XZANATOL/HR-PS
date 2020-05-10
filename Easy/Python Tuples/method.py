if __name__ == '__main__':
    #recieving inputs
    n = int(input())
    integer_list = input().split()
    #loop of integer conversion
    for i in range(n):
        integer_list[i] = int(integer_list[i])
    t= tuple(integer_list)
    #hash print
    print(hash(t))