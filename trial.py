import os
from os.path import join, dirname
from dotenv import load_dotenv

import logging

from slack_sdk import WebClient


class Trial:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        load_dotenv(verbose=True)
        dotenv = join(dirname(__file__), '.env')
        load_dotenv(dotenv)

        self.API_TOKEN = os.environ['API_TOKEN']
        self.client = WebClient(self.API_TOKEN)

    
    def send_text_msg(self):
        res = self.client.chat_postMessage(
                channel='#random',
                text='HelloWorld!'
                )


if __name__ == '__main__':
    trl = Trial()
    trl.send_text_msg()
