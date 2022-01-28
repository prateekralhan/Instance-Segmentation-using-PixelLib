import pixellib
from pixellib.instance import instance_segmentation
import streamlit as st
import cv2

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def segment_image(uploaded_image, downloaded_image):
    segmentation_model = instance_segmentation()
    segmentation_model.load_model('weights/mask_rcnn_coco.h5')
    segmentation_model.segmentImage(uploaded_image, show_bboxes = True,output_image_name = downloaded_image)

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def segment_video(uploaded_video, downloaded_video):
    segmentation_model = instance_segmentation()
    segmentation_model.load_model('weights/mask_rcnn_coco.h5')
    segmentation_model.process_video(uploaded_video, show_bboxes = True, frames_per_second= 20, output_video_name = downloaded_video)

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def segment_live_feed(capture):
    segmentation_model = instance_segmentation()
    segmentation_model.load_model('weights/mask_rcnn_coco.h5')
    res = segmentation_model.segmentFrame(capture, show_bboxes=True)
    return res[1]

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
    st.success('✅ Download Successful !!')
