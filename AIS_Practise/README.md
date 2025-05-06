# ai_coursework

This repo contains code for course work.
Install CUDA 11.8 and PyTorch 2.4.1

Then install ultralytics, streamlit and opencv
```
pip install ultralytics streamlit opencv-python
```
And run server
```
streamlit run app.py
```
If you want to disable YOLO's warnings, set flag YOLO_VERBOSE to False
```
YOLO_VERBOSE=False streamlit run app.py
```
## sources
- [Streamlit with YOLO](https://medium.com/@radhikaramsen3131/build-an-object-detection-webapp-with-yolov8-and-streamlit-29dd2d09be26) (if you don't have VPN, change `medium.com` on `scribe.rip`)
- [OpenCV with video](https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html) 
- [YOLO+OpenImagesV7](https://docs.ultralytics.com/ru/datasets/detect/open-images-v7/)
- [YOLO+OpenImages with specific classes](https://github.com/smk75/Electronics_Object_Detection)
- [Template for images and web-cam](https://medium.com/@codeaigo/building-an-object-detection-app-with-yolov8-and-streamlit-d3aa416f7b6a) (same as the first one)
- [Object counting with YOLO, if you do not need saving video](https://docs.ultralytics.com/ru/guides/object-counting/)