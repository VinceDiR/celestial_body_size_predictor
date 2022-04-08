from re import I
import pandas as pd
import streamlit as st
import xgboost as xgb
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
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

st.header('Features to be Removed')
st.write(
    """
    1. Longitude of Ascending Node (deg)
    2. Argument of Perihelion (deg)
    3. Mean Anomaly (deg)
    4. Oribtal Period (years)
    """
)

st.header('Features to be Encoded')
st.write(
    """
    1. Condition Code
    2. Class"""
)

st.header('Train/Test Split')
col3,col4 = st.columns(2)
with col3:
    st.metric(label='Train Set', value=.75)
with col4:
    st.metric(label='Test Set', value=.25)


model_data = data2.drop(columns=['Longitude of Ascending Node (deg)', 'Argument of Perihelion (deg)', 'Mean Anomaly (deg)', 'Orbital Period (years)', 'Name'])
model_data = pd.get_dummies(model_data, prefix='class', columns=['Asteroid Orbit Class'])
model_data = pd.get_dummies(model_data, prefix='condition_code', columns=['Condition Code'], drop_first=False)
X, y = model_data.drop('Diameter (km)',axis=1), model_data['Diameter (km)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=13)



if st.checkbox('Pre-process Data'):
        col5,col6 = st.columns(2)
        with col5:
            st.metric(label='Train Set Size', value=len(X_train))
        with col6:
            st.metric(label='Test Set Size', value=len(X_test))
        st.dataframe(X_train)

gbm = xgb.XGBRegressor( 
                n_estimators=30000,
                max_depth=10,
                objective="reg:squarederror", 
                learning_rate=.1, 
                subsample=1,
                min_child_weight=1,
                colsample_bytree=.8
                )

eval_set=[(X_train,y_train),(X_test,y_test)]

gbm.fit( 
    X_train, y_train, 
    eval_set=eval_set,
    eval_metric='rmse',
    early_stopping_rounds=20,
    verbose=False
    )

y_train_pred = gbm.predict(X_train, ntree_limit=gbm.best_ntree_limit)
y_test_pred = gbm.predict(X_test, ntree_limit=gbm.best_ntree_limit)
r2 = r2_score(y_test, y_test_pred)
mae = mean_absolute_error(y_test, y_test_pred)
if st.checkbox('Train Model'):
    col7, col8 = st.columns(2)
    with col7:
        st.metric(label='Test MAE', value=mae)
    with col8:
        st.metric(label='Test R2', value=r2)


actual_df = pd.DataFrame(y_test)
actual_df.reset_index(drop=True, inplace=True)

preds_df = pd.DataFrame(y_test_pred)
preds_df.reset_index(drop=True, inplace=True)

maren = pd.concat([actual_df, preds_df], axis=1)
maren.columns = ['Actual', 'Predicted']

if st.checkbox('See Predictions'):
    st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
    st.dataframe(maren)
        
