#%%
r=input('Begin?(y/n):')
while r!='n':
    import random
    import time
    hanger=['''
                     _____
                    |     |
                          |
                          |
                          |
                         _|_''', '''
                     _____
                    |     |
                    O     |
                          |
                          |
                         _|_''', '''
                     _____
                    |     |
                    O     |
                    |     |
                    |     |
                         _|_''', '''
                     _____
                    |     |
                    O     |
                   /|     |
                    |     |
                         _|_''', '''
                     _____
                    |     |
                    O     |
                   /|\    |
                    |     |
                         _|_''', ''' 
                     _____
                    |     |
                    O     |
                   /|\    |
                    |     |
                   /     _|_''', '''
                     _____
                    |     |
                    O     |
                   /|\    |
                    |     |
                   / \   _|_''','''
           ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
           ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    
                    
                        \O/      
              ~WINNER~   |   ~WINNER~        
                         |    
                        / \ 
                                           
           ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
           ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']
    looper=1
    while looper==1:
        word_list="anarchy mechanic apple bananna couch habanero pepper walking dead oak dog nut nuts peanut dayman hangman horse basketball tree barn chicken television phone chair table cat".split()
        guessed_letters=[]
    
    
        def get_word():
            the_word=random.choice(word_list)
            return the_word
            
        word=get_word()
        word=word.upper()
        blanks='-' * len(word)  
        wrong=-1   
        right=[]
        
        def get_guess():
            print()
            print()
            guess=input("             Guess A Letter - ")
            time.sleep(1,1)
            guess=guess.upper()
            print() 
            if guess in guessed_letters:
                time.sleep(1.1)
                print("   " + guess + " Has Already Been Chosen, Try Again")
                get_guess()
            elif len(guess) !=1:
                time.sleep(1.1)
                print("         Pick One Letter At A Time")
                get_guess()
            elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ':
                time.sleep(1.1)
                print("            Only Pick Letters")
                get_guess()
            else:
                guessed_letters.append(guess)
            return guess
    
        running=True
        while running==True: 
            right=[]  
            for i in range(len(word)):
               if word[i] in guessed_letters:
                    blanks=blanks[:i] + word[i] + blanks[i+1:]                
                    right.append(i)
            time.sleep(1.1)
            print("\n" * 7)
        
            if wrong < 5:
                print(hanger[wrong+1])
            else:
                print(hanger[wrong+1])
                print()
                print("                   Loser")
                running=False
                
            if len(right)==len(word):
                print()
                print()
                print(hanger[7])
                running=False
                break
         
        
            print()
            print()
            print("                " + blanks + "") 
            print()
            print()
            print("         ", end=' ')
         
            for i in range(len(guessed_letters)):
                 print("", end='')
                 print(guessed_letters[i], end='')
             
            guess=get_guess()   
            if not guess in word:
                wrong=wrong+1
    time.sleep(11)
    r=input('Wanna play again?:')