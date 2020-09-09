declare -a array
array[0]= /home/bilbo/@workspace/python_projects/sentimentalAnalysis/monkeylearn
array[1]= /home/bilbo/@workspace/python_projects/sentimentalAnalysis/scrapeYTcomments
export PYTHONPATH=$(printf "%s:${PYTHONPATH}" ${array[@]})

python3 visualization/basicAnalysisPlot.py