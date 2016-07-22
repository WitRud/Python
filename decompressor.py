#!/usr/bin/env python
# -*- coding: utf-8 -*-
dictionary = []
with open('dictionary_a.txt','r') as d:
    line = d.read()
    dictionary = line.split(';')#loading dictionary into a python list

outputFile = open('output.txt', 'w')#opening file where we want to write

with open('comp.txt') as input:#reading compressed file line by line
    for line in input:
        temp = line.split(' ')#selecting words
        for w in temp:
            if w[0] == '&':#check if word is a number
                outputFile.write(w[-1])
            else:
                try:
                    outputFile.write(dictionary[int(w)])#try to unpack
                except:
                    outputFile.write('\n')
            outputFile.write(' ')
outputFile.close()
