import face_recognition
from PIL import Image, ImageDraw

image_of_cumberbatch = face_recognition.load_image_file('./images/known_faces/Benedict Cumberbatch.jpg')
cumberbatch_face_encoding = face_recognition.face_encodings(image_of_cumberbatch)[0]

image_of_evans = face_recognition.load_image_file('./images/known_faces/Chris Evans.jpg')
evans_face_encoding = face_recognition.face_encodings(image_of_evans)[0]

image_of_hemsworth = face_recognition.load_image_file('./images/known_faces/Chris Hemsworth.jpg')
hemsworth_face_encoding = face_recognition.face_encodings(image_of_hemsworth)[0]

image_of_olsen = face_recognition.load_image_file('./images/known_faces/Elizabeth Olsen.jpg')
olsen_face_encoding = face_recognition.face_encodings(image_of_olsen)[0]

image_of_ruffalo = face_recognition.load_image_file('./images/known_faces/Mark Ruffalo.jpg')
ruffalo_face_encoding = face_recognition.face_encodings(image_of_ruffalo)[0]

image_of_downey = face_recognition.load_image_file('./images/known_faces/Robert Downey Jr..jpg')
downey_face_encoding = face_recognition.face_encodings(image_of_downey)[0]

# image_of_stan = face_recognition.load_image_file('./images/known_faces/Sebastian Stan.jpg')
# stan_face_encoding = face_recognition.face_encodings(image_of_stan)[0]

image_of_hiddleston = face_recognition.load_image_file('./images/known_faces/Tom Hiddleston.jpg')
hiddleston_face_encoding = face_recognition.face_encodings(image_of_hiddleston)[0]

image_of_holland = face_recognition.load_image_file('./images/known_faces/Tom Holland.jpg')
holland_face_encoding = face_recognition.face_encodings(image_of_holland)[0]

#Array of encodings of known faces and names
known_face_encodings = [
    cumberbatch_face_encoding,
    evans_face_encoding,
    hemsworth_face_encoding,
    olsen_face_encoding,
    ruffalo_face_encoding,
    downey_face_encoding,
    # stan_face_encoding,
    hiddleston_face_encoding,
    holland_face_encoding
]

known_face_names = [
    "Benedict Cumberbatch",
    "Chris Evans",
    "Chris Hemsworth",
    "Elizabeth Olsen",
    "Mark Ruffalo",
    "Robert Downey Jr.",
    # "Sebastian Stan",
    "Tom Hiddleston",
    "Tom Holland"
]

#Load image to find faces
test_image = face_recognition.load_image_file('./images/group/marvel group 2.jpg')

#Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

#Covert to PIL Format
pil_image = Image.fromarray(test_image)

#Create ImageDraw instance
draw = ImageDraw.Draw(pil_image)

#Loop through known faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    match = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    #If face matches
    if True in match:
        first_match_index = match.index(True)
        name = known_face_names[first_match_index]

    #Draw box outline around face
    draw.rectangle(((left, top), (right, bottom)), outline = (255,0,0))

    #Draw name label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill = (255,0,0), outline = (255,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill = (255,255,255,255))

del draw

#Display image with draws
pil_image.show()