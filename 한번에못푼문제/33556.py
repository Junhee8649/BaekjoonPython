A = input()
B = input()
equal = "true"
Ignore = "true"

if A == "null":
    equal = "NullPointerException"
    Ignore = "NullPointerException"
elif A != B:
    equal = "false"
    if A.lower() == B.lower():
        Ignore = "true"
    else:
        Ignore = "false"
if B == "null" and A != "null":
    equal = "false"
    Ignore = "false"

print(equal)
print(Ignore)