def cast(number):
    try:
        number = int(number)
        return number
    except ValueError:
        print ("NUMBER IS NOT VALID. Try again!")
        return False
        

a = ""
print(cast(a))