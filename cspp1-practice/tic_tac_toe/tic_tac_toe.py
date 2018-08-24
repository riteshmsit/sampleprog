"""
This function is to declare the winner of tic-tac-toe game.
"""
# def replace_element(element_1, position_1):
#   dummy_matrix = [[00, 01, 02], [10, 11, 12], [20, 21, 22]]
#   dummy_matrix[position_1[0]][position_1[1]] = element_1
#   return dummy_matrix

# def display_matrix(element_1, position_1):
#   resultant_matrix = replace_element(element_1, position_1)
#   for each_row in resultant_matrix:
#       for each_element in each_row:


def declare_result(user_input):
    """
    This function is to take input and declare the winner.
    """
    # The valid user inputs are x, o.
    # iterable_element = 0
    # if iterable_element == 0:
    #   print(diplay_matrix(0, 00))
    # user_input = input()
    # Please choose where you want to place your element x or o.
    # user_input1 = input()
    # user_input = diaplay_matrix(user_input, user_input1)
    count_x = user_input.count("x")
    count_o = user_input.count("o")
    count_dot = user_input.count(".")
    if count_x + count_o + count_dot != 9:
        return "invalid input"
    if not (count_x <= 5 and count_o <= 5):
        return "invalid game"
    elif count_x == count_o:
        return "invalid game"
    user_input = user_input.splitlines()
    #print(user_input)
    for each_element in range(3):
        user_input[each_element] = user_input[each_element].split(" ")
    if ((user_input[0][0] == "x" and user_input[1][1] == "x") and user_input[2][2] == "x")\
        or ((user_input[0][2] == "x" and user_input[1][1] == "x") and user_input[2][0] == "x"):
        return "x"
    elif ((user_input[0][0] == "o" and user_input[1][1] == "o") and user_input[2][2] == "o")\
        or ((user_input[0][2] == "o" and user_input[1][1] == "o") and user_input[2][0] == "o"):
        # print(1)
        return "o"
    for each_row in user_input:
        count_x = each_row.count("x")
        count_o = each_row.count("o")
        #print(count_x, count_o)
        if count_x == 3:
            #print(1_1)
            return "x"
        elif count_o == 3:
            #print(2)
            return "o"
    for each_row in range(3):
        for each_element in range(3):
            x_list = []
            #print(user_input[each_row][each_element])
            if user_input[each_row][each_element] == "x":
                for each_row in range(3):
                    x_list.append(user_input[each_row][each_element])
                    #print(x_list)
                    #print(count_x)
                    count_x = x_list.count("x")
                    #print(count_x)
                    if count_x == 3:
                        #print("b")
                        return "x"
        for each_element in range(3):
            o_list = []
            if user_input[each_row][each_element] == "o":
                for each_row in range(3):
                    o_list.append(user_input[each_row][each_element])
                    count_o = o_list.count("o")
                    if count_o == 3:
                        #print(3)
                        return "o"
    return "draw"

def main():
    """
    This function is to take input and call the result function.
    """
    user_input1 = input()
    user_input2 = input()
    user_input3 = input()
    user_input = user_input1 + "\n" + user_input2 + "\n" + user_input3
    #print(user_input)
    print(declare_result(user_input))

if __name__ == '__main__':
    main()
