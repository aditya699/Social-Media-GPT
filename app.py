'''
Author     - Aditya Bhatt 22:11

Objective  -
1.Create a system to automate social media management.

AI System By Aditya
'''
import streamlit as st
import os


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
            st.write("App In Development") 
            pass
            #AI Agent -1 Researcher

  


if __name__ == "__main__":
      main()