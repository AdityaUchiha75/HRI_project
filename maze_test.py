import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import asyncio
import logging


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
        #robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail)
        return

    print("Yay, found cube")

    #cube.set_lights(cozmo.lights.green_light.flash())

    anim = robot.play_anim_trigger(cozmo.anim.Triggers.BlockReact, ignore_body_track=True)
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

    #anim = robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True)
    #cube.set_light_corners(None, None, None, None)
    #anim.wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()


def part1(robot: cozmo.robot.Robot):
    global flag
    robot.drive_straight(distance_mm(200), speed_mmps(75),in_parallel=True).wait_for_completed() #first_bit
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabScaredCozmo, ignore_body_track=True, in_parallel=True).wait_for_completed()
    out_ch='R'
    if out_ch=='R':
        logging.info("Outcome based on the choices made: "+"Reward")
        robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True, in_parallel=True).wait_for_completed()
        #robot expression
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabThinking, ignore_body_track=True, in_parallel=True).wait_for_completed()
        find_and_displace_cube(robot)
        robot.play_anim_trigger(cozmo.anim.Triggers.DanceMambo, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(100), speed_mmps(75)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.drive_straight(distance_mm(150), speed_mmps(75)).wait_for_completed()
    elif out_ch=='B_C':
        logging.info("Outcome based on the choices made: "+"Betrayal")
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated, ignore_body_track=True, in_parallel=True).wait_for_completed()
        #robot expression
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWhoa, ignore_body_track=True, in_parallel=True).wait_for_completed()
        find_and_displace_cube(robot)
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabBored, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(100), speed_mmps(75)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.drive_straight(distance_mm(150), speed_mmps(75)).wait_for_completed()

    elif out_ch=='B_U':
        logging.info("Outcome based on the choices made: "+"Betrayal")
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabCurious, ignore_body_track=True, in_parallel=True).wait_for_completed()
        #robot expression
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabConducting, ignore_body_track=True, in_parallel=True).wait_for_completed()
        find_and_displace_cube(robot)
        robot.play_anim_trigger(cozmo.anim.Triggers.DanceMambo, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(100), speed_mmps(75)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.drive_straight(distance_mm(150), speed_mmps(75)).wait_for_completed()

    else:
        logging.info("Outcome based on the choices made: "+"Punishment")
        robot.play_anim_trigger(cozmo.anim.Triggers.DriveStartAngry, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.turn_in_place(degrees(-90)).wait_for_completed()
        robot.drive_straight(distance_mm(100), speed_mmps(75)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDejected, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(150), speed_mmps(75)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.drive_straight(distance_mm(250), speed_mmps(75)).wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.DriveEndAngry, ignore_body_track=True, in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()

def part2(robot: cozmo.robot.Robot):
    global flag
    robot.drive_straight(distance_mm(100), speed_mmps(75),in_parallel=True).wait_for_completed() #first_bit
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabScaredCozmo, ignore_body_track=True, in_parallel=True).wait_for_completed()
    out_ch='R'
    if out_ch=='R':
        logging.info("Outcome based on the choices made: "+"Reward")
        robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True, in_parallel=True).wait_for_completed()
        #robot expression
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabThinking, ignore_body_track=True, in_parallel=True).wait_for_completed()
        find_and_displace_cube(robot)
        robot.play_anim_trigger(cozmo.anim.Triggers.DanceMambo, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(200), speed_mmps(75)).wait_for_completed()
        
    elif out_ch=='B_C':
        logging.info("Outcome based on the choices made: "+"Betrayal")
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated, ignore_body_track=True, in_parallel=True).wait_for_completed()
        #robot expression
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWhoa, ignore_body_track=True, in_parallel=True).wait_for_completed()
        find_and_displace_cube(robot)
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabBored, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(200), speed_mmps(75)).wait_for_completed()

    elif out_ch=='B_U':
        logging.info("Outcome based on the choices made: "+"Betrayal")
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabCurious, ignore_body_track=True, in_parallel=True).wait_for_completed()
        #robot expression
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabConducting, ignore_body_track=True, in_parallel=True).wait_for_completed()
        find_and_displace_cube(robot)
        robot.play_anim_trigger(cozmo.anim.Triggers.DanceMambo, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(200), speed_mmps(75)).wait_for_completed()
    else:
        logging.info("Outcome based on the choices made: "+"Punishment")
        robot.play_anim_trigger(cozmo.anim.Triggers.DriveStartAngry, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.turn_in_place(degrees(-90)).wait_for_completed()
        robot.drive_straight(distance_mm(250), speed_mmps(75)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.drive_straight(distance_mm(150), speed_mmps(75)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.drive_straight(distance_mm(250), speed_mmps(75)).wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.DriveEndAngry, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.turn_in_place(degrees(-90)).wait_for_completed()
        robot.drive_straight(distance_mm(100), speed_mmps(75)).wait_for_completed()

def part3(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(70), speed_mmps(75)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWhoa, ignore_body_track=True, in_parallel=True).wait_for_completed()
    #left_or_right
    robot.turn_in_place(degrees(45)).wait_for_completed()
    robot.drive_straight(distance_mm(40), speed_mmps(75)).wait_for_completed()
    robot.turn_in_place(degrees(-45)).wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(75)).wait_for_completed()
    robot.turn_in_place(degrees(-45)).wait_for_completed()
    robot.drive_straight(distance_mm(40), speed_mmps(75)).wait_for_completed()
    robot.turn_in_place(degrees(45)).wait_for_completed()
    robot.drive_straight(distance_mm(50), speed_mmps(75)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

def part4(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(200), speed_mmps(75)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabScaredCozmo, ignore_body_track=True, in_parallel=True).wait_for_completed()
    out_ch='R'
    if out_ch=='R':
        logging.info("Outcome based on the choices made: "+"Reward")
        robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True, in_parallel=True).wait_for_completed()
        #robot expression
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabThinking, ignore_body_track=True, in_parallel=True).wait_for_completed()
        find_and_displace_cube(robot)
        robot.play_anim_trigger(cozmo.anim.Triggers.DanceMambo, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(150), speed_mmps(75)).wait_for_completed()
       
    elif out_ch=='B_C':
        logging.info("Outcome based on the choices made: "+"Betrayal")
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabFrustrated, ignore_body_track=True, in_parallel=True).wait_for_completed()
        #robot expression
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWhoa, ignore_body_track=True, in_parallel=True).wait_for_completed()
        find_and_displace_cube(robot)
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabBored, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(150), speed_mmps(75)).wait_for_completed()

    elif out_ch=='B_U':
        logging.info("Outcome based on the choices made: "+"Betrayal")
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabCurious, ignore_body_track=True, in_parallel=True).wait_for_completed()
        #robot expression
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabConducting, ignore_body_track=True, in_parallel=True).wait_for_completed()
        find_and_displace_cube(robot)
        robot.play_anim_trigger(cozmo.anim.Triggers.DanceMambo, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.drive_straight(distance_mm(150), speed_mmps(75)).wait_for_completed()

    else:
        logging.info("Outcome based on the choices made: "+"Punishment")
        robot.play_anim_trigger(cozmo.anim.Triggers.DriveStartAngry, ignore_body_track=True, in_parallel=True).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.drive_straight(distance_mm(250), speed_mmps(75)).wait_for_completed()
        robot.turn_in_place(degrees(-90)).wait_for_completed()
        robot.drive_straight(distance_mm(150), speed_mmps(75)).wait_for_completed()


cozmo.run_program(part1)