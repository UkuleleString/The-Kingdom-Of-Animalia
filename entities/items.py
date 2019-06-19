import random

itemDict = {
    "weapons": {
        "iron sword":
            {"name": "Iron Sword",
             "flavorText": "Just a regular iron sword",
             "level": 0,
             "damage": 0,
             "damageType": "melee",
             "unique": False,
             "modifiers": None
             },
        "long bow":
            {"name": "Long Bow",
             "flavorText": "thing",
             "level": 0,
             "damage": 0,
             "damageType": "ranged",
             "unique": False,
             "modifiers": None
             }
    },
    "Armour": {
        "leather helmet":
            {"name": "Leather Helmet",
             "ArmourType": "helmet",
             "flavorText": "A leather helmet",
             "level": 0,
             "generalDefense": 0,
             "magicDefenseModifier": 0,
             "unique": False,
             "modifiers": None
             }
    }
}

gods = {
    "water": {
        "good": {
            0:
            {"name": "Poseidon",
             "modifiers": ["the Great", "the Powerful"]
             },
            1:
            {"name": "fewfw",
             "modifiers": ["the Great", "the Powerful"]
             }
        }
    }
}

modifiers = {
    "weapon": {
        "sharpness":
        {"name": "Sharpness",
         "flavorText": "bleh.",
         "modType": "damage",
         "positiveChange?": True,
         "changeInStat": ""
         }
    }
}


def nameRandomizer(originalName, godType, godAlignment, godID):
    modifier = gods[godType][godAlignment][godID]["modifiers"][
        random.randint(0, 2)]
    godName = gods[godType][godAlignment][godID]["name"]
    return "The " + originalName + " of " + modifier + " " + godName


def uniqueify(itemType="weapons", nameOfItem="iron sword", modifierType="benefit",
              godType="water", godAlignment="good"):
    uniqueItem = itemDict[itemType][nameOfItem].copy()
    uniqueItem["unique"] = True
    originalName = uniqueItem["name"]
    uniqueItem["name"] = nameRandomizer(
        originalName, godType, godAlignment, random.randint(1, 1))
    # uniqueItem["modifiers"] = modifiers
    return uniqueItem

if __name__ == "__main__":
    print("Items: ", itemDict)
    print("\nGods: ", gods)
    print("\nModifiers: ", modifiers)
    print()
    print(uniqueify())
