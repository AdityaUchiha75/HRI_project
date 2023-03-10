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
import asyncio

def find_and_displace_cube(robot: cozmo.robot.Robot):
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    # try to find a block
    cube = None

    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        print("Found cube", cube)

    except asyncio.TimeoutError:
        print("Didn't find a cube :-(")

    finally:
        # whether we find it or not, we want to stop the behavior
        look_around.stop()

    if cube is None:
        robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail)
        return

    print("Yay, found cube")

    cube.set_lights(cozmo.lights.green_light.flash())

    anim = robot.play_anim_trigger(cozmo.anim.Triggers.BlockReact)
    anim.wait_for_completed()


    action = robot.pickup_object(cube)
    print("got action", action)
    result = action.wait_for_completed(timeout=30)
    print("got action result", result)

    robot.turn_in_place(degrees(90)).wait_for_completed()

    action = robot.place_object_on_ground_here(cube)
    print("got action", action)
    result = action.wait_for_completed(timeout=30)
    print("got action result", result)

    anim = robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin)
    cube.set_light_corners(None, None, None, None)
    anim.wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()


def cozmo_program(robot: cozmo.robot.Robot):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    # robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

    # # Turn 90 degrees to the left.
    # # Note: To turn to the right, just use a negative number.
    # robot.turn_in_place(degrees(90)).wait_for_completed(){
    robot.play_anim_trigger(cozmo.anim.Triggers.NothingToDoBoredIdle, ignore_body_track=True).wait_for_completed()
    robot.drive_straight(distance_mm(500), speed_mmps(50)).wait_for_completed()
    robot.drive_straight(distance_mm(300), speed_mmps(50)).wait_for_completed()
    #robot expression
    find_and_displace_cube(robot)
    robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True).wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(50)).wait_for_completed()
    robot.drive_straight(distance_mm(500), speed_mmps(50)).wait_for_completed()
    #cond 3
    # robot.drive_straight(distance_mm(500), speed_mmps(50)).wait_for_completed()
    # robot.drive_straight(distance_mm(300), speed_mmps(50)).wait_for_completed()
    # robot.turn_in_place(degrees(180)).wait_for_completed()
    # robot.drive_straight(distance_mm(300), speed_mmps(50)).wait_for_completed()

    # robot.turn_in_place(degrees(90)).wait_for_completed()
    # robot.drive_straight(distance_mm(500), speed_mmps(50)).wait_for_completed()
    # robot.turn_in_place(degrees(90)).wait_for_completed()
    # robot.drive_straight(distance_mm(500), speed_mmps(50)).wait_for_completed()
    # robot.turn_in_place(degrees(90)).wait_for_completed()
    # robot.drive_straight(distance_mm(500), speed_mmps(50)).wait_for_completed()
    # robot.turn_in_place(degrees(-90)).wait_for_completed()
    # #robot expression
    #robot pick and displace cube
    robot.drive_straight(distance_mm(200), speed_mmps(50)).wait_for_completed()

cozmo.run_program(cozmo_program)
