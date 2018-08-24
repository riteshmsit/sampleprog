global TTT, pos_input, count_input, X, o
TTT = []
pos_input = ['o', 'X', '.']
count_input = {'o':0, 'X':0, '.':0}
X = ['X', 'X', 'X'];o = ['o', 'o', 'o']
def game_TTT():
    """game ttt"""
    global c_X, c_o
    c_X = 0;c_o = 0
    for i in range(3):
        if TTT[i] == X or [TTT[0][i], TTT[1][i], TTT[2][i]] == X:
            c_X += 1
        if TTT[i] == o or [TTT[0][i], TTT[1][i], TTT[2][i]] == o:
            c_o += 1
    if [TTT[0][0], TTT[1][1], TTT[2][2]] == X or [TTT[0][2], TTT[1][1], TTT[2][0]] == X:
        c_X += 1
    if [TTT[0][0], TTT[1][1], TTT[2][2]] == o or [TTT[0][2], TTT[1][1], TTT[2][0]] == o:
        c_o += 1
def check_invalid():
    """invalid game"""
    for i in range(3):
        for j in range(3):
            if TTT[i][j] not in pos_input:
                return 0
            count_input[TTT[i][j]] += 1
    return 1
def read_input():
    """read input"""
    str_line = []
    for i in range(3):
        str_line = input()
        str_line = str_line.split()
        TTT.append(str_line)
def write_output():
    """write output"""
    if (check_invalid() == 0):
        print("invalid input")
    elif abs(count_input['X'] - count_input['o']) > 1:
        print("invalid game")
    else:
        game_TTT()
        if c_X == 1 and c_o == 1:
            print("invalid game")
        elif c_X == 1:
            print("X")
        elif c_o == 1:
            print("o")
        else:
            print("draw")
def main():
    """main"""
    read_input()
    write_output()
main()
