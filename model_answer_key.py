from ultralytics import YOLO

# You may edit the variable below to be any path to an image
img = "code_next_students.jpg"
#img = "seedless_fruits.jpg" # Step 5

model = YOLO("yolov8n.pt") # Import the model
# Predict on an image - CODE ALONG for this line:
results = model(img)  # Step 1

print("Successly ran model!")


# Run a for-loop to peek through the results
for result in results:
    #####################################################################
    # CODE ALONG:
    # After each line, have students pause and run the program.
    # Ask: "What do you observe?"
    #
    # Be mindful that some students have experience in Python,
    # while others may never have used Python. Give students time
    # to type. Such students may need help with parentheses placement.
    # Remind students to "save" if they have not enabled auto-save
    #####################################################################

    # Step 2: Have students delete "pass"
    print(result.verbose()) # Optional. Prints to command line
    result.show() # Step 3. Opens in a new tab
    result.save() # Step 4. Saves to current directory