# Celestial Body Size Predictor #
### By: Nate DiRenzo 

## Statement of Need:

Potentially Hazard Objects (PHO) are near-Earth objects with an orbit that can bring them within close proximity to the planet, and large enough to cause significant damage in the event of an impact.  

Asteroids larger than 35 meters in daimater can pose a threat to a city or town. However, the diameter of most small celestial objects is not well determined, as they are usually estimated using brightness and distinace, as opposed to direct radar measurements.  

Because the true size of most celestial objects is not well determined, we will strive to produce a model that can accurately estimate the diameter of objects in space, given a set of easily observable features.
<br></br>
## Goal:
The goal of this project is to productionize a model that predicts the diameter of celestial objects with some degree of accuracy. To do so, we will store a database of 800,000 measurements of celesrial objects in MongoDB, create a model with Python, and a front-end web application with Streamlit. As a further goal, I would like to containerize the script and web application using Docker.
<br></br>
## Success Metrics:
The metric for success is whether or not the model functions in production, and to a lesser extent the accuracy of the model at predicting size of celestial objects. 
<br></br>
## Data Description:
The data is taken from the Jet Propulsion Laboratory at the California Institute of Technology. The Small-Body Database contains 1.2million entries with measurements of objects in our solar system. 
<br></br>
## Tools:
- MongoDB Atlas for Data Warehousing
- Google Colab for Scripting
- Spark for Modelling
- Streamlit for Frontend Application
- Docker for Containerization
<br></br>
## Models:
- Linear Regression with pySpark
<br></br>
## MVP Goal:
Basic implimentation of the model running on local machine, and deployed to streamlit. From there, I can work on expanding the data and moving the entire pipeline into the cloud.
