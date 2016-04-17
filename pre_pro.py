import nltk
import csv
from nltk.corpus import wordnet as wn
words = {}
#food = {}
#drink = {}
food_and_drinks = {}
def is_food_drink(word):
    "This function determines whether a word is a type of food or drink"
    words = word.split('_')
    for w in words:
        synsets = wn.synsets(w,pos='n')
        result = {}
        result['food'] = False
        result['drink'] = False
        food_1 = wn.synset('food.n.01')
        food_2 = wn.synset('food.n.02')
        drink_1 = wn.synset('drink.n.01')
        beverage = wn.synset('beverage.n.01')
        for i in range(0, len(synsets)):
            food_common_1 = synsets[i].lowest_common_hypernyms(food_1)
            food_common_2 = synsets[i].lowest_common_hypernyms(food_2)
            drink_common_1 = synsets[i].lowest_common_hypernyms(drink_1)
            beverage_common = synsets[i].lowest_common_hypernyms(beverage)
            if len(food_common_1) != 0:
                if food_common_1[0].name() == 'food.n.01':
                    result['food'] = True
            if len(food_common_2) != 0:
                if food_common_2[0].name() == 'food.n.02':
                    result['food'] = True
            if len(drink_common_1) != 0:
                if drink_common_1[0].name() == 'drink.n.01':
                    result['drink'] = True
            if len(beverage_common) != 0:
                if beverage_common[0].name() == 'beverage.n.01':
                    result['drink'] = True
    return result



with open('data_tfidf.csv','r') as data:
    reader = csv.DictReader(data,delimiter=',')
    for row in reader:
        if len(row['topic']) == 1 and (ord(row['topic'][0]) < ord('a') or ord(row['topic'][0]) > ord('z')):
            pass
        words[row['topic']] = row['tfidfscore']
for word,value in words.items():
    if is_food_drink(word)['food'] or is_food_drink(word)['drink']:
        food_and_drinks[word] = value
others_data = open('others.csv','w')
food_and_drinks_data = open('food_drink.csv','w')
others_data.write('topic,tfidfscore\n')
food_and_drinks_data.write('topic,tfidfscore\n')
for word,value in words.items():
    if word in food_and_drinks:
        food_and_drinks_data.write(word + ',' + value + '\n')
    else:
        others_data.write(word + ',' + value + '\n')
others_data.close()
food_and_drinks_data.close()
