# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from rasa.core.channels.channel import InputChannel


class MyIO(InputChannel):
    def name(self,Text):
        """Name of your custom channel."""
        return "myio"
