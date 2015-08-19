import random 

def get_randomdigit_grover(length):
    magic_num = random.randint(000, 10**length-1)
    str_magic_num = str(magic_num)
    print str_magic_num
    if (len(str_magic_num)<length):
        y = str_magic_num.zfill(length)
        print y
    
   
def main():   # DO NOT CHANGE BELOW
	get_randomdigit_grover(3)
  


if __name__ == '__main__':
    main()
