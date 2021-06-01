# -*- coding: utf-8 -*-
import requests

r = requests.get("http://0.0.0.0:8080/tokenize", params={'text':'3.janúar sl. keypti   ég 64kWst rafbíl. Hann kostaði € 30.000'})
assert r.text == '[["3.","janúar","sl.","keypti","ég","64kWst","rafbíl","."],["Hann","kostaði","€30.000"]]'
print(r.text)

