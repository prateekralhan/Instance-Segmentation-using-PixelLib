import streamlit as st
import cv2
import os
from PIL import Image
from app_funcs import segment_image, segment_video, segment_live_feed, download_success

st.set_page_config(
    page_title="Instance Segmentator",
    page_icon="🖼",
    layout="centered",
    initial_sidebar_state="auto",
)

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')

upload_path = "uploads/"
download_path = "downloads/"

st.sidebar.image(top_image,use_column_width='auto')
segmentation_type = st.sidebar.selectbox('Select segmentation type 🎯',["Image","Video","Live Feed"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.image(main_image,use_column_width='auto')
st.title("Instance Segmentator")

if segmentation_type == "Image":
    st.info('Supports all popular image formats 📷 - PNG, JPG, BMP ')
    uploaded_file = st.file_uploader("Upload Image 🖼", type=["png","jpg","bmp","jpeg"])

    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        with st.spinner(f"Working... "):
            uploaded_image = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
            downloaded_image = os.path.abspath(os.path.join(download_path,str("segmented_"+uploaded_file.name)))
            segment_image(uploaded_image, downloaded_image)

            final_image = Image.open(downloaded_image)
            print("Opening ",final_image)
            st.markdown("---")
            st.image(final_image, caption='This is how your final image looks like ')
            with open(downloaded_image, "rb") as file:
                if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.JPG'):
                    if st.download_button(
                                            label="Download Segmented Image 📷",
                                            data=file,
                                            file_name=str("segmented_"+uploaded_file.name),
                                            mime='image/jpg'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.jpeg') or uploaded_file.name.endswith('.JPEG'):
                    if st.download_button(
                                            label="Download Segmented Image 📷",
                                            data=file,
                                            file_name=str("segmented_"+uploaded_file.name),
                                            mime='image/jpeg'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.png') or uploaded_file.name.endswith('.PNG'):
                    if st.download_button(
                                            label="Download Segmented Image 📷",
                                            data=file,
                                            file_name=str("segmented_"+uploaded_file.name),
                                            mime='image/png'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.bmp') or uploaded_file.name.endswith('.BMP'):
                    if st.download_button(
                                            label="Download Segmented Image 📷",
                                            data=file,
                                            file_name=str("segmented_"+uploaded_file.name),
                                            mime='image/bmp'
                                         ):
                        download_success()
    else:
        st.warning(' Please upload your Image file ')

if segmentation_type == "Video":
    st.info('Supports all popular video formats 🎥 - MP4, MOV, MKV, AVI ')
    uploaded_file = st.file_uploader("Upload Video 📽", type=["mp4","avi","mov","mkv"])
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        with st.spinner(f"Working... "):
            uploaded_video = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
            downloaded_video = os.path.abspath(os.path.join(download_path,str("segmented_"+uploaded_file.name)))
            segment_video(uploaded_video, downloaded_video)

            final_video = open(downloaded_video, 'rb')
            video_bytes = final_video.read()
            print("Opening ",final_video)
            st.markdown("---")
            with open(downloaded_video, "rb") as file:
                if uploaded_file.name.endswith('.avi') or uploaded_file.name.endswith('.AVI'):
                    st.success('Your results are ready !! ')
                    if st.download_button(
                                            label="Download Segmented Video 📽",
                                            data=file,
                                            file_name=str("segmented_"+uploaded_file.name),
                                            mime='video/x-msvideo'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.mp4') or uploaded_file.name.endswith('.MP4'):
                    st.success('Your results are ready !! ')
                    if st.download_button(
                                            label="Download Segmented Video 📽",
                                            data=file,
                                            file_name=str("segmented_"+uploaded_file.name),
                                            mime='video/mp4'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.mov') or uploaded_file.name.endswith('.MOV'):
                    st.success('Your results are ready !! ')
                    if st.download_button(
                                            label="Download Segmented Video 📽",
                                            data=file,
                                            file_name=str("segmented_"+uploaded_file.name),
                                            mime='video/quicktime'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.mkv') or uploaded_file.name.endswith('.MKV'):
                    st.success(' Your results are ready !! ')
                    if st.download_button(
                                            label="Download Segmented Video 📽",
                                            data=file,
                                            file_name=str("segmented_"+uploaded_file.name),
                                            mime='video/x-matroska'
                                         ):
                        download_success()
    else:
        st.warning('⚠ Please upload your Video file ')

