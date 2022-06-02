from tkinter import *
import GUI.MainWindow
import ArduinoInstructions.ArduinoInstructions as Arduino


def main():
    # window = Tk()
    # mainWindow = GUI.MainWindow.MainWindow(window)
    # window.mainloop()
    arduino = Arduino.ArduinoInstructions("COM6")
    arduino.UseColor(1)
    arduino.Pos(100,100)
    arduino.ContinueDown(100)
    arduino.Beginning()
    arduino.UseColor(0)
    arduino.run()


if __name__ == '__main__':
    main()
