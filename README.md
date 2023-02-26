# AttentionMonitor  
  
## Inspiration
Online Education is fun for students, but teachers have a tough time managing students. Students tend to distract and they cannot concentrate on their lectures. Our idea was to notify the teacher about the attentivity of the students and would help the teachers to help their students, in turn the students would also pay attention to their lecture as their actions would be notified to their teachers.
## What it does
Attention Monitor is an application that tackles the problem of teachers that they face during online classes. It helps teachers in monitoring a class online which becomes difficult in online mode
## How we built it
 - This is a web platform build using Django as the backend. 
 - To integrate the video conferencing feature we used Jitsi API.
 - Build a telegram bot using telegram API to notify the teachers. 
 - We also used a computer vision python script to detect the faces and eyes of the students.

## Challenges we ran into
 - It was really a challenging task to integrate the video conferencing feature into our platform.
 - We also had a tough time integrating the computer vision script with the platform
## Installation Instructions
The portal is primarily a django based application, and to set it up we require to have 
python environment with django and other project dependencies installed. Though one can
work with the project without an virtual environment,  it is recommended to use one so 
as to avoid conflicts with other projects.

0. Make sure that you have `Python 3`, `python-3-devel`, `gcc`, `virtualenv`, and `pip` installed.     
1. Clone the repository

    ```
        $ git clone https://github.com/lazyCodes7/AttentionMonitor.git
        $ cd AttentionMonitor
    ```
2. Create a python 3 virtualenv, and activate the environment.
    ```bash
        $ virtualenv -p python3
        $ source bin/activate
    ```   
3. Install the project dependencies
    ```
        $ pip install -r requirements.txt
    ```

You have now successfully set up the project on your environment. 

### After Setting Up
From now when you start your work, run ``source bin/activate`` inside the project repository and you can work with the django application as usual - 

* `python manage.py migrate` - set up database
* `python manage.py createsuperuser` - create admin user
* `python manage.py runserver`  - run the project locally
