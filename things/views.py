from django.shortcuts import render
from things.forms import ThingForm

def home(request):
    form = ThingForm()
    return render(request, 'hmoe.html', {'form': form})
