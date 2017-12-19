#!/usr/bin/env python3

from wordListHandler import *

listaPalabras = loadData()

populateWordList(listaPalabras)

print(listaPalabras)

saveData(listaPalabras)
