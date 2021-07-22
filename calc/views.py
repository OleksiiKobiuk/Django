from django.shortcuts import render


err = False


def calculation(request, num1, sign, num2):
    a = None

    if sign == '+':
        a = num1 + num2
    elif sign == '-':
        a = num1 - num2
    elif sign == 'dev':
        try:
            a = num1 / num2
        except ZeroDivisionError:
            pass
        sign = ':'
    elif sign == '*':
        a = num1 * num2


    return render(request, 'index_calc.html', {'num1': num1,'sign': sign, 'num2': num2,'result': a})
        # return render(request, 'index_calc.html',{'result': a})
