import os
import logging

class Settings:
    def __init__(self) -> None:
        if os.path.isfile('api_key'):
            with open('api_key', 'r') as file:
                self.apikey=file.read()
        else:
            logging.error('Missing api_key file')
            exit()