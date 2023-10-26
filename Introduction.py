import streamlit as st 
import main
def app():
    st.markdown('# Travel Package Purchase Prediction')
    st.markdown("----")
    st.markdown('<h2>Introduction</h2>', unsafe_allow_html=True)
    st.markdown("The goal of the project is to create a data-driven prediction engine that can accurately anticipate , if the potential clients are likely to buy trip package  potential . The purpose of this classification model is to increase customer happiness, optimize operational procedures, and personalize travel packages to meet the needs of different travelers. ")
    st.markdown("The travel business may increase income and acquire a competitive edge in the market by utilizing insights from consumer demographics, historical preferences, seasonal patterns, and marketing data.")
    st.markdown('<h2>Problem Statement With Objectives</h2>', unsafe_allow_html=True)
    st.markdown("To predict which customer is more likely to purchase the newly introduced travel package")
    st.markdown("Which variables are most significant?")
    st.markdown("Which segment of customers should be targeted more?")
    st.markdown("utilization of  customers' data and information to provide actionable recommendations to the policymaker and Marketing Team regarding the newly introduced travel package. ")
    st.markdown('<h2>Label Encoding</h2>', unsafe_allow_html=True)
    st.markdown("Type of contact:  0 = company invited , 1 = self-invited.")
    st.markdown("Gender: 0 = Female, 1 = Male")
    st.markdown("Passport: 0 = No, 1 = Yes")
