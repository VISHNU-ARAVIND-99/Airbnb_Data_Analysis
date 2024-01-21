import streamlit as st
import plot as p


st.set_page_config(layout="wide")


st.title("Airbnb Data Analysis")
st.text('This is a web app allow exploration of Airbnb Data')

st.sidebar.title("Navigation")
side_bar_object = st.sidebar.radio("Pages", options=["About", "Price Analysis and Visualization"])

if side_bar_object == "About":
    st.subheader("About:")
    st.markdown("This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation,"
                " develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing"
                " variations, availability patterns, and location-based trends.")

if side_bar_object == "Price Analysis and Visualization":

    st.header("Price Analysis and Visualization")
    st.write("")
    st.write("")
    st.write("")

    ops1 = st.selectbox("Select any categorical data type", ['Room_type', 'Country', 'Property_type', 'Bed_type'])
    ops2 = st.selectbox("Select any price data type", ['Price', 'Security_deposit', 'Cleaning_fee', 'Review_Scores',
                                                       'Number_Of_Reviews', 'Accomodates'])
    if ops1 and ops2:
        st.pyplot(p.mean_count_plot(x=ops1, y=ops2))

