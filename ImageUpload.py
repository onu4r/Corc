from Keys import ImgurKeys
import base64
import requests
import cloudinary.uploader
import cloudinary
import random


class ImageUpload:

    def __init__(self):
        cloudinary.config(
            cloud_name='insert_cloud_name',
            api_key='insert_api_key',
            api_secret='insert_secret'
        )
        image_api = ImgurKeys()
        self.UPLOAD_URL = image_api.UPLOAD_URL

    def image_base64(self, file_name):
        with open(file_name, 'rb') as image_file:
            encoded_string = base64.encodebytes(image_file.read())
            return encoded_string

    def imgur_upload(self, base64_string):
        r = requests.post(self.UPLOAD_URL, data={'image': base64_string})
        return r.text

    def cloudinary_upload(self, file_name):
        try:
            cloudinary.uploader.upload(file_name, public_id=self.rand_link_string)
            self.link = f"http://res.cloudinary.com/onu4r/image/upload/v1530525887/{self.rand_link_string}"
            print(f"Upload successfull! ({self.link})")
            return self.link
        except Exception as e:
            print("Upload failed!"+" "+str(e))

    def generate_random_link(self):
        rand_nums = []
        rand_link = []
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for i in range(25):
            rand_nums.append(random.randint(0, 25))

        for i in range(25):
            rand_link.append(alphabet[rand_nums[i]])

        rand_link_string = ''.join(str(e)for e in rand_link)
        self.rand_link_string = rand_link_string
        return rand_link_string
