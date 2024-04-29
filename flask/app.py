from flask import Flask, render_template, redirect, url_for, request
from bson import ObjectId 
from db import db
from models.models import Pacientes 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def alpha():
    return render_template('cadastrar.html')

@app.route('/bemvindo')
def bemvindo():
    return render_template('bemvindo.html')
    


@app.route('/create', methods=['POST'])
def create():
    data = request.form.to_dict()
    
    paciente = Pacientes(nome=data['nome'], email=data['email'], senha=data['senha'])
    db.session.add(paciente)
    db.session.commit()
    return redirect(url_for('bemvindo   '))
     
@app.route('/lista', methods=['GET'])
def listar():
    pacientes = Pacientes.query.all()
    return render_template('lista.html', pacientes = pacientes)
    
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    paciente = Pacientes.query.get(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect(url_for('listar'))
     
     
#     if mongo.db is None:
#         return "Não foi possível conectar ao banco de dados", 500

#     mongo.db.usuarios.insert_one(user)
#     return redirect(url_for('alpha'))

# @app.route('/update', methods = ['POST'])
# def update():
#     user_id = request.form['id']
#     update = {}
#     if 'nome' in request.form and request.form['nome']:
#         update['nome'] = request.form['nome']
        
#     if 'senha' in request.form and request.form['senha']:
#         update['senha'] = request.form['senha']
    
#     if 'email' in request.form and request.form['email']:
#         update['email'] = request.form['email']   
    
#     if update:
#         mongo.db.usuarios.update_one(
#             {'_id':ObjectId(user_id)},
#             {'$set': update}
#             )
#         return redirect(url_for('alpha'))
        
     
# @app.route('/delete', methods = ['POST'])
# def delete():
#     del_id = request.form['delId']
#     if del_id:
#         mongo.db.usuarios.delete_one({'_id': ObjectId(del_id)})
#     return redirect(url_for('alpha'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')