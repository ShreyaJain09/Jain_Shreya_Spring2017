# Midterm Assignment for Introduction to Python

Three analysis to be done on different dataset
•	Enron Company Dataset.
•	New York Times Dataset.
    	- Most Popular
   	 - Books

##Question 1- Analysis on Enron Email Dataset

The Enron Email Corpus is one of the biggest email data sources in the world. Almost half a million files spread over 2.5 GB. By 2002, it had collapsed into bankruptcy due to widespread corporate fraud. In the resulting Federal investigation, there was a significant amount of typically confidential information entered into public record, including tens of thousands of emails and detailed financial data for top executives.

###Kenneth Lay was the one time CEO and director of Enron.

The goal of the project is to go through the thought process of data exploration (learning, cleaning and preparing the data), feature selecting/engineering (selecting the features which influence mostly on the target.


###Three different analysis done on Enron email dataset.

## 1. Analyzing the emails to find the count of the emails, to find out who the top 10 most popular addresses are.


To get this data,
-	Initially the data was in MIME type format.
-	Loop through all the emails sent by lay-k
-	Using email.parser to open emails in Python,
-	Getting the to, from, subject from all the emails.
-	Analyzing the emails using email_analyse()
-	Creating email instance, to read the different fields and store them in the lists
-	Convert the to_email_list to Counter object. This will count all the unique emails in the list. When then call the most_common() function to get the ten most common emails. Package used for this is Counter and Collections

###Result: 

-	From this analysis, we see that the most of the emails were sent with Lay’s own email address (as we are looking at his data). It seemed he had two email addreses: kenneth.lay@enron.com and klay@enron.com.
-	The most emails he received were from Rosalee Fleming.



-	From the maildir overall dataset we see that,  In the To list, the top person is Richard Shapiro, the Vice President for Enron. The fact that he received the most emails shows he was in touch with everything that was happening.
-	The highest From field, which is emails received from, is Kay Mann, who was the head of legal for Enron. 


## 2. Cleaning & Preprocessing for getting the frequency of the Most Common Words in Kenneth Lay’s emails 


To clean the data,
- Using the ken_lay_emails.txt file 
-	Remove all the stopwords using the NLTK stopword
-	Remove all the punctuations to get the count of the words only
-	Getting the word count of the most used words in the kay-l emails as well as the most used words in the maildir folder as a whole.



###Result


-	From the results we can say that the words communication and energy is expected as this is seen.
-	Other words that have high occurrence is Communication, lay, stocks, funds, crisis, selling and Bankruptcy. 
-	Other than Houston, California is the only city that has very high reference, which says they would have had some connection over there as well.
-	


## 3. Topic Modelling of the dataset

This uses gensim's online latent dirichlet allocation implementation to topic model the Enron Email dataset. The Enron Emails contain 517,431 emails from 150 Enron executive accounts covering a period from December 1979 through February 2004, with the majority of emails occurring during 1999, 2000, and 2001. After training, we can infer 100 latent topics in the corpus. Topics are interpreted by their probability distribution over words

With a trained model we can also infer, for each email, a probability distribution over topics. With each email represented as a vector of topic probabilities, we can do things like cluster similar emails together via the cosine similarity measure, or assign topics to new unseen documents (like user queries) and retrieve all emails that match that topic.


Output word distributions:

 * topic #34: 0.010*nymex + 0.008*exchange + 0.007*futures + 0.007*member + 0.005*clearing + 0.005*notice
 * topic #15: 0.011*game + 0.006*fantasy + 0.005*football + 0.005*wr + 0.005*play + 0.005*rb
 * topic #39: 0.007*emissions + 0.007*environmental + 0.005*etrade + 0.005*epa + 0.005*lcampbensf + 0.004*permit
 * topic #76: 0.006*chairman + 0.005*president + 0.004*ceo + 0.004*global + 0.004*businesses + 0.004*chief 
 * topic #17: 0.022*sally + 0.013*beck + 0.012*becks + 0.010*sbecknsf + 0.007*sallybeckdec
 * topic #96: 0.004*agreement + 0.003*credit + 0.003*language + 0.003*such + 0.003*section + 0.003*under
 * topic #58: 0.006*california + 0.005*market + 0.005*said + 0.004*iso + 0.004*electricity + 0.004*ferc

-	Used the clean dataset and normalize the corpus.
-	Prepare the Document-Term matrix
-	Run the lda model
-	Print the result



#Question2 - NYTAPI Analysis

NYT provides APIs to access its rich contect to its readers and other people for analysis. There are many APIs provided, but used for analysis here are 

  - BOOKS API
  - MOST POPULAR API
  

## API 1 : MOST POPULAR ARTICLES ANALYSIS

This analysis requires following operations to be performed: 
  - Generate NYTAPI Key
  - Store it as environment variable for global access and security
  - Make connection with API service to read data
  - Collect data from NYTAPI in json format using API calls
  - Process the data to save it as CSV at local disk
  - Prepare data for descriptive analysis/exploratory analysis
  - Perform the analysis on collected data


Steps:
- Retrieve Data> 
MostEmailed URL emailed_url= 'https://api.nytimes.com/svc/mostpopular/v2/mostemailed/all-sections/30.json?api-key=8171f9b6eba24d638bd7986a927e3a35'

MostViewed URLviewed_url= 'https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/30.json?api-key=8171f9b6eba24d638bd7986a927e3a35'

MostShared URL shared_url= 'https://api.nytimes.com/svc/mostpopular/v2/mostshared/all-sections/30.json?api-key=8171f9b6eba24d638bd7986a927e3a35'
 - Iterate through multiple API calls
   >for i in range(0, pages):
    >    offset = i*20
    >    myurl = url+ '&' + 'offset=' + str(offset)
    >    r = requests.get(myurl)
    >    json_data = r.json()
    >    myFunction(json_data)
    >    time.sleep(0.5)
- Export data as csv
    ###writing data in csv format at local disk
    with open('popular_3.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(popular)

The most challenging part of the collecting data was to iterate through multiple api calls. Unlike other APIs, this API uses [*offset*] value instead of ['pages']. Also, the 'offset value has to be multiple of [20][dill] to get successful results. 

### Analysis 1: Number of Popular articles by Year

-	Looping through each list item to fetch particular attribute such as title, section, date, etc
-	Using counters to get the count of most popular books by year.
-	Output: 2013: 2, 2014: 2, 2015: 8, 2016: 120, 2017: 1727
-	We can see that most of the books fall in 2017 category

### Analysis 2: Number of Popular articles by various sections
-	Using counter to segment the articles based on category and hetting how many counts of articles falls into each category every year. 
-	Few of the sample output is shown below
Output: 'Arts': 108,
         'Books': 23,
         'Briefing': 22,
         'Business Day': 134,
         'Crosswords & Games': 2,
         'Education': 12,
         'Fashion & Style': 32

###Analysis 3: Top 20 byLine(contributor) for the Most Popular Articles
-	Getting the count of Contributors based on the articles
-	Output : ('By THE EDITORIAL BOARD', 48),
('By JULIE HIRSCHFELD DAVIS', 16),
('By THE NEW YORK TIMES', 16),
('By PAUL KRUGMAN', 15),
('By GIOVANNI RUSSONELLO', 14),
('By KIMIKO de FREYTAS-TAMURA', 13),
('By PETER BAKER', 12)


## API 2 : BEST SELLING BOOKS ANALYSIS

This analysis requires following operations to be performed: 
  - Generate NYTAPI Key
  - Store it as environment variable for global access and security
  - Make connection with API service to read data
  - Collect data from NYTAPI in json format using API calls
  - Process the data to save it as CSV at local disk
  - Prepare data for descriptive analysis/exploratory analysis
  - Perform the analysis on collected data


Steps:
- Retrieve Data
- Define a function that collects data from json and writes it to a list
- Save data as a CSV

### Analysis 4 : Count of number of Bestselling Books by age_group of the readers
-	Get the title, publisher of the books and the age category that reads that kind of books. 
-	For all the different category we can see how many best seller books is read by what age group.
-	Output : We can see that most books are read by age 12 and above

### Anslysis 5: Top 30 Publishers of Bestselling Books
-	To get the top 30 publishers of the best selling books
-	Output : We can see that few of the best publishers are Simon & Schuster, Mira, Ballantine





