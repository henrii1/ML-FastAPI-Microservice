#notes on running:  https://docs.streamlit.io/knowledge-base/deploy/remote-start

import streamlit as st
from app_openai import create_code, submit_question
from app_greedy import greedy_coin
from app_wiki import get_wiki_keyword, get_wiki_page, get_wiki_summary, search_wiki_pages

st.title("Chat Bot")
st.write("ask question and get answers for each")

texts = st.text_area("Enter your questions here")

if st.button("Ask Question"):
    with st.spinner(text="generating"):
        output = submit_question(texts)
        st.markdown(output)


st.title("Code Generator")
st.write("Convert a comment into code in any language")

language = st.text_input("Language", "python")
text = st.text_area("Comment", "W")

if st.button("Generate Code"):
    with st.spinner(text='In progress'):
        code = create_code(text, language)
        st.code(code)


st.title("Greedy algorithm for coins")
st.write(" submit a change amount and retrieve the minimum number of coins")

greedy = st.number_input("Enter a number here")

if st.button("Find minimum change"):
    with st.spinner(text = "In progress"):
        coin = greedy_coin(greedy)
        st.markdown(coin)


st.title("Wikipedia Pages")
st.write("Outputs a wikipedia page corresponding to the keyword entered")

pages = st.text_input("Enter the keyword to find wikipedia page from")

if st.button("search for page"):
    with st.spinner():
        summary = get_wiki_summary(pages)
        st.markdown(summary)
        


st.title("Wikipedia keywords")
st.write("Outputs the top 10 keywords from a wikipedia search")

keyword = st.text_input("Enter the Keyword to generate top keywords from page")

if st.button("Find Keywords"):
    with st.spinner():
        keywords = get_wiki_keyword(keyword)
        list_val = []
        for key, val in keywords.items():
            a = [key, val]
            list_val.append(a)
        st.markdown(list_val)



