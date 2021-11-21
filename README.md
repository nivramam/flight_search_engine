# flight_search_engine
**PHASE 1**

Scraping the goibibo website for flights from and to a specified destination in India. The working of the engine is as follows:
1. Collecting data through web scraping.
2. Removing irrelevant data and storing relevant.
3. Sending the data for tokenization and constructing inverted index.
4. APART: collect data for Recommendations of flights from scraping the website goibibo. 

**PHASE 2**
1. Perform vector space modelling on documents containing city data (used to determine info about destination of the flight)
2. Train the model based on predefined queries. 
3. Receive a query from user
4. Rank the documents based on COSINE similarity

**PHASE 3**
1. Intialize the server to host the flight engine service.
2. Once the user gives query try to route to pages containing details regarding the similarity of the query with the documents. 
3. After that route the user to page containg all recommendations based on flight and also the destination information. 
