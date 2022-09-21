#!/usr/bin/env python
from __future__ import absolute_import

import rospy
import unittest
from std_msgs.msg import UInt16

from io_manager.io_listener import IoListener


class TestIoListener(unittest.TestCase):

    # reference: https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass
    @classmethod
    def setUpClass(cls) -> None:
        cls.input_pubs = [rospy.Publisher(
            'io/input/port%d' % (i), UInt16, queue_size=10) for i in range(1, 9)]
        cls.output_pubs = [rospy.Publisher(
            'io/output/port%d' % (i), UInt16, queue_size=10) for i in range(1, 9)]
        cls.io_listener = IoListener()
        rospy.sleep(1)  # wait of initialization

    # reference: https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    def setUp(self) -> None:
        # reset inputs and outputs before each test fixture
        self.io_listener.reset_inputs_outputs()

    def test_input_callback(self):
        inputs = [801, 37, 55, 67, 94, 131, 153, 155]
        for i in range(8):
            self.input_pubs[i].publish(UInt16(data=inputs[i]))
            rospy.sleep(0.2)  # give some time for callback function to execute
        self.assertEqual(self.io_listener.get_inputs(), inputs)

    def test_output_callback(self):
        outputs = [31, 13, 512, 127, 92, 121, 413, 515]
        for i in range(8):
            self.output_pubs[i].publish(UInt16(data=outputs[i]))
            rospy.sleep(0.2)  # give some time for callback function to execute
        self.assertEqual(self.io_listener.get_outputs(), outputs)


if __name__ == "__main__":
    import rostest
    # When publisher/subscriber involved, we have to init a ROS node
    rospy.init_node('test_io_listener')
    rostest.rosrun('demo_pkg', 'test_io_listener', TestIoListener)
