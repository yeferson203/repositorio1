from typing import Any
from django import http
from django.http.response import JsonResponse
from django.views import View 
from .models import Usuario, Tarea, Proyecto
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
class UsuarioView(View): #esta es la clase solo para usuario, aplica lo mismo para Tarea y Proyecto
    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            usuarios=list(Usuario.objects.filter(id = id).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos = {'message': "Success", 'usuarios': usuarios }
            else:
                datos = {'message': "Usuario no encontrado ..." }
                #return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'messaje':'Success','usuarios':usuarios}
            else:
                datos = {'messaje': "Usuarios no encontrados..."}
        return JsonResponse(datos)
    def post(self,request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Usuario.objects.create(nombre=jd['nombre'] , correo_electronico = jd['correo_electronico'], contrasena =
        jd['contrasena'])
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id = id).values())
        if len(usuarios) > 0:
            usuario = Usuario.objects.get(id = id)
            usuario.nombre = jd['nombre']
            usuario.correo_electronico = jd['correo_electronico']
            usuario.contrasena = jd['contrasena']
            usuario.save()#para guardar los cambios
            datos = {'message': "Success"}
            return JsonResponse(datos)
        else:
            datos = {'message': "Usuarios no encontrado... "}
            return JsonResponse(datos)
    def delete(self,request, id):
        usuarios = list(Usuario.objects.filter(id = id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id = id).delete()
            datos = {'message': "Success"}
            return JsonResponse(datos)
        else:
            datos = {'message': "Usuario no encontrado ..."}
            return JsonResponse(datos)

class TareaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            tareas = list(Tarea.objects.filter(id=id).values())
            if len(tareas) > 0:
                tarea = tareas[0]
                datos = {'message': "Success", 'tareas': tareas}
            else:
                datos = {'message': "Tarea no encontrada ..."}
        else:
            tareas = list(Tarea.objects.values())
            if len(tareas) > 0:
                datos = {'message': 'Success', 'tareas': tareas}
            else:
                datos = {'message': "Tareas no encontradas..."}
        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Tarea.objects.create(
            nombre=jd['nombre'],
            descripcion=jd['descripcion'],
            fecha_vencimiento=jd['fecha_vencimiento'],
            estado=jd['estado'],
            idusuario_id=jd['idusuario_id'],
            idproyecto_id=jd['idproyecto_id']
        )
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        tareas = list(Tarea.objects.filter(id=id).values())
        if len(tareas) > 0:
            tarea = Tarea.objects.get(id=id)
            tarea.nombre = jd['nombre']
            tarea.descripcion = jd['descripcion']
            tarea.fecha_vencimiento = jd['fecha_vencimiento']
            tarea.estado = jd['estado']
            tarea.idusuario_id = jd['idusuario_id']
            tarea.idproyecto_id = jd['idproyecto_id']
            tarea.save()
            datos = {'message': "Success"}
            return JsonResponse(datos)
        else:
            datos = {'message': "Tarea no encontrada... "}
            return JsonResponse(datos)
        

    def delete(self, request, id):
        tareas = list(Tarea.objects.filter(id=id).values())
        if len(tareas) > 0:
            Tarea.objects.filter(id=id).delete()
            datos = {'message': "Success"}
            return JsonResponse(datos)
        else:
            datos = {'message': "Tarea no encontrada ..."}
            return JsonResponse(datos)

class ProyectoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            proyectos = list(Proyecto.objects.filter(id=id).values())
            if len(proyectos) > 0:
                proyecto = proyectos[0]
                datos = {'message': "Success", 'proyectos': proyectos}
            else:
                datos = {'message': "Proyecto no encontrado ..."}
        else:
            proyectos = list(Proyecto.objects.values())
            if len(proyectos) > 0:
                datos = {'message': 'Success', 'proyectos': proyectos}
            else:
                datos = {'message': "Proyectos no encontrados..."}
        return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Proyecto.objects.create(
            nombre=jd['nombre'],
            descripcion=jd['descripcion'],
            fecha_inicio=jd['fecha_inicio'],
            fecha_finalizacion=jd['fecha_finalizacion']
        )
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        proyectos = list(Proyecto.objects.filter(id=id).values())
        if len(proyectos) > 0:
            proyecto = Proyecto.objects.get(id=id)
            proyecto.nombre = jd['nombre']
            proyecto.descripcion = jd['descripcion']
            proyecto.fecha_inicio = jd['fecha_inicio']
            proyecto.fecha_finalizacion = jd['fecha_finalizacion']
            proyecto.save()
            datos = {'message': "Success"}
            return JsonResponse(datos)
        else:
            datos = {'message': "Proyecto no encontrado... "}
            return JsonResponse(datos)
        

    def delete(self, request, id):
        proyectos = list(Proyecto.objects.filter(id=id).values())
        if len(proyectos) > 0:
            Proyecto.objects.filter(id=id).delete()
            datos = {'message': "Success"}
            return JsonResponse(datos)
        else:
            datos = {'message': "Proyecto no encontrado ..."}
            return JsonResponse(datos)
