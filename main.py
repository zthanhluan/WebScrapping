import streamlit as st
    
from scrape import (
    scrapWebsite , 
    split_dom_content , 
    clean_body_content , 
    extract_body_content
    )
from Ollama import parseUsingOllama

st.title ("AI Scraper")

url = st.text_input("Search For Website")

if st.button("Start Scraping"):
    if url :
        st.write("Scraping...")
        result = scrapWebsite(url)  
        # print(result)
        bodyContent = extract_body_content(result)
        cleanedContent = clean_body_content(bodyContent)

        st.session_state.dom_content = cleanedContent

        with st.expander ("View All Content") :
            st.text_area("Content" , cleanedContent, height=300)

dom_chunks = None
parsed_result = None
parse_description = None      
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what's in Your Mind ..'")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)

if dom_chunks is not None and parse_description is not None:          
    parsed_result = parseUsingOllama(dom_chunks, parse_description)
    st.write(parsed_result)