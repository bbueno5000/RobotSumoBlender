import bge
import random

def main():

    cont = bge.logic.getCurrentController()

    if not cont.sensors['Property'].positive:
        return

    scene = bge.logic.getCurrentScene()

    sumoRed = scene.objects['SumoRed']
    sumoBlue = scene.objects['SumoBlue']

    for i in range(0, 18):
        sumoRed['prop' + str(i)] = random.random() * (random.randint(0, 2) - 1)
        sumoBlue['prop' + str(i)] = random.random() * (random.randint(0, 2) - 1)

    bge.logic.getCurrentScene().objects['SumoRed'].position = [3.4505, -0.0804, 1]
    bge.logic.getCurrentScene().objects['SumoBlue'].position = [-3.489, -0.1379, 1]

    plane = scene.objects['Plane']
    plane['timer'] = 0
    plane['round'] = 0
    print(str(plane['round']) + ": delay reset.")

main()
