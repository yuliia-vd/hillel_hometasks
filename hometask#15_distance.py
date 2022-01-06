# Написать функцию, которая считает расстояние между двумя точками с координатами x1, y1 и x2, y2.
#
# (Применить теорему пифагора и т.д.)

def distance(x1,y1,x2,y2):
    distance_between_two_points = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance_between_two_points

result = distance(1,2,3,4)
print(result)
