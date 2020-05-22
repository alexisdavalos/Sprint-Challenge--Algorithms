'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    #check if word is a str
    if isinstance(word, str):
        # base case word is less than 2 characters it cannot contain "th"
        if len(word) < 2:
            return 0
        # check first two characters of input 
        elif word[0:2] == 'th':
            #recurse and check next two characters
            print(f'counting... {word[2:]}')
            return 1 + count_th(word[2:])
            
        else:
            return count_th(word[1:])
        #change state
    else:
        print('invalid input')
        return 0
    

print(count_th('thoththoththoth'))
