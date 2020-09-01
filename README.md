# sentimentalAnalysis
This project analyses the sentiment of the statement. This could be used to analyse the sentiments of the viewers of youtube channel by analysing their comments

## For using MonkeyLearn API, monkeylearn library has to be installed first. To install monkeylearn library, 
    
    -> pip install monkeylearn

In the module monkeylearn/basicAnalyseML.py and monkeylearn/BasicAnaluseMLAPI.py, 
public model id and public API of monleylearn server is used.
For more detailed analysis and higher accuracy of the results, it is recommended to train
personal model. This could be done in monkeylearn website using their SaaS platform.

## To analyse the statements
### 1. Using Bash (monkeylearn/basicAnalyseBash.sh)
    Add the statements to be analysed in the data list. Multiple statements are allowed, each statement is in the form of a string, separated by comma.

    Run the file: This could be done by either of the following two ways:
        --> bash <fileName>
        OR
        --> chmod +x <fileName> (Required once, this makes the file executable)
        --> ./<fileName>

### 2. Using python to send HTTP POST request to monkeylearn server, using model ID and API key (monkeylearn/basicAnalysisMLAPI.py)
    Add all the statements to the data variable which is basicall a dict of data, where the value corresponds to a list of statements which are to be analysed.

    In the module, public API key is used and the public model is used. To get the results with higher accuracy, custom models could be used. This could be done via monkeylearn website using their SaaS.

    To analyse the statements, simply run
    --> python <ModuleName>

## The output would look like:
    This is a great tool!   tag: Positive   confidence: 0.998

    Horray! I love it.      tag: Positive   confidence: 0.99

    I hate it.      tag: Negative   confidence: 0.96