import streamlit as st 
from streamlit_option_menu import option_menu
import  Prediction, contact,Introduction
import os



class MultiApp:
    st.write(os.getcwd())
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        
        with st.sidebar:        
            app = option_menu(
                menu_title='Main Menu ',
                options=['Introduction','Prediction','Contact'],
                icons=['house-fill','chat-fill','person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'#0E1117'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#FFCCCB"},
        "nav-link-selected": {"background-color": "#ff4b4b"},}
                
            )
        
        if app == "Introduction":
            Introduction.app()
        if app == "Prediction":
            Prediction.app()    
        if app == "Contact":
            contact.app()

    run()
             
