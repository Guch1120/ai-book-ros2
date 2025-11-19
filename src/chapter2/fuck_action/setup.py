from setuptools import find_packages, setup

package_name = 'fuck_action'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='e1x22089@oit.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fuck_action_server_node = fuck_action.fuck_action_server_node:main',
            'fuck_action_client_node = fuck_action.fuck_action_client_node:main'
        ],
    },
)
