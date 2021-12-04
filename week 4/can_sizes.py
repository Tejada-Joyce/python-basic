# computes and prints the storage efficiency for each of the following 12 steel can sizes. 

import math

def main():
    """
    Parameters: no input
    Return:
    """
    print()
    can_list = [
            ["#1 Picnic", 6.83 , 10.16],
            ["#1 Tall", 7.78 , 11.91],
            ["#2", 8.73 , 11.59],
            ["#2.5", 10.32 , 11.91],
            ["#3 Cylinder", 10.79 , 17.78],
            ["#5", 13.02 , 14.29],
            ["#6Z", 5.40 , 8.89],
            ["#8Z short", 6.83 , 7.62],
            ["#10", 15.72 , 17.78],
            ["#211", 6.83 , 12.38],
            ["#300", 7.62 , 11.16],
            ["#303", 8.10 , 11.11],
            ]

    # for i in range(len(can_list)):
    #     name = can_list[i][0]
    #     radius = can_list[i][1]
    #     height = can_list[i][2]
    #     print(f"{name} {storage_efficiency(cylinder_volume(radius, height), cylinder_surface_area(radius, height)):.1f}")

    for i in can_list:
        name = i[0]
        radius = i[1]
        height = i[2]
        print(f"{name} {storage_efficiency(cylinder_volume(radius, height), cylinder_surface_area(radius, height)):.1f}")

def cylinder_volume(radius, height):
    """
    Parameters: the radius (base) and the height of the cylinder
    Return: volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume

def cylinder_surface_area(radius, height):
    """
    Parameters: the radius (base) and the height of the cylinder
    Return: area of the cylinder
    """
    area = 2 * math.pi * radius * (radius + height)
    return area

def storage_efficiency (volume, area):
    """
    Parameters: the volume and the area of the can
    Return: The storage efficiency of a steel can
    """
    storage_efficiency = volume / area
    return storage_efficiency

def cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()