# Python Integrated Facial Recognition Intensive


Recognize and manipulate faces from Python or from the command line with
the world's simplest face recognition library.

Built using [dlib](http://dlib.net/)'s state-of-the-art face recognition
built with deep learning. The model has an accuracy of 99.38% on the
[Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) benchmark.

This also provides a simple `face_recognition` command line tool that lets
you do face recognition on a folder of images from the command line!


[![PyPI](https://img.shields.io/pypi/v/face_recognition.svg)](https://pypi.python.org/pypi/face_recognition)

[![Documentation Status](https://readthedocs.org/projects/face-recognition/badge/?version=latest)](http://face-recognition.readthedocs.io/en/latest/?badge=latest)

## Initial Steps

### Requirements

  * Python 3.3+ or Python 2.7
  * macOS or Linux (Windows not officially supported, but might work)

### Installation Options:

#### Installing on Mac or Linux

First, make sure you have dlib already installed with Python bindings: 
 
```brew install cmake```

1. #### Install & launch virtual environment:
      - Open your device's terminal
      - $ pip3 install pipenv
      - $ pipenv shell
          - This will start your virtual environment
2. #### Install Python's Facial Recognition Library
      - $ pipenv install face_recognition

3. #### Install tolerance for face_recognition implementation
      - $ pip3 install tolerance
4. #### Run a match on known and unknown to see which of these are pictures of specific people.
      - $ face_recognition ./img/known ./img/unknown
      - #### we can show the distance of each match with:
            - $ face_recognition --show-distance true ./img/known ./img/unknown
                  - gives us a number for the differences between pictures 
            - you can set a tolerance and implement it for stronger differences using:
                  - $ face_recognition --tolerance 0.50 ./img/known ./img/unknown

5. #### If you want just a list of names of the faces of the people in the image, you can do:
      - $ face_recognition ./img/known ./img/unknown | cut -d ',' -f2

6. #### Now that you have installed and launched your virtual environment, you're ready to code!


## Features & Project Results

#### Find faces in pictures

Find all the front-facing faces that appear in a picture:

![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/img/groups/theboyz.png?raw=true)

![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/img/faces-pulled/345.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/img/faces-pulled/167.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/img/faces-pulled/811.jpg?raw=true)

![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/img/groups/group1-ravecrew.png?raw=true)

![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/653.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/641.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/414.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/387.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/385.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/364.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/354.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/345.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/312.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/288.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/271.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/254.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/253.jpg?raw=true)
![](https://github.com/aldrinbrillante/DS-Facial-Recognition/blob/main/246.jpg?raw=true)

#### Text Output: "There are {num of people} in the photo."


```python
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
```

#### Find and manipulate facial features in pictures

Get the locations and outlines of each person's eyes, nose, mouth and chin.

![](https://cloud.githubusercontent.com/assets/896692/23625282/7f2d79dc-025d-11e7-8728-d8924596f8fa.png)

```python
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
```


![](https://cloud.githubusercontent.com/assets/896692/23625283/80638760-025d-11e7-80a2-1d2779f7ccab.png)

#### Identify faces in pictures

Recognize who appears in each photo.

![](https://cloud.githubusercontent.com/assets/896692/23625229/45e049b6-025d-11e7-89cc-8a71cf89e713.png)

```python
import face_recognition
known_image = face_recognition.load_image_file("biden.jpg")
unknown_image = face_recognition.load_image_file("unknown.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
```

You can even use this library with other Python libraries to do real-time face recognition:

![](https://cloud.githubusercontent.com/assets/896692/24430398/36f0e3f0-13cb-11e7-8258-4d0c9ce1e419.gif)

# Note: this specific project has not integrated live cam facial recognition as of yet (10/15/2021). Will update soon. Stay tuned!



## Detailed Installation Requirements Post-Project

### Requirements

  * Python 3.3+ or Python 2.7
  * macOS or Linux (Windows not officially supported, but might work)

### Installation Options:

#### Installing on Mac or Linux

First, make sure you have dlib already installed with Python bindings:

  
Then, make sure you have cmake installed:  
 
```brew install cmake```

Finally, install this module from pypi using `pip3` (or `pip2` for Python 2):

```bash
pip3 install face_recognition
```

Alternatively, you can try this library with [Docker](https://www.docker.com/), see [this section](#deployment).

#### Installing on an Nvidia Jetson Nano board

#### Installing on FreeBSD

```bash
pkg install graphics/py-face_recognition
```

## Usage

### Command-Line Interface

When you install `face_recognition`, you get two simple command-line 
programs:

* `face_recognition` - Recognize faces in a photograph or folder full for 
   photographs.
* `face_detection` - Find faces in a photograph or folder full for photographs.

#### `face_recognition` command line tool

The `face_recognition` command lets you recognize faces in a photograph or 
folder full  for photographs.

First, you need to provide a folder with one picture of each person you
already know. There should be one image file for each person with the
files named according to who is in the picture:

![known](https://cloud.githubusercontent.com/assets/896692/23582466/8324810e-00df-11e7-82cf-41515eba704d.png)

Next, you need a second folder with the files you want to identify:

![unknown](https://cloud.githubusercontent.com/assets/896692/23582465/81f422f8-00df-11e7-8b0d-75364f641f58.png)

Then in you simply run the command `face_recognition`, passing in
the folder of known people and the folder (or single image) with unknown
people and it tells you who is in each image:

```bash
$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person
```

There's one line in the output for each face. The data is comma-separated
with the filename and the name of the person found.

An `unknown_person` is a face in the image that didn't match anyone in
your folder of known people.

#### `face_detection` command line tool

The `face_detection` command lets you find the location (pixel coordinatates) 
of any faces in an image.

Just run the command `face_detection`, passing in a folder of images 
to check (or a single image):

```bash
$ face_detection  ./folder_with_pictures/

examples/image1.jpg,65,215,169,112
examples/image2.jpg,62,394,211,244
examples/image2.jpg,95,941,244,792
```

It prints one line for each face that was detected. The coordinates
reported are the top, right, bottom and left coordinates of the face (in pixels).
 
##### Adjusting Tolerance / Sensitivity

If you are getting multiple matches for the same person, it might be that
the people in your photos look very similar and a lower tolerance value
is needed to make face comparisons more strict.

You can do that with the `--tolerance` parameter. The default tolerance
value is 0.6 and lower numbers make face comparisons more strict:

```bash
$ face_recognition --tolerance 0.54 ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person
```

If you want to see the face distance calculated for each match in order
to adjust the tolerance setting, you can use `--show-distance true`:

```bash
$ face_recognition --show-distance true ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama,0.378542298956785
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person,None
```

##### More Examples

If you simply want to know the names of the people in each photograph but don't
care about file names, you could do this:

```bash
$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/ | cut -d ',' -f2

Barack Obama
unknown_person
```

##### Speeding up Face Recognition

Face recognition can be done in parallel if you have a computer with
multiple CPU cores. For example, if your system has 4 CPU cores, you can
process about 4 times as many images in the same amount of time by using
all your CPU cores in parallel.

If you are using Python 3.4 or newer, pass in a `--cpus <number_of_cpu_cores_to_use>` parameter:

```bash
$ face_recognition --cpus 4 ./pictures_of_people_i_know/ ./unknown_pictures/
```

You can also pass in `--cpus -1` to use all CPU cores in your system.

#### Python Module

You can import the `face_recognition` module and then easily manipulate
faces with just a couple of lines of code. It's super easy!

API Docs: [https://face-recognition.readthedocs.io](https://face-recognition.readthedocs.io/en/latest/face_recognition.html).

##### Automatically find all the faces in an image

```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_locations = face_recognition.face_locations(image)

# face_locations is now an array listing the co-ordinates of each face!
```



You can also opt-in to a somewhat more accurate deep-learning-based face detection model.

Note: GPU acceleration (via NVidia's CUDA library) is required for good
performance with this model. You'll also want to enable CUDA support
when compliling `dlib`.

```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_locations = face_recognition.face_locations(image, model="cnn")

# face_locations is now an array listing the co-ordinates of each face!
```

##### Automatically locate the facial features of a person in an image

```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)

# face_landmarks_list is now an array with the locations of each facial feature in each face.
# face_landmarks_list[0]['left_eye'] would be the location and outline of the first person's left eye.
```



##### Recognize faces in images and identify who they are

```python
import face_recognition

picture_of_me = face_recognition.load_image_file("me.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("unknown.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")
```


## Thanks, Happy Hacking!