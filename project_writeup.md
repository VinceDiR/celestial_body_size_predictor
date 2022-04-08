# Asteroid Diameter Predictor App

Nate DiRenzo

## Abstract

The goal of this project was to create a publicly available application for predicting the size of asteroids. To accomplish this, I used a large dataset from NASA's Jet Proopulsion Laboratory, munged it down to a managable size with PySpark, stored the output in Google Cloud Storage, and created a model to deploy on a Streamlit application using XGBoost. The purpose of the project was to showcase data engineering skills by not storing any data on my local machine, and to make a useful tool available to scientists and amateur astronomers alike.

## Design

The design of this project was a proof of concept. I used a relatively clean dataset that, while large, was not massive. I hacked it down to size with basic pySpark queries, and stored the results in a simple object storage service (Google Cloud Storage) that was suboptimal. I created a simple model with XGBoost, and deployed a simple web application using Streamlit. Every step of this pipeline could be improved upon, but the pipeline exists, which was the goal of the project.

## Data

The [dataset](https://ssd.jpl.nasa.gov/tools/sbdb_query.html) is used with permission by NASA's Jet Propulsion Laboratory at CalTech. It contains 1.2 million asteroids observed in our solar system with 20+ features:

### Feature Info

- a: semi-major axis (au)
- e: eccentricity
- i: inclination with respect to ecliptic plane
- om: longitude of the ascending node
- w: argument of perihelion
- q: perihelion distance (au)
- ad: aphelion distance (au)
- per_y: orbital period (years)
- data_arc: span of recorded data (days)
- condition_code: orbital condition code
- n_obs_used: number of observations used
- H: absolute magnitude parameter
- neo: near-earth object
- pha: physically hazardous object
- diameter: diameter (target variable)
- extent: Object bi/tri axial ellipsoid dimensions(Km)
- albedo: geometric albedo
- rot_per: rotation period (hours)
- GM: gravitational parameter. Product of mass and gravitational constant
- BV: Color index B-V magnitude difference
- UB: Color index U-B magnitude difference
- IR: Color index I-R magnitude difference
- specB: Spectral taxonomic type(SMASSII)
- specT: Spectral taxonomic type (Tholen)
- G: Magnitude slope parameter
- moid: Earth minimum orbit intersection distance
- class: asteroid orbit class
- n: mean motion (degrees/day)
- per: orbital period (days)
- ma: mean ananomly (degrees)

## Pipeline

### Data Wrangling with PySpark

1. Eliminating NaN/Infinity Values
2. Dropping unnecessary columns
3. Coercing all data types into numeric
4. Encoding categorical columns column

### Data Storage

- Google Cloud Storage

### Modelling
  
- PySpark Gradient Boosted Tree
- Scikit-Learn Preprocessing
- XGBoost Gradient Boosted Regressor

### Model Evaluation and Selection
  
- PySpark GridSearch
- XGBoost Evaluation & Early Stopping

### Selected Metrics

- Mean Absolute Error
- R2 Score

### Final XGBoost Model

#### Test Set Metric Scores

- Mean Absolute Error: .97 (kilometers)
- R2 Score: .79

## Frontend Tools

- **Numpy**, **Google Cloud**, **Pandas**, and **PySpark** for data ingestion & manipulation.
- **Scikit-learn**, **PySpark**, and **XGBoost** for modeling and evaluation
- **Matplotlib** and **Seaborn** for visualization
- **Streamlit** for Frontend

## Communication

- See [PDF](https://github.com/NateDiR/celestial_body_size_predictor/blob/main/Asteroid%20Predictor%20Presentation.pdf) of slides.

- See [Streamlit Application](https://share.streamlit.io/natedir/celestial_body_size_predictor/main)
