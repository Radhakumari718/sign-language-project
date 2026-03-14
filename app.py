import streamlit as st
import pyttsx3

st.title("Sign Language to Text and Speech Converter")

st.write("Show your hand gesture in front of the camera")

camera = st.camera_input("Capture Gesture")

if camera is not None:
    st.image(camera)

    text = "HELLO"

    st.subheader("Detected Text:")
    st.write(text)

    if st.button("Speak"):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()