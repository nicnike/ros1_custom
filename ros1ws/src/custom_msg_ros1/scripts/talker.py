#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from brics_actuator.msg import Poison 

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Poison, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Poison()
        msg.originator = "originator_ABC"
        msg.description = "description_DEF"
        msg.qos = 42.0
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.originator} {msg.description} {msg.qos}")


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
