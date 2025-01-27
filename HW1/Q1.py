def print_multiplication_table(max_num : int) -> None:
    ''' function to print out a multiplication table using input "max_num" 
        O(n^2) complxity 
    '''
    # Print the table rows
    for i in range(1, max_num + 1):
        for j in range(1, max_num + 1):
            print(f"{i * j}\t", end="")
        print()
    return

if __name__ == "__main__":
    print_multiplication_table(12)