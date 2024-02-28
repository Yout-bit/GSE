### HOW TO RUN HELLO WORLD

*(This is in windows)* 

1. Make sure you have python and django installed. (I have used Python 3.11.8 and Django 5.0.2) (Also make sure that python and django have been added to `PATH`)
2. Check out the `develop` branch 
3. In the `~\GSE\src\gseproject` directory, run the command `py manage.py runserver`
4. That should run the server locally, and provide a link for you to view (probably http://127.0.0.1:8000/) the server that shows a 404 error
5. Edit the link to have look like : http://127.0.0.1:8000/hello/
6. This should return "Hello World!"
7. Back on the command line, press `CTL+C` to close the server 