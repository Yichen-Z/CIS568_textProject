import pandas as pd
import time

# Combine review title and text into one field, then write to another csv file 
INPUT_FILE = r'indeed_reviews_processed.csv'
OUTPUT_FILE = r'reviews_postProcessed.csv'

df = pd.read_csv(INPUT_FILE)

# Combine review title and body
df['combined_text'] = df['review_title'] + '. ' + df['review_verbatim']
# df.to_csv(OUTPUT_FILE)

# Change date into MM/dd/yyyy format from written out format
# df = pd.read_csv(OUTPUT_FILE)
# try:
#     df['date'] = pd.to_datetime(df['date'])
#     df['date'] = df['']
# except ValueError as e:
#     pass
# df.to_csv(OUTPUT_FILE)

