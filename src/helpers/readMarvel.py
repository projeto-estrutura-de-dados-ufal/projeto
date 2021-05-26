import pandas as pd
import random

def readMarvel(path):
    hero = pd.read_csv(path)

    hundredElements = {
        "hero1": [],
        "hero2": []
    }

    chosenIndexes = []

    for i in range(100):
        # element = random.choice(hero['hero1'])
        index = random.randint(0, len(hero['hero1']) - 1)

        while (index in chosenIndexes):
            index = random.randint(0, len(hero['hero1']) - 1)

        hundredElements['hero1'].append(hero['hero1'][index])
        hundredElements['hero2'].append(hero['hero2'][index])
        chosenIndexes.append(index)
    

    return hundredElements
