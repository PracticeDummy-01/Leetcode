#Integer to Roman Numerals
def intToRoman(num: int) -> str:
    symList = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        
    res = ""
    for sym,val in reversed(symList):
        if num//val:
            count = num // val
            res += (sym*count)
            num = num % val
    return res
    


#Roman Numeral to Integer

def romanToInt(s: str) -> int:
    #largest to Smallest : add them up
    #smaller before larger: subtract smaller

    roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    
    res = 0

    for i in range(len(s)):
        if i+1< len(s) and roman[s[i]]<roman[s[i+1]]:
            res-=roman[s[i]]
        else:
            res+=roman[s[i]]
    return res


#Main Code

while True:
    print("""
Menu :- 
      1) Integer to Roman
      2) Roman to Integer
      3) Exit""")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        num = int(input("Enter a number :- "))
        re = intToRoman(num)
        print(re)
    elif ch == 2:
        romn = str(input("Enter a Roman number :- "))
        re = romanToInt(romn)
        print(re)
    elif ch == 3:
        exit()
    else:
        print("Invalid Input")
