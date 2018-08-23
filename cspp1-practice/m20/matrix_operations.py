def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''

    

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    try:
        row_1 = 0
        row_2 = 0
        for i in range(len(m1)):
            row_1 += 1
            col_1 = len(m1[i])
        for i in range(len(m2)):
            row_2 += 1
            col_2 = len(m2[i])
        m_3 = []
        if row_1 == row_2 and col_2 == col_1: 
            for r in range(len(row_1)):
                for c in range(len(col_1)):
                    m_3[r][c] += m1[r][c] + m2[r][c]


    except :
        print("Error: Matrix shapes invalid for addition")


    
    return m_3




def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    size_of_matrix1 = input()
    size_of_matrix1 = size_of_matrix1.split(",")
    matrix1 = []
    size_of_matrix1[0] = int(size_of_matrix1[0])
    size_of_matrix1[1] = int(size_of_matrix1[1])
    for i in range(size_of_matrix1[1]):
        matrix1.append([])
    for i in range(size_of_matrix1[0]):
        for j in range(size_of_matrix1[1]):
            matrix1[i].append(j)
            matrix1[i][j]=0
    for i in range(0,size_of_matrix1[0],size_of_matrix1[1]):
        for j in range(size_of_matrix1[1]):
            row_values = input()
            row_values = [int(number) for number in row_values.split(" ")]
            matrix1[j] = row_values
    return matrix1
    except :
        print("Error: Invalid input for the matrix")
        return None

def main():
    # read matrix 1
    a = read_matrix()
    # read matrix 2
    b = read_matrix()
    # add matrix 1 and matrix 2
    addition = add_matrix(a,b)

    # multiply matrix 1 and matrix 2
    multiplication = mult_matrix(a,b)

if __name__ == '__main__':
    main()
