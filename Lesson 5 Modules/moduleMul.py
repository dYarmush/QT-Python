from  ModuleAdd import add

def mul(num1, num2):
    prod = num1
    for i in range(num2-1):
        prod = add(prod,num1)
    return prod
 
if __name__ =="__main__":
    num1 = int(input("input num1: "))
    num2 = int(input("input num2: "))
    mul(num1, num2)
