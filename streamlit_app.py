import pandas as pd
import streamlit as st
import xgboost as xgb
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from google.oauth2 import service_account

credentials = st.secrets['gcp_service_account']

credentials = service_account.Credentials.from_service_account_info(
    credentials, scopes=["https://www.googleapis.com/auth/cloud-platform"])

st.title('Asteroid Diameter Predictor')
st.header('There are over 1,000,000 asteroids in our solar system.')
st.image('images/known_asteroids.gif')

bucket_name="ndir-metis-bucket"
path=f"gs://{bucket_name}/asteroid/processed_asteroid_data.csv"
data = pd.read_csv(path,
                    storage_options={'token' : credentials},
                    low_memory=False,
                    index_col=0)

data = data.rename(columns={'a': 'Semi-major axis (AU)',
                            'e': 'Eccentricity',
                            'i': 'Inclination (deg)',
                            'om' : 'Longitude of Ascending Node (deg)',
                            'w' : 'Argument of Perihelion (deg)',
                            'q' : 'Perihelion Distance (AU)',
                            'ad' : 'Aphelion Distance (AU)',
                            'per_y' : 'Orbital Period (years)',
                            'data_arc' : 'Span of Data (days)',
                            'n_obs_used' : 'Number of Observations Used',
                            'H' : 'Absolute Magnitude',
                            'neo' : 'Near Earth Object',
                            'pha' : 'Potentially Hazardous Asteroid',
                            'extent' : 'Object Dimensions',
                            'condition_code' : 'Condition Code',
                            'diameter' : 'Diameter (km)',
                            'moid' : 'Earth Minimum Orbit Intersection Distance (km)',
                            'class' : 'Asteroid Orbit Class',
                            'n' : 'Mean Motion (deg/day)',
                            'name' : 'Name',
                            'per' : 'Orbital Period (days)',
                            'ma' : 'Mean Anomaly (deg)'
                            })

data_display = data[['Name', 'Diameter (km)']]

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Display a static table
st.table(data_display.head(10))


st.header('But most are relatively small.')

data2 = data[data['Diameter (km)'] < np.quantile(data['Diameter (km)'], 0.99)]

col1, col2 = st.columns(2)

with col1:
    st.subheader('All Known Asteroids')
    st.pyplot(sns.displot(data['Diameter (km)']))

with col2:
    st.subheader('99th Percentile')
    st.pyplot(sns.displot(data2['Diameter (km)']))

st.header("Let's see if we can predict the diameter of asteroids using Gradient Boosted Regression")
st.subheader("""The Data, courtesy of [NASA's Jet Propulsion Laboratory](https://ssd.jpl.nasa.gov/tools/sbdb_query.html)""")

hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
st.dataframe(data)

fig, ax = plt.subplots()
ax = sns.heatmap(data.corr(), annot=True, fmt='.2f', cmap='coolwarm', cbar=False, yticklabels=False, xticklabels=False, annot_kws={"size": 6})
st.pyplot(fig, width='auto', transparent=True)
st.caption('Correlation between the features')