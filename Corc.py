from Keys import SkyBiometryKeys
from ImageUpload import ImageUpload
import requests
from colorama import init
from termcolor import colored


class Corc:

    def __init__(self):
        init()
        self.keys = SkyBiometryKeys()
        self.API_KEY = self.keys.API_KEY
        self.API_SECRET = self.keys.API_SECRET

    def face_detection(self, file_name):
        image_upload = ImageUpload()
        image_upload.generate_random_link()
        link = image_upload.cloudinary_upload(file_name)
        r = requests.post(self.keys.API_URL, data={
            'api_key': self.keys.API_KEY, 'api_secret': self.keys.API_SECRET, 'urls': link,
            'detect_all_feature_points': False, 'attributes': 'gender,glasses,smiling,lips,eyes,age,mood'})
        r_json = r.json()
        # Spaghetti code :)
        self.face = r_json['photos'][0]['tags'][0]['attributes']['face']['value']
        self.face_confidence = r_json['photos'][0]['tags'][0]['attributes']['face']['confidence']
        self.gender = r_json['photos'][0]['tags'][0]['attributes']['gender']['value']
        self.gender_confidence = r_json['photos'][0]['tags'][0]['attributes']['gender']['confidence']
        self.glasses = r_json['photos'][0]['tags'][0]['attributes']['glasses']['value']
        self.glasses_confidence = r_json['photos'][0]['tags'][0]['attributes']['glasses']['confidence']
        self.smiling = r_json['photos'][0]['tags'][0]['attributes']['smiling']['value']
        self.smiling_confidence = r_json['photos'][0]['tags'][0]['attributes']['smiling']['confidence']
        self.age_est = r_json['photos'][0]['tags'][0]['attributes']['age_est']['value']
        self.age_est_confidence = r_json['photos'][0]['tags'][0]['attributes']['age_est']['confidence']
        self.mood = r_json['photos'][0]['tags'][0]['attributes']['mood']['value']
        self.mood_confidence = r_json['photos'][0]['tags'][0]['attributes']['mood']['confidence']
        self.lips = r_json['photos'][0]['tags'][0]['attributes']['lips']['value']
        self.lips_confidence = r_json['photos'][0]['tags'][0]['attributes']['lips']['confidence']
        self.eyes = r_json['photos'][0]['tags'][0]['attributes']['eyes']['value']
        self.eyes_confidence = r_json['photos'][0]['tags'][0]['attributes']['eyes']['confidence']
        self.neutral_mood = r_json['photos'][0]['tags'][0]['attributes']['neutral_mood']['value']
        self.neutral_mood_confidence = r_json['photos'][0]['tags'][0]['attributes']['neutral_mood']['confidence']
        self.anger = r_json['photos'][0]['tags'][0]['attributes']['anger']['value']
        self.anger_confidence = r_json['photos'][0]['tags'][0]['attributes']['anger']['confidence']
        self.disgust = r_json['photos'][0]['tags'][0]['attributes']['disgust']['value']
        self.disgust_confidence = r_json['photos'][0]['tags'][0]['attributes']['disgust']['confidence']
        self.fear = r_json['photos'][0]['tags'][0]['attributes']['fear']['value']
        self.fear_confidence = r_json['photos'][0]['tags'][0]['attributes']['fear']['confidence']
        self.happiness = r_json['photos'][0]['tags'][0]['attributes']['happiness']['value']
        self.happiness_confidence = r_json['photos'][0]['tags'][0]['attributes']['happiness']['confidence']
        self.sadness = r_json['photos'][0]['tags'][0]['attributes']['sadness']['value']
        self.sadness_confidence = r_json['photos'][0]['tags'][0]['attributes']['sadness']['confidence']
        self.surprise = r_json['photos'][0]['tags'][0]['attributes']['surprise']['value']
        self.surprise_confidence = r_json['photos'][0]['tags'][0]['attributes']['surprise']['confidence']

    def show_features(self):
        print("Face: "+colored(self.face, 'red', 'on_white'))
        print("Gender: "+colored(self.gender, 'red', 'on_white'))
        print("Glasses: "+colored(self.glasses, 'red', 'on_white'))
        print("Smiling: "+colored(self.smiling, 'red', 'on_white'))
        print("Age Estimation: "+colored(self.age_est, 'red', 'on_white'))
        print("Mood: "+colored(self.mood, 'red', 'on_white'))
        print("Lips: "+colored(self.lips, 'red', 'on_white'))
        print("Eyes: "+colored(self.eyes, 'red', 'on_white'))
        print("Neutral Mood: "+colored(self.neutral_mood, 'red', 'on_white'))
        print("Anger: "+colored(self.anger, 'red', 'on_white'))
        print("Disgust: "+colored(self.disgust, 'red', 'on_white'))
        print("Fear: "+colored(self.fear, 'red', 'on_white'))
        print("Happiness: "+colored(self.happiness, 'red', 'on_white'))
        print("Sadness: "+colored(self.sadness, 'red', 'on_white'))
        print("Suprise: "+colored(self.surprise, 'red', 'on_white'))


corc = Corc()
corc.face_detection('elon.jpg')
corc.show_features()
