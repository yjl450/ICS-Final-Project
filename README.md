# ICS-Final-Project
A cross-platform chat system with GUI, real-time multilingual translation, and face recognition authentication.

## Creators
Creators are Carol Long (`@ql816`), Amanda Huang (`@Oysters1874`) and me (Yijian Liu `@yjl450`).
The original chat system belongs to NYUSH Computer Science department.

## This project is dependent on
**GUI**  
[PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro)  
Install by `pip3 install pyqt5`  

**Face Recognition Authentication**  
[face_recognition](https://github.com/ageitgey/face_recognition) for registering faces and logging in with faces.  
Install by `pip3 install face_recognition` (CMake and Dlib needed)

[opencv-python](https://pypi.org/project/opencv-python/) for displaying webcam image.  
Installation varies according to operating system

**Real-time Multilingual Translation**  
[langdetect](https://pypi.org/project/langdetect/) for detecting the language of the imcoming messages.  
Install by `pip3 install langdetect`  

[Baidu Translation API](http://api.fanyi.baidu.com) for auto translation.  

How it works
-----------------------
Before logging in, register your face with an image containing a clear face of yours and your username.
