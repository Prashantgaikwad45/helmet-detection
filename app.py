import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile

st.title("Helmet Detection System")

model = YOLO("yolov8m.pt")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])

if uploaded_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    img = cv2.imread(tfile.name)
    results = model(img)

    res_plotted = results[0].plot()
    st.image(res_plotted, caption="Detection Result")