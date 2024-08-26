import random as random
import csv as csv

def randomHadithNum():
    return random.randint(1, 2006)

def hadith_getter(hadithNum):
    with open('all_hadiths_clean.csv') as hadiths:
        one_hadith = csv.DictReader(hadiths)
        for row in one_hadith:
            if int(row['hadith_no']) == (hadithNum):
                result = [row['chapter'], row['text_en']]
                return result

