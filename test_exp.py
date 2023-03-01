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

'''Drive And Turn

Make Cozmo drive forwards and then turn 90 degrees to the left.
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    for i in range(0,3):
        print(i,"\n")
    robot.play_anim_trigger(cozmo.anim.Triggers.NothingToDoBoredIdle, ignore_body_track=True, in_parallel=True).wait_for_completed()
    #robot.drive_straight(distance_mm(200), speed_mmps(50),in_parallel=True).wait_for_completed()


    robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True, in_parallel=True).wait_for_completed()
    #robot.drive_straight(distance_mm(200), speed_mmps(50),in_parallel=True).wait_for_completed()

    #robot.turn_in_place(degrees(180)).wait_for_completed()
    #robot.drive_straight(distance_mm(200), speed_mmps(50),in_parallel=True)
    robot.play_anim_trigger(cozmo.anim.Triggers.GuardDogPlayerSuccess, ignore_body_track=True, in_parallel=True).wait_for_completed()
    #cozmo.faces.FACIAL_EXPRESSION_HAPPY= 'happy'

cozmo.run_program(cozmo_program)
