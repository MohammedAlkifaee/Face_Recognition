![image](https://github.com/user-attachments/assets/51f68aca-164d-40ab-941a-6b14cedc972c)


## Credits

This project was collaboratively developed by:
- **Dr. Asad Noori Alsharefi**
- **Mohammad Abbas Shareef**
- **Anfal Hayder Abd-Alrasol**
- **Esraa Muhsin Qasim**

# Face Recognition System with SQLite Integration

This project is a Python-based face recognition system that integrates a local SQLite database to manage authorized persons. The application allows adding, deleting, and listing authorized individuals and uses the DeepFace library for face verification. It provides a real-time camera feed to recognize authorized and unauthorized individuals.

## Features

- **Add Authorized Persons**: Register a person's name and image for face recognition.
- **Delete Authorized Persons**: Remove a person from the database.
- **View Authorized Persons**: Display a list of all registered persons.
- **Real-Time Face Recognition**: Uses OpenCV and DeepFace for live detection and verification.
- **SQLite Integration**: Stores and retrieves authorized persons' data locally.

## Requirements

- Python 3.8+
- OpenCV (`cv2`)
- SQLite3
- [DeepFace](https://github.com/serengil/deepface)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MohammedAlkifaee/Face_Recognition.git
   cd face-recognition-system
   ```

2. Install the required dependencies:
   ```bash
   pip install opencv-python deepface
   ```

3. Ensure the SQLite database is initialized automatically when running the script.

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Choose an option from the menu:
   - **1**: Add a new authorized person.
   - **2**: Delete an existing authorized person.
   - **3**: Show the list of authorized persons.
   - **4**: Start real-time face recognition.
   - **5**: Exit the application.

## Directory Structure

```
.
├── main.py           # Main script file
├── authorized_persons.db # SQLite database (auto-created if not present)
├── temp_face.jpg     # Temporary file for face recognition
└── README.md         # Project documentation
```

## Example

### Adding an Authorized Person
1. Select option **1**.
2. Enter the name and image path (e.g., `images/john_doe.jpg`).

### Starting Face Recognition
1. Select option **4**.
2. Press `q` to quit the camera feed.

### Deleting an Authorized Person
1. Select option **2**.
2. Enter the name of the person to be removed.


