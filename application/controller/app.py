from flask import Flask, render_template, request, url_for, redirect
from application import app
from application.model.dao import formulario_dao

from application.model.dao.formulario_dao import Cad_DAO
from application.model.entity.form import Cad

app = Flask(__name__)

Cad_DAO = ()
cad_list = formulario_dao.listar_cad()



@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")


@app.route("/list", methods=['GET'])
def listacad():
    return render_template("form.html", cad_list=cad_list)


@app.route("/inserir", methods=['POST'])
def inserir():
    
    id = len(cad_list) + 1
    titulo = request.form.get("form_titulo", None)
    descricao = request.form.get("form_descricao", None)
    link = request.form.get("form_link", None)
    tags = request.form.get("form_tags", None).split(" ")
    cad = Cad(id, titulo, descricao, link, tags)
    cad_list.append(cad)
    return render_template("form.html", cad_list=cad_list)


@app.route("/excluir/<int:id>", methods=['DELETE'])
def excluir(id: int):
    for cad in cad_list:
        if cad.id == id:
            cad_list.remove(cad)
            return render_template("form.html", cad_list=cad_list)
    return render_template("form.html", cad_list=cad_list), 404


@app.route("/busca")
def busca():
    cad_list_filtrado = []
    palavra_chave = request.args.get('palavra_chave')
    for cad in cad_list:
        if palavra_chave in cad.titulo or palavra_chave in cad.descricao:
            cad_list_filtrado.append(cad)
    return render_template("form.html", cad_list=cad_list_filtrado)


@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id: int):
    if request.method == 'GET':
        for cad in cad_list:
            if cad.id == id:
                return render_template("home.html", cad_list= cad_list, cad_atualizar=cad)
        return render_template("home.html", cad_list= cad_list), 404
    else:
        titulo = request.form.get('titulo', None)
        descricao = request.form.get('descricao', None)
        link = request.form.get('link', None)
        tag = request.form.get('tag', None)
        for cad in cad_list:
            if cad.id == id:
                cad.titulo = titulo
                cad.descricao = descricao
                cad.link = link
                cad.tag = tag
        return render_template("home.html", cad_list= cad_list)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)