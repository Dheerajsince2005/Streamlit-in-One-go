import streamlit as st

st.title('Are You Kamma?')
st.header("Heads up! This is just for fun. Don't take it seriously.")
st.subheader("Enter your name to find out if you are Kamma or not.")
st.warning("This is just for fun. Don't take it seriously.")
st.error("This is just for fun. Don't take it seriously.")
st.info("Kamma is a caste in Andhra Pradesh, India.")
st.success("Kamma is a caste in Andhra Pradesh, India.")
exp = ZeroDivisionError("You are wrong.")
st.exception(exp)
st.help(ZeroDivisionError)
st.button("Click me!")
if(st.button("Click me! x")):
    st.write("You clicked the button!")
radiobutton = st.radio("Are you Kamma?", ("Yes", "No"))
if radiobutton == "Yes":
    st.write("You are Kamma!")
else:
    st.write("Are You Madivada?")
selectbox = st.selectbox("Select your caste", ["Kamma", "Kapu", "Reddy", "Madivada"])
st.write(f"You have selected {selectbox}")
st.multiselect("Select your caste", ["Kamma", "Kapu", "Reddy", "Madivada"])
st.button("Click me! baby you can touch me ")
st.slider("Select your age", 0, 100)
name = st.text_input("Enter your name")
if(name!=""):
    st.write(f"Hello {name}")
st.text_area("Enter your address")
st.date_input("Enter your birthdate")  
st.time_input("Enter your time of birth")
password = st.text_input("Enter your password", type="password")
aboutyourself = st.text_area("Tell us about yourself in 100 words", height=100)