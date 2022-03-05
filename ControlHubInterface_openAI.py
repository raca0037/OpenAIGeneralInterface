# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_ControlHub.ui'
# updated march 5, 2022.
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

#Goal is to have this file be a class to just call into ControlHubIntegration.py
import gym
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
# TODO import the interface stuff
import ControlHubInterface #check if this is correct syntax later.
"""
https://gym.openai.com/envs/CarRacing-v0/

Actions: (direction, gas, brake)
    direction is left (-1) or right (+1)
    gas is off (0) or on (+1)
    brake is off (0) or on (+1)

## Original gym ai file

pip install gym
pip install matplotlib
"""

# Global variable to capture keyboard input
control_action = 0


class race_car:
    """
    Interface for controlling the race car
    """

    def __init__(self):
        self._reward = 0.0
        self._action = ''

    def display(self, img_array, reward, done):
        """
        Display the image and data to the user

        :param img_array:
        :param reward:
        :param done:
        :return:
        """
        self._reward += reward
        plt.imshow(img_array)
        cumulative_reward_string = "Cumulative reward: {:.2f}".format(self._reward)
        done_string = "Done: {}".format(done)
        action_string = "Action: {}".format(self._action)
        data_string = "{}\n{}\n{}".format(cumulative_reward_string, done_string, action_string)
        plt.title(data_string)
        plt.draw()
        plt.pause(0.00001)
        plt.clf()



    # def key_press(key, mod):
    """
    Capture key press events
    :param key:
    :param mod:
    :return:
    """
    # global control_action
    # a = int(key - ord('0'))
    # control_action = a

    # def key_release(key, mod):
    """
    Capture key release events
    :param key:
    :param mod:
    :return:
    """


#   global control_action
#  a = int(key - ord('0'))
# if control_action == a:
#    control_action = 0


def run():
    global control_action  # Global variable to capture keyboard input

    # Start the race car environment
    env = gym.make('CarRacing-v0')
    env.reset()

    # Used to keyboard input
    # env.unwrapped.viewer.window.on_key_press = key_press
    # env.unwrapped.viewer.window.on_key_release = key_release

    car = race_car()
    myWindow = ControlHubInterface.Ui_MainWindow()

        #displaying the control hub interface by calling associating classes/functions
    import sys
    app = QtWidgets.QApplication(sys.argv) #calling QtWidget
    MainWindow = QtWidgets.QMainWindow() #calling the main window class within controlhubinterface.py
    ui = ControlHubInterface.Ui_MainWindow() #translating from ui -> .py.
    ui.setupUi(MainWindow)
    MainWindow.show() #diplaying control interface
    #MainWindow.callback_pb_load()

    #app.exec_()

    while True:
        # Get the action from the user
        # TODO get the action from the interface instead
        action = myWindow.a # calling the action function with ControlHubInterface to return action value
        # Send the action to the racecar, get some information back
        _, reward, done, _ = env.step(action)
        # Get the rendered frame
        arr = env.render(mode='human')

        # Display the rendered frame and information to the user
        #car.display(arr, reward, done)
        # TODO send the data to the interface for display


run()

