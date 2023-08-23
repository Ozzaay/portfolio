import time
import itertools

password = "rambo1"
wordlist = ["a","b","c","d","e","f","g","h","j","i","k","l","m","n","o","p","q","r","s","t","x","y","z","å","ä","ö","1","2","3","4","5","6","7","8","9","0"]

def guess_password(cracked):
    global start
    global end
    start = time.time()
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(wordlist, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == cracked:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            # ta bort kommentaren från print om man vill se den jobba men det tar mycket längre tid
            # print(guess, attempts)
            end = time.time()
            
            
            
def main():
    print(guess_password(password))
    print(end - start)
    
if __name__ == "__main__":
    main()