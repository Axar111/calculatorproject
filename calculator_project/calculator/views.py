# calculator/views.py
from django.shortcuts import render
from .forms import CalculatorForm

def calculator(request):
    result = None

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operation = form.cleaned_data['operation']

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Division by zero is not allowed."

    else:
        form = CalculatorForm()

    return render(request, 'calculator.html', {'form': form, 'result': result})

# calculator/views.py
from django.shortcuts import render

def get_calculator(request):
    result = None

    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operation = request.GET.get('operation')

    if num1 and num2 and operation:
        num1 = float(num1)
        num2 = float(num2)

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Division by zero is not allowed."

    return render(request, 'get_calculator.html', {'result': result})
