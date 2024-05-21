from django.http import JsonResponse
from django.shortcuts import render
from .forms import MyForm

def my_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Form submitted successfully.'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = MyForm()
    return render(request, 'myapp/my_form.html', {'form': form})
