###################################################################################################
#                                 Identify Faces Goal:
# identify faces and draw a box around them with their names. If known face, labeled 'unknown'
###################################################################################################


###################################################################################################
#      Faces Used for Program (Will Change Names on Finalized Commit for privacy purposes):
# Aldrin Brillante
# 
###################################################################################################

import face_recognition
from PIL import Image, ImageDraw #needed to draw on top of an image



#Aldrin
image_of_aldrin = face_recognition.load_image_file('./img/known/Aldrin Brillante.png')
aldrin_face_encoding = face_recognition.face_encodings(image_of_aldrin)[0]

#Shanelle
image_of_shanelle = face_recognition.load_image_file('./img/known/Shanelle Valencia.png')
shanelle_face_encoding = face_recognition.face_encodings(image_of_shanelle)[0]

#Brian
image_of_brian = face_recognition.load_image_file('./img/known/Brian Ross.png')
brian_face_encoding = face_recognition.face_encodings(image_of_brian)[0]

#Gobind
image_of_gobind = face_recognition.load_image_file('./img/known/Gobind Puniani.png')
gobind_face_encoding = face_recognition.face_encodings(image_of_gobind)[0]



#  Create arrays of encodings and names
known_face_encodings = [
  aldrin_face_encoding,
  shanelle_face_encoding,
  brian_face_encoding,
  gobind_face_encoding
]

known_face_names = [
  "Aldrin Brillante",
  "Shanelle Valencia",
  "Brian Ross",
  "Gobind Puniani"
]

# Load test image to find faces in
# test_image = face_recognition.load_image_file('./img/groups/group1.png')
# test_image = face_recognition.load_image_file('./img/groups/random-group.png')

####BEWARE OF THIS RUN SEMI RIGHT####
# test_image = face_recognition.load_image_file('./img/groups/workaholics.png')
test_image = face_recognition.load_image_file('./img/groups/theboyz.png')


# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)


# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  # If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
  
  # Draw box
  draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  # Draw label
  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw

# Display image
pil_image.show()

# Save image
pil_image.save('identification-results.jpg')

