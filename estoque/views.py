from django.shortcuts import render
from . models import Categoria, Produto, Imagem
from django.http import HttpResponse
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def add_produto(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        return render(request, 'add_produto.html', {'categoria': categoria})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        preco_compra = request.POST.get('preco_compra')
        preco_venda = request.POST.get('preco_venda')


        produto = Produto(nome=nome, 
                          categoria_id=categoria,   
                          quantidade=quantidade, 
                          preco_compra=preco_compra, 
                          preco_venda=preco_venda)
        produto.save()

        for f in request.FILES.getlist('imagens'):
            name = f'{date.today()}-{produto.id}.jpg'
            img = Image.open(f)
            img = img.convert('RGB')
            img = img.resize((300, 300))
            draw = ImageDraw.Draw(img)
            draw.text((20, 280), f'CONSTRUCT {date.today()}', (255, 255, 255))
            output = BytesIO()
            img.save(output, format='JPEG', quality=100)
            output.seek(0)
            img_final = InMemoryUploadedFile(output, 'ImageField', name, 'image/jpeg', sys.getsizeof(output), None)


            img_dj = Imagem(imagem = img_final, produto = produto)
            img_dj.save()

        return HttpResponse('foi')