# CIS568_textProject
Team repo for CIS 568/ECE 537 Data Mining course project Fall 2022

## Data 
Indeed company reviews

### Data Pre-processing
    Data cleaning 
        ❌ 48 reviews end with "more..." - most are probably irretrievable 
        ✔ Some reviews have no role/geographic location/valid review - slate for removal
        ✔ Remove 2+ blank spaces
    
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