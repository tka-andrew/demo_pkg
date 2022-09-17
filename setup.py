from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# reference: http://docs.ros.org/en/jade/api/catkin/html/user_guide/setup_dot_py.html
d = generate_distutils_setup(
    packages=['io_manager'],
    package_dir={'': 'scripts'}
)

setup(**d)