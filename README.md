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
<div align="center">
  <img src = "https://github.com/yjl450/ICS-Final-Project/blob/master/Presentation/login.png" width = "400"/>
</div>  


You'll then be able to see the chat interface.
<div align="center">
  <img src = "https://github.com/yjl450/ICS-Final-Project/blob/master/Presentation/chat.png" width = "500"/>
</div>  


First, click \"Connect\" to connect to a peer. All your peers will be shown in a new window.
Once you successfully connect to a peer, you can start chatting.
<div align="center">
  <img src = "https://github.com/yjl450/ICS-Final-Project/blob/master/Presentation/connect.png" width = "500"/>
</div>  


During chatting, if you want to translate the message into another language, click \"Translate\" after choosing which language you want to see.
An indicating message will be shown.
<div align="center">
  <img src = "https://github.com/yjl450/ICS-Final-Project/blob/master/Presentation/translate.png" width = "500"/>
</div>  


When not chatting, you can see the system time by clicking \"Time\" or search message history by clicking \"History\".
If there are too many messages in the display, click \"Clear\" to remove them from screen.
<div align="center">
  <img src = "https://github.com/yjl450/ICS-Final-Project/blob/master/Presentation/time.png" width = "500"/>
  <img src = "https://github.com/yjl450/ICS-Final-Project/blob/master/Presentation/search.png" height = "499"/>
</div>  


If you want to leave, simply close the chat window.
You'll be able to log in directly with your face next time.
<div align="center">
  <img src = "https://github.com/yjl450/ICS-Final-Project/blob/master/Presentation/quit.png" width = "500"/>
</div> 
