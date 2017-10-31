# Title

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

# Research questions
A list of research questions you would like to address during the project. 

# Dataset
Patents dataset - we will use the patents dataset from http://www.patentsview.org/api/doc.html from where you can get the data through the API Endpoint. With HTTP GET or POST method we can search for patents matching the query string and this will return the data fields we are looking for. The response data format is JSON. 

An example of a API call using the GET method:
```http://www.patentsview.org/api/patents/query?q={"_gte":{"patent_date":"2007-01-04"}}&f=["patent_number","patent_date"]```
This will return all patent numbers and patent dates after 2007-01-04

Also, the raw data is available for download, and maybe we will use it for some more complex queries.


# A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

# Questions for TAa
Add here some questions you have for us, in general or project-specific.
