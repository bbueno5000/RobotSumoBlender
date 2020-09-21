import bge
import random

def main():

    cont = bge.logic.getCurrentController()

    if not cont.sensors['Collision'].positive:
        return

    scene = bge.logic.getCurrentScene()

    sumoRed = scene.objects['SumoRed']
    sumoBlue = scene.objects['SumoBlue']

    if cont.sensors['Collision'].hitObjectList[0].name == 'SumoRed':
        for i in range(0, 18):
            if random.random() < 0.25:
                sumoRed['prop' + str(i)] = random.random() * (random.randint(0, 2) - 1)
            else:
                sumoRed['prop' + str(i)] = sumoBlue['prop' + str(i)]

    elif cont.sensors['Collision'].hitObjectList[0].name == 'SumoBlue':
        for i in range(0, 18):
            if random.random() < 0.25:
                sumoBlue['prop' + str(i)] = random.random() * (random.randint(0, 2) - 1)
            else:
                sumoBlue['prop' + str(i)] = sumoRed['prop' + str(i)]

    bge.logic.getCurrentScene().objects['SumoRed'].position = [3.4505, -0.0804, 0.5932]
    bge.logic.getCurrentScene().objects['SumoBlue'].position = [-3.489, -0.1379, 1.1474]

    plane = scene.objects['Plane']
    plane['timer'] = 0
    plane['round'] += 1
    print(str(plane['round']) + ": collision reset: " + cont.sensors['Collision'].hitObjectList[0].name)

main()
