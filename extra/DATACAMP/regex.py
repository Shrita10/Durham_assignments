# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:04:33 2020

@author: Shrita
"""

import re


re.findall(r'movie','movie is great, movie is super great, movie')


string = 'hello!You!are'

re.split(r'!',string)

re.sub(r'hello','helloww',string)

re.findall(r'User\d','the winners: User9, UserN, User8')

re.findall(r'User\D','the winners: User9, UserN, User8')
re.findall(r'User\w','the winners: User9, UserN, User8')

re.findall(r'\W\d','THE skirt is on sale for &5 dollars')

re.findall(r'data\sScience','I enjoy learning data Science')

re.sub(r'ice\Scream','icecream','i hate ice-cream')

'''
\d is for digit
\D is for non-digit
\w is for word
\W is for non-word
\s is for whitespace
\S is for nonspace 
'''

sentiment_analysis = 'He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready'


# Write a regex to match pattern separating sentences
regex_sentence = ' '

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, "", df['location'])

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, ' ', sentiment_sub)
print(sentiment_final)






