def check(password):
    if not(any(i.isdigit() for i in password)):
        return check(password + "1")
    elif not(any(i.islower() for i in password)):
        return check(password + "a")
    elif not(any(i.isupper() for i in password)):
        return check(password + "A")
    elif not(any(i in ['#', '@', '*', '&'] for i in password)):
        return check(password + "#")
    elif len(password) <= 6:
        return check(password + "1")
    else:
        return password

t = int(input())
for i in range(t):
    n = int(input())
    password = input()
    print("Case #{}: {}".format(i+1, check(password)))