import cv2
import numpy as np
import pygame

# Load pre-trained YOLOv3 model and classes
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Define output layer names
layer_names = net.getLayerNames()

# Debugging: Print the output of net.getUnconnectedOutLayers()
print("Output of net.getUnconnectedOutLayers():", net.getUnconnectedOutLayers())

output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Define the target animals
target_animals = ['bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe']

# Load alert sound
alert_sound = r"C:\Users\hp\Desktop\animaldetection\alert_sound.wav.mp3"  # Replace this with the correct path to your alert sound file

# Initialize the pygame mixer
pygame.mixer.init()

# Function to play alert sound
def play_alert_sound():
    pygame.mixer.music.load(alert_sound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Function to detect and classify animals
def detect_animals(image):
    height, width, _ = image.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                label = str(classes[class_id])
                if label.lower() in target_animals:
                    x, y, w, h = map(int, detection[0:4] * [width, height, width, height])
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(image, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    print("Detected:", label)
                    play_alert_sound()

    return image

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = detect_animals(frame)

    cv2.imshow('Animal Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break  # Exit the loop when 'q' is pressed

cap.release()
cv2.destroyAllWindows()
