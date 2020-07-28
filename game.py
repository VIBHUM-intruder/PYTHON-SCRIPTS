#try block to prevent ValueError and other errors if any

try :
    
    import random                     #module for random function
    
    guess=random.randint(0,100)       #guess no. should be random so that creators of the code can also play

#    print(guess)   #printing guessed no. for debugging purpose this line can be removed while playing
        
    noa=9          #noa ---> no. of attempts
            
    while noa!=0:   

        
                print(" ")
                num = (input("ENTER YOUR GUESS   \n"))
                
                if int(num)>100:                    #limiting entered value upto 100
                         print(" ")
                         print("WARNING ---> YOU'VE ENTERED A WRONG ! VALUE ENTER FROM 0 TO 100 ")
                         print(" ")
                         continue
                          
                
                if int(num)<0:                      #limiting entered value for atleast 0
                         print("WARNING ---> YOU'VE ENTERED A WRONG ! VALUE ENTER FROM 0 TO 100 ")
                         continue                   #continue so that if wrong value is entered noa shouldn't decrease 
                                                    #so as to provide efficiency to uses
 
                if int(num)==guess :
                         print("NICE, YOU WON")
                         break

# IF EVERYTHING IS CORRECT HERE ARE THE LOOPS
                                        
                if int(num)!=guess and noa!=0  :

                    noa-=1                                     
                    
                    if int(num)<=(guess+5) and int(num)>(guess):
                        print("no. of guesses left"," ",noa)
                        print("                                ")
                        print(" msg -> close enough")
                        print(" ")
                        print("##################################")
                                            
                    elif int(num)<=(guess+10) and int(num)>(guess+5):
                        print("no. of guesses left"," ",noa)
                        print("                                ")
                        print("msg -> you're close from no.")
                        print(" ")
                        print("##################################")

                    elif int(num)<=(guess+20) and int(num)>(guess+10) :
                        print("no. of guesses left"," ",noa)
                        print("                                ")
                        print("msg -> you're still far from no.")
                        print(" ")
                        print("##################################")

                    elif int(num)>(guess+20) :
                        print("no. of guesses left"," ",noa)
                        print("                                ")
                        print("msg -> you're too far from no.")
                        print(" ")
                        print("##################################")
                                            
                    elif int(num)>=(guess-5) and int(num)<(guess) :
                        print("no. of guesses left"," ",noa)
                        print("                                ")
                        print("msg -> close enough")
                        print(" ")
                        print("##################################")

                    elif int(num)>=(guess-10) and int(num)<(guess-5):
                        print("no. of guess left"," ",noa)
                        print("                                ")
                        print("msg -> you're close from no.")
                        print(" ")
                        print("##################################")

                    elif int(num)>=(guess-20) and int(num)<(guess-10):
                        print("no. of guesses left"," ",noa)
                        print("                                ")
                        print("msg -> you're still far from no.")
                        print(" ")
                        print("##################################")

                    elif int(num)<(guess-20) :
                        print("no. of guesses left"," ",noa)
                        print("                                ")
                        print("msg -> you're too far from no.")
                        print(" ")
                        print("##################################")
                        
                        
    if noa==0 :
        print(" GAME OVER ")

except ValueError :
    print("WARNING ---> ENTERED VALUE SHOULD BE AN INTEGER !!")       #prevent ValueError
except Exception :
    print("WARNING ---> SOMETHING IS WRONG FROM YOUR END")            #prevent other errors
    
        
