#!/usr/bin/env python
import rospy
import unittest
import random
from demo_pkg.srv import AddTwoInts


class TestAddTwoIntsServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        max_int = pow(2, 64)/2
        # as the add_two_ints currently cannot handle overflow,
        # so we need to divide the max_int by 2
        cls.max_random_int = max_int / 2
        # necessary to wait for service to ready
        rospy.wait_for_service('add_two_ints')

    def test_handle_add_two_ints(self):
        A = [random.randint(-self.max_random_int, self.max_random_int) for i in range(10)]
        B = [random.randint(-self.max_random_int, self.max_random_int) for i in range(10)]
        expected_list = [A[i] + B[i] for i in range(10)]
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        for i in range(len(A)):
            resp = add_two_ints(A[i], B[i])
            self.assertEqual(resp.sum, expected_list[i])


if __name__ == "__main__":
    import rostest
    rostest.rosrun('demo_pkg', 'test_add_two_ints_server',
                   TestAddTwoIntsServer)
