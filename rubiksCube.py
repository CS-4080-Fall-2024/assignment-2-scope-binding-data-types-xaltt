class RubiksCube:
    def __init__(self, size=3):
        self.size = size
        #adding labels to faces
        self.faces = {
            "Front": [[f"G" for _ in range(size)] for _ in range(size)],
            "Back": [[f"B" for _ in range(size)] for _ in range(size)],
            "Left": [[f"O" for _ in range(size)] for _ in range(size)],
            "Right": [[f"R" for _ in range(size)] for _ in range(size)],
            "Up": [[f"W" for _ in range(size)] for _ in range(size)],
            "Down": [[f"Y" for _ in range(size)] for _ in range(size)],
        }

    def rotate_face(self, face):
        """Rotate a specific face 90 degrees clockwise."""
        if face in self.faces:
            self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]
        else:
            print(f"Invalid face: {face}. Choose from {list(self.faces.keys())}.")

    def display(self):
        """Display the state of the Rubik’s Cube."""
        print("\nRubik's Cube State:")
        for label, face in self.faces.items():
            print(f"\nFace: {label}")
            for row in face:
                print(" ".join(row))
        print()

#ex use
cube = RubiksCube(3)
cube.display()  #show initial display

#rotate front face
print("Rotating the Front face...\n")
cube.rotate_face("Front")
cube.display()  #disp state after
