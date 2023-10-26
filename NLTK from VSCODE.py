# Import libraries and load the data

import numpy as np
import pandas as pd
import re
import nltk
#nltk.download('all')
nltk.download('punkt')
nltk.download("book")
nltk.download('stopwords')
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import contractions
import unidecode
import demoji
from num2words import num2words
from spellchecker import SpellChecker
pd.options.display.max_columns=None
pd.options.display.max_rows=None
pd.options.display.max_colwidth=None
import pandas as pd

import pandas as pd

# Replace the file path with the full path to your CSV file on your local drive
file_path = 'H:/Mi unidad/Ejercicio/scopus.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

#for abstract in df['Abstract']:
#    print(len(abstract))
#print("")

#print(df['Abstract'])

import pandas as pd
import nltk

# Replace the file path with the full path to your CSV file on your local drive
file_path = 'H:/Mi unidad/Ejercicio/scopus.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

#print(df['Abstract'])

import pandas as pd
import nltk

# Replace the file path with the full path to your CSV file on your local drive
file_path = 'H:/Mi unidad/Ejercicio/scopus.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

#print(df['Abstract'])

import pandas as pd
import nltk

# Replace the file path with the full path to your CSV file on your local drive
file_path = 'H:/Mi unidad/Ejercicio/scopus.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

#print(df['Abstract'])

print("\n","\n",f'Shape of the whole data is: {df.shape[0]} rows and {df.shape[1]} columns')

print("\n",df.columns)

print("\nChacters per row in the Abstract column")
# how many tokens are in each row
df['Abstract_len'] = df['Abstract'].apply(lambda x: len(nltk.word_tokenize(x)))

for abstract in df['Abstract']:
    print(len(abstract))

print(" \nTokens or Strings per row in the Abstract column")
# print number of tokens per row
df['Abstract_len']