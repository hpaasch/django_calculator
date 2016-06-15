from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from hep_app.forms import Calculation
from hep_app.models import SavedCalculation


def create_user_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login_view"))
        else:
            return render(request, "create_user_view.html", {'form': form})
    form = UserCreationForm
    return render(request, "create_user_view.html", {'form': form})


@login_required
def old_math_view(request):
    old_math = SavedCalculation.objects.filter(math_user__username=request.user)
    return render(request, "old_math_view.html", {'old_math': old_math})


def saved_calculate_view(request):
    return render(request, "saved_calculate_view.html")


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
            if request.user.is_authenticated():
                SavedCalculation.objects.create(entry_one=entry_one, entry_two=entry_two,
                                                math=math, result=result, math_user=request.user)

    form_new = Calculation(initial={'entry_one': result})
    return render(request, 'calculator.html', {'form': Calculation, 'result': result,
                                               'one': entry_one, 'two': entry_two,
                                               'math': math, 'form_new': form_new})

