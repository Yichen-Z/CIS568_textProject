import pandas as pd

INPUT_FILE = r'indeed_reviews.csv'
OUTPUT_FILE = r'reviews_textCombine.csv'

df = pd.read_csv(INPUT_FILE)
df['combined_text'] = df['review_title'] + '. ' + df['review_verbatim']
df.to_csv(OUTPUT_FILE)