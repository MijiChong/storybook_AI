import streamlit as st

#set app title
st.title("My first streamlit app")

# to run it ==> streamlit run [filename.py]
#display output
st.write("welcome to my first app")

#display a button
st.button("reset", type = 'primary')
if st.button("say hello"):
  st.write("hello there")
else:
  st.write("goodbye")