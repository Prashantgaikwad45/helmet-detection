import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
from ultralytics import YOLO

st.title("Helmet Detection - Live Camera")

model = YOLO("yolov8n.pt")

class VideoProcessor(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        results = model(img)
        annotated_frame = results[0].plot()
        
        return annotated_frame

webrtc_streamer(key="helmet-detection", video_processor_factory=VideoProcessor)
