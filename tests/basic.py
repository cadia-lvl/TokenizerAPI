# -*- coding: utf-8 -*-
import requests

r = requests.post("http://0.0.0.0:8080/tokenize/impl", params={'text':'3.janúar sl. keypti   ég 64kWst rafbíl. Hann kostaði € 30.000'})
print(r.text)
assert r.text == '{"response":{"type":"texts","content":[["3.","janúar","sl.","keypti","ég","64kWst","rafbíl","."],["Hann","kostaði","€30.000"]]}}'



r = requests.post("http://0.0.0.0:8080/tokenize/impl", params={'text':''})
print(r.text)
assert r.text == '{"response":{"type":"texts","content":[]}}'
