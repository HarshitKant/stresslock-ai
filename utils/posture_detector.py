import mediapipe as mp

def check_posture(landmarks):
    # Simplified: compare shoulder and ear y-coordinates
    slouch_score = abs(landmarks['left_shoulder'].y - landmarks['left_ear'].y)
    return slouch_score > 0.1
