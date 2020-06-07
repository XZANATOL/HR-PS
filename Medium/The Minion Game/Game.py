#!/bin/python3
def minion_game(string):
    #consonants, vowels
    Stuart, kevin = 0, 0


    #check loop
    for i in range(len(string)):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            kevin += len(string) - i
        else:
            Stuart += len(string) - i
    

    #print score
    if kevin > Stuart:
        print("Kevin", kevin)
    elif Stuart > kevin:
        print("Stuart", Stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
