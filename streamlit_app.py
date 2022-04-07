import pandas as pd
import streamlit as st
import xgboost as xgb
import matplotlib.pyplot as plt
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp-service-account"]
)

st.image('images/known_asteroids.gif')

'''
## Asteroid Diameter Predictor
How well can we predict the size of an asteroid with Gradient Boosted Regression?

'''

bucket_name="ndir-metis-bucket"
path=f"gs://{bucket_name}/asteroid/processed_asteroid_data.csv"
data = pd.read_csv(path,
                    storage_options={'token' : credentials},
                    low_memory=False,
                    index_col=0)

show_df = st.sidebar.checkbox('Show Asteroid Data', value=True)

if show_df:
    st.dataframe(data)

model = xgb.Booster()
model.load_model("xgb_model.json")

