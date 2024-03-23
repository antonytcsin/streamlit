import streamlit as st

st.title("This is my stremlit application")

st.header ("This is my page heading")

st.subheader("This is my subheader")

st.text("This is the text")

st.success("This is done sucessfully")



if st.checkbox("select / un select"):
    st.text("User has selected the check box")
else:
    st.text("User has NOT selected the check box")

state=st.radio("Please select any of the option",("red","black"))

if state=="red":
    st.text(f"User has selected {state}")

select=st.selectbox("Please select any of the below option",["Read","Write","Read/write"])

st.text(f"The selected option is {select}")

if st.button("Click here"):
    st.success("You have clicked me ")
else:
    st.error("You have NOT  clicked me ")

st.sidebar.header("This is my sidebar")
st.sidebar.title("This is my title")

