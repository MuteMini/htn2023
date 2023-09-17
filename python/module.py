#This is a support Module mainly for the speech from text and also to aid the
#System into knowing when a finger is up or when a finger is down based on the
#joints

import cv2

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

drawingModule = mp.solutions.drawing_utils
handsModule = mp.solutions.hands

mod=handsModule.Hands()

h=480
w=640

def findpostion(frame1):
    results=[]
    image = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    recognition_result = recognizer.recognize(mp.Image(image_format=mp.ImageFormat.SRGB, data=image))

    # STEP 5: Process the result. In this case, visualize it.
    if len(recognition_result.gestures) > 0:
        top_gesture = recognition_result.gestures[0][0]
        hand_landmarks = recognition_result.hand_landmarks
        results.append(top_gesture.category_name)

    # draw = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    # if draw.multi_hand_landmarks != None:
    #    for handLandmarks in draw.multi_hand_landmarks:
    #        drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
    #        list=[]
    #        for id, pt in enumerate (handLandmarks.landmark):
    #             x = int(pt.x * w)
    #             y = int(pt.y * h)
    #             list.append([id,x,y])

    return results            


# def findnameoflandmark(frame1):
#      list=[]
#      results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
#      if results.multi_hand_landmarks != None:
#         for handLandmarks in results.multi_hand_landmarks:


#             for point in handsModule.HandLandmark:
#                  list.append(str(point).replace ("< ","").replace("HandLandmark.", "").replace("_"," ").replace("[]",""))
#      return list