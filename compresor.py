#!/usr/bin/env python
# -*- coding: utf-8 -*-
dictionary = []
with open('dictionary_a.txt') as d:
    line = d.read()
    dictionary = line.split(';')#importing dictionary from csv file to simple list

outputFile = open('wyjsciea.txt', 'w')

with open('wejscie.txt') as input:#opening file from input
    for line in input:#reading line by line
        temp = line.split(' ')#selecting words from lines
        for w in temp:
            try:
                outputFile.write('%d' % dictionary.index(w))#try to code whole word as integer reffering to dictionary
            except ValueError:
                try:
                    int(w)#cast world to integer if possible
                    outputFile.write('&')#&-special symbol for handling numbers
                    outputFile.write(str(w))#save as string
                except:
                    dictionary.append(w)#if it is impossible to cast word to integer means that we need to append it to our dictionary(learning)
                    outputFile.write('%d' % dictionary.index(w))#saving new word in dictionary
            outputFile.write(' ')#separate word by whitespace
        outputFile.write('\n')#newline as in input file
outputFile.close()#closing our compressed file
with open('dictionary_a.txt', 'w') as d:
    for di in dictionary:
        d.write(di)
        d.write(';')#updating dictionary
