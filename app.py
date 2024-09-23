from flask import Flask  # Imports the Flask framework
from helper import pets  # Imports the 'pets' dictionary from the helper.py file

app = Flask(__name__)  # Creates an instance of Flask, which will be used to set up routes

# Defining the route for the home page
@app.route('/')
def index():
    # Returns a simple HTML with links to the pet categories
    return '''<h1>Adopt a Pet</h1>
              <p>Browse through the links below to find your new furry friend:</p>
              <ul>
                <li><a href='/animals/dogs'>Dogs</a></li>
                <li><a href='/animals/cats'>Cats</a></li>
                <li><a href='/animals/rabbits'>Rabbits</a></li>
              </ul>
           '''

# Defining the route to display the list of animals by type (e.g., dogs, cats, rabbits)
@app.route('/animals/<pet_type>')  # 'pet_type' will be a dynamic variable in the URL
def animals(pet_type):
    # Generates an HTML listing all pets of a specific type
    html = f'<h1>List of {pet_type}</h1>'  # Title displaying the type of animal
    html += "<ul>"  # Opens an unordered list
    # Iterates through each pet in the list of pets of the specified type
    for index, pet in enumerate(pets[pet_type]):
        # Adds a link for each pet, including its name and index as part of the URL
        html += f'<li><a href="/animals/{pet_type}/{index}">{pet["name"]}</a></li>'
    html += "</ul>"  # Closes the list
    return html  # Returns the generated HTML

# Defining the route to display an individual pet's profile
@app.route('/animals/<pet_type>/<int:pet_id>')  # 'pet_id' is the index of the pet in the list
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]  # Retrieves the dictionary containing the specific pet's information
    # Generates an HTML page to display the detailed information about the pet
    return f'''
    <h1>{pet['name']}</h1>  <!-- Displays the pet's name -->
    <img src="{pet['url']}" alt="Image of {pet['name']}">  <!-- Displays the pet's image -->
    <p>{pet['description']}</p>  <!-- Displays the pet's description -->
    <ul>
      <li><strong>Breed:</strong> {pet['breed']}</li>  <!-- Displays the pet's breed -->
      <li><strong>Age:</strong> {pet['age']} years old</li>  <!-- Displays the pet's age -->
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)  # Runs the Flask app in debug mode
