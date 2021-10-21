from django.db import models
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2, decode_predictions, preprocess_input


class Image(models.Model):
    photo = models.ImageField()
    classification = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.classification

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            image = load_img(path=self.photo.path, target_size=(299, 299))
            image_array = img_to_array(image)
            prediction = np.expand_dims(image_array, axis=0)
            preprocess_image = preprocess_input(prediction)
            image_model = InceptionResNetV2(weights='imagenet')
            data_prediction = image_model.predict(preprocess_image)
            decoded_data = decode_predictions(data_prediction)[0][0][1]
            self.classification = str(decoded_data)
        except Exception as e:
            print("Error Message", e)
        super().save(force_insert, force_update, using, update_fields)
