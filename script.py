"""
TODO: provide an automatic way to deal with the header and first file -> see ### spots
"""
from datetime import datetime
import logging
import os
import pandas as pd
from transformers import pipeline
import spacy
from fastcoref import spacy_component

# Combine review title and text into one field, then write to another csv file 
ORIGINAL = 'indeed_reviews_processed.csv'
INPUT_DIR = 'review_chunks'
OUTPUT_FILE = 'review_post.csv'

# Do just once - does this save time?
logging.basicConfig(filename=r'review_processor.log',encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
nlp = spacy.load("en_core_web_sm", exclude=["parser", "lemmatizer", "ner", "textcat"])
nlp.add_pipe("fastcoref")
simple_nlp = spacy.load("en_core_web_sm", exclude=["lemmatizer", "ner", "textcat"])
sentiment_model = pipeline("sentiment-analysis")

def preprocess(in_file, out_file):
    """
    (function)
    Takes string filename in_file (use .csv)
        and appends the post-processed version to out_file (also .csv)
    """
    logging.info(f'Begin processing {in_file}')
    ### CHANGE HERE AFTER PROCESSING 1st FILE!! REST WILL NOT HAVE HEADER -> also SEE TO_CSV at END!!
    # df = pd.read_csv(in_file)

    ## TO PROCESS THE REST -> also SEE TO_CSV AT END!!
    df = pd.read_csv(in_file, header=None)
    df.columns=["review_id","review_title","review_verbatim","role","status","location","date","rating"]
    logging.info(f'Read into dataframe')

    # Combine review title and body
    df['combined_text'] = df['review_title'] + '. ' + df['review_verbatim']
    # new: drop text columns that got combined
    df = df.drop(columns=['review_title','review_verbatim'])
    df['date'] = df['date'].apply(lambda x: datetime.strptime(x, r"%B %d, %Y").strftime(r"%m/%d/%Y"))
    logging.info(f'Made combined_text column from review title and body')

    # Replace pronouns
    review = df['combined_text']
    docs = nlp.pipe(
        review, 
        component_cfg={"fastcoref": {'resolve_text': True}}
    )
    changed_list = []
    for doc in docs:
       changed_list.append(doc._.resolved_text)
    df['antecedents_replaced'] = changed_list
    logging.info(f'Replaced pronouns')

    # Split each review into individual sentences
    df["A"] = df["antecedents_replaced"].apply(lambda x: [sent.text for sent in simple_nlp(x).sents])
    df = df.drop(columns=['antecedents_replaced'])
    logging.info(f'Split sentences')

    # Sentiment
    df["B"] = df["A"].apply(lambda x: sentiment_model(x))
    logging.info(f'Sentiment predicted')

    # Explode into rows
    df = df.explode(list('AB'))
    df.rename(columns={'A':'sentences', 'B':'sentiment'}, inplace=True)
    df = df.reset_index(drop=True) # bash script already created the review_id prior to all this
    df['sentence_id'] = df.index # not unique, but OK since we have the unique review_id to use in combination
    logging.info(f'Expanded each sentence into its own row')

    # At end, append to csv
    ### ONLY RUN THIS ON THE 1st FILE!!!
    # df.to_csv(out_file, index=False)

    ## RUN THIS ON ALL SUBSEQUENT FILES!
    df.to_csv(out_file, mode='a', index=False, header=False)
    logging.info(f'Pre-processing complete for this file.')

for file in os.listdir(INPUT_DIR):
    file = os.path.join(INPUT_DIR, file)
    preprocess(file, OUTPUT_FILE)