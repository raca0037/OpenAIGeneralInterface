import gym
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
# TODO import the interface stuff
import ControlHubInterface_openAI #check if this is correct syntax later.
import threading #importing threading qualities.
from queue import Queue
from threading import Thread
"""
https://gym.openai.com/envs/CarRacing-v0/
#updated march 5th.

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


def interface_function(q):
    """ Needs to be outside the race_car class.
    # copy all interface starting code here
   # myWindow = ControlHubInterface_openAI.Ui_MainWindow() #starting running code for interface, moved from line 59 to main function
   """
    import sys
    app = QtWidgets.QApplication(sys.argv)  # calling QtWidget, Qapplication is created.
    MainWindow = QtWidgets.QMainWindow()  # calling the main window class within controlhubinterface.py
    ui = ControlHubInterface_openAI.Ui_MainWindow(q)  # translating from ui -> .py.
    ui.setupUi(MainWindow)
    MainWindow.show()  # displaying control interface, end of starting code for interface.
    #action = myWindow.a #Moved from openai_function to interface function: getting action variable from ControlHubInterface_openAI via button press on interface.
    app.exec_() #executing interface

"""
have action outputted from interface_function as the input of the open_ai.
# want the action data from the interface to be inputted into open_ai function, then have the map updated.
# will have the input "action" inputted into the below function. This will probably in the form of (0,0,0)
"""


def openai_function(q):
    # Start the race car environment
    env = gym.make('CarRacing-v0')
    env.reset()
    car = race_car()
    while True:
        # Get the action from the user
        # TODO get the action from the interface instead

        action = q.get() #getting action values from interface (producer) function into the queue for this consumer function (open ai) so it can run its data on the display.
        # Send the action to the racecar, get some information back
        print(action)
        _, reward, done, _ = env.step(action)
        # Get the rendered frame
        arr = env.render(mode='rgb_array')

        # Display the rendered frame and information to the user
        car.display(arr, reward, done)
        # TODO send the data to the interface for display


def run():

    """
    The following code starts up our consumer (openaigym) and producer (interface) functions.... 
    threads then use put() or get() operations to add or remove data from queue!
    out_q basically assigns q a local variable within the t1 thread when we are assigning data to be produced. 
    In our thread call though we just want to read in queue or "q" as defined in line 113.
    """
    q = Queue()
    t1 = Thread(target=openai_function, args=(q,)) #where q represents all the data being communicated between the two threads via "queue"
    t1.start()
    interface_function(q,)#calling our function after the thread begins.
"""
When I put the map on it - it lags a whole lot and freezes the two windows. 
"""

run()
