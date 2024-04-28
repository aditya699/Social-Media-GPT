'''
Author     - Aditya Bhatt 22:11 PM 25-04-2024

Objective            -
1.Create a system to automate social media management.

Employee 1 Planning -
1.Julia Get's Information from  Internet
2.Jinny Your AI Writer
3.Jane your AI Editor
4.John is your Artist

Julia ->Jinny->Jane ->John

AI System By Aditya
'''
import os
import json
import requests
import streamlit as st
from langchain.adapters.openai import convert_openai_messages
from langchain_community.chat_models import ChatOpenAI
from tavily import TavilyClient
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from openai import AzureOpenAI



# run tavily search
OPENAI_API_KEY ="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"
os.environ['OPENAI_API_KEY']="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"


def main():
        st.title("Social MediaGPT A AI COMPANY WITH 0 EMPLOYEES")
        st.sidebar.image("robots_working_on_social_media.png","Made By Aditya Bhatt")
        st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/adityaabhatt/)")
        st.sidebar.markdown("[About Me](https://aiwithaditya.odoo.com/)")
        

        title = st.text_input('Enter topic on which you want to create a post:')
        mood_options = ["Funny", "Casual", "Formal"]
        tone_of_post=st.selectbox("Select mood of post", mood_options)
        
        

        if st.button("Start the Magic"):
            st.header("Julia(Your AI Researcher is at it)...")
            st.image("https://chracters.blob.core.windows.net/images/Julia.PNG")
            try:
                #AI Agent -1 Researcher
                st.write("Julia is searching over the internet...")
                client = TavilyClient(api_key="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")
                content = client.search(title, search_depth="advanced")["results"]
                # setup prompt
                prompt = [{
                    "role": "system",
                    "content":  f'You are an AI critical thinker research assistant. '\
                                f'Your sole purpose is to write well written, critically acclaimed,'\
                                f'objective and structured reports on given text.'
                }, {
                    "role": "user",
                    "content": f'Information: """{content}"""\n\n' \
                            f'Using the above information, answer the following'\
                            f'query: "{title}" in a detailed report --'\
                            f'Please use MLA format and markdown syntax.'
                }]

                st.write("Julia is still working.... what you thought research is an easy task...😄")

                # run gpt-3.5
                lc_messages = convert_openai_messages(prompt)
                report = ChatOpenAI(model='gpt-3.5-turbo',openai_api_key=OPENAI_API_KEY).invoke(lc_messages).content

                # print report
                st.write("Here the report which Julia has made")
                st.write(report)
    
            except Exception as e:
                  st.write("Julia is not working as expected",e)

                

                 #Agent -2 Simi Writer
            st.header("Jinny your Writer is  Writing the text...")
            st.image("https://chracters.blob.core.windows.net/images/Simi.PNG")
            prompt = ChatPromptTemplate.from_template(
                "Write a deatalied Social Media Post about {topic} in a {tone}and add relevant hashtags take points from text provided in input and add your knowledge as well"   
                )
            output_parser = StrOutputParser()
            model = ChatOpenAI(model="gpt-3.5-turbo")
            chain = (
                    {"topic": RunnablePassthrough() , "tone": RunnablePassthrough()} 
                    | prompt
                    | model
                    | output_parser
                )
            try:
                result=chain.invoke([report,tone_of_post])
                st.write(result)
                
            except Exception as e:
                st.write("Jinny is Not Working as expected")
            #Agent 3 Jane
            st.header("Jane your Editor is  Editing the text...")
            st.image("https://chracters.blob.core.windows.net/images/Jane.PNG")
            prompt = ChatPromptTemplate.from_template(
                "Act as editor make sure no grammer errors are in the {topic}.Output the same text with grammer modifications"   
                )
            chain = (
                    {"topic": RunnablePassthrough()} 
                    | prompt
                    | model
                    | output_parser
                )
            try:
                result=chain.invoke(result)
                st.write(result)
            except Exception as e:
                st.write("Jane is Not Working as expected")

            

            #Agent 4 Artist
            st.header("John your own artist is creating a image for you...")
            st.image("https://chracters.blob.core.windows.net/images/John.PNG")
            client = AzureOpenAI(
                api_version="2024-02-01",
                azure_endpoint="https://aiagents.openai.azure.com/",
                api_key="198e8394cb0f47e69807d2bcd7a26c60",
                )
            
            try:

                result = client.images.generate(
                    model="sass", # the name of your DALL-E 3 deployment
                    prompt=title,
                    n=1
                ) 

                # Send a GET request to the URL
                image_url = json.loads(result.model_dump_json())['data'][0]['url']
                response = requests.get(image_url)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Open a file in binary write mode and write the content of the response
                    with open("image.jpg", "wb") as file:
                       z= file.write(response.content)
                    #print("Image downloaded successfully.")
                else:
                    print("Failed to download image.")
                
                st.write(f"Find ur image at {image_url}")

            except Exception as e:
                 st.write("John is not working as expected.")

if __name__ == "__main__":
      main()