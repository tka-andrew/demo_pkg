# ROS demo package
This is just a simple package mainly based on beginner_tutorials of ROS Wiki Tutorial. 
This can be used as a minimal package for testing some implementations.


# Usage
1. Add this package into your workspace, and run `catkin_make`
2. Open 3 terminals and run these for C++ publisher and subscriber examples, remember to source your workspace's setup.bash first:
    ```
    $ roscore
    ```
    ```
    $ rosrun demo_pkg demo_talker
    ```
    ```
    $ rosrun demo_pkg demo_listener
    ```
3. Open 3 terminals and run these for Python publisher and subscriber examples, remember to source your workspace's setup.bash first:
    ```
    $ roscore
    ```
    ```
    $ rosrun demo_pkg talker.py
    ```
    ```
    $ rosrun demo_pkg listener.py
    ```
4. Open 3 terminals and run these for C++ service client examples, remember to source your workspace's setup.bash first:
    ```
    $ roscore
    ```
    ```
    $ rosrun demo_pkg demo_add_two_ints_server
    ```
    ```
    $ rosrun demo_pkg demo_add_two_ints_client 2 5
    ```
5. Open 3 terminals and run these for Python service client examples, remember to source your workspace's setup.bash first:
    ```
    $ roscore
    ```
    ```
    $ rosrun demo_pkg add_two_ints_server.py
    ```
    ```
    $ rosrun demo_pkg add_two_ints_client.py 2 5
    ```
6. Open 3 terminals and run these to ensure the io_listener.py is working, remember to source your workspace's setup.bash first:
    ```
    $ roscore
    ```
    ```
    $ rosrun demo_pkg io_listener.py
    ```
    ```
    $ rostopic list | grep /io/
    ```