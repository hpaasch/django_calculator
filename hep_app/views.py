from django.shortcuts import render

from hep_app.forms import Calculation


def calculate_view(request):
    print(request.POST)
    if request.method == 'POST':
        form = Calculation(request.POST)
        if form.is_valid():
            entry_one = form.cleaned_data['entry_one']
            entry_two = form.cleaned_data['entry_two']
            do_math = form.cleaned_data['do_math']
            print(entry_one)
            print(entry_two)
            print(do_math)
            if do_math == "Multiply":
                result = entry_one * entry_two
            elif do_math == "Add":
                result = entry_one + entry_two
            elif do_math == "Subtract":
                result = entry_one - entry_two
            elif do_math == "Divide":
                result = entry_one / entry_two
            print(result)

    else:
        form = Calculation()
    return render(request, 'calculator.html', {'form': Calculation})

