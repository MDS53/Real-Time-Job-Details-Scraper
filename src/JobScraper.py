     
import streamlit as st
import pandas as pd
import Webscraping as w
from datetime import datetime
import os
import DataAnalysis as da


def page1():
    """This function returns Data files containing .csv,.json files from Webscraping package"""
    current_datetime = datetime.now()
    formatted_date =current_datetime.strftime("%d-%m-%Y ")
    fname=f"{ab} {formatted_date}"
    filename = f"{ab} {formatted_date}.csv"
   
    if not ab:
        st.error("Please enter some text.")
    
    else:
        st.success(f"User entered: {ab}") 
        if os.path.isfile(filename):
            with st.spinner("Kindly wait, the content is on its way!..."):
                print(f"The file {filename} is present in the current directory.")
                #global df
                df=pd.read_csv(f"{ab} {formatted_date}.csv")
                df.drop(df.columns[0],axis=1,inplace=True)
                st.dataframe(df)
                st.download_button('Download Csv file', df.to_csv(),file_name=f"{fname}.csv")
                st.download_button('Download Json file', df.to_json(),file_name=f"{fname}.json")
            st.success("Loading completed!")
            st.snow()
            st.balloons()
        else:
            print(f"The file {filename} is not present in the current directory.")
            with st.spinner("Kindly wait, the content is on its way!..."):
                C=w.Webscraping(ab)
                df=pd.read_csv(f"{ab} {formatted_date}.csv")
                df.drop(df.columns[0],axis=1,inplace=True)
                st.dataframe(df)
                st.download_button('Download Csv file', df.to_csv(),file_name=f"{fname}.csv")
                st.download_button('Download Json file', df.to_json(),file_name=f"{fname}.json")
            st.success("Loading completed!")
            st.snow()
            st.balloons()
        if st.button("Explore Statistical Insights"):
        # Setting a session state variable to indicate the page change
             st.session_state.page_number = 2
    

def page2():
    """This function returns Data file statistical insights  from DataAnalysis package"""
    current_datetime = datetime.now()
    formatted_date =current_datetime.strftime("%d-%m-%Y ")
    
    df=pd.read_csv(f"{ab} {formatted_date}.csv")
    df.drop(df.columns[0],axis=1,inplace=True)
    st.header("Sample data")
    st.dataframe(df.tail(5))
    analysis=da.Data_Analysis(df)
    st.header("")
    st.header("")
    st.header("")
    st.write("Note : Piecharts are made on Top30 records from grouped data ")
    st.header("")
    if st.button("Go to Previous Page"):
        # Setting a session state variable to indicate the page change
        st.session_state.page_number = 1#This will through you to page1




def main():
    st.title('Real-Time Job Details Scraper')
    st.header('Please enter Job title and get data of it')

    current_datetime = datetime.now()
    formatted_date =current_datetime.strftime("%d-%m-%Y ")
    
    global ab
    ab = st.text_input("Enter Job Title")
    #st.write("You've entered :",ab)
    
  
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 1
    if st.session_state.page_number == 1:
        page1()
    elif st.session_state.page_number == 2:
        page2()
        

if __name__ == "__main__":
    main()
    



