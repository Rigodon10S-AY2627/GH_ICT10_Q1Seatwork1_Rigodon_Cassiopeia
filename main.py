# Declaring Variables and Identifying Data Types
from pyscript import display, document

_name = 'Cassiopeia Rigodon'
age = 15
height1 = 157.48
countries_visit = ['Germany', 'France', 'United Kingdom']
student_type = False
student_info = {'color': 'Lavender','car_brand': 'BYD','shoe_size':8,'best_friend': 'Elijah Mae'}
favorite_fruits = {'Lychee','Kiwi', 'Rambutan', 'Mango', 'Melon'}
days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

display(type(_name), target='result')
display(type(age), target='result')
display(type(height1), target='result')
display(type(countries_visit), target='result')
display(type(student_type), target='result')
display(type(student_info), target='result')
display(type(favorite_fruits), target='result')
display(type(days), target='result')

document.getElementById('result').innerHTML = f'''

<h2>About Me, Myself, & I</h2>

<p><b>Name:</b> {_name}</p>
<p><b>Age:</b> {age}</p>
<p><b>Height:</b> {height1} cm</p>
<p><b>Countries I Want to Visit:</b> {countries_visit}</p>
<p><b>New Student:</b> {student_type}</p>

<p><b>Student Information:</b></p>
<ul>
    <li>Color: {student_info['color']}</li>
    <li>Car Brand: {student_info['car_brand']}</li>
    <li>Shoe Size: {student_info['shoe_size']}</li>
    <li>Best Friend: {student_info['best_friend']}</li>
</ul>

<p><b>Favorite Fruits:</b> {favorite_fruits}</p>

<p><b>Days of the Week:</b> {days}</p>
'''