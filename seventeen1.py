def correct_input(input):
    correct_input = [1,2,3]
    if input in correct_input:
        return 1
    else:
        return -1
        
def check_for_num(number):
	""" This function checks if the value entered by the user is numeric"""
	try:
		int_num = int(number)
	except:
		return -1
	else:
		return int_num        

def computers_turn(remaining,user_input):
    if remaining >user_input:
        still_remaining = remaining - user_input
        print "Computer removed",user_input,"marbles."
    elif remaining == user_input:
        still_remaining = remaining - user_input
        print "Computer removed",user_input,"marbles."
    else:
        print "Computer removed",1,"marble."
        still_remaining = remaining - 1
    return still_remaining
    
 
def humans_turn(remaining_marbels):
    while True:
        raw_user_input = raw_input("Your turn: How many marbles will you remove (1-3)?")
        
        user_input = check_for_num(raw_user_input)
        if (user_input == -1 or correct_input(user_input) == -1):
            print "Sorry, that is not a valid option. Try again!."
            continue
        elif user_input > remaining_marbels:
            print "Sorry, that is not a valid option. Try again!."
            continue
        else:
                remaining_marbels_ret = remaining_marbels - user_input
                print "You removed",user_input,"marbles."
                return user_input, remaining_marbels_ret
 

def main(): 
    print "\nLet's play the game of Seventeen!"

    num_of_marbels = 17
    print "Number of marbles left in jar:",num_of_marbels,"\n"

    while(num_of_marbels>0):
    
        user_input, remaining_after_human = humans_turn(num_of_marbels)
        print "Number of marbles left in jar:",remaining_after_human
        
        if remaining_after_human  == 0 :
            print "There are no marbles left. Computer wins!"
            exit(0)
        else:
            print "\nComputer's turn..."
            remaining_after_comp = computers_turn(remaining_after_human,user_input)
          
        num_of_marbels = remaining_after_comp
        print "Number of marbels left in jar",num_of_marbels  
    
    print "You won" 
        
         
if __name__ == '__main__':
    main()