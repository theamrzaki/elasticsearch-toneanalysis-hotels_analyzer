# Hotel Analyzer
![enter image description here](https://github.com/theamrzaki/elasticsearch-toneanalysis-hotels_analyzer/blob/master/app/static/img/icons/Hotel-05-05.png?raw=true)

Hotel analyzer is a **Flast app** containing 2 main modules
 - Tone analysis using **IBM watson**
 - Indexer using **elasticsearch**


# App Structure

## Tone analysis
![enter image description here](https://github.com/theamrzaki/elasticsearch-toneanalysis-hotels_analyzer/blob/master/app/static/img/icons/Hotel-03.png?raw=true)
 1. First choose a hotel from the list
 2. then the app would use **IBM Watson** to get the analysis of each review of that selected hotel 
 3. then it aggregates all of them and views the final output 

## Indexer
![enter image description here](https://github.com/theamrzaki/elasticsearch-toneanalysis-hotels_analyzer/blob/master/app/static/img/icons/Hotel-04.png?raw=true)

> first the app would ask you to index the csv file, you must have **Elastic search** and it must be opened on the default port


 1. First choose a hotel from the list
 2. Tone analysis
	 - then the app would use **IBM Watson** to get the analysis of each review of that selected hotel 
	 - then it aggregates all of them and views the final output 
 3. Indexer
	 - using **Elastic search** , queries on the selected hotel
	 - views the output having **max score**


# How to run

    pip install -r requirements.txt
    python manage.py runserver -d

# Samples

## Dashboard
![enter image description here](https://github.com/theamrzaki/elasticsearch-toneanalysis-hotels_analyzer/blob/master/app/static/img/samples/Dashboard.png?raw=true)

## Tone Analyzer
![enter image description here](https://github.com/theamrzaki/elasticsearch-toneanalysis-hotels_analyzer/blob/master/app/static/img/samples/Tone%20Analyzer.png?raw=true)

## Hotel Indexer
### First set index
![enter image description here](https://github.com/theamrzaki/elasticsearch-toneanalysis-hotels_analyzer/blob/master/app/static/img/samples/First%20Index.png?raw=true)
### Then Choose hotel to get all its details
![enter image description here](https://github.com/theamrzaki/elasticsearch-toneanalysis-hotels_analyzer/blob/master/app/static/img/samples/Hotel%20indexer.png?raw=true)



> ### IF any problem occurs while running
> Feel free to reach out , i am happy to help
