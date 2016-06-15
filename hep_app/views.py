from django.shortcuts import render

from hep_app.forms import Calculation


def create_user_view(request):
    return render(request, "create_user_view.html")


def login_view(request):
    return render(request, "login_view.html")



def calculate_view(request):
    result = 0
    entry_one = 'X'
    entry_two = 'Y'
    math = '+'
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
    form_new = Calculation(initial={'entry_one': result})
    return render(request, 'calculator.html', {'form': Calculation, 'result': result,
                                               'one': entry_one, 'two': entry_two,
                                               'math': math, 'form_new': form_new})

