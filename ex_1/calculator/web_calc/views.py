from django.shortcuts import render
from decimal import Decimal


def calculator_view(request):
    context = dict()

    if request.method == 'GET':
        return render(request, 'calculator.html', context)

    elif request.method == 'POST':
        num_1 = request.POST.get('first_number')
        num_2 = request.POST.get('second_number')

        if 'e' in num_1 or 'e' in num_2:
            res_string = 'Введите пожалуйста 2 целых числа, или с плавающей точкой (запятой) !'
            context = {'answer': res_string}
            return render(request, 'calculator.html', context)

        num_1, num_2 = Decimal(num_1), Decimal(num_2)

        match request.POST.get('operation'):
            case 'add':
                result = num_1 + num_2
                act = '+'
            case 'subtract':
                result = num_1 - num_2
                act = '-'
            case 'multiply':
                result = num_1 * num_2
                act = '*'
            case 'divide':
                if num_2 == 0:
                    res_string = 'Деление на ноль невозможно, введите другие числа !'
                    context = {'answer': res_string}
                    return render(request, 'calculator.html', context)

                result = num_1 / num_2
                act = '/'

        res_string = f'Result: {num_1} {act} {num_2} = {result}'

        context = {'answer': res_string}

        return render(request, 'calculator.html', context)
