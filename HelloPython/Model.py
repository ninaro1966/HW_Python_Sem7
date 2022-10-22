import View

string: str = ''
result: int = 0


opSelect = {
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: (int(x) / int(y)) if int(y) != 0 else
View.division_be_zero(),
     "+": lambda x, y: int(x) + int(y),
     "-": lambda x, y: int(x) - int(y)}

def stringToList(string: str):
    string = string.replace(' ', '').strip()
    string = string.replace('+', ' + ')\
    . replace('-', ' - ')\
    . replace('*', ' * ')\
    . replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ')
    list = string.split()
    return list