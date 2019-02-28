#Dash Buttons
#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Hello World

Make Cozmo communicate with other Cozmo robots
'''

import cozmo
import socket
import errno
from socket import error as socket_error

#need to get movement info
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket_error as msg:
        robot.say_text("socket failed" + msg).wait_for_completed()
    ip = "10.0.1.10"
    port = 5000
    
    try:
        s.connect((ip, port))
    except socket_error as msg:
        robot.say_text("socket failed to bind").wait_for_completed()
    cont = True
    
    robot.say_text("alex").wait_for_completed()    
    
    #SET COZMO's NAME
    BrandName = 'maxwell'
    while cont:
        bytedata = s.recv(4048)
        #data = str(bytedata)
        data = bytedata.decode('utf-8')
        if not data:
            cont = False
            s.close()
            quit()
        else:
            #---------------------------------------------------------
            #This is where you need to adjust the program
            #---------------------------------------------------------

            instructions = data.split(';')
            instructions = instructions[0:-1]
            print(instructions)
            
            for item in instructions:
                if item == "maxwell":
                    #turn
                    robot.say_text("maxwell").wait_for_completed()
                if item == "cottonelle":
                    robot.say_text("cottonelle").wait_for_completed()
                if item == "poof":
                    robot.say_text("poof").wait_for_completed()
                if item == "quest":
                    robot.say_text("quest").wait_for_completed()
                if item == "gatorade":
                    robot.say_text("gatorade").wait_for_completed()
                if item == "emergency":
                    robot.say_text("emergency").wait_for_completed()
                if item == "temptation":
                    robot.say_text("temptation").wait_for_completed()
                if item == "elements":
                    robot.say_text("elements").wait_for_completed()
                if item == "sky":
                    robot.say_text("sky").wait_for_completed()
                if item == "human":
                    robot.say_text("human").wait_for_completed()
                if item == "kitty":
                    robot.say_text("kitty").wait_for_completed()
                if item == "mashup":
                    robot.say_text("mashup").wait_for_completed()
                if item == "mac_cheese":
                    robot.say_text("mac and cheese").wait_for_completed()

cozmo.run_program(cozmo_program)
