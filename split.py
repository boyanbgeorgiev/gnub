import os
import shutil
import random

shark_types = ['hammerhead', 'bull', 'nurse', 'mako', 'blue', 'lemon', 'basking', 'tiger', 'whale', 'whitetip', 'thresher', 'sand tiger', 'white', 'blacktip']

for shark in shark_types:
    images = os.listdir('sharks/' + shark)
    random.shuffle(images)
    num_images = len(images)
    num_train = int(num_images * 0.8)
    num_validation = num_images - num_train
    train_images = images[:num_train]
    validation_images = images[num_train:]
    if not os.path.exists('data/train/' + shark):
        os.makedirs('data/train/' + shark)
    if not os.path.exists('data/validation/' + shark):
        os.makedirs('data/validation/' + shark)
    for image in train_images:
        shutil.move('sharks/' + shark + '/' + image, 'data/train/' + shark + '/' + image)
    for image in validation_images:
        shutil.move('sharks/' + shark + '/' + image, 'data/validation/' + shark + '/' + image)
    os.rmdir('sharks/' + shark) 