
# init

## read Oxford 300
file = open('dictionaries/oxford_300.csv', 'r')

## load dictionary
dictionary = {}        
word = file.readline().replace('\n', '')
while word != '':
    pos = word.split(',')
    w = pos.pop(0) 
    dictionary[w] = pos
    word = file.readline().replace('\n', '')


