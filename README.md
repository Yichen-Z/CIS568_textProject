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
    Data cleaning 
        ❌ 48 reviews end with "more..." - most are probably irretrievable 
        ✔ Some reviews have no role/geographic location/valid review - slate for removal
        ✔ Remove 2+ blank spaces
    
    LDA to see if there are groupings
    Use Fast-Coref's spaCy component to replace pronouns with their antecedents
    Break review body into its component sentences
    Classify each sentence by its topic(s)
        Manual labeling
    MonkeyLearn
        Get sentiment from each sentence (positive, neutral, or negative)
            Partially done - 1000 limit
        Check out usefulness:
            Sample: I enjoy the people at this bank, made some lifelong relationships, but the environment is stressful a lot of the time and you often have to follow strict work schedules due to schedule adherence rules
                Topic Classifier: Society, 47% confidence
                Opinion Unit Extractor: See monkeylearn_oneoff.json -> has promise

### Post-processing Issues
    Non-ASCII characters that can get garbled:
        …

## Resources
    Pandas
        [Append dataframe to existing file](https://www.geeksforgeeks.org/how-to-append-pandas-dataframe-to-existing-csv-file/)

    Python 
        [logging](https://docs.python.org/3/howto/logging.html)
        os module
            [Iterating through files](https://www.geeksforgeeks.org/python-loop-through-files-of-certain-extensions/)
            [Joining paths](https://www.geeksforgeeks.org/python-os-path-join-method/)

    [Sentence Separation with spaCy](https://spacy.io/api/sentencizer)

    [Sentiment Models](https://huggingface.co/blog/sentiment-analysis-python#2-how-to-use-pre-trained-sentiment-analysis-models-with-python)