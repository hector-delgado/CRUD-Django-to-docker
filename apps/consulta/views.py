# from django.shortcuts import render,redirect
from django.http import HttpResponse
# from apps.registro.forms import UsuarioForm
# from apps.registro.models import Usuario


# # Create your views here.

def consulta_view(request):
    return HttpResponse('Hola')
#     mascota = Usuario.objects.all().order_by('id')
#     contexto = {'mascotas':mascota}
#     return render(request, 'consulta/consulta_list.html',contexto)


# def usuario_edit(request, id_usuario):
# 	usr = Usuario.objects.get(id=id_usuario)
# 	if request.method == 'GET':
# 		form = UsuarioForm(instance=usr)
# 	else:
# 		form = UsuarioForm(request.POST, instance=usr)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('/consulta/')
# 	return render(request, '/registro/registro_form.html', {'form':form})

# def usuario_delete(request, id_usuario):
#     usr = Usuario.objects.get(id=id_usuario)
#     if request.method == 'POST':
#         usr.delete()
#         return redirect('/consulta/')
#     return render(request, '/registro/registro_delete.html',{'usr':mascota})             