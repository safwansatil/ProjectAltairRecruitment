from setuptools import find_packages, setup

package_name = 'task4_video'

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
    maintainer='safwansatil',
    maintainer_email='asf1k.til@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'video_pub = task4_video.video_publisher:main', 
        'video_sub = task4_video.video_subscriber:main',
    ],
},
)
