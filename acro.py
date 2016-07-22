import re
try:
    inputFile = open('inp.txt','r')
    inputF = inputFile.read()
    inputFile.close()#opening file
    
except IOError:
    print "Cannot read a file . Check if inp.txt exists in this directory"
else:

    names = re.findall(r'[A-Z][a-z]*\s[A-Z][a-z]*',inputF,re.M|re.S)#list of names(first name+'  '+second name)
    replacement = {}#creating a dictionary

    if names:
        for i in names:#iterating via list searching for separete names 
            replacement[i.split(' ')[1]] = re.search(r'\s[A-Z]',i,re.M|re.S).group()[1]+"."#add new position in dictionary: 'key value' is second name, 'value' is acronym from second name


    for key, value in replacement.iteritems():
        inputF = re.sub(r'\b(?=\w)%s\b(?!\w)' % key,value,inputF)#search for full second names and replace them by acronym
        
    outputFile = open('off.txt','w')
    if inputF:
        outputFile.write(inputF)#saving file

    else:
        print 'error while saving file'
    outputFile.close()
