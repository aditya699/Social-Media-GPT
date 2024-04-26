'''
Author     - Aditya Bhatt 22:11 PM 25-04-2024

Objective            -
1.Create a system to automate social media management.

Employee 1 Planning -
1.Julia Get's Information from Wikipedia + Internet

AI System By Aditya
'''
import os
import streamlit as st
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.adapters.openai import convert_openai_messages
from langchain_community.chat_models import ChatOpenAI
from tavily import TavilyClient
client = TavilyClient(api_key="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")
# run tavily search
OPENAI_API_KEY ="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"
os.environ['OPENAI_API_KEY']="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"

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=2000)
tool = WikipediaQueryRun(api_wrapper=api_wrapper)

def main():
        st.title("Social MediaGPT")
        st.sidebar.image("robots_working_on_social_media.png","Made By Aditya Bhatt")
        st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/adityaabhatt/)")
        st.sidebar.markdown("[About Me](https://aiwithaditya.odoo.com/)")
        

        title = st.text_input('Enter topic on which you want to create a post:')
        mood_options = ["Funny", "Casual", "Formal"]
        tone_of_post=st.selectbox("Select mood of post", mood_options)
        print(f"The User wants a post on the title : {title} and the mood of the post is {tone_of_post}")
        

        if st.button("Start the Magic"):
            st.write("Julia(Your AI Researcher is at it)...")
            st.image("JULIA.png")
            st.write("She is searching in wikipedia...")
            try:
                wiki_result=tool.run({"query": f"{title}"})
                st.write(wiki_result)
                st.write("Julia is searching over the internet...")
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

                st.write("Julia is still working.... what you think research is an easy task...😄")

                # run gpt-3.5
                lc_messages = convert_openai_messages(prompt)
                report = ChatOpenAI(model='gpt-3.5-turbo',openai_api_key=OPENAI_API_KEY).invoke(lc_messages).content

                # print report
                st.write("Here the report which Julia has made")
                st.write(report)
                context=[wiki_result,report]
                st.write("App in Development") 

            except Exception as e:
                  st.write("Julia is not working as expected")
            pass
            #AI Agent -1 Researcher

  


if __name__ == "__main__":
      main()