# BCI-repo


Motivation:
We see a lot of people with active mind who loose their limbs and therefore ability to move due to accidents or maybe by birth.

Problem Statement:
With the development of means and resources every science fiction things are now the reality. The matrix of the movie matrix or the
Brain power of Charles Xavier from the Xmen. Science fiction of 90s are the reality of today. What if we can do something that
is worth a great deal. Our project Brain Computer Interface along with the blinker talker is one of which comes with a motive to
help the disabled with movement impairment as well as inability to talk.

Solution:
This project is an application of Brain Computer Interface. Using the neurosky electrode we receive the brain waves (alpha and beta in our case).
With the waves taken into account, from the collection of the raw data it is necessary to extract the features for doing so
signal processing should be done. For this first the alpha and beta bands were seperated along with the power,
this was fed to the ANN which predicted that power above 4 was generally due to our mind being on active state i.e beta wave while power 
less than 4 represented our mind being on meditation i.e alpha waves. After coming to this conclusion, we used finite state machine
to count stages if 3 corresponding states are below 4 then the meditation state is triggered while the opposite is true for active state.
With the two features the wheelchair moves forward in meditation stage while it stops in active stage.


Installation:
before running it is necessary to import all the modules like pyserial for connecting the usb dongol, matplotlib, scipy,itertools,
numpy,espeak,queue,etc. After installing all these packages we are ready to run the code. To run this project it is necessary to have 
neurosky mindwave, raspberry pi as well.

Installation instructions:
It is recommended to use Linux Machine for this purpose.
Install all the packages as mentiond before.
keep all the files in the same folder.
run the file mindwave.py and keyboard.py
run the file main.py for the wheelchair project only after using the usb dongole of neurosky mindwave turning the mindwave on.
for blinker talker application run the file talker.py after connecting the usb and turning on mindwave.

for the wheelchair part the connection should be made through raspberry pi.
a simple program should be written as server.py in the pi and client.py in the pc to send the pulses of 1 and 0 for wheelchair movement.


Acknowledgements:
->Well the main credit for the project goes to our team Rajan and Kushal including me of course. While we had good support
from our supervisor Sachin Shrestha Sir. Finally Madan Gyawali from the electronics lab also deserves special mention for his
help and support for completing the Project.
