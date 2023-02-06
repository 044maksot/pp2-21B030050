age = 18
name = 'Maksot'
speciality = 'automation and control'
course = '2'
aboutme = "My name is {}, I'm {} and I'm studying in the {} course in the speciality {}"
print(aboutme.format(name, age, course, speciality))

# Named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))