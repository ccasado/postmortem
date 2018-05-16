# -*- coding: utf-8 -*-
from slackclient import SlackClient
import os
from django.conf import settings

def slack(message):
    slack_token = os.environ['SLACK_TOKEN']
    sc = SlackClient(slack_token)

    sc.api_call(
        "chat.postMessage",
        channel=settings.CHANNEL,
        text=message
    )