import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/safwansatil/Desktop/ProjectAltairRecruitment/230042117_Safwan_WEEK3_ProjectAltair/ros2/install/task5_urdf'
