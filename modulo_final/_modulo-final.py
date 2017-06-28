#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
import os.path
import io


classe = str(input('Digite o nome da classe: '))
classe_maiuscula = classe.title()
classe_minuscula = classe.lower()
print('\n' + '=========================')
print('\n')
html = str(input('Digite o nome arquivo da sua template base \n' 
    +'    ex:_base.html \n    '))
print('\n' + '=========================')
print('\n')

url = str(input('As URLs estão sendo extendidas de outro lugar? \n'
    '    -(ex: localhost:8000/post/cadastrar_exemplo está extendendo \n'
    '    -(ex: localhost:8000/cadastrar_exemplo não está extendendo \n'
    'Digite 0 se não estiver extendendo; ou o nome da extensão, começando SEM / e terminando COM / \n'
    '    -ex: 0 \n'\
    '    -ex: algoritmo/smartconnexion/ \n'
    'R: '))
url = url.lower()
print('\n' + '=========================')
print('\n')

print('Done!')

if url == "0":
    url = ""

# ============================================================== #
# Adicionando textos no arquivo Models
# ============================================================== #
with open(os.path.join(os.pardir, "models.py"), "a+", encoding="utf-8") as models:
    models.writelines(
        "# ================ COMEÇO do MÓDULO FINAL ================ #" + '\n' + '\n'
        "from django.db import models" + '\n' + '\n'
        "class " + classe_maiuscula + "(models.Model):" + '\n'
        "    nome = models.CharField('Nome', max_length=64)" + '\n'
        "    atributo2 = models.IntegerField('Atributo2')" + '\n'
        "    atributo3 = models.BooleanField('Atributo3')" + '\n' 
    )




# ============================================================== #
# Adicionando textos no arquivo Forms
# ============================================================== #
with open(os.path.join(os.pardir, "forms.py"), "a+", encoding="utf-8") as forms:
    forms.writelines(
        "# ================ COMEÇO do MÓDULO FINAL ================ #" + '\n' + '\n'
        "from django.forms import ModelForm, fields" + '\n' + '\n'
        "from .models import *" + '\n' + '\n'
        "class " + classe_maiuscula + "Form(ModelForm):" + '\n'
        "    def __init__(self, *args, **kwargs):" + '\n'
        "        super(ModelForm, self).__init__(*args, **kwargs)" + '\n'
        "        for field_name, field in self.fields.items():" + '\n'
        "           field.widget.attrs['class'] = 'form-control'" + '\n'
        "    class Meta:" + '\n'
        "        model = " + classe_maiuscula + '\n'
        "        fields = [" + '\n'
        "            'nome'," + '\n'
        "            'atributo2'," + '\n'
        "            'atributo3'," + '\n'
        "        ]"
    )





# ============================================================== #
# Adicionando textos no arquivo urls
# ============================================================== #
with open(os.path.join(os.pardir, "urls.py"), "a+", encoding="utf-8") as forms:
    forms.writelines(
        "# ================ COMEÇO do MÓDULO FINAL ================ #" + '\n' + '\n'
        "# Django imports" + '\n'
        "from __future__ import unicode_literals" + '\n'
        "from django.conf.urls import url" + '\n' + '\n'
        "# App imports" + '\n'
        "from .views import *"  + '\n' + '\n'
        "urlpatterns = [" + '\n'

        #URL CADASTRAR
        "    url(r'^cadastrar_" + classe_minuscula + "/', Cadastrar" + classe_maiuscula + ".as_view(), name=" +
        "'cadastrar " + classe_minuscula + "')," + '\n'

        #URL LISTAR
        "    url(r'^listar_" + classe_minuscula + "/$', Listar" + classe_maiuscula +
        ".as_view(), name='listar " + classe_minuscula + "')," + '\n'

        #URL DETALHAR
        "    url(r'^detalhar_" + classe_minuscula + "/(?P<pk>\d+)/$', Detalhar" + classe_maiuscula +
        ".as_view(), name='detalhar " + classe_minuscula + "')," + '\n'

        #URL EDITAR
        "    url(r'^editar_" + classe_minuscula + "/(?P<pk>\d+)/$', Editar" + classe_maiuscula + 
        ".as_view(), name='editar " + classe_minuscula + "')," + '\n'

        #URL DELETAR
        "    url(r'^deletar_" + classe_minuscula + "/(?P<pk>\d+)/$', Deletar" + classe_maiuscula +
        ".as_view(), name='deletar " + classe_minuscula + "')," + '\n'
        "]"
    )



# ============================================================== #
# Adicionando textos no arquivo views
# ============================================================== #
with open(os.path.join(os.pardir, "views.py"), "a+", encoding="utf-8") as models:
    models.writelines(
        "# ================ COMEÇO do MÓDULO FINAL ================ #" + '\n' + '\n'
        "# Django imports" + '\n'
        "from vanilla import CreateView, UpdateView, DeleteView, ListView, DetailView" + '\n' + '\n'

        "# App imports" + '\n'
        "from .models import *" + '\n'
        "from .forms import *" + '\n' + '\n'





        # CADASTRAR
        "class Cadastrar" + classe_maiuscula + "(CreateView):" + '\n'
        "    model = " + classe_maiuscula + '\n'
        "    form_class = " + classe_maiuscula + "Form" + '\n'
        "    template_name = 'cadastrar_" + classe_minuscula + ".html'" + '\n'
        "    success_url = '/" + url + "listar_" + classe_minuscula + "'" + '\n' + '\n'

        # LISTAR
        "class Listar" + classe_maiuscula + "(ListView):" + '\n'
        "    model = " + classe_maiuscula + '\n'
        "    template_name = 'listar_" + classe_minuscula + ".html'" + '\n' + '\n'



        # DETALHAR
        "class Detalhar" + classe_maiuscula + "(DetailView):" + '\n'
        "    model = " + classe_maiuscula + '\n'
        "    template_name = 'detalhar_" + classe_minuscula + ".html'" + '\n' + '\n'




        # EDITAR
        "class Editar" + classe_maiuscula + "(UpdateView):" + '\n'
        "    model = " + classe_maiuscula + '\n'
        "    form_class = " + classe_maiuscula + "Form" + '\n'
        "    template_name = 'editar_" + classe_minuscula + ".html'" + '\n'
        "    success_url = '/" + url + "listar_" + classe_minuscula + "'" + '\n' + '\n'




        # DELETAR
        "class Deletar" + classe_maiuscula + "(DeleteView):" + '\n'
        "    model = " + classe_maiuscula + '\n'
        "    template_name = 'deletar_" + classe_minuscula + ".html'" + '\n'
        "    success_url = '/" + url + "listar_" + classe_minuscula + "'" + '\n' + '\n'

    )
















# ============================================================== #
# Templates - Cadastrar
# ============================================================== #
directory = os.path.join(os.pardir, "templates")
if not os.path.exists(directory):
    os.makedirs(directory)
open(os.path.join(os.pardir, "templates/cadastrar_" + classe + ".html"), "w", encoding="utf-8").write(
    "{% extends '" + html + " '%}" + '\n\n'
    "{% block title %}Cadastrar " + classe + "{% endblock title %}" + '\n\n'
    "{% block content %}" + '\n'
    "<form role='form' method='post' enctype='multipart/form-data'>{%csrf_token%}" + '\n'
    "    {% for campo in form %}" + '\n'
    "        <div class='form-group'>" + '\n'
    "            <label class='form-label'>{{campo.label}}</label>" + '\n'
    "            <span class='help'>{{campo.help_text}}</span>" + '\n'
    "            <div class='controls'>" + '\n'
    "                {{campo}}" + '\n'
    "            </div>" + '\n'
    "        </div>" + '\n'
    "    {% endfor %}" + '\n'
    "    <button class='btn btn-primary' method = 'post' type ='submit' style='background-color:#339933'>Cadastrar</button>" + '\n'
    "    <a aria-expanded='false' class='btn btn-primary btn-demo-space' href='/" +
    url + "listar_" + classe_minuscula + "'style='background-color: #339933'>\n"
    "        Listar " + classe_maiuscula + '\n' +
    "    </a>" + '\n'
    "</form>" + '\n'
    "{% endblock content %}"
)


# ============================================================== #
# Templates - Listar
# ============================================================== #
open(os.path.join(os.pardir, "templates/listar_" + classe + ".html"), "w", encoding="utf-8").write(
    "{% extends '" + html + " '%}" + '\n\n'
    "{% block title %}Listar " + classe + "{% endblock title %}" + '\n\n'
    "{% block content %}" + '\n'
    '<div class="row-fluid">' + '\n'
    '    <div class="span12">' + '\n'
    '        <div class="grid simple ">' + '\n'
    '            <div class="grid-title">' + '\n'
    '                <h3>Lista de '+ classe_maiuscula + 's</h3>' + '\n'
    '            </div>' + '\n'
    '            <div class="grid-body ">' + '\n'
    '                <table class="table">' + '\n'
    '                    <a aria-expanded="false" class="btn btn-primary btn-demo-space" href="/' +
                         url + 'cadastrar_' + classe_minuscula + '" style="background-color: #339933">Cadastrar ' +
                         classe_maiuscula + '</a>' + '\n'
    '                    <br><br>' + '\n'
    '                    <thead>' + '\n'
    '                        <tr>' + '\n'
    '                            <th>Nome</th>' + '\n'
    '                            <th>Atributo2</th>' + '\n'
    '                            <th>Atributo3</th>' + '\n'
    '                            <th>Deletar</th>' + '\n'
    '                    </thead>' + '\n'
    '                    <tbody>' + '\n'
    '                        {% for objeto in ' + classe_minuscula + '_list %}' + '\n'
    '                            <tr>' + '\n'
    '                                <td>' +
                                     '<a href="/' + url + 'detalhar_' + classe_minuscula + '/{{objeto.pk}}">' +
                                        '{{ objeto.nome }}</a></td>' + '\n'
    '                                <td>{{ objeto.atributo2 }}</td>' + '\n'
    '                                <td>{{ objeto.atributo3 }}</td>' + '\n'
    '                                <td>' + '\n'
    '                                    <a href="/' + url + 'deletar_' + classe_minuscula + '/{{objeto.pk}}"' +
                                             ' class="btn btn-primary btn-xs btn-mini" style = "background-color: #FF0707">' + '\n'
    '                                    DELETAR' + '\n'
    '                                    </a>' + '\n'
    '                                </td>' + '\n'
    '                            </tr>' + '\n'
    '                        {% endfor %}' + '\n'
    '                    </tbody>' + '\n'
    '                </table>' + '\n'
    '            </div>' + '\n'
    '        </div>' + '\n'
    '    </div>' + '\n'
    '</div>' + '\n'
    "{% endblock content %}"
)

# ============================================================== #
# Templates - Detalhar
# ============================================================== #
open(os.path.join(os.pardir, "templates/detalhar_" + classe + ".html"), "w", encoding="utf-8").write(
    "{% extends '" + html + " '%}" + '\n\n'
    "{% block title %}Detalhar " + classe + "{% endblock title %}" + '\n\n'
    "{% block content %}" + '\n'

    '<div class="row">' + '\n'
    '    <div class="col-md-12">' + '\n'
    '        <div class="grid simple">' + '\n'
    '            <div class="grid-body no-border invoice-body">' + '\n'
    '                <h3><span class="semi-bold">Perfil </span>do  {{object.nome}}</h3>' + '\n'
    '                <div class="col-md-2 col-sm-2">' + '\n'
    '                    <br>' + '\n'
    '                    <div style="background-color:purple; height:150px; width:150px; border-radius:50%">&nbsp;</div>' + '\n'
    '                </div>' + '\n'
    '                <div class="col-md-9 user-description-box col-sm-9" style="padding-left:20px">' + '\n'
    '                    <h4 class="semi-bold no-margin">{{object.nome}}</h4>' + '\n'
    '                    <h4 class="semi-bold no-margin">{{object.atributo2}}</h4>' + '\n'
    '                    <h4 class="semi-bold no-margin">{{object.atributo3}}</h4>' + '\n'
    '                </div>' + '\n'
    '                <br><br><br><br><br><br>' + '\n'
    '                <a aria-expanded="false" class="btn btn-primary btn-demo-space" href="/' + url + 'listar_' + 
                     classe_minuscula + '" style="background-color: #339933; margin-left:50px">Listar ' + classe_maiuscula + "</a>" + '\n'
    '                <a aria-expanded="false" class="btn btn-primary btn-demo-space" href="/' + url + 'editar_' + 
                     classe_minuscula + '/{{object.pk}}" style="background-color: #339933;">Editar Usuário</a>' + '\n'
    '            </div>' + '\n'
    '        </div>' + '\n'
    '    </div>' + '\n'
    '</div>' + '\n'
    '{%endblock content%}'

)




# ============================================================== #
# Templates - Editar
# ============================================================== #
open(os.path.join(os.pardir, "templates/editar_" + classe + ".html"), "w", encoding="utf-8").write(
    "{% extends '" + html + " '%}" + '\n\n'
    "{% block title %}Editar " + classe + "{% endblock title %}" + '\n\n'
    "{% block content %}" + '\n'
    "<form role='form' method='post' enctype='multipart/form-data'>{%csrf_token%}" + '\n'
    "    {% for campo in form %}" + '\n'
    "        <div class='form-group'>" + '\n'
    "            <label class='form-label'>{{campo.label}}</label>" + '\n'
    "            <span class='help'>{{campo.help_text}}</span>" + '\n'
    "            <div class='controls'>" + '\n'
    "                {{campo}}" + '\n'
    "            </div>" + '\n'
    "        </div>" + '\n'
    "    {% endfor %}" + '\n'
    "    <button class='btn btn-primary' method = 'post' type ='submit' style='background-color:#339933'>Update Values</button>" + '\n'
    "    <a aria-expanded='false' class='btn btn-primary btn-demo-space' href='/" +
    url + "listar_" + classe_minuscula + "'style='background-color: #339933'>\n"
    "        Listar " + classe_maiuscula + '\n' +
    "    </a>" + '\n'
    "</form>" + '\n'
    "{% endblock content %}"
)



# ============================================================== #
# Templates - Deletar
# ============================================================== #
open(os.path.join(os.pardir, "templates/deletar_" + classe + ".html"), "w", encoding="utf-8").write(
    "{% extends '" + html + " '%}" + '\n\n'
    "{% block title %}Editar " + classe + "{% endblock title %}" + '\n\n'
    "{% block content %}" + '\n'
    '<form action="" method="post">{% csrf_token %}'  + '\n'
    '    <p>O Objeto: "{{ object.nome }}" estará sendo deletado. Aperte confirmar para prosseguir.</p>'  + '\n'
    '    <input type="submit" value="Confirm"/>'  + '\n'
    '</form>'  + '\n'
    "{% endblock content %}"
)












