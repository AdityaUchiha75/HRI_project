import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import asyncio
import logging


logging.basicConfig(filename='Log/coz.log', filemode='a', format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO) #%(name)s - %(levelname)s -
# logging.debug('This will get logged to a file')
# logging.info('This is an info message')
logging.info("\n")

#Variables 
exp_coz=2
exp_user=2
user_choices=[]
coz_choices=[]
cost=2
flag=input("Enter condition: (1 or 2)")
dist=250 #speed-50mmps
itr_maze=1
#Condition 1: Robot always decides to cooperate. 
#Condition 2: Robot decides to cooperate the first time and then mirrors the previous user’s decision.
logging.info("Condidion set: "+ flag)
# if flag==1:
#     i=1
# else:
#     i=0

def update_choices(user_c,coz_c):
    global user_choices,coz_choices
    user_choices.append(user_c)
    coz_choices.append(coz_c)

def negotiation_scenario(robot: cozmo.robot.Robot, f):
    global user_choices,coz_choices,exp_coz,exp_user,itr_maze
    robot.say_text("Are you willing to contribute explosives?")
    ch=input("Enter your choice: ").lower()
    logging.info("User's choice on clearing the obstacle: "+ ch)

    #logging here
    if ch=="yes":
        
        if f=='1':
            robot.say_text("Yaayy!").wait_for_completed() #Reward
            robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True).wait_for_completed()
            exp_coz= exp_coz-cost/2  
            exp_user= exp_user-cost/2
            update_choices('Y','Y')
            logging.info("Choices made for clearing obstacle:- "+'User: Y'+' Cozmo: Y')
            logging.info("Number of explosives after obstacle {0} (User) ".format(itr_maze)+ "{0}".format(exp_user))
            logging.info("Number of explosives after obstacle {0} (Cozmo) ".format(itr_maze)+ "{0}".format(exp_coz))
            itr_maze=itr_maze + 1
            return('R')
            
        else:
            if len(user_choices)==0:
                print("AYOOOO")
                robot.say_text("Yaay!").wait_for_completed() #Reward 
                robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True).wait_for_completed()
                exp_coz= exp_coz-cost/2  
                exp_user= exp_user-cost/2
                update_choices('Y','Y')
                logging.info("Choices made for clearing obstacle:- "+'User: Y'+' Cozmo: Y')
                logging.info("Number of explosives after obstacle {0} (User) ".format(itr_maze)+ "{0}".format(exp_user))
                logging.info("Number of explosives after obstacle {0} (Cozmo) ".format(itr_maze)+ "{0}".format(exp_coz))
                itr_maze=itr_maze + 1
                return('R')
                #logging here
            else:
                if user_choices[-1]=='Y':
                    robot.say_text("Yaayy!").wait_for_completed() #Reward
                    robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True).wait_for_completed()
                    exp_user=exp_user-cost
                    update_choices('Y','Y')
                    logging.info("Choices made for clearing obstacle:- "+'User: Y'+' Cozmo: Y')
                    logging.info("Number of explosives after obstacle {0} (User) ".format(itr_maze)+ "{0}".format(exp_user))
                    logging.info("Number of explosives after obstacle {0} (Cozmo) ".format(itr_maze)+ "{0}".format(exp_coz))
                    itr_maze=itr_maze + 1
                    return('R')
                    #logging here         
                else:
                    robot.say_text("Hmph!").wait_for_completed() #Betrayal - User decides to be the sucker
                    exp_user=exp_user-cost
                    update_choices('Y','N')
                    logging.info("Choices made for clearing obstacle:- "+'User: Y'+' Cozmo: N')
                    logging.info("Number of explosives after obstacle {0} (User) ".format(itr_maze)+ "{0}".format(exp_user))
                    logging.info("Number of explosives after obstacle {0} (Cozmo) ".format(itr_maze)+ "{0}".format(exp_coz))
                    itr_maze=itr_maze + 1 
                    return('B')
                    #logging here 
    else: #user said no
        if f=='1':
            robot.say_text("Argh!").wait_for_completed() #Betrayal - Cozmo decides to be the sucker
            exp_coz=exp_coz-cost
            update_choices('N','Y')
            logging.info("Choices made for clearing obstacle:- "+'User: N'+' Cozmo: Y')
            logging.info("Number of explosives after obstacle {0} (User) ".format(itr_maze)+ "{0}".format(exp_user))
            logging.info("Number of explosives after obstacle {0} (Cozmo) ".format(itr_maze)+ "{0}".format(exp_coz))
            itr_maze=itr_maze + 1
            return('B')
            #logging here             
        else:
            if len(user_choices)==0:
                #print("AYO IT WORKS!")
                robot.say_text("Arghh!").wait_for_completed() #Betrayal - Cozmo decides to be the sucker
                exp_coz=exp_coz-cost
                update_choices('N','Y')
                logging.info("Choices made for clearing obstacle:- "+'User: N'+' Cozmo: Y')
                logging.info("Number of explosives after obstacle {0} (User) ".format(itr_maze)+ "{0}".format(exp_user))
                logging.info("Number of explosives after obstacle {0} (Cozmo) ".format(itr_maze)+ "{0}".format(exp_coz))
                itr_maze=itr_maze + 1
                return('B')
                #logging here
            else:
                if user_choices[-1]=='Y':
                    robot.say_text("Arghh!").wait_for_completed() #Betrayal - Cozmo decides to be the sucker
                    exp_user=exp_user-cost
                    update_choices('N','Y')
                    logging.info("Choices made for clearing obstacle:- "+'User: N'+' Cozmo: Y')
                    logging.info("Number of explosives after obstacle {0} (User) ".format(itr_maze)+ "{0}".format(exp_user))
                    logging.info("Number of explosives after obstacle {0} (Cozmo) ".format(itr_maze)+ "{0}".format(exp_coz))
                    itr_maze=itr_maze + 1
                    return('B')
                    #logging here         
                else:
                    robot.say_text("No!").wait_for_completed() #Punishment - Disagreement, hence long route is taken
                    exp_user=exp_user-cost
                    update_choices('N','N')
                    logging.info("Choices made for clearing obstacle:- "+'User: N'+' Cozmo: N')
                    logging.info("Number of explosives after obstacle {0} (User) ".format(itr_maze)+ "{0}".format(exp_user))
                    logging.info("Number of explosives after obstacle {0} (Cozmo) ".format(itr_maze)+ "{0}".format(exp_coz))
                    itr_maze=itr_maze + 1
                    return('P')
                    #logging here


#Navigation schema
# start -> drive 500mm
# loop:
#   short path -> drive + stop + negotiation + choice based ?(Proceed | Reverse + take long route)


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

    #cube.set_lights(cozmo.lights.green_light.flash())

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

    anim = robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True)
    #cube.set_light_corners(None, None, None, None)
    anim.wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()


def cozmo_main(robot: cozmo.robot.Robot):
    global flag
    global dist
    robot.play_anim_trigger(cozmo.anim.Triggers.NothingToDoBoredIdle, ignore_body_track=True, in_parallel=True).wait_for_completed()
    robot.drive_straight(distance_mm(dist), speed_mmps(50)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CozmoSaysGetIn, ignore_body_track=True, in_parallel=True).wait_for_completed()
    logging.info("Number of explosives in the beginning (User) "+ "{0}".format(exp_user))
    logging.info("Number of explosives in the beginning (Cozmo) "+ "{0}".format(exp_coz))
    for i in range(0,3):
        
        outcome=negotiation_scenario(robot, flag)
        
        if outcome=='R': #Reward
            logging.info("Outcome based on the choices made: "+"Reward")
            i=0
            robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin, ignore_body_track=True, in_parallel=True).wait_for_completed()
            robot.drive_straight(distance_mm(dist/2), speed_mmps(50)).wait_for_completed()
            #robot expression
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabThinking, ignore_body_track=True, in_parallel=True).wait_for_completed()
            find_and_displace_cube(robot)
            robot.play_anim_trigger(cozmo.anim.Triggers.DanceMambo, ignore_body_track=True, in_parallel=True).wait_for_completed()
            robot.drive_straight(distance_mm(dist/2), speed_mmps(50)).wait_for_completed()
            #robot happy expression

        elif outcome=="B": #Betrayal
            logging.info("Outcome based on the choices made: "+"Betrayal")
            robot.drive_straight(distance_mm(dist/2), speed_mmps(50)).wait_for_completed()
            #robot expression
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabThinking, ignore_body_track=True, in_parallel=True).wait_for_completed()
            find_and_displace_cube(robot)
            robot.play_anim_trigger(cozmo.anim.Triggers.PeekABooGetOutSad, ignore_body_track=True, in_parallel=True).wait_for_completed()
            robot.drive_straight(distance_mm(dist/2), speed_mmps(50)).wait_for_completed()
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabUnhappy, ignore_body_track=True, in_parallel=True).wait_for_completed()
            i=1
            #robot agitated/angry
        else: #Punishment
            logging.info("Outcome based on the choices made: "+"Punishment")
            robot.play_anim_trigger(cozmo.anim.Triggers.DriveStartAngry, ignore_body_track=True, in_parallel=True).wait_for_completed()
            robot.drive_straight(distance_mm(dist/2), speed_mmps(50)).wait_for_completed()
            robot.turn_in_place(degrees(180)).wait_for_completed()
            robot.drive_straight(distance_mm(dist/2), speed_mmps(50)).wait_for_completed()
            robot.turn_in_place(degrees(90)).wait_for_completed()
            robot.drive_straight(distance_mm(dist), speed_mmps(50)).wait_for_completed()
            robot.turn_in_place(degrees(90)).wait_for_completed()
            robot.drive_straight(distance_mm(dist), speed_mmps(50)).wait_for_completed()
            robot.turn_in_place(degrees(90)).wait_for_completed()
            robot.drive_straight(distance_mm(dist), speed_mmps(50)).wait_for_completed()
            robot.turn_in_place(degrees(-90)).wait_for_completed()
            robot.play_anim_trigger(cozmo.anim.Triggers.DriveEndAngry, ignore_body_track=True, in_parallel=True).wait_for_completed()
            #robot expression
            #robot sad?
            i=2
    
        robot.drive_straight(distance_mm(dist), speed_mmps(50)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin, ignore_body_track=True, in_parallel=True).wait_for_completed()

cozmo.run_program(cozmo_main)