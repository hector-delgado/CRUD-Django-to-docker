from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.registro.forms import UsuarioForm
from apps.registro.models import Usuario

# Create your views here.


def registro_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/registro/consu/')
    else:
        form = UsuarioForm()
    
    return render(request, 'registro/registro_form.html', {'form':form})


def consulta_view(request):
    mascota = Usuario.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request, 'registro/consulta_list.html',contexto)


def usuario_edit(request, id_usuario):
	usr = Usuario.objects.get(id=id_usuario)
	if request.method == 'GET':
		form = UsuarioForm(instance=usr)
	else:
		form = UsuarioForm(request.POST, instance=usr)
		if form.is_valid():
			form.save()
		return redirect('/registro/consu/')
	return render(request, 'registro/registro_form.html', {'form':form})

def usuario_delete(request, id_usuario):
    usr = Usuario.objects.get(id=id_usuario)
    if request.method == 'POST':
        usr.delete()
        return redirect('/registro/consu/')
    return render(request, 'registro/registro_delete.html',{'mascota':usr})  





# def mascota_delete(request, id_mascota):
# 	mascota = Mascota.objects.get(id=id_mascota)
# 	if request.method == 'POST':
# 		mascota.delete()
# 		return redirect('mascota:mascota_listar')
# 	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})