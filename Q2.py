def is_palindrome(word : str) -> bool:
    ''' Check whether input str is a palindrome
        Time complexity O(n)
    '''
    word = word.lower()
    length = len(word)
    
    for i in range (0, int(length/2)):
        if word[i] != word[length-i-1]:
            return False    
    return True

def main() -> None:
    while True:
        keyboard_ip = input("Enter a string for palindrome checking: ")
        if keyboard_ip.lower() == 'q':
            print("Thank you! Goodbye!")
            break
        if is_palindrome(keyboard_ip):
            print(f'{keyboard_ip} is a palindrome.' )
        else:
            print(f'{keyboard_ip} is NOT a palindrome.' )
    return

if __name__ == '__main__':
    main()