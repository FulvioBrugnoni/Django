from django.shortcuts import render
from django.http import HttpResponse
from .forms import Inserimento

def vquest(request):
        return HttpResponse('vquest')


def creazione_inserimento(request):

        form = Inserimento(request.POST or None)
        if form.is_valid():
            form.save()
            form = Inserimento()

        contestx = {'form': form}
        return render(request,'questionario/tquest.html', contestx)
