# a Python module is a file
# pycache everytime we use imports / modules 
# package is a folder, modules are python files

import shopping.shopping_cart as my_package
import pyjokes
print(__name__)
my_package.functie()

if __name__ == '__main__':
    print('the name of the file, the current file is __main__')
    print(pyjokes.get_joke('en', 'neutral'))
