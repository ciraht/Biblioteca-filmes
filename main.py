from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
dataList = []

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', dataList=dataList)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        nome = request.form['nome']
        especie = request.form['especie']
        peso = request.form['peso']
        nometutor = request.form['nome-tutor']

        for paciente in dataList:
            if paciente[1] == nome:
                flash("Erro: filme já cadastrado.", "error")
                return redirect('add_item')

        id = len(dataList)
        dataList.append([id, nome, especie, peso, nometutor])
        return redirect('/')
    else:
        return render_template('add-item.html')


@app.route('/edit_item/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    if request.method == 'POST':
        nome = request.form['nome']
        especie = request.form['especie']
        peso = request.form['peso']
        nometutor = request.form['nome-tutor']

        dataList[id] = [id, nome, especie, peso, nometutor]

        return redirect('/')
    else:
        paciente = dataList[id]
        return render_template('edit-item.html', paciente=paciente)

@app.route('/del/<int:id>')
def cancelar_paciente(id):
    del dataList[id]
    return redirect('/')






if __name__ == '__main__':
    app.run(debug=True)