from deepface import DeepFace
import cv2

def analyze_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        return result[0]['emotion']
    except:
        return None
