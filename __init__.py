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
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.skills.context import *

class SillyNameMakerSkill(MycroftSkill):

    def __init__(self):
        super(SillyNameMakerSkill, self).__init__(name="SillyNameMakerSkill")

    @intent_handler(IntentBuilder("SillyNameMakerIntent").require("SillyNameMakerStart").build())
    @adds_context('SillyNameMakerContext')
    def handle_silly_name_maker_start(self, message):
        self.speak('Hi! Welcome to Silly Name Maker! Lets get started. What is your lucky number?', expect_response=True)
		
    @intent_handler(IntentBuilder("NumberIntent").require("LuckyNumber").require("SillyNameMakerContext").build())
    @adds_context('NumberContext')
    def handle_number(self, message):
        self.number = message.data.get("LuckyNumber")
        self.speak('What is your favorite color?', expect_response=True)
        print(self.number)

    @intent_handler(IntentBuilder("ColorIntent").require("FavoriteColor").require("NumberContext").build())
    @removes_context('NumberContext')
    def handle_color(self, message):
        self.color = message.data.get("FavoriteColor")
        self.speak('Alright, your silly name is {} {}! I hope you like it. See you next time.'.format(self.color, self.number), expect_response=False)
        print(self.color)

    @removes_context('NumberContext')
    @removes_context('SillyNameMakerContext')
    def stop(self):
       pass

def create_skill():
    return SillyNameMakerSkill()
