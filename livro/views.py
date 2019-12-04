from django.shortcuts import render, redirect
from livro.models import Livro
from livro.forms import LivroCreate
from django.http import HttpResponse

# Create your views here.
def index(request):
    shelf = Livro.objects.all()
    return render(request, 'livro/biblioteca.html', {'shelf': shelf})

def upload(request):
    upload = LivroCreate()
    if request.method == 'POST':
        upload = LivroCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'livro/upload_form.html', {'upload_form':upload})
def update_livro(request, livro_id):
    livro_id = int(livro_id)
    try:
        livro_sel = Livro.objects.get(id = livro_id)
    except Livro.DoesNotExist:
        return redirect('index')
    livro_form = LivroCreate(request.POST or None, instance = livro_sel)
    if livro_form.is_valid():
       livro_form.save()
       return redirect('index')
    return render(request, 'livro/upload_form.html', {'upload_form':livro_form})

def delete_livro(request, livro_id):
    livro_id = int(livro_id)
    try:
        livro_sel = Livro.objects.get(id = livro_id)
    except Livro.DoesNotExist:
        return redirect('index')
    livro_sel.delete()
    return redirect('index')
