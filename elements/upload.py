import base64
import os
import random

from generator.generator import generated_file
from selenium_base.base import SeleniumBase


class UploadsDownloads(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.page_item = '#item-7'
        self.download = 'a[id="downloadButton"]'
        self.upload_file_control = 'input[id="uploadFile"]'
        self.uploaded_file_path = 'p[id="uploadedFilePath"]'
        self. download_file = 'a[download="sampleFile.jpeg"]'

    def find_item(self):
        page = self.is_visible('css', self.page_item)
        self.go_to_element(page)
        page.click()

    def upload_check(self):
        file_name, path = generated_file()
        self.is_present('css', self.upload_file_control).send_keys(path)
        os.remove(path)
        text = self.is_present('css', self.uploaded_file_path).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_files(self):
        link = self.is_present('css', self.download_file).get_attribute('href')
        link_base = base64.b64decode(link)
        #print(link_base)
        file = rf'C:\Users\ASUS\Downloads\filetest{random.randint(0, 999)}.jpg'
        with open(file, 'wb+') as f:
            offset = link_base.find(b'\x8af\xa0')
            f.write(link_base[offset:])
            check_file = os.path.exists(file)
            f.close()
        os.remove(file)
        return check_file



