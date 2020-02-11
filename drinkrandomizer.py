import random

numIngredients = (random.randint(3,4))

liquorList = ['vodka', 'tequila', 'everclear', 'fireball', 'dark rum', 'light rum', 'cointreau']
secondaryLiquor = ['rumchata', 'midori', 'kahlua', 'blue curacao', 'baileys', 'amaretto', 'creme de menthe', 'elderflower liqueur']
mixerList = ['tonic water', 'ginger beer', 'orange juice', 'cranberry juice', 'cream', 'pineapple juice', ' grapefruit juice', 'coke', 'sprite', 'club soda', 'lime juice', 'lemon juice', 'sweet and sour']
extrasList = ['dash of grenadine', 'lemon wedge', 'lime wedge', 'simple syrup', 'mint sprig']

if numIngredients == 3:
    print("Liquor/Liqueur: ", random.choice(liquorList))
    print("Mixer: ", random.choice(mixerList))
    print("Extra: ", random.choice(extrasList))
else:
    print("Liquor/Liqueur: ", random.choice(liquorList))
    print("Secondary Liqueur: ", random.choice(secondaryLiquor))
    print("Mixer: ", random.choice(mixerList))
    print("Extra: ", random.choice(extrasList))