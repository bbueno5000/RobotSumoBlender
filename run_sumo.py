import bge
from bge import render

def main():

    scene = bge.logic.getCurrentScene()

    sumoRed = scene.objects['SumoRed']
    sumoBlue = scene.objects['SumoBlue']

    contRed = sumoRed.controllers['Or']
    contBlue = sumoBlue.controllers['Or']

    sensRed = contRed.sensors['Ray']
    sensRed1 = contRed.sensors['Ray1']
    sensRed2 = contRed.sensors['Ray2']
    sensBlue = contBlue.sensors['Ray']
    sensBlue1 = contBlue.sensors['Ray1']
    sensBlue2 = contBlue.sensors['Ray2']

    actuRed = contRed.actuators['Motion']
    actuBlue = contBlue.actuators['Motion']

    if sensRed.positive:
        render.drawLine(sumoRed.worldPosition, sensRed.hitPosition, [255,0,0])
    if sensRed1.positive:
        render.drawLine(sumoRed.worldPosition, sensRed1.hitPosition, [255,0,0])
    if sensRed2.positive:
        render.drawLine(sumoRed.worldPosition, sensRed2.hitPosition, [255,0,0])

    if sensBlue.positive:
        render.drawLine(sumoBlue.worldPosition, sensBlue.hitPosition, [0,0,255])
    if sensBlue1.positive:
        render.drawLine(sumoBlue.worldPosition, sensBlue1.hitPosition, [0,0,255])
    if sensBlue2.positive:
        render.drawLine(sumoBlue.worldPosition, sensBlue2.hitPosition, [0,0,255])

    posRed = sensRed.hitPosition
    posRed1 = sensRed1.hitPosition
    posRed2 = sensRed2.hitPosition
    posBlue = sensBlue.hitPosition
    posBlue1 = sensBlue1.hitPosition
    posBlue2 = sensBlue2.hitPosition

    xRed = (posRed[0] * sumoRed['prop0']) + (posRed[1] * sumoRed['prop1']) + (posRed[2] * sumoRed['prop2']) + (posRed1[0] * sumoRed['prop3']) + (posRed1[1] * sumoRed['prop4']) + (posRed1[2] * sumoRed['prop5']) + (posRed2[0] * sumoRed['prop6']) + (posRed2[1] * sumoRed['prop7']) + (posRed2[2] * sumoRed['prop8']) + sumoRed['bias1']
    yRed = (posRed[0] * sumoRed['prop9']) + (posRed[1] * sumoRed['prop10']) + (posRed[2] * sumoRed['prop11']) + (posRed1[0] * sumoRed['prop12']) + (posRed1[1] * sumoRed['prop13']) + (posRed1[2] * sumoRed['prop14']) + (posRed2[0] * sumoRed['prop15']) + (posRed2[1] * sumoRed['prop16']) + (posRed2[2] * sumoRed['prop17']) + sumoRed['bias2']

    xBlue = (posBlue[0] * sumoBlue['prop0']) + (posBlue[1] * sumoBlue['prop1']) + (posBlue[2] * sumoBlue['prop2']) + (posBlue1[0] * sumoBlue['prop3']) + (posBlue1[1] * sumoBlue['prop4']) + (posBlue1[2] * sumoBlue['prop5']) + (posBlue2[0] * sumoBlue['prop6']) + (posBlue2[1] * sumoBlue['prop7']) + (posBlue2[2] * sumoBlue['prop8']) + sumoBlue['bias1']
    yBlue = (posBlue[0] * sumoBlue['prop9']) + (posBlue[1] * sumoBlue['prop10']) + (posBlue[2] * sumoBlue['prop11']) + (posBlue1[0] * sumoBlue['prop12']) + (posBlue1[1] * sumoBlue['prop13']) + (posBlue1[2] * sumoBlue['prop14']) + (posBlue2[0] * sumoBlue['prop15']) + (posBlue2[1] * sumoBlue['prop16']) + (posBlue2[2] * sumoBlue['prop17']) + sumoBlue['bias2']

    actuRed.linV = [xRed, yRed, 0]
    actuBlue.linV = [xBlue, yBlue, 0]

main()
