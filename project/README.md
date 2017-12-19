# The cool patent

## Website [link](https://antonino-barbera.github.io/seanbi/)

## Abstract
Finding the common characteristics or relations to their features among influential patents, can help inventors to follow the same practice. And moreover, it opens possibility of predicting patent’s influentience. In this project, by using number of references to individual patent, we’ll evaluate each patent’s influence. Then, we can do exploratory analysis on dataset and our evaluations to find general trends. From here, we will try to apply machine learning methods to create prediction model. 

## Research questions
At the beginning we would like to see some general information:
* Is there a trend for the number of patents applications during the years? 
* Which countries have the most assigned patents? 
* What are the most popular technology fields for patents assigned in the last 5 years?
* What's the most frequent technology field by inventor's country? 
* What percentage of patents belongs to private and what to organizations?

Then we will focus on the citations:
* Are the citations inside each patent and the citations to a patent increasing with passing of the years?
* How the number of citations relates to the category of the patent?

We will also try to answer the question: 
* How "famous" is a patent?

## Dataset
The patent dataset is maintained by the National Bureau of Economic Research (NBER). We downloaded them at the following link: http://www.nber.org/patents/

The data are in 5 zipped ASCII CSV files as follows:
* Pat63_99.zip contains the patent data, including the constructed variables
* Coname.zip contains the assignee names.
* Match.zip contains the match to CUSIP numbers
* Inventor.zip contains the individual inventor records
* Cite75_99.zip contains the pairwise citations data, between 1975 and 1999.

Each of these files has a corresponding "txt" file that contains the variable names and other documentation. The whole dataset is more analysed in notebook.


## A list of internal milestones up until project milestone 2
* Nov. 11, 2017 - Get comfortable using the API, getting the needed data and trying to answer some of the questions and make some demo plots.
* Nov. 21, 2017 - We should have answered all of the questions and try to find a way to answer how "famous" a patent is. 

## Questions for TAa
* Does the focus need to be only on citations or we can study general caratheristics on the patents?
* Should we also use the dataset provided at http://snap.stanford.edu/data/cit-Patents.html and should we somehow combine the 2 datasets?
* Does it make sense to create a machine learning system to predict how cited a patent is going to be?
