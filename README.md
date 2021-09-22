## TECHFLIX - MOVIE RECOMMENDER SYSTEM

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
_Content Based Recommendation Model_

### _Workflow_:

![Image](https://github.com/MageshwariSingaravadivelou/Techflix/blob/main/workflow.png)

- Input: User Preference (API request)
- Output: 3 Movies
