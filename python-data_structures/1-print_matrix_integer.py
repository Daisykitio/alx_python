

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            # Use str.format() to print integers without casting them to strings
            if i == len(row) - 1:
                # For the last element in the row, add a newline character after the number
                print("{:d}".format(num))
            else:
                # For other elements, add a space after the number
                print("{:d}".format(num), end=" ")
