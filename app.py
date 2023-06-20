from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pets = []


@app.route('/')
def lista_pet():
    return render_template('lista_pet.html', pets=pets)

@app.route('/cadastrar_pet', methods=['GET', 'POST'])
def cadastrar_pet():
    if request.method == 'POST':
        
        pet= {
            'id': len(pets)+1,
            'nome': request.form['nome'],
            'raça': (request.form['raça']),
        }
        pets.append(pet)
        

        return redirect('/')
    return render_template('cadastrar_pet.html', pets=pets)

@app.route('/editar-pet/<int:id>', methods=['GET', 'POST'])
def editar_pet(id):
    for pet in pets:
        if pet['id'] == id:
            if request.method == 'POST':
                pet['nome'] = request.form['nome']
                pet['raça'] = (request.form['raça'])
        
                return redirect('/')
            return render_template('editar_pet.html', pet=pet)
    return redirect('/')

@app.route('/excluir-pet/<int:id>')
def excluir_pet(id):
    for pet in pets:
        if pet['id'] == id:
            pets.remove(pets)
            break
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
