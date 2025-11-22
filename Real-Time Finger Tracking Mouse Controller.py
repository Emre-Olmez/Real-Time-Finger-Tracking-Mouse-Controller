import cv2
import mediapipe as mp
import pyautogui


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils


screen_w, screen_h = pyautogui.size()

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,800)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,700)

fps = cam.get(cv2.CAP_PROP_FPS)


while True:
    kontrol, matris = cam.read()
    matris = cv2.flip(matris, 1)
    rgb = cv2.cvtColor(matris, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    h, w, c = matris.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

          
            x_tip = handLms.landmark[8].x
            y_tip = handLms.landmark[8].y

         
            px = int(x_tip * w)
            py = int(y_tip * h)

           
            mouse_x = int(x_tip * screen_w)
            mouse_y = int(y_tip * screen_h)

           
            pyautogui.moveTo(mouse_x, mouse_y)


            mp_draw.draw_landmarks(matris, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("El ile Mouse Kontrolu", matris)
    if cv2.waitKey(int(1000 / fps))  == 27: 
        break

cam.release()
cv2.destroyAllWindows()
