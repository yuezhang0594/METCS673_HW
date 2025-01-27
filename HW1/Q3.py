def parse_inp(text:str) -> list:
    ''' Parse keyboard input for combining lists.
        in format of [a,b,c]
    '''
    try:
        inp_list = text.strip('[]').split(',')
        oup_list = [item.strip() for item in inp_list]
        return oup_list
         
    except ValueError:
        print("Error: Invalid input format. Please use the format [a,b,c].")

def main():
    inp_list1 = input("Input 1st lists of equal length in the format of [a,b,c]: ")
    inp_list2 = input("Input 2nd lists of equal length in the format of [1,2,3]: ")
    
    list1  = parse_inp(inp_list1)
    list2  = parse_inp(inp_list2)
    
    if len(list1) != len(list2):
        print("Error: The two lists should have an equal length.")
        return
    
    combined_list = []
    for i in range(len(list1)):
            combined_list.append(list1[i])
            combined_list.append(list2[i])
    print(combined_list)
    return

if __name__ == '__main__':
    main()