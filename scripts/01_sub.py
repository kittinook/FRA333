#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
# EDIT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


class SubscriberClass(Node):

    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            Twist,
            "/turtle1/cmd_vel",
            self.listener_callback,
            10
        )
        # EDIT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def listener_callback(self, msg):
        print(msg)
        # EDIT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # pass


def main(args=None):
    rclpy.init(args=args)

    # EDIT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    subscriber = SubscriberClass()
    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

