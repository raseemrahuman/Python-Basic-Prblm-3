def userinput(times):
    if times>= 1 and times<= 25:
        return True
    return False 
while True:
    try:
        times = int(input("how many rows? "))
    except ValueError:
        continue

    if userinput(times):  
        break
    print('Out of Range must be between 1 and 25')
    
def printing():
    for k in range(times):
        #(9 ,0 ,-1) Here 9=>Start of Range,0=>End of Range,-1=>decrement.

          for i in range(9 ,0 ,-1):
                for j in range(i):
                    print(i,end='')  
          print()             
def main():
    userinput(times)
    printing()

if __name__ == "__main__":
    main() 