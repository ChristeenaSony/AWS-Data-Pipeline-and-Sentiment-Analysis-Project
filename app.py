# import streamlit as st
# import pandas as pd
# from sqlalchemy import create_engine

# # Function to fetch data from RDS PostgreSQL
# def get_data_from_rds():
#     # Replace with your actual database credentials
#     engine = create_engine('postgresql://postgres:RA6OJmLgFjxcySGCNxEk@database-1.czakiqaesl4k.ap-south-1.rds.amazonaws.com:5432/my_database')
    
#     # SQL query to fetch data from the 'news_articles' table
#     query = "SELECT * FROM news_articles;"
    
#     # Use pandas to execute the query and load the data into a DataFrame
#     df = pd.read_sql(query, engine)
#     return df

# # Load data from RDS
# st.title("News Sentiment Dashboard")
# data = get_data_from_rds()

# # Display raw data as a table
# st.write("Raw News Data with Sentiment Scores")
# st.dataframe(data)

# # Optionally, add more charts or graphs to visualize sentiment
# st.write("Sentiment Distribution")

# # Assuming the 'sentiment_score' column contains sentiment scores
# if 'sentiment_score' in data.columns:
#     st.bar_chart(data['sentiment_score'])  # Create a bar chart for sentiment scores
# else:
#     st.write("No sentiment_score column found in the data.")


# import streamlit as st
# import pandas as pd
# from sqlalchemy import create_engine

# # Function to fetch data from RDS PostgreSQL
# def get_data_from_rds():
#     # Replace with your actual database credentials
#     engine = create_engine('postgresql://postgres:RA6OJmLgFjxcySGCNxEk@database-1.czakiqaesl4k.ap-south-1.rds.amazonaws.com:5432/my_database')
    
#     # SQL query to fetch data from the 'news_articles' table
#     query = "SELECT * FROM news_articles;"
    
#     # Use pandas to execute the query and load the data into a DataFrame
#     df = pd.read_sql(query, engine)
#     return df

# # Load data from RDS
# st.title("News Sentiment Dashboard")
# data = get_data_from_rds()

# # Function to create a color bar based on sentiment score
# def sentiment_color_bar(val):
#     if val > 0:
#         color = 'green'
#     elif val < 0:
#         color = 'red'
#     else:
#         color = 'gray'  # Neutral sentiment
#     return f'width: {abs(val) * 100}%; background-color: {color}; height: 20px'

# # Display raw data as a table with color bars
# st.write("Raw News Data with Sentiment Scores")
# styled_df = data.style.applymap(sentiment_color_bar, subset=['sentiment_score'])

# # Show the styled DataFrame
# st.dataframe(styled_df)

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Set the maximum number of cells allowed in Pandas Styler
pd.set_option("styler.render.max_elements", 446600)

# Function to fetch data from RDS PostgreSQL
def get_data_from_rds():
    # Replace with your actual database credentials
    engine = create_engine('postgresql://postgres:RA6OJmLgFjxcySGCNxEk@database-1.czakiqaesl4k.ap-south-1.rds.amazonaws.com:5432/my_database')
    
    # SQL query to fetch data from the 'news_articles' table
    query = "SELECT * FROM news_articles;"
    
    # Use pandas to execute the query and load the data into a DataFrame
    df = pd.read_sql(query, engine)
    return df

# Load data from RDS
st.title("News Sentiment Dashboard")
data = get_data_from_rds()

# Function to create a color bar based on sentiment score
def sentiment_color_bar(val):
    if val > 0:
        color = 'green'
    elif val < 0:
        color = 'red'
    else:
        color = 'gray'  # Neutral sentiment
    return f'width: {abs(val) * 100}%; background-color: {color}; height: 20px'

# Display raw data as a table with color bars
st.write("Raw News Data with Sentiment Scores")

# Limit the displayed rows to 1000 for better performance
styled_df = data.head(1000).style.applymap(sentiment_color_bar, subset=['sentiment_score'])

# Show the styled DataFrame
st.dataframe(styled_df)
