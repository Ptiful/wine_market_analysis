import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as pxµ
import altair as alt

conn = sqlite3.connect("database/vivino_v2.db")

# Title and headers
st.set_page_config(page_title="Vivino les bons plans", layout="wide")
st.title(body="Vivino 🍇")
st.subheader(body="Analysis and probably some metrics if I managed to do it.")

chart7, chart8 = st.columns(2)
# Bar Chart

SQL_query = pd.read_sql(
    "SELECT name, users_count FROM countries ORDER BY users_count ASC", conn
)
# st.write("Users by country")
# df = pd.DataFrame(SQL_query)
# st.bar_chart(data=df, x="name", y="users_count")
# st.markdown(body="Global amount of users by country.")

# q1 = open("1 - 10_wines_to_increse_sales.sql", "r").read()
# q1 = pd.read_sql_query(q1, conn)

# st.write(data)
df = pd.DataFrame(SQL_query)

# st.write(df)

test = (
    alt.Chart(
        df,
        title="Global amount of users per country",
    )
    .mark_bar()
    .encode(
        x=alt.X("name", sort=("-y")),
        y="users_count",
    )
)

st.altair_chart(test, use_container_width=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Making charts1
chart1, chart2 = st.columns(2)

with chart1:
    st.subheader(body="10 wines to increase sales")
    ten_wines_to_increase = pd.read_sql_query(
        open("1 - 10_wines_to_increse_sales.sql", "r").read(),
        conn,
    )
    st.dataframe(ten_wines_to_increase, hide_index=True)
    st.markdown(
        body="You'll find here ten wines I think you need to focus on to increase your sells."
    )


# Making charts2
with chart2:
    st.subheader(body="Country to prioritize")
    country_to_prioritize = pd.read_sql_query(
        open("2 - Country_to_prioritize.sql", "r").read(), conn
    )
    st.dataframe(country_to_prioritize, hide_index=True)
    st.markdown(
        body=" Here, you'll be happy to see which country you need to prioritize so you can boomin."
    )
st.markdown("<hr>", unsafe_allow_html=True)


# Making charts3
st.subheader(body="Price for the best winery")
price_for_the_best_winery = pd.read_sql_query(
    open("3 - Price_to_best_winery.sql", "r").read(),
    conn,
)
st.dataframe(price_for_the_best_winery, hide_index=True, width=1700)
st.markdown(body="This winery has the best ratings average amongs all your wines.")
st.markdown("<hr>", unsafe_allow_html=True)

# Making chart4
st.subheader(body="Arome")
wine_keywords_by_10_users = pd.read_sql_query(
    open("4 - Wine_keywords_by_10_users.sql", "r").read(), conn
)
st.dataframe(wine_keywords_by_10_users, hide_index=True, use_container_width=True)
st.markdown(
    body=" These are all the wines where you can find the same taste, like Coffee Toast Green apple cream and citrus"
)
st.markdown("<hr>", unsafe_allow_html=True)

# Making charts5
chart3, chart4 = st.columns(2)

with chart3:
    st.subheader(body="Grapes and wines")
    grapes_and_wines = pd.read_sql_query(
        open("5 - Grapes_and_wines.sql", "r").read(), conn
    )
    st.dataframe(grapes_and_wines, hide_index=True)
    st.markdown(body="You'll find here all your best grapes and wines from all time !")
st.markdown("<hr>", unsafe_allow_html=True)
# Making charts6
with chart4:
    st.subheader(body="Country Leaderbord")
    country_leaderbord = pd.read_sql_query(
        open("6 - Country_leaderboard.sql", "r").read(), conn
    )
    st.dataframe(country_leaderbord, hide_index=True)
    st.markdown(body="That would be the average wine rating by country.")

# Making charts7
chart5, chart6 = st.columns(2)

with chart5:
    st.subheader(body="Country Leaderbord Vintages")
    country_leaderbord_vintages = pd.read_sql_query(
        open("6.1 - Country_leaderboard_vintage.sql", "r").read(), conn
    )
    st.dataframe(country_leaderbord_vintages, hide_index=True)
    st.markdown(body="That would be the average vintage wine rating by country.")

# Making charts8
with chart6:
    st.subheader(body="Top 5 Carbent Sauvignon like")
    top_5_Cabernet_Sauvignon_like = pd.read_sql_query(
        open("7 - Top_5_for_Sauvignon.sql", "r").read(), conn
    )
    st.dataframe(top_5_Cabernet_Sauvignon_like, hide_index=True)
    st.markdown(
        body="These are all vines that are Carbernet Sauvignon like. They are feeling the same as this wonderfull wine. You can definitly propose these wines to your richest client you is tired to dring Cabernet Sauvignon."
    )
st.markdown("<hr>", unsafe_allow_html=True)
