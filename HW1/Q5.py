def is_leap_yr(yr:int) -> bool:
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