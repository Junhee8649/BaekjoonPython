def allPrint(N):
    for i in range(N):
        print("@@@@@"*N)

def somePrint(N):
    for i in range(3 * N):
        print("@"*N, end="")
        print("   "*N, end="")
        print("@"*N)

N = int(input())

allPrint(N)
somePrint(N)
allPrint(N)