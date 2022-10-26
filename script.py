import logging
import os
import pandas as pd
from transformers import pipeline
import spacy
from fastcoref import spacy_component

# Combine review title and text into one field, then write to another csv file 
INPUT_DIR = 'review_chunks'
OUTPUT_FILE = 'review_post.csv'

logging.basicConfig(filename=r'C:/Users/house/workspace/CIS_568_DataMining/CIS568_textProject/review_processor.log',encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def preprocess(in_file, out_file):
    """
    (function)
    Takes string filename in_file (use .csv)
        and appends the post-processed version to out_file (also .csv)
    """
    logging.info(f'Begin processing {in_file}')
    df = pd.read_csv(in_file, header=None)
    df.columns=["review_title","review_verbatim","role","status","location","date","rating"]
    logging.info(f'Read into dataframe')

    # Combine review title and body
    df['combined_text'] = df['review_title'] + '. ' + df['review_verbatim']
    logging.info(f'Made combined_text column from review title and body')

    # Replace pronouns
    review = df['combined_text']
    nlp = spacy.load("en_core_web_sm", exclude=["parser", "lemmatizer", "ner", "textcat"])
    nlp.add_pipe("fastcoref")
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
    simple_nlp = spacy.load("en_core_web_sm", exclude=["lemmatizer", "ner", "textcat"])
    df["sentences"] = df["antecedents_replaced"].apply(lambda x: [sent.text for sent in simple_nlp(x).sents])
    logging.info(f'Split sentences')

    # Sentiment
    sentiment_model = pipeline("sentiment-analysis")
    df["sentiment"] = df["sentences"].apply(lambda x: sentiment_model(x))
    logging.info(f'Sentiment predicted')

    # At end, append to csv
    df.to_csv(out_file, mode='a', index=False, header=False)
    logging.info(f'Pre-processing complete for this file.')

for file in os.listdir(INPUT_DIR):
    file = os.path.join(INPUT_DIR, file)
    preprocess(file, OUTPUT_FILE)