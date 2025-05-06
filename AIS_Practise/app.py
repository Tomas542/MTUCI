import cv2
import streamlit as st
from ultralytics import YOLO
import pandas as pd

import json
import datetime

def app() -> None:
    st.header('Object Detection Web App')
    st.subheader('Artyom Iudin TV set detection web app')
    model = YOLO('yolov8x-oiv7.pt')
    data = []

    with st.form("my_form"):
        uploaded_file = st.file_uploader("Upload video", type=['mp4'])
        min_confidence = st.slider('Confidence score', 0.2, 1.0)
        st.form_submit_button(label='Submit')
    
    if uploaded_file is not None: 
        start_time = datetime.datetime.now()
        captures = 0
        times = 0
        tv_count = []

        input_path = uploaded_file.name
        file_binary = uploaded_file.read()

        with open(input_path, "wb") as temp_file:
            temp_file.write(file_binary)

        video_stream = cv2.VideoCapture(input_path)
        
        width = int(video_stream.get(cv2.CAP_PROP_FRAME_WIDTH)) 
        height = int(video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT))  
        fps = int(video_stream.get(cv2.CAP_PROP_FPS)) 

        output_path = input_path.split('.')[0] + '_output.mp4' 
        out_video = cv2.VideoWriter(output_path, int(cv2.VideoWriter_fourcc(*'mp4v')) , fps, (width, height)) 

        with st.spinner('Processing video...'): 
            while True:
                ret, frame = video_stream.read()
                if not ret:
                    break
                result = model(frame)
                found = False
                current_tv = 0
                
                for detection in result[0].boxes.data:
                    x0, y0 = (int(detection[0]), int(detection[1]))
                    x1, y1 = (int(detection[2]), int(detection[3]))

                    score = round(float(detection[4]), 2)
                    cls = int(detection[5])

                    if model.names[cls] == "Television" and score > min_confidence:
                        captures += 1
                        found = True
                        current_tv += 1
                        cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 0, 0), 2)
                        cv2.putText(frame, f'{score}', (x0, y0 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                if found:
                    times += 1

                tv_count.append(current_tv)
                detections = result[0].verbose()
                cv2.putText(frame, detections, (10, 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                out_video.write(frame) 

            data.append({
                "name":input_path,
                "width": width,
                "height": height,
                "fps":fps,
                "date and time": str(start_time),
                "processing took in seconds": (datetime.datetime.now() - start_time).seconds
            })
            with open("data.json", "w") as file:
                json.dump(data, file)

            # print(len(tv_count))
            # print(len([i for i in range(1, len(tv_count)+2)]))
            report = pd.DataFrame({
                "frame": [i for i in range(1, len(tv_count)+1)],
                "TVs on frame": tv_count
            }).to_csv(index=False)

            video_stream.release()
            out_video.release()
            cv2.destroyAllWindows()

        st.video(output_path)
        st.write(f"Avg TVs on frame: {captures/times}")
        with open("data.json", "r") as file:
            st.download_button(
                label="Download JSON history",
                data=file,
                file_name="data.json"
            )
        
        st.download_button(
            label="Download report",
            data=report,
            file_name="report.csv"
        )

if __name__ == "__main__":
    app()
