mkdir -p hexapod/{src/{kinematics,legs,locomotion,hardware,control,utils},tests,scripts,data,docs}

# Create empty Python modules
touch hexapod/src/{__init__.py,main.py}

touch hexapod/src/kinematics/{__init__.py,inverse_kinematics.py,forward_kinematics.py,transformations.py}
touch hexapod/src/legs/{__init__.py,leg.py,leg_controller.py}
touch hexapod/src/locomotion/{__init__.py,gait_controller.py,trajectory_planner.py}
touch hexapod/src/hardware/{__init__.py,motor_driver.py,sensor_interface.py}
touch hexapod/src/control/{__init__.py,hexapod_controller.py}
touch hexapod/src/utils/{__init__.py,math_utils.py,config_loader.py}

touch hexapod/tests/__init__.py

touch hexapod/config.yaml

touch hexapod/requirements.txt hexapod/setup.py hexapod/README.md
