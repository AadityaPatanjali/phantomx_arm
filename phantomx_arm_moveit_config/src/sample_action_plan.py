#!/usr/bin/env python

import roslib; roslib.load_manifest('simple_arm_server')
import rospy
import sys

import tf
from tf.transformations import euler_from_quaternion, quaternion_from_euler

from simple_arm_server.msg import *
from simple_arm_server.srv import * 

if __name__ == '__main__':
    rospy.init_node('simple_arm_server_test')
    rospy.wait_for_service('simple_arm_server/move')
    move_srv = rospy.ServiceProxy('simple_arm_server/move', MoveArm) 

    req = MoveArmRequest()  
    req.header.frame_id = "arm_base_link"
 
    action = ArmAction()
    action.type = ArmAction.MOVE_ARM
    action.goal.position.x = 0.2
    action.goal.position.y = -0.09
    action.goal.position.z = .1
    q = quaternion_from_euler(0.0, 1.57, 0.0, 'sxyz')
    action.goal.orientation.x = q[0]
    action.goal.orientation.y = q[1]
    action.goal.orientation.z = q[2]
    action.goal.orientation.w = q[3]
    action.move_time = rospy.Duration(5.0)
    req.goals.append(action)

    action = ArmAction()
    action.type = ArmAction.MOVE_GRIPPER
    action.command = 0.03
    action.move_time = rospy.Duration(1.0)
    req.goals.append(action)

    action = ArmAction()
    action.type = ArmAction.MOVE_ARM
    action.goal.position.x = 0.2
    action.goal.position.y = -0.09
    action.goal.position.z = .04
    q = quaternion_from_euler(0.0, 1.57, 0.0, 'sxyz')
    action.goal.orientation.x = q[0]
    action.goal.orientation.y = q[1]
    action.goal.orientation.z = q[2]
    action.goal.orientation.w = q[3]
    action.move_time = rospy.Duration(1.0)
    req.goals.append(action)

    action = ArmAction()
    action.type = ArmAction.MOVE_GRIPPER
    action.command = 0.0254
    action.move_time = rospy.Duration(2.0)
    req.goals.append(action)

    action = ArmAction()
    action.type = ArmAction.MOVE_ARM
    action.goal.position.x = 0.2
    action.goal.position.y = -0.09
    action.goal.position.z = .1
    q = quaternion_from_euler(0.0, 1.57, 0.0, 'sxyz')
    action.goal.orientation.x = q[0]
    action.goal.orientation.y = q[1]
    action.goal.orientation.z = q[2]
    action.goal.orientation.w = q[3]
    action.move_time = rospy.Duration(1.0)
    req.goals.append(action)

    action = ArmAction()
    action.type = ArmAction.MOVE_ARM
    action.goal.position.x = 0.2
    action.goal.position.y = 0.09
    action.goal.position.z = .1
    q = quaternion_from_euler(0.0, 1.57, 0.0, 'sxyz')
    action.goal.orientation.x = q[0]
    action.goal.orientation.y = q[1]
    action.goal.orientation.z = q[2]
    action.goal.orientation.w = q[3]
    action.move_time = rospy.Duration(5.0)
    req.goals.append(action)
    
    action = ArmAction()
    action.type = ArmAction.MOVE_GRIPPER
    action.command = 0.03
    action.move_time = rospy.Duration(2.0)
    req.goals.append(action)

    action = ArmAction()
    action.type = ArmAction.MOVE_GRIPPER
    action.command = 0.0254
    action.move_time = rospy.Duration(1.0)
    req.goals.append(action)

    try:
        r = move_srv(req)
        print r
    except rospy.ServiceException, e:
        print "Service did not process request: %s"%str(e)
