# NTU Tools
#### Video Demo:  https://youtu.be/rMNi--hYWlQ
#### Description:
I developed a web application using Javascript, Python, and SQL to assist NTU students in planning their semester schedules. Students bid for the courses they wish to take in the upcoming semester. A course may contain various indexes, each of which corresponds to a different time slot. Users would choose from a drop-down menu of all NTU courses. The program will calculate all possible combinations and display a visual representation of each and every timetable that does not have a scheduling conflict.



The application is designed with Flask to allow for interaction between the frontend and backend.



The frontend web display can be found in "index.html" and styled in "styles.css". Web elements like tables are used to display information about the selected timetable to users. These elements are styled through their classes, which allows the programmer to control the look and feel of these web elements. I also created a dynamic input section where users could add input if they so desired. This dynamic input section is controlled in Javascript.



The web page elements are designed to be controlled and governed by Javascript written in "main.js". Javascript code is used to interact with the website. Features like appending the input into the div as well as appending the various tables seen on the website to the table are controlled through Javascript.



Web page processing and computation are done server-side using Python in "app.py". Certain events in Javascript will also have AJAX calls, which lead to the same server-side processing. AJAX allows the reloading of portions of the page to update only certain web elements. Functions were created in "helpers.py" to assist in the computation of all possible timetable combinations. The itertools product function was used to create an iterator that holds all of the timetable combinations. After checking each combination to ensure no scheduling conflicts, a generator of all possible combinations was created.



The server side is also supported by the backend database in "courses_actual.db". The database holds all course indexes and time slots for each of the courses. The database information was scrapped from the school website. By engaging with the html page source stored in a text file, I created a program to automate the extraction of key information from the webpage to craft INSERT statements to insert the corresponding data into my database.



My final project went through multiple iterations as it did not live up to expectations when handling real-life data. Early iterations of the project took upwards of 10 minutes to complete processing. This was partly due to the unnecessary additional processing steps involved. In earlier iterations of the program, I used the Pandas library in Python for logic processing. However, I soon realized that insertions into Pandas dataframes were slowing down my program. To combat this, I created a new data structure, a list of lists, to store the data instead. This significantly reduced processing time.These extra processing steps could be avoided by writing more concise code and thinking through each step of the process to better optimize processing time.


Another issue was memory. When the number of total combinations gets large, out-of-memory issues can occur when executing the program. This was due to the storage of a large number of unnecessary global variables. To combat this, iterators and generators are used instead to avoid having to access too much memory in order to be memory efficient.