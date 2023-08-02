## Try block opens the run
def divide(a,b):
    try:
        result=a/b
        return result
## except dictates what errors are being looked for
    except ZeroDivisionError:
        print("Error: Division by Zero is not allowed")
    except TypeError:
        print("Error: One of the values has a wrong type")
        return None
    except  Exception as e:
        print("An unexpected error occured with details "+str(e))
        return None
## Else is if an error hasn't occured
##  else:
        print("No errors are raised")
## Finally block closes the run
## Finally runs regardless of an error occuring or not
    finally:
        print("finally block run")

firstnum=5
secondnum=2.5

result=divide(firstnum,secondnum)
print("result is "+str(result))

print('')
print('')



