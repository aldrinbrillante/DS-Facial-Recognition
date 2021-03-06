#####################################################################
#                      Find Faces Goal:
# able to recognize, locate, and count faces in image
#####################################################################


import face_recognition

image = face_recognition.load_image_file('./img/groups/group1-ravecrew.png') # There are 15 forward facing people in this photo
image_2 = face_recognition.load_image_file('./img/groups/group2-solo.png')
# image_2 = face_recognition.load_image_file('./img/groups/squad.png')


face_locations = face_recognition.face_locations(image)
face_locations_2 = face_recognition.face_locations(image_2)

# Array of coordinates of each face
print(face_locations)

print(f'In this image, there are {len(face_locations)} people.')
print(f'In this image, there are {len(face_locations_2)} people.')