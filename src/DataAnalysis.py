import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import logging
import streamlit as st

class Data_Analysis:
    logging.basicConfig(filename="JobScraper_Log_file.log",level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')
    #This class is used as a package in webscraping.py file 
    def __init__(self,df):# Df will be replaced with role in the future.
        logging.info('Data_Analysis class entered successfully')
        try:
            logging.info('_init_() entered successfully')
            st.subheader('')
            self.colors = px.colors.sequential.Turbo[:30]
            self.df=df
            #self.df.drop(self.df.columns[0],axis=1,inplace=True)
            self.df_1=self.df.groupby(['Role'])['Company_Name'].value_counts().sort_values(ascending=False).reset_index()# Roles in company and its count
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            self.fig = ff.create_table(self.df_1[:30], height_constant=20)
            self.fig.update_layout(width=2000)  # Adjust the width value as needed
            st.subheader('Roles in company and Vacancies')
            st.dataframe(self.df_1)
            st.subheader('')
            
            self.fig = px.pie(self.df_1[:30], values= 'Vacancies' , names='Role', title='Roles in company and Vacancies',hover_data=['Company_Name'],color_discrete_sequence=self.colors,template='plotly_dark')  # Use a dark template for better contrast
            st.plotly_chart(self.fig)
            st.subheader('')
            st.subheader('') 
            
            
            st.subheader('Vacancies at Company with respect to Location')
            self.df_1=self.df.groupby(['Company_Name'])['Location'].value_counts().sort_values(ascending=False).reset_index()#count of openings at Company with respect to Location
              # Adjust the width value as needed
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)
            st.subheader('')
            
            self.fig = px.pie(self.df_1[:30], values= 'Vacancies' , names='Company_Name', title='Vacancies at Company with respect to Location',hover_data=['Location'],color_discrete_sequence=self.colors,template='plotly_dark')  # Use a dark template for better contrast
            st.plotly_chart(self.fig)
            st.subheader('')
            st.subheader('')
            
            
            st.subheader('Vacancies at Company with respect to Location,Role')
            self.df_1=self.df.groupby(['Company_Name'])[['Location','Role']].value_counts().sort_values(ascending=False).reset_index()#which role in which company and in which branch has more vacancies 
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)  # Adjust the width value as needed
            st.subheader('')
            st.subheader('')
            
            st.subheader('Vacancies at Company with respect to Location,Role,Experience')
            self.df_1=self.df.groupby(['Company_Name'])[['Location','Role','Experience']].value_counts().sort_values(ascending=False).reset_index()#which role in which company and in which branch has more vacancies with experience
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)  # Adjust the width value as needed
            st.subheader('')
            st.subheader('')
            
            st.subheader('Vacancies at Company with respect to Role,Experience')
            self.df_1=self.df.groupby(['Company_Name'])[['Role','Experience']].value_counts().sort_values(ascending=False).reset_index()#which role in which company and in which branch has more vacancies 
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)  # Adjust the width value as needed
            st.subheader('')
            st.subheader('')
            
            
            st.subheader('Vacancies at Company with respect to Experience')
            self.df_1=self.df.groupby(['Experience'])[['Company_Name']].value_counts().sort_values(ascending=False).reset_index()#Specific company is hiring for specific role with specific Experience , it can be freshers, less experienced, more experienced at specific location
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)
            st.subheader('')
            
            self.fig = px.pie(self.df_1[:30], values= 'Vacancies' , names='Company_Name', title='Vacancies at Company with respect to Experience',hover_data=['Experience'],color_discrete_sequence=self.colors,template='plotly_dark')  # Use a dark template for better contrast
            st.plotly_chart(self.fig)
            st.subheader('')
            st.subheader('')
            
            
            st.subheader('Vacancies at Company with respect to Role,Experience,Location')
            self.df_1=self.df.groupby(['Experience'])[['Location','Role','Company_Name','Rating']].value_counts().sort_values(ascending=False).reset_index()#which city has more vacancies with respect to experience
          # Adjust the width value as needed
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)
            st.subheader('')
            
            self.fig = px.pie(self.df_1[:30], values= 'Vacancies' , names='Experience', title='Vacancies with respect to Role,Experience',hover_data=['Role'],color_discrete_sequence=self.colors,template='plotly_dark')  # Use a dark template for better contrast
            st.plotly_chart(self.fig)
            st.subheader('')
            st.subheader('')
            
            
            st.subheader('Vacancies with respect to Role,Experience')
            self.df_1=self.df.groupby(['Experience'])[['Role']].value_counts().sort_values(ascending=False).reset_index()#which role has more vacancies for freshers, Less experienced, and more experienced
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)  # Adjust the width value as needed
            st.subheader('')
            st.subheader('')
            
            
            st.subheader('Vacancies at company with respect to Role,Experience and company Rating')
            self.df_1=self.df.groupby(['Experience'])[['Role','Company_Name','Rating']].value_counts().sort_values(ascending=False).reset_index()#Specific company is hiring for specific role with specific Experience , it can be freshers, less experienced, more experienced
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)
            st.subheader('')
            st.subheader('')
            
            
            st.subheader('Vacancies at companya at specific location with respect to Role,Experience and company Rating')
            self.df_1=self.df.groupby(['Experience'])[['Role','Location','Company_Name','Rating']].value_counts().sort_values(ascending=False).reset_index()#Specific company is hiring for specific role with specific Experience , it can be freshers, less experienced, more experienced at specific location
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)
            st.subheader('')
            st.subheader('')
            
            
            st.subheader('Vacancies at specific location of specific company with respect to Role,Experience and Company Rating')
            self.df_1=self.df.groupby(['Location'])[['Experience','Role','Company_Name','Rating']].value_counts().sort_values(ascending=False).reset_index()#Specific Location in specific company with specific Experience
            self.df_1.rename(columns={'count': 'Vacancies'}, inplace=True)
            st.dataframe(self.df_1)
            st.subheader('')
            
            self.fig = px.pie(self.df_1[:30], values= 'Vacancies' , names='Company_Name', title='Company and its Ratings',hover_data=['Rating'],color_discrete_sequence=self.colors,template='plotly_dark')  # Use a dark template for better contrast
            st.plotly_chart(self.fig)
            logging.info('Data_Analysis class completed successfully')
        except Exception as e:
            logging.debug(e,"at Data_Analysis class")
            logging.exception(e)
            #print(e)  
#c=Data_Analysis('Developer')


