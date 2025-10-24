def compute_stress(emotions, posture_flag):
    stress_factors = ['angry', 'sad', 'fear']
    score = sum(emotions[e] for e in stress_factors if e in emotions) / 100
    if posture_flag:
        score += 0.1
    return min(score, 1.0)
def draw_stress_on_frame(frame, stress_score):
    cv2.putText(frame, f'Stress Level: {stress_score:.2f}', (10, 90), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return frame