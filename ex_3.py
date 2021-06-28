numbers_of_the_grades = int(input('Enter count of the grades'))
grades = []

i = 1
while i <= numbers_of_the_grades:
  grades.append(int(input(f'Insert grade {i}: ')))
  i += 1

print(f' averade is {sum(grades ) / numbers_of_the_grades}')
