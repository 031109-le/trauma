from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Professor, Aluno

# ---------- CURSOS ----------
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {'cursos': cursos})

def criar_curso(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        professor_id = request.POST['professor']
        professor = Professor.objects.get(id=professor_id)
        Curso.objects.create(nome=nome, descricao=descricao, professor=professor)
        return redirect('lista_cursos')
    professores = Professor.objects.all()
    return render(request, 'criar_curso.html', {'professores': professores})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.nome = request.POST['nome']
        curso.descricao = request.POST['descricao']
        curso.professor_id = request.POST['professor']
        curso.save()
        return redirect('lista_cursos')
    professores = Professor.objects.all()
    return render(request, 'editar_curso.html', {'curso': curso, 'professores': professores})

def deletar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('lista_cursos')

