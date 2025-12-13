
def sum(number, method):
    sum = 0
    if method == 1:
        while number > 0:
            sum += number % 10
            number //= 10
        return sum
    elif method == 2:
        number = str(number)
        for i in number:
            sum += int(i)
        return sum

def listify(number):
    res = []
    res.extend(str(number))
    return res