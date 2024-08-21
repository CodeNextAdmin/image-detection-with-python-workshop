from ultralytics import YOLO

# You may edit the variable below to be any path to an image
img = "code_next_students.jpg"


model = YOLO("yolov8n.pt") # Import the model

# TODO: Follow along with your instructor to run the model
# on your image. Store in a variable called results:

# results =

print("Successly ran model!")


# Run a for-loop to peek through the results

for result in results:

    # TODOs - Follow along with your instructor
    pass # Delete me!

    # Show the result using show():

    # Save the result using save():
