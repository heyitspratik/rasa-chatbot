# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sanic.response import HTTPResponse
from rasa.core.channels.channel import InputChannel
import requests
import os
from slack import WebClient
from slack.errors import SlackApiError
from rasa_sdk.events import ConversationPaused, ConversationResumed, FollowupAction, Restarted
import json
import langid


class MyIO(InputChannel):
    def name() -> Text:
        """Name of your custom channel."""
        return "myio"


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # define language-specific responses
        responses = {
            'en': {
                'greet': 'utter_greet',
                'english': 'utter_english',
                'profile_menu': 'utter_profile_menu',
                'update_profile_picture': 'utter_update_profile_picture',
                'update_mobile': 'utter_update_mobile',
                'update_personal_details': 'utter_update_personal_details',
                'certificates': 'utter_certificates',
                'password_menu': 'utter_password_menu',
                'policy_menu': 'utter_policy_menu',
                'happy': 'utter_happy',
                'affirm': 'utter_affirm',
                'goodbye': 'utter_goodbye',
                'iamabot': 'utter_iamabot',
                'Thanks': 'utter_Thanks',
                'out_of_scope': 'utter_out_of_scope',
            },
            'hi': {
                'hindi': 'utter_hindi',
                'profile_menu_hindi': 'utter_profile_menu_hindi',
                'update_profile_picture_hindi': 'utter_update_profile_picture_hindi',
                'update_mobile_hindi': 'utter_update_mobile_hindi',
                'update_personal_details_hindi': 'utter_update_personal_details_hindi',
                'certificates_hindi': 'utter_certificates_hindi',
                'password_menu_hindi': 'utter_password_menu_hindi',
                'policy_menu_hindi': 'utter_policy_menu_hindi',
                'happy_hindi': 'utter_happy_hindi',
                'affirm_hindi': 'utter_affirm_hindi',
                'goodbye_hindi': 'utter_goodbye_hindi',
                'iamabot_hindi': 'utter_iamabot_hindi',
                'Thanks_hindi': 'utter_Thanks_hindi',
                'out_of_scope_hindi': 'utter_out_of_scope_hindi',
            },
            'mr': {
                'marathi': 'utter_marathi',
                'profile_menu_marathi': 'utter_profile_menu_marathi',
                'update_profile_picture_marathi': 'utter_update_profile_picture_marathi',
                'update_mobile_marathi': 'utter_update_mobile_marathi',
                'update_personal_details_marathi': 'utter_update_personal_details_marathi',
                'certificates_marathi': 'utter_certificates_marathi',
                'password_menu_marathi': 'utter_password_menu_marathi',
                'policy_menu_marathi': 'utter_policy_menu_marathi',
                'happy_marathi': 'utter_happy_marathi',
                'affirm_marathi': 'utter_affirm_marathi',
                'goodbye_marathi': 'utter_goodbye_marathi',
                'iamabot_marathi': 'utter_iamabot_marathi',
                'Thanks_marathi': 'utter_Thanks_marathi',
                'out_of_scope_marathi': 'utter_out_of_scope_marathi',
            },
            'te': {
                'telugu': 'utter_telugu',
                'profile_menu_telugu': 'utter_profile_menu_telugu',
                'update_profile_picture_telugu': 'utter_update_profile_picture_telugu',
                'update_mobile_telugu': 'utter_update_mobile_telugu',
                'update_personal_details_telugu': 'utter_update_personal_details_telugu',
                'certificates_telugu': 'utter_certificates_telugu',
                'password_menu_telugu': 'utter_password_menu_telugu',
                'policy_menu_telugu': 'utter_policy_menu_telugu',
                'happy_telugu': 'utter_happy_telugu',
                'affirm_telugu': 'utter_affirm_telugu',
                'goodbye_telugu': 'utter_goodbye_telugu',
                'iamabot_telugu': 'utter_iamabot_telugu',
                'Thanks_telugu': 'utter_Thanks_telugu',
                'out_of_scope_telugu': 'utter_out_of_scope_telugu',
            },
            
            # add more language codes and language-specific responses dictionaries here
        }
        
        # detect the language of the user input
        user_input = tracker.latest_message['text']
        lang, _ = langid.classify(user_input)
        
        # select the appropriate response based on the language and intent of the user input
        intent = tracker.latest_message['intent'].get('name')
        response_key = responses.get(lang, {}).get(intent, 'utter_default')
        dispatcher.utter_message(response_key)
        
        return []

    

    




