#! /home/harsh/Machine_learning/ML_virtual_env/bin/python

## copy same code from 02file and then write another function in end to open files and take input 
## from 1st file and give output to 2nd file

from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

sample_text = """I loved this movie <br /><br /> since I was 7 and I saw it on the opening day. It was so touching and beautiful. I strongly recommend seeing for all. It's a movie to watch with your family by far.<br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disastor, nudity/sexuality and some language."""

# Init Objects
tokenizer = RegexpTokenizer(r'\w+')
eng_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


def getStemmedReview(review):
    
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    tokens = tokenizer.tokenize(review)
    useful_tokens = [i for i in tokens if (i not in eng_stopwords or i=='not')]
    stemmed_tokens = [ps.stem(i) for i in useful_tokens]    
    cleaned_review = ' '.join(stemmed_tokens)
    return cleaned_review


# Write one function that accepts input file and returns clean output file of movie reviews
def getStemmedDocument(inputFile,outputFile):

    ## sometimes in windows, there are some encoding issues in opening files. So we will use encoding='utf-8' to open the files and transfer data.
    out = open(outputFile,'w',encoding="utf8") # open output file in write mode
    with open(inputFile,encoding="utf8") as f:  # open input file in read mode(default mode)
        reviews = f.readlines()  # readline() reads a single line
    # it will input linewise and 'with' statement will automatically close file at end.

# As getStemmedReview() only takes single review as argument. So use for loop
    for review in reviews:
        cleaned_review = getStemmedReview(review)
        print((cleaned_review),file=out)  # send print(output) to 'out' file that we have opened earlier.
        ## by default 'file=sys.stdout' which sents output of print to our screen.        
    out.close()   # close output file
    ## input file was automatically closed after reading all file as we used 'with' statement.

# Read command line arguments(import sys module for this)
inputFile = sys.argv[1]
outputFile = sys.argv[2]
getStemmedDocument(inputFile,outputFile)  # call this function for all file operations.

## now we will execute this file from commandline like following:
#         ./03.2_data_cleaning.py imdb_toy_x.txt imdb_toy_clean.txt
#  (or)   python3 03.2_data_cleaning.py imdb_toy_x.txt imdb_toy_clean.txt

## And after this open both of these files: 'imdb_toy_x.txt' and  'imdb_toy_clean.txt'
## We can clearly see that after cleaning, our file text has almost deacreased to half.