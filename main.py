from flask import Flask, render_template, request, redirect

app = Flask(__name__)
dataList = []

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', dataList=dataList)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        especie = request.form['especie']
        peso = request.form['peso']
        nometutor = request.form['nome-tutor']
        id = len(dataList)
        dataList.append([id, nomeanimal, especie, peso, nometutor])
        return redirect('/')
    else:
        return render_template('add-item.html')


@app.route('/edit_item/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        especie = request.form['especie']
        peso = request.form['peso']
        nometutor = request.form['nome-tutor']

        dataList[id] = [id, nomeanimal, especie, peso, nometutor]

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