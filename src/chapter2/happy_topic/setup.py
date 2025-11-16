from setuptools import find_packages, setup

package_name = 'happy_topic'

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
            'happy_publisher_node = happy_topic.happy_publisher_node:main',
            'fuck_subscriber_node = happy_topic.fuck_subscriber_node:main',
            'fuck_pub_and_sub_node = happy_topic.fuck_pub_and_sub_node:main'
        ],
    },
)
