import math
from colour import Color

red = (1, 0, 0)
white = (1, 1, 1)


class Country:
    code: str = None
    value: float = None
    color: Color = None

    def __init__(self, code: str, value: str):
        self.code = code
        try:
            self.value = float(value)
        except:
            self.color = value

    def isValid(self) -> bool:
        return self.code != None and (self.value != None or self.color != None)

    def setColor(self, minval: float, maxval: float):
        if self.value == None or self.value > maxval or self.value < minval:
            return
        color = (
            white[i] + (red[i] - white[i]) * (self.value - minval) / (maxval - minval)
            for i in range(3)
        )
        self.color = Color(rgb=color)


class CountryContainer:
    countries: list[Country] = []

    def addCountry(self, country: Country):
        if not country.isValid():
            return
        self.countries.append(country)

    def setColors(self):
        maxval = -math.inf
        minval = math.inf
        for i in range(len(self.countries)):
            country = self.countries[i]
            if country.value is None:
                continue
            maxval = max(maxval, country.value)
            minval = min(minval, country.value)

        for i in range(len(self.countries)):
            self.countries[i].setColor(minval, maxval)

    def getColor(self, code: str):
        for i in range(len(self.countries)):
            if self.countries[i].code.lower() == code.lower():
                return self.countries[i].color
