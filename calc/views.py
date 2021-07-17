from django.shortcuts import render

# a = 'HI'
err = False


def calculation(request, num1, sign, num2):

        if sign == '+':
            a = num1 + num2
        elif sign == '-':
            a = num1 - num2
        elif sign == 'dev':
            a = num1 / num2
        elif sign == '*':
            a = num1 * num2


        # try:
        #     if sign == '+':
        #         a = num1 + num2
        #     elif sign == '-':
        #         a = num1 - num2
        #     elif sign == 'dev':
        #         a = num1 / num2
        #     elif sign == '*':
        #         a = num1 * num2
        # except:
        #     a = 'wrong'

        # return render(request, 'index_calc.html', {'num1': num1}, {'sign': sign}, {'num2': num2},
        #           {'result': a}, {'err': err})
        return render(request, 'index_calc.html',{'result': a})
