import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

conn = sqlite3.connect("database/vivino_v2.db")

st.set_page_config(page_title="Vivino les bons plans", layout="wide")
st.title(body="Vivino")
st.subheader(body="Analysis and probably some metrics if I managed to do it.")

SQL_Query = pd.read_sql("SELECT name, users_count FROM countries", conn)
st.write("Users by country")
df = pd.DataFrame(SQL_Query)
st.bar_chart(data=df, x="name", y="users_count")

chart1, chart2 = st.columns(2)

with chart1:
    st.subheader(body="10 wines to increase sales")
    ten_wines_to_increase = pd.read_sql_query(
        open("1 - 10_wines_to_increse_sales.sql", "r").read(),
        conn,
    )
    st.dataframe(ten_wines_to_increase, hide_index=True)

with chart2:
    st.subheader(body="Country to prioritize")
    country_to_prioritize = pd.read_sql_query(
        open("2 - Country_to_prioritize.sql", "r").read(), conn
    )
    st.dataframe(country_to_prioritize, hide_index=True)

st.subheader(body="Price for the best winery")
price_for_the_best_winery = pd.read_sql_query(
    open("3 - Price_to_best_winery.sql", "r").read(),
    conn,
)
st.dataframe(price_for_the_best_winery, hide_index=True, width=1700)

st.subheader(body="Wine Keywords by 10 users")
wine_keywords_by_10_users = pd.read_sql_query(
    open("4 - Wine_keywords_by_10_users.sql", "r").read(), conn
)
st.dataframe(wine_keywords_by_10_users, hide_index=True, use_container_width=True)


chart3, chart4 = st.columns(2)

with chart3:
    st.subheader(body="Grapes and wines")
    grapes_and_wines = pd.read_sql_query(
        open("5 - Grapes_and_wines.sql", "r").read(), conn
    )
    st.dataframe(grapes_and_wines, hide_index=True)

with chart4:
    st.subheader(body="Country Leaderbord")
    country_leaderbord = pd.read_sql_query(
        open("6 - Country_leaderboard.sql", "r").read(), conn
    )
    st.dataframe(country_leaderbord, hide_index=True)

chart5, chart6 = st.columns(2)

with chart5:
    st.subheader(body="Country Leaderbord Vintages")
    country_leaderbord_vintages = pd.read_sql_query(
        open("6.1 - Country_leaderboard_vintage.sql", "r").read(), conn
    )
    st.dataframe(country_leaderbord_vintages, hide_index=True)

with chart6:
    st.subheader(body="Top 5 Carbent Sauvignon like")
    top_5_Cabernet_Sauvignon_like = pd.read_sql_query(
        open("7 - Top_5_for_Sauvignon.sql", "r").read(), conn
    )
    st.dataframe(top_5_Cabernet_Sauvignon_like, hide_index=True)
