"""
__ dunder or magic methods
"""


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod  # not used often, cls stands for class
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod  # we don't have class
    def adding_things2(num1, num2):
        return num1 + num2


def main():
    """
        OOP subject
    """
    a_player = PlayerCharacter('Emanuel', 27)
    b_player = PlayerCharacter('Cindy', 23)
    b_player.shout()
    a_player.shout()

    print(a_player.adding_things(2, 3))
    player3 = PlayerCharacter.adding_things(2, 3)
    print(player3.age)


""" 
    users
        - archers
        - wizards
"""


class User:
    def __init__(self, email):
        self.email = email 
        
    def sign_in(self):
        print('logged in')
        
    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power, email='chica@gmail.com'):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')
    
    def check_arrows(self):
        print(f'{self.num_arrows} remaining')
    
    def run(self):
        print('ran really fast')
        
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):

        # Wizard.__init__(self, name, power)
         Archer.__init__(self, name, num_arrows)
    
    

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age   = age
        self.my_dict = {
            'name' : 'Yoyo',
            'has_pets' : False
        }
    
    # modify dunder methods       
    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __del__(self):
        print('deleted')
        
    def __call__(self):
        return('yess?')
    
    def __getitem__(self, i):
        return self.my_dict[i]



#MRO - MEthod Resolution Order
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1 
    
class D(B, C):
    pass


class X:pass
class Y:pass 
class Z:pass
class AA(X, Y): pass
class BB(Y, Z): pass 
class M(BB, AA, Z): pass

if __name__ == '__main__':
    # main()
    wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
    archer1 = Archer('Robin', 100)
    wizard1.attack()
    archer1.attack()
    
    print(wizard1.email)
    print(dir(wizard1)) # see all the methods + object methods
    
    
    # introspection - determine the type of an object at runtime
    action_figure = Toy('red', 0)
    print(action_figure.__str__())
    # the same like above 
    print(str(action_figure))
    
    print(len(action_figure))
    print(action_figure())
    
    print(action_figure['name'])

    del action_figure
    
    hb1 = HybridBorg('borgie', 50, 100)
    print(hb1.run())
    print(hb1.check_arrows())
    # print(hb1.attack())
    # print(hb1.sign_in())
    
    print(D.mro())
    print(D.num)
    
    print(M.mro()) #DFS algorithm
    
 