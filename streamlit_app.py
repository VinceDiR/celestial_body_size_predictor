from numpy import False_
import pandas as pd
import streamlit as st
import xgboost as xgb
import matplotlib.pyplot as plt
from PIL import Image

st.image('images/known_asteroids.gif')

'''
## Asteroid Diameter Predictor
How well can we predict the size of an asteroid with Gradient Boosted Regression?

'''

bucket_name="ndir-metis-bucket"
path=f"gs://{bucket_name}/asteroid/processed_asteroid_data.csv"
data = pd.read_csv(path,
                   # storage_options={'token' : 'secrets.json'},
                    low_memory=False,
                    index_col=0)

show_df = st.sidebar.checkbox('Show Asteroid Data', value=True)

if show_df:
    st.dataframe(data)

model = xgb.Booster()
model.load_model("xgb_model.json")

