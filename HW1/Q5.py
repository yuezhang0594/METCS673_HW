def is_leap_yr(yr:int) -> bool:
    ''' Check input year number is leap year or not'''
    
    # A leap year meet 2 cases:  
    #   1: can be divided by 4  and  NOT dividead by 100
    #   2: can be divided by 400
     
    if (yr % 4 == 0 and yr % 100 !=0) or (yr % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        yr = int(input("Enter a year: ")) 
        
        if is_leap_yr(yr):
            print(f'{yr} is a leap year!!!')
        else:
            print(f'{yr} is NOT a leap year... \t:(')
                    
    except ValueError:
        print("Please enter a valid year (in num).")   

if __name__ == '__main__':
    main()