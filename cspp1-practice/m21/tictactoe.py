def play_tto():
    try:
        #count = 0
        #for i in range(len(tto)):
            #for j in range(len(tto[i])):
                #if tto[i][j] == 'x':
                    #count+=1
                #if tto[i][j] !='x' and tto[i][j]!='o' and tto[i][j]!='.':
                    #return 'invalid game'
            #if count == 9:
                #print('invalid game')
            #top row
        if tto[0][0] == 'x' and tto[0][1] == 'x' and tto[0][2] == 'x':
            return 'x'
            #across the middle 1
        elif tto[0][0] == 'x' and tto[1][1] == 'x' and tto[2][2] == 'x':
            return 'x'
            #across the middle 2
        elif tto[0][2] == 'x' and tto[1][1] == 'x' and tto[2][0] == 'x':
            return 'x'
            # first column
        elif tto[0][0] == 'x' and tto[1][0] == 'x' and tto[2][0] == 'x':
            return 'x'
            #second column
        elif tto[0][1] == 'x' and tto[1][1] == 'x' and tto[2][1] == 'x':
            return 'x'
            #third column
        elif tto[1][2] == 'x' and tto[0][2] == 'x' and tto[2][2] == 'x':
            return 'x'
            #middle row
        elif tto[1][0] == 'x' and tto[1][1] == 'x' and tto[1][2] == 'x':
            return 'x'
            #bottom row
        elif tto[2][0] == 'x' and tto[2][1] == 'x' and tto[2][2] == 'x':
            return 'x'
       
        else:
            return "o"

    except:
        print('invalid game')
        

import re   
def main():
    global tto
    tto =[]
    for i in range(3):
        b=input()
        a=list(re.sub("[^x,.,o]","",b))
        tto += [a]
    winner = play_tto()
    print(winner)
    
main()
