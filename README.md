## TECHFLIX - MOVIE RECOMMENDER SYSTEM
App URL - [Link](https://cinebuzz.herokuapp.com/)

### _Objective_:
- To build a recommender system which accepts the user preferences through an API and gives out three movie recommendations
- Note: Movies should be only films & Feature films in English language

### _Methods Used_:
### 1. **Web Scraping**:
- _Sources Considered_: TMDB, IMDb, Box Office Mojo
- _Data Collected_: Top rated English movies are considered
- _Scripting Language_: Python
- _Python Packages used_:- **Scraping**: Beautiful Soup, Requests and Selenium. **File Handling**: Pandas
- _API_: TMDB API to fetch the movie data

How to create the TMDB API?
- Create TMDB account
- In profile section, select **API request** and provide contact information with application details
- Then use the API for getting data from TMDB website

How to use Selenium in Chrome?
- Open the Chrome browser and navigate to "Help -> About Google Chrome" and check the browser version
- Download the same version driver from this [Link](https://chromedriver.chromium.org/downloads)

Install the Packages
```
pip install requests
pip install selenium
pip install beautifulsoup4
```

### 2. **Model Development**:
_Cosine Similarity Model_:
Recommender systems are an important class of machine learning algorithms offers “relevant” suggestions to users. There are 2 major types such as **Content-based Filtering** and **Collaborative Filtering**. Recommendation Systems work based on the _similarity_ between either the content or the users who access the content.
There are several ways to measure the similarity between two items. The recommendation systems use this _similarity matrix_ to recommend the next most similar product to the user.

We will use the Cosine Similarity from Sklearn, as the metric to compute the similarity between two movies.
**Cosine similarity** is a metric used to measure how similar two items are. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The output value ranges from 0–1.
```
0 means no similarity, where as 1 means that both the items are 100% similar.
```

### _Workflow_:

![Image](https://github.com/MageshwariSingaravadivelou/Techflix/blob/main/workflow.png)

### _How to Use_:
- Select the Radio button as per the User wish 
- Give any of the movies name from the list provided in the [URL](https://github.com/MageshwariSingaravadivelou/Techflix/blob/main/data/Movies_list.xlsx)
- Click on the Search icon

Note:
- Recommend Movie will give 3 movies which is similar to the movie given as input
- Search Details will give the basic details of the movie

- Input: 1 Movie name
- Output: 3 Movies

### _Author_:
- Mageshwari Singaravadivelou
- P. Saimounika