import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import datetime
import logging
import DataAnalysis as da
import streamlit as st
class Webscraping:
    logging.basicConfig(filename='Webscraping.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')
    try:
        def __init__(self,Role):
            #logging.basicConfig(filename='Webscraping.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')
            try:
                self.Role=Role
                logging.info('Webscraping constructor started')
                self.Role,self.df=self.get_Job_details_df(self.Role)
                self.Saving_the_file(self.df,self.Rol)
                #self.analysis=da.DataAnalysiscopy(self.df)
                logging.info('Data saved successfully')
            except Exception as e:
                logging.debug(e)
                logging.exception(e)
                #print(e)
        def get_response(self,Rol,i):
            """This function takes Role and i which is page number is a iterator returns the beutified response using beautifulsoup """
            try:
                self.i=i
                self.Rol=Rol
                self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                self.url=f"https://www.ambitionbox.com/jobs/search?tag={self.Rol}&page={self.i}"
                self.response = r.get(self.url, headers=self.headers)
                self.Html_data=bs(self.response.text,"html.parser")
                logging.info('Response sent successfully')
                return self.Html_data
            except Exception as e:
                logging.debug(e)
                logging.exception(e,'At get_response()')
                #print(e)
                
        def get_Job_details_df(self,Role):
            """This function returns a dataframe containing the information about the job details"""
            try:
                logging.info('get_Job_details_df() started')
                self.k=10
                self.columns=["Role","Company_Name","Rating","Reviews","Experience","Location","Skill","Posted","Posted_on","Job_link","Company_info"]
                self.df= pd.DataFrame(columns=self.columns)
                self.Rol=Role
                for self.i in range(1,6000):
                    try:
                        self.Html_data=self.get_response(self.Rol,self.i)
                        self.big_box=self.Html_data.find_all('div',id='jobsList')[0]
                        #print(self.big_box)
                        if self.k==10:
                            self.k=0 
                            for self.j in self.big_box.find_all('div',class_='jobsInfoCardCont'):
                                #print("Hello")  
                                self.company_name=self.j.find('div',class_='info').find_all('div')[0].p.text.replace('\n','').replace('\t','')
                                self.k+=1
                                self.role,self.rating,self.reviews,self.Experience=self.get_job_info(self.j) 
                                self.skill=self.get_skills(self.j)
                                self.Location=self.get_location(self.j,self.big_box)
                                #print('Hello')
                                self.posted,self.link,self.posted_on,self.Apply_job_link,self.Company_link,self.Company_info,self.Company_direct_link=self.get_apply_info(self.j)
                                self.new_record1={"Role":self.role,"Company_Name":self.company_name,"Rating":self.rating,"Reviews":self.reviews,"Experience":self.Experience,"Location":self.Location,"Skill":self.skill,"Posted":self.posted,"Posted_on":self.posted_on,"Job_link":self.Apply_job_link,"Company_info":self.Company_info,"Company_direct_link":self.Company_direct_link}
                                self.new_record1=[self.new_record1]
                                #print(self.new_record1)
                                self.df = pd.concat([self.df, pd.DataFrame(self.new_record1)], ignore_index=True)
                                #print(self.df)
                        else:
                        
                            break
                    except : 
                        continue
                logging.info("get_Job_details_df() successfully completed")
                return self.Rol,self.df
            except Exception as e:
                pass
                #print(e)
            
        def Saving_the_file(self,df,Rol):
            """This function takes Dataframe and Role and saves the dataframe to a csv and json file """
            try:
                logging.info('Saving_the_file() started')
                self.df=df
                self.Rol=Rol
                self.current_datetime = datetime.now()
                self.formatted_date = self.current_datetime.strftime("%d-%m-%Y ")
                self.formatted_time = self.current_datetime.strftime("%H:%M:%S")
                self.df.to_csv(f"{self.Rol} {self.formatted_date}.csv")
                self.df.to_json(f"{self.Rol}_{self.formatted_date}.json")
                logging.info('Saving_the_file() completed successfully')
            except Exception as e:
                logging.debug(e,'at Saving_the_file()')
                logging.exception(e)
                #print(e)
        def get_location(self,j,big_box):
            """This function takes j value which is iterator from big_box.find_all('div',class_='jobsInfoCardCont') and returns Location"""
            try:
                logging.info('get_location() started')
                self.j=j
                self.bigbox=big_box
                self.q=self.j.find('div',class_='other-info').find_all('p')[1].text.replace('\n','').replace('\t','')
                if self.q.endswith("(AmbitionBox estimate)"):
                    self.Location=j.find('div',class_='other-info').find_all('p')[2].text.replace('\n','').replace('\t','')
                    self.y=self.big_box.find_all('div',class_='jobsInfoCardCont')[0].find('div',class_='other-info').find_all('div')
                    self.title=str(self.y[len(self.y)-1])
                    self.skill=self.title[self.title.find('title=')+7:self.title.find(">")]
                else:
                    self.Location=j.find('div',class_='other-info').find_all('p')[1].text.replace('\n','').replace('\t','')
                    logging.info('get_location() completed successfully')
                return self.Location
            except Exception as e:
                logging.debug(e,'at get_location()')
                logging.exception(e)
                #print(e)
        def get_apply_info(self,j):
            """This function takes j value which is iterator from big_box.find_all('div',class_='jobsInfoCardCont') and returns posted,link,posted_on,Apply_job_link,Company_link,Company_info,Company_direct_link"""
            try:
                logging.info('get_apply_info() started')
                self.j=j
                #print('Hello3')
                self.posted=self.j.find('div',class_='other-info').span.text
                self.link=str(self.j.find('div',class_='info').find_all('meta')[1])
                self.posted_on=self.j.find('div',class_='other-info').find_all('span')[2].text
                self.Apply_job_link=self.link[self.link.find('=')+2:self.link.find('" itemprop="url"')]
                #print("Hello2")
                self.Company_link=self.Apply_job_link[self.Apply_job_link.find('/jobs')+6:self.Apply_job_link.find('-jobs?')]
                self.Company_info=f"https://www.ambitionbox.com/overview/{self.Company_link}-overview"
                self.Company_direct_link=f"https://www.{self.Company_link}.com"
                logging.info('get_apply_info() completed successfully')
                return self.posted,self.link,self.posted_on,self.Apply_job_link,self.Company_link,self.Company_info,self.Company_direct_link
            except Exception as e:
                logging.debug(e,'at get_apply_info()')
                logging.exception(e)
                #print(e)
        def get_job_info(self,j):
            """This function takes j value which is iterator from big_box.find_all('div',class_='jobsInfoCardCont') and returns role,rating,reviews,Experience"""
            try:
                logging.info('get_job_info() started')
                self.j=j
                self.a=str(j.find('div',class_='info').find_all('meta')[2])
                self.role=self.a[self.a.find('"')+1:self.a.find('itemprop')-2]
                self.rating=self.j.find('div',class_='info').find_all('div')[1].a.text
                self.reviews=self.j.find('div',class_='info').find_all('div')[1].find_all('a')[1].text.replace('\n','').replace('\t','')
                self.reviews=self.reviews[1:self.reviews.find('Reviews')]
                self.Experience=self.j.find('div',class_='other-info').div.div.p.text.replace('\n','').replace('\t','')
                logging.info('get_job_info() completed successfully')
                return self.role,self.rating,self.reviews,self.Experience
            except Exception as e:
                logging.debug(e,'at get_job_info()')
                logging.exception(e)
                #print(e)
        def get_skills(self,j):
            """This function takes j value which is iterator from big_box.find_all('div',class_='jobsInfoCardCont') and return skills"""
            try:
                logging.info('get_skills() started')
                self.j=j
                self.title=str(self.j.find('div',class_='other-info').find_all('div')[3])
                self.skill=self.title[self.title.find('title=')+7:self.title.find(">")]
                logging.info('get_skills() completed successfully')
                return self.skill
            except Exception as e:
                logging.debug(e,'at get_skills()')
                logging.exception(e)
                #print(e)
        logging.info('Webscrapping class completed successfully')
    except Exception as e:
        logging.debug(e,'at At Webscrapping class')
        logging.exception(e)
        #print(e)
#C=Webscraping()
