import streamlit as st

st.title("A Example Streamlit App")

st.write("Testing the CI/CD pipeline on github to automatically deploy to cloud run")


c1, c2 = st.columns(2)

with c1:
    st.video("https://www.youtube.com/watch?v=LxwoCKM1Qik")

with c2:
    st.video("https://www.youtube.com/watch?v=cP0I9w2coGU")