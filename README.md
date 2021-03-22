There are three scripts in this folder: 
1) get_svc_status.py
2) webservice.py
3) coldiff.py
------------------------------

Pre-requisites:

Make sure panda, flask and Elasticsearch is installed on the machine. You can use pip3 to install these.

---------------------
1) get_svc_status.py 
---------------------

This script runs the following funcitonality.
 
It creates a JSON object with application_name, application_status and host_name.
Sample JSON Payload
{
   "service_name":"httpd",
   "service_status":"	",
   "host_name":"host1"
}
It wrrite tthis JSOON object to a file named {serviceName}-status-{@timestamp}.json

-------------------------------------------------------------------------

----------------
2) webservice.py 
------------------
This script crerate the endpoints and perform the following functions.

Accepts the above created JSON file(from previous step) and writes it to Elasticsearch.
Provides a second endpoint where the data can be retrieved, i.e

POST /add to Insert payload into Elasticsearch
GET /healthcheck -->  Return the all Application status (“UP” or “DOWN”)
GET /healthcheck/{serviceName} -->  Return the specific Application status (“UP” or “DOWN”)

***NOTE
Make sure to run the POST /add first. It will create index and POST json to ES.


Sample calls
http://127.0.0.1:5000/add
http://127.0.0.1:5000/healthcheck
http://127.0.0.1:5000/healthcheck/httpd

---------------------------------------------------------------------------------------

--------------
3) coldiff.py 
---------------

This script accepts the csv file at run time and generate a new CSV file that only includes properties sold for less than the average price / foot.
If csv file and this script is present at the same location then give the csv file name only otherwise give the absolute path of the csv.
Make sure panda is installed.
Eliminating the rows, which has sq__ft value zero. since denominator can't be zero while division.
Get the average of each row i.e price/sq__ft.
Find the mean value.
Compare each value obtained with mean value i.e < mean
Final.csv will be generated.

---------------------------------------------------------------------------------------
