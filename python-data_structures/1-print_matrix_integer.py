

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Print each element of the row using str.format()
            # with end=' ' to print a space instead of a newline after each element
            print("{:d}".format(row[i]), end=' ')

        # After printing each row, add a newline to start the next row
        print()

# Test the function with the provided example
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
