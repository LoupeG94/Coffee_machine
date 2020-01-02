n = int(input())
if 1900 <= n <= 3000:
    print("Leap" if (n % 4 ==0 and n % 100 == 1) or n % 400 == 0 else "Ordinary")






# put your python code here