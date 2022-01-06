# Повторить через наследование научную классификацию леща и атлантической сельди
#
# на каждом уровне(домен, царство, тип, класс, отряд и т.д.)
# выделить и описать по одному-два свойсва характеризующие уровень

class Eukaryote:
    nucleus = 'cells have nucleus'

class Animals(Eukaryote):
    def breathe_oxygen(self):
        print('I can breathe oxygen')
    def eat_organic_food(self):
        print('I eat organic food')
    def move(self):
        print('I can move independently')

class Chordate(Animals):
    chord = 'have сhord skeleton'

class Fish(Chordate):
    def live_in_water(self):
        print('I can not live without water')
    def breathe_with_gills(self):
        print('I can breathe only with gills')

class Сельдеобразные(Fish):
    lateral_line = 'no lateral line'
    dorsal_fin = 'one dorsal fin'

class Сельдевые(Сельдеобразные):
    scales = 'have no scales on the head'
    teeth = 'have small teeth'

class Сельди(Сельдевые):
    dorsal_fin_size = 'small'

class Атлантическая_cельдь(Сельди):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.color = 'silver'
        self.length = '45 cm'
        self.weight = '1.1 kg'
        self.habitat = 'both sides of the Atlantic Ocean'
        self.food = 'copepods, krill and small fish'


class Карпообразные(Fish):
    weberian_apparatus = 'have Weberian apparatus'
    dorsal_fin = 'single dorsal fin'

class Карповые(Карпообразные):
    stomach = 'no stomach'
    teeth = 'no teeth'

class Лещи(Карповые):
    dorsal_fin_size = 'short'

class Лещ(Лещи):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.color = 'silvery-grey'
        self.length = '75 cm'
        self.weight = '4 kg'
        self.habitat = 'rivers and lakes'
        self.food = 'chironomid larvae, Tubifex worms, bivalves, water plants and plankton'

Fish1 = Атлантическая_cельдь('Herring')
Fish2 = Лещ('Common_bream')

print(f'{Fish1.name} color is {Fish1.color}')
print(f'{Fish1.name} weight is {Fish1.weight}')
print(f'{Fish2.name} color is {Fish2.color}')
print(f'{Fish2.name} food is {Fish2.food}')
print(f'{Fish1.name} dorsal fin size is {Fish1.dorsal_fin_size}')
print(f'{Fish2.name} dorsal fin size is {Fish2.dorsal_fin_size}')

Fish1.move()
Fish2.breathe_oxygen()