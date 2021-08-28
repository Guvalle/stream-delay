# stream-delay
stream-delay is an application developed to allow streammers to broadcast their content with delay while being able to interact with the audience in real time.

What it does is simply capture frames from the current active window and buffer them for the configured amount of time, and display the frame after that.

To work with it it's very simple. You set your chosen streamming software to capture stream-delay instead of your application, and then let stream-delay be the one who captures frames from the application, and it'll work as a proxy for the capture while your camera and sound are broadcasted in realtime to your audience.

## Running it:
stream-delay is coded in python and compiled using pyinstaller to create an executable file.

You can either download the code and compile yourself or run the pre-compiled version contained inside de **dist** folder.

## Settings:
The settings file is called **config.txt** and is composed by 4 configurations:
- SET MODE: 
  - This tells the app where the frames will come from.
  - The value can either be **"mode": 1** or **"mode": 2** with 1 being a full display capture and 2 being an active window capture

- SET WINDOW SIZE
  - This tells the app the resolution of the output frames
  - The value is set in two variables: **"window_width"** and **"window_height"**

- SET FRAMES PER SECOND FOR RECORDING
  - This tell the app how many frames it should capture per second. *PS: The computer performance may influence the workings of this option. The app will try to stay at the chosen value but he might dip a little during heavy workload so it's recommended to set up a value a little higher than expected.*
  - The value is set in the variable **"fps"**

- SET DELAY IN SECONDS
  - This tells the app how long it should buffer the captured frames.
  - The value is set in the variable **"delay"**

## Improvements
*The code is available to download and use as desired as long as the goal isn't comercial. If you make any improvements on the existing code please push it to this original project so it get's even better for future users* :D
