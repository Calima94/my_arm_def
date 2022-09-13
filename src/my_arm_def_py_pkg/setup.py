from setuptools import setup

package_name = 'my_arm_def_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='caio',
    maintainer_email='caiolima2000@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "arm_controller = my_arm_def_py.arm_controller:main",
            "spawn_arm = my_arm_def_py.spawn_arm:main",
            "myo_raw = my_arm_def_py.myo_raw:main",
            "capture_braco_pos = my_arm_def_py.capture_braco_pos:main"
        ],
    },
)
