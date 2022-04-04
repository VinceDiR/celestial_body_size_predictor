# Celestial Body Size Predictor

The goal of this project is to create a model that can predict the size of celestial objects in our solar system with some degree of accuracy, and make it publicly available via a streamlit web app.

I have succeeded in getting my dataset stored in Google Cloud Storage, and creating a data preprocessing pipeline using PySpark.

I've run into some technical issues creating the model with PySpark, and am working to resolve those so I can move onto deploying it with Streamlit.

If the problem persists, I may roll my data processing pipeline back to pre-vectorization so I can export the results for use in a sci-kit learn model, and then proceed to streamlit.

[MVP Script Here](/Users/nathanieldirenzo/Documents/GitHub/celestial_body_size_predictor/asteroid_size_predictor.ipynb)

