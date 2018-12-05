def face_recog():
    import time
    import face_recognition
    import cv2
    list = open('facelib/user.txt', 'r')

    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    faces = eval(list.readline())
    recog = locals()
    # Load a sample picture and learn how to recognize it.
    # obama_image = face_recognition.load_image_file("facelib/obama.jpg")
    # obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    #
    # helium_image = face_recognition.load_image_file("facelib/helium.jpg")
    # helium_face_encoding = face_recognition.face_encodings(helium_image)[0]
    known_face_encodings = []
    known_face_names = []
    for i in faces:
        recog[i +'_image'] = face_recognition.load_image_file("facelib/" + i + '.jpg')
        recog[i + '_face_encoding'] = face_recognition.face_encodings(recog[i +'_image'])[0]
        known_face_encodings.append(recog[i + '_face_encoding'])
    known_face_names = faces
    # Create arrays of known face encodings and their names
    list.close()
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    time = 0
    while True:
        name = ''
        time += 1
        # Grab a single frame of video
        ret, frame = video_capture.read()

        frame = cv2.flip(frame, 1)

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
                name = "$$$Unknown$$$"
                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    # print(name)
                    video_capture.release()
                    cv2.destroyAllWindows()
                    return name

        process_this_frame = not process_this_frame


        cv2.imshow('Video', frame)
        if time == 50:
            if name == '$$$Unknown$$$':
                break
            else:
                name = '$$$Timeout$$$'
                break
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q') or (time >= 1 and name in known_face_names):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

    return name


def reg(path, name):
    from PIL import Image
    import face_recognition
    list = open('facelib/user.txt', 'r')
    users = eval(list.readline())
    list.close()

    if name in users:
        return 'User already exists'
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(path)

    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) == 0:
        return 'No face Detected'

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    list = open('facelib/user.txt', 'w')
    users.append(name)
    list.write(str(users))
    list.close()
    pil_image.save('facelib/' + name+'.jpg', 'JPEG')
    return True

if __name__ == '__main__':
    print(face_recog())
