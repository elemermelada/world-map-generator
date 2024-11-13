import lxml.etree as ET
import sys
import csv

from util import CountryContainer, Country

if len(sys.argv) < 3:
    raise "Invalid number of argumentrs. Usage: `python main.py data.csv output.svg`"

[_, datafile, outputfile] = sys.argv

# READ CSV FILE
countrycontainer = CountryContainer()
with open(datafile, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        country = Country(row[0], row[1])
        countrycontainer.addCountry(country)
countrycontainer.setColors()

# OPEN SVG FILE
parser = ET.XMLParser(remove_blank_text=True)
SVGTREE = ET.parse("world-map.svg", parser=parser)
svgroot = SVGTREE.getroot()
maproot = svgroot[2]
NROFCOUNTRIES = len(maproot)

# REDRAW COUNTRIES WITH COLORS
for i in range(NROFCOUNTRIES):
    country = maproot[i]
    color = countrycontainer.getColor(country.get("id"))
    if not color is None:
        country.set("fill", color.get_hex())

SVGTREE.write(outputfile, pretty_print=True)
print("")
