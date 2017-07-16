import time
import sys

'''
Function to check if given string is a completed and valid
sudoku.
Returns True if the string is valid and complete.
Else it returns False
'''
def gameover(string):
    if string.find('0')!=-1:
        return False
    i = 0

    #Checks if all rows have all digits from 1-9 
    for count in range(0,9):
        if len(set(string[i:i+9])) != 9:
            return False
        i += 9
    count = 0
    i = 0

    #Checks if all columns have all digits from 1-9
    for count in range(0,9):
        temp = ""
        for j in range(0,9):
            temp += string[count + 9*j]
        if len(set(temp)) != 9:
            return False
    l = [0,1,2,9,10,11,18,19,20]

    #Checks all 3x3 boxes of sudoku for digits from 1-9
    for i in range(0,3):
        temp1 = [k + 27*i for k in l]  
        for j in range(0,3):
            temp2 = [x + 3*j for x in temp1]
            if len(set([string[y] for y in temp2])) != 9:
                return False

    #String is valid if rows,columns, and 3x3 boxes have digits from 1-9
    return True


'''
Expands the current string to possible partial solutions.
'''
def expander(string):
    final_loc = string.find('0')
    final_domain = [1,2,3,4,5,6,7,8,9]
    locations = []
    for i in range(0,81):
        if string[i]=='0':
            locations.append(i)
    for loc in locations:
        box = [0,1,2,9,10,11,18,19,20]
        row = loc/9
        col = loc - 9*row
        row_elements = string[row*9:((row+1)*9)]
        col_elements = ""
        for i in range(0,9):
            col_elements += string[col + 9*i]
        box_col = col/3
        box_row = row/3
        box = [x + 3*box_col for x in box]
        box = [x + 27*box_row for x in box]
        box_elements = ""
        for x in box:
            box_elements += string[x]
        domain = list(set(['1','2','3','4','5','6','7','8','9']) - set(row_elements + col_elements + box_elements) - set(['0']))
        if len(domain)==0:
            return False
        if len(domain)<len(final_domain):
            final_domain = domain[:]
            final_loc = 1*loc
        if len(domain)==1:
            break
        temp = string[loc+1:]
    return [string[:final_loc] + str(i) + string[final_loc+1:] for i in final_domain]


'''
Function to display sudoku strings in 9x9 grid
'''
def display(string):
    for i in range(0,9):
        temp = string[i*9:i*9 + 9]
        disp = ""
        for j in range(0,9):
            disp += temp[j]
            if (j+1)%3==0:
                disp += " : "
            else:
                disp += "   "
        print disp
        if (i+1)%3==0:
            print "- - - - - - - - - - - - - - - - - - - - - - "
    print "------------"
    
if __name__=="__main__":
    file_name = sys.argv[1]
    display_option = sys.argv[2]
    f = open(file_name)
    avg = []

    for j in f:
        game_string = j.replace('.','0').strip()[:81]
        stack = []
        stack.append(game_string)
        start = time.time()
        while True:
            game = stack.pop()
            if gameover(game):
                print "solved"
                time_taken = time.time()-start
                print "time taken: ", str(time_taken)
                avg.append(time_taken)
                if display_option=='y':
                    display(game)
                break
            expanded = expander(game)
            if expanded:
                for i in expanded:
                    stack.append(i)  
    print "mean time: ", float(sum(avg)/len(avg))
     
     
            
