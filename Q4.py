def fibonacci(n:int) -> list:
    '''Compute a list fibonacci numbers with a "memoery"
        time complexity O(n)
        space O(n)
        '''
    fibo_list = [1, 1]
    
    # computer next fibonacci number 
    for i in range(2, n):
        next_fibo = fibo_list[i-2] + fibo_list[i-1]
        fibo_list.append(next_fibo)
    
    return fibo_list

def main():
    num = input("Number of Fibonacci numbers to compute: ")
    num = int(num)
    
    fibo_num = fibonacci(num)
    # print the list of fibo_num
    print(f'A list of {num}  Fibonacci numbers:')
    print(fibo_num)
    
if __name__ == '__main__':
    main()