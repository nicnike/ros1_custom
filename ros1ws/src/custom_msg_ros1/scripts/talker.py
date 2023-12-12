#!/usr/bin/env python
import rospy
from brics_actuator.msg import Poison

class PoisonPublisher(object):
    def __init__(self):
        self.publisher = rospy.Publisher('topic', Poison, queue_size=10)
        rospy.init_node('poison_publisher', anonymous=True)
        self.rate = rospy.Rate(10)  # 10hz

    def publish_message(self):
        msg = Poison()
        msg.originator = "originator_ABC"
        msg.description = "description_DEF"
        msg.qos = 42.0

        while not rospy.is_shutdown():
            self.publisher.publish(msg)
            rospy.loginfo("Publishing: originator: %s, description: %s, qos: %f", msg.originator, msg.description, msg.qos)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        publisher = PoisonPublisher()
        publisher.publish_message()
    except rospy.ROSInterruptException:
        pass
