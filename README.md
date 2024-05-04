Q: Using ( https://docs.openexchangerates.org/ ) provide a data pipeline that pulls the data from the API. Display the change of USD vs SAR in the last 3 months. This data must run and be updated on a daily
basis.

note: the code might take 2-3 minutes to run because in the URL to use ( started to end ) to describe the period you want to display (3 months), you must have a paid account so I made a for loop to hit the route 90 times to retrieve all data 

Requirements:

1 . Describe the architecture.

2 . Please clearly demonstrate the steps you have taken, the libraries and modules implemented and any data manipulation in the task.
 
3 . architecture :

    A. Used Python to extract data from Open Exchange Rates API using the "requests" library.
    
    B. Used "pandas" to transform the data from the JSON file into a data frame then added a date column and stored data in an Excel file for data tracking and further manipulation.
    
    C. displayed the data in a plot using the "matplotlib" library.
    
    D. used the libraries (schedule and time) to run the code and update the data.  


4 . libraries and modules implemented :
- "requests"
- "pandas" 
- from "DateTime" library used models ( DateTime, time delta, timezone ) 
- "matplotlib"

steps :

A. imported the necessary libraries.

B. defined a function to retrieve data called (fetch_data) using Request library.

c. defined a function to save all retrieved data into an Excel (.csv) file using the "pandas" library called (save_data).

D. defined a function to call the fetch_data method through a for loop to retrieve all data in the time frame needed then save all the data in a data frame using "pandas" library display the data in a plot using the "matplotlib" library and return all data.

E. used schedule and time libraries to run the code and update the data every 24h
