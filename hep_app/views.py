from django.shortcuts import render

from hep_app.forms import Calculation


def calculate_view(request):
    result = 'C'
    entry_one = 'One number'
    entry_two = 'another number'
    math = '(add/subtract/multiple/divide)'
    print(request.POST)
    if request.method == 'POST':
        form = Calculation(request.POST)
        if form.is_valid():
            entry_one = form.cleaned_data['entry_one']
            entry_two = form.cleaned_data['entry_two']
            do_math = form.cleaned_data['do_math']
            if do_math == "Multiply":
                math = "x"
                result = entry_one * entry_two
            elif do_math == "Add":
                math = "+"
                result = entry_one + entry_two
            elif do_math == "Subtract":
                math = "-"
                result = entry_one - entry_two
            elif do_math == "Divide":
                math = "/"
                result = entry_one / entry_two

    return render(request, 'calculator.html', {'form': Calculation, 'result': result,
                                               'one': entry_one, 'two': entry_two,
                                               'math': math})

