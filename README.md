# CIS568_textProject
Team repo for CIS 568/ECE 537 Data Mining course project Fall 2022

## Virtual Environment Setup
In Visual Studio Code
    Powershell terminal
        ```
        python -m venv review_venv
        ```
    Pop-up at right bottom corner: select new interpreter/virtual environment for current workspace
    Close current Powershell terminal and reopen
        (review_venv) should now head the command line
    
## Packages
    First update pip
        ```
        python -m pip install --upgrade pip
        ```
    FastCoref: antecedent resolution
        ```
        python -m pip install fastcoref
        ```
    spaCy language model
        ```
        python -m spacy download en_core_web_sm
        ```

## Data 
Indeed company reviews

### Data Pre-processing
    Data cleaning -> indeed_reviews_processed.csv
        ❌ 48 reviews end with "more..." - most are probably irretrievable 
        ✔ Some reviews have no role/geographic location/valid review - removed
        ✔ Some reviews had formatting errors on employee status - fixed
        ✔ Remove 2+ blank spaces
    
    Git Bash 
        sh add_index.sh
        (this adds in review_id)
        sh split_csv.sh 
        (this splits into small enough chunks for local machine memory)
    
    LDA to see if there are groupings
    ✔ Use Fast-Coref's spaCy component to replace pronouns with their antecedents
        Issue: need to break data into smaller batches - try 50 lines
    ✔ Break review body into its component sentences
    ✔ Use Kaggle's basic Sentiment prediction (positive, negative)
    Classify each sentence by its topic(s)
        Manual labeling
    MonkeyLearn
        Get sentiment from each sentence (positive, neutral, or negative)
            Partially done - 1000 limit
        Check out usefulness:
            Sample: I enjoy the people at this bank, made some lifelong relationships, but the environment is stressful a lot of the time and you often have to follow strict work schedules due to schedule adherence rules
                Topic Classifier: Society, 47% confidence
                Opinion Unit Extractor: See monkeylearn_oneoff.json -> has promise
    
    Issues
        Skipped ab -> split further?

### Post-processing Issues
    Non-ASCII characters that can get garbled:
        …

## Resources
    Pandas
        [Append dataframe to existing file](https://www.geeksforgeeks.org/how-to-append-pandas-dataframe-to-existing-csv-file/)
        [Reset index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html)

    Python 
        [logging](https://docs.python.org/3/howto/logging.html)
        os module
            [Iterating through files](https://www.geeksforgeeks.org/python-loop-through-files-of-certain-extensions/)
            [Joining paths](https://www.geeksforgeeks.org/python-os-path-join-method/)

    [Sentence Separation with spaCy](https://spacy.io/api/sentencizer)

    [Sentiment Models](https://huggingface.co/blog/sentiment-analysis-python#2-how-to-use-pre-trained-sentiment-analysis-models-with-python)