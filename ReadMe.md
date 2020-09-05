The python file does the following:
 
1. It uses the sample dataset https://raw.githubusercontent.com/localytics/data-viz-challenge/master/data.json
2. Loads this data (make sure that you don't manually download the data but do it programmatically), processes it and outputs the following CSV file to s3:
3. Create an output file  total_events with these parameters: 
a. it has the following columns:  age, device, date, count, sum.
b. group on gender, age, device and date of client_time 
c. the date column has the format of YYYY-MM-DD
d. count column is the count of entries
e. sum column is the summing the value of the 'amount' key
f. only calculates entries for female ( "gender": "F" ) and Californian ("state": "CA") users.