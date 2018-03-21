# The MIT License (MIT)	
# 
# Copyright (c) 2018 RHackrid
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from adapt.intent import IntentBuilder

from mycroft.util.log import getLogger
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.skills.context import *

LOGGER = getLogger(__name__)

class SillyNameMakerSkill(MycroftSkill):

    def __init__(self):
        super(SillyNameMakerSkill, self).__init__(name="SillyNameMakerSkill")

    @intent_handler(IntentBuilder("SillyNameMakerIntent").require("SillyNameMakerStart").build())
    @adds_context('SillyNameMakerContext')
    def handle_silly_name_maker_start(self, message):
        self.speak_dialog("hello", expect_response=True)
		
    @intent_handler(IntentBuilder("NumberIntent").require("LuckyNumber").require("SillyNameMakerContext").build())
    @adds_context('NumberContext')
    def handle_number(self, message):
        self.number = message.data.get("LuckyNumber")
        self.speak_dialog("question.color", expect_response=True)
        LOGGER.debug(self.number)

    @intent_handler(IntentBuilder("ColorIntent").require("FavoriteColor").require("NumberContext").build())
    @removes_context('NumberContext')
    @removes_context('SillyNameMakerContext')
    def handle_color(self, message):
        self.color = message.data.get("FavoriteColor")
        self.speak_dialog("result", data={"favorite_color": self.color, "lucky_number": self.number})
        LOGGER.debug(self.color)

    @removes_context('NumberContext')
    @removes_context('SillyNameMakerContext')
    def stop(self):
       pass

def create_skill():
    return SillyNameMakerSkill()
