import cv2
import sqlite3
import os
from deepface import DeepFace

conn = sqlite3.connect("authorized_persons.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    image_path TEXT NOT NULL
)
""")
conn.commit()
def add_person(name, image_path):
    cursor.execute("INSERT INTO persons (name, image_path) VALUES (?, ?)", (name, image_path))
    conn.commit()
    print(f"{name} has been added to the authorized list.")

def delete_person(name):
    cursor.execute("DELETE FROM persons WHERE name = ?", (name,))
    conn.commit()
    print(f"{name} has been removed from the authorized list.")

def show_authorized_list():
    cursor.execute("SELECT name FROM persons")
    persons = cursor.fetchall()
    print("Authorized persons list:")
    for person in persons:
        print("- ", person[0])

def face_recognition():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_img = frame[y:y + h, x:x + w]
            cv2.imwrite("temp_face.jpg", face_img)
            cursor.execute("SELECT name, image_path FROM persons")
            persons = cursor.fetchall()
            authorized = False
            for person in persons:
                authorized = compare_faces("temp_face.jpg", person[1])
                if authorized:
                    cv2.putText(frame, f"Authorized: {person[0]}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (0, 255, 0), 2)
                    break
            if not authorized:
                cv2.putText(frame, "Unauthorized", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.imshow("Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
    os.remove("temp_face.jpg")


def compare_faces(face_img_path, stored_image_path):
    try:
        result = DeepFace.verify(img1_path=face_img_path, img2_path=stored_image_path, model_name="VGG-Face",
                                 enforce_detection=False)
        return result["verified"]
    except Exception as e:
        print("Error in face verification:", e)
        return False


ASCI_C = """
$$\   $$\ $$\   $$\ $$$$$$\ $$\    $$\ $$$$$$$$\ $$$$$$$\   $$$$$$\  $$$$$$\ $$$$$$$$\ $$\     $$\        $$$$$$\  $$$$$$$$\       $$\   $$\ $$\   $$\ $$$$$$$$\  $$$$$$\  
$$ |  $$ |$$$\  $$ |\_$$  _|$$ |   $$ |$$  _____|$$  __$$\ $$  __$$\ \_$$  _|\__$$  __|\$$\   $$  |      $$  __$$\ $$  _____|      $$ | $$  |$$ |  $$ |$$  _____|$$  __$$\ 
$$ |  $$ |$$$$\ $$ |  $$ |  $$ |   $$ |$$ |      $$ |  $$ |$$ /  \__|  $$ |     $$ |    \$$\ $$  /       $$ /  $$ |$$ |            $$ |$$  / $$ |  $$ |$$ |      $$ /  $$ |
$$ |  $$ |$$ $$\$$ |  $$ |  \$$\  $$  |$$$$$\    $$$$$$$  |\$$$$$$\    $$ |     $$ |     \$$$$  /        $$ |  $$ |$$$$$\          $$$$$  /  $$ |  $$ |$$$$$\    $$$$$$$$ |
$$ |  $$ |$$ \$$$$ |  $$ |   \$$\$$  / $$  __|   $$  __$$<  \____$$\   $$ |     $$ |      \$$  /         $$ |  $$ |$$  __|         $$  $$<   $$ |  $$ |$$  __|   $$  __$$ |
$$ |  $$ |$$ |\$$$ |  $$ |    \$$$  /  $$ |      $$ |  $$ |$$\   $$ |  $$ |     $$ |       $$ |          $$ |  $$ |$$ |            $$ |\$$\  $$ |  $$ |$$ |      $$ |  $$ |
\$$$$$$  |$$ | \$$ |$$$$$$\    \$  /   $$$$$$$$\ $$ |  $$ |\$$$$$$  |$$$$$$\    $$ |       $$ |           $$$$$$  |$$ |            $$ | \$$\ \$$$$$$  |$$ |      $$ |  $$ |
 \______/ \__|  \__|\______|    \_/    \________|\__|  \__| \______/ \______|   \__|       \__|           \______/ \__|            \__|  \__| \______/ \__|      \__|  \__|

"""
print(ASCI_C)
print("   By  Dr.Asad noori Alsharefi & Mohammad Abbas Shareef & Anfal Hayder Abd-alrasol & Esraa Muhsin qasim ")
print("")
while True:
    print("\n Options:")
    print("1. Add Authorized Person")
    print("2. Delete Authorized Person")
    print("3. Show Authorized Persons List")
    print("4. Start Camera for Face Recognition")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        image_path = input("Enter image path: ")
        add_person(name, image_path)
    elif choice == '2':
        name = input("Enter name to delete: ")
        delete_person(name)
    elif choice == '3':
        show_authorized_list()
    elif choice == '4':
        face_recognition()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()
