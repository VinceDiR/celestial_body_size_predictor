# NBA Scoring Predictor #
### By: Nate DiRenzo 

## Statement of Need:

As sports betting continues to grow in popularity, bettors seek out better tools to inform to inform their strategies. The purpose of this project is to make a scoring prediction model created during the Linear Regression and Web Scraping Module publicly available.
<br></br>
## Goal:
The goal of this project is to productionize a model that predicts NBA scoring performances for individual players. This is an extension of the work done in the Linear Regression and Web Scraping module, and the goal is to expand on that model, update it on a daily basis, and make it publicly available using tools like Google Cloud Platform and Streamlit.
<br></br>
## Success Metrics:
The metric for success is whether or not the model functions in production 
<br></br>
## Data Description:
Data is collected via webscraping the betting website, and the nba-api. Betting data and player stats need to be updated daily.
<br></br>
## Tools:
- Cloud Hosted Database or MongoDB
- BeatufilSoup and Selenium for Scraping
- NBA API for collecting player, team, game stats
- Google Colab for all-cloud
- Keras/Tensorflow/Scikit Learn
- Streamlit for hosting
<br></br>
## Models:
- Linear Regression Model
- RNN/LSTM
<br></br>
## MVP Goal:
Basic implimentation of the model running on local machine, and deployed to streamlit. From there, I can work on expanding the data and moving the entire pipeline into the cloud.
