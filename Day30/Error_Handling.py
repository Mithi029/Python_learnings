fruits = ['Apple', 'Pear', 'Orange']

def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + 'pie')
    except IndexError as e:
        print(e)

make_pie(1)