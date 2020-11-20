import xml.etree.ElementTree as ET

tree = ET.parse("New Arrivals22.rws")
root = tree.getroot()

for thing in root.findall('thing'):
    row = {}
    print(thing)
    break

game = root.findall('game')[0]
maps = game.findall('maps')[0]
li = maps.findall('li')[0]
things = li.findall('things')[0]
peruse = things.findall('thing')

thing = peruse[0]
print(thing)
print(thing.tag)
print(thing.attrib)

for thing in peruse:
    if thing.attrib['Class'] == 'Plant':
        pos = thing.find('pos')
        t = thing.find('def')
        h = thing.find('health')
        g = thing.find('growth')
        a = thing.find('age')

        type = t.text
        health = float(h.text) # percentage
        growth = float(g.text) # percentage
        age = float(a.text) / 21900000 # to years
        moisture = 0.25 * health # percentage (hardwood to algae)
        density = growth * health # percentage (young grass to old bramble)
        # print('Position: ', pos)  //needs conversion to floats
        print('Density: ', density)
        print('Moisture: ', moisture)