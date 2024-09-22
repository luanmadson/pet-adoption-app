from flask import Flask  # Importa o framework Flask
from helper import pets  # Importa o dicionário 'pets' do arquivo helper.py

app = Flask(__name__)  # Cria uma instância do Flask, que será usada para configurar as rotas

# Definindo a rota para a página inicial
@app.route('/')
def index():
    # Retorna um HTML simples com links para as categorias de animais
    return '''<h1>Adopt a Pet</h1>
              <p>Browse through the links below to find your new furry friend:</p>
              <ul>
                <li><a href='/animals/dogs'>Dogs</a></li>
                <li><a href='/animals/cats'>Cats</a></li>
                <li><a href='/animals/rabbits'>Rabbits</a></li>
              </ul>
           '''

# Definindo a rota para exibir a lista de animais por tipo (ex: dogs, cats, rabbits)
@app.route('/animals/<pet_type>')  # 'pet_type' será uma variável dinâmica na URL
def animals(pet_type):
    # Gera um HTML que lista todos os animais de um tipo específico
    html = f'<h1>List of {pet_type}</h1>'  # Título com o tipo de animal
    html += "<ul>"  # Abre uma lista não ordenada
    # Itera sobre cada pet na lista de pets do tipo especificado
    for index, pet in enumerate(pets[pet_type]):
        # Adiciona um link para cada pet, com seu nome e índice como parte da URL
        html += f'<li><a href="/animals/{pet_type}/{index}">{pet["name"]}</a></li>'
    html += "</ul>"  # Fecha a lista
    return html  # Retorna o HTML gerado

# Definindo a rota para exibir o perfil individual de cada pet
@app.route('/animals/<pet_type>/<int:pet_id>')  # 'pet_id' é o índice do pet na lista
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]  # Obtém o dicionário de informações do pet específico
    # Gera um HTML para exibir as informações detalhadas do pet
    return f'''
    <h1>{pet['name']}</h1>  <!-- Exibe o nome do pet -->
    <img src="{pet['url']}" alt="Image of {pet['name']}">  <!-- Exibe a imagem do pet -->
    <p>{pet['description']}</p>  <!-- Descrição do pet -->
    <ul>
      <li><strong>Breed:</strong> {pet['breed']}</li>  <!-- Exibe a raça do pet -->
      <li><strong>Age:</strong> {pet['age']} years old</li>  <!-- Exibe a idade do pet -->
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)
