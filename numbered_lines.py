import random 

def main():   # DO NOT CHANGE BELOW
    with open("small.txt") as f:
        x = f.read().split("\n")
    cnt = 1
    f = open('new.txt', 'w')
    for item in x:
        f.write(str(cnt)+ " ")
        f.write(item+"\r\n")
        cnt += 1
        
if __name__ == '__main__':
    main()