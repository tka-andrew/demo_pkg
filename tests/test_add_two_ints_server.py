#!/usr/bin/env python
import rospy
import unittest
from demo_pkg.srv import AddTwoInts


class TestAddTwoIntsServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # necessary to wait for service to ready
        rospy.wait_for_service('add_two_ints')

    def test_handle_add_two_ints(self):
        inputs = [1, 2, 4, 5, 11, 100]
        outputs = [100, 219, 214, 45, 1121, 1200]
        expected_list = [101, 221, 218, 50, 1132, 1300]
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        for i in range(len(inputs)):
            resp = add_two_ints(inputs[i], outputs[i])
            self.assertEqual(resp.sum, expected_list[i])


if __name__ == "__main__":
    import rostest
    rostest.rosrun('demo_pkg', 'test_add_two_ints_server',
                   TestAddTwoIntsServer)
