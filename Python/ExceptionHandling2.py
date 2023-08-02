def divide(a,b):
    if b==0:
        raise ValueError("Error occurred:Division by Zero")
    try:
        result=a/b
        return result
    except Exception as e:
        print("An error has occurred"+str(e))
        return None

firstnum=5
secondnum=0

try:
    result=divide(firstnum,secondnum)
    print("result is "+str(result))
except ValueError as v:
    print(v)
