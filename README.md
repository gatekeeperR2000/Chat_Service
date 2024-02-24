# Overview

For this project I wanted to see more about how devices can communicate. I feel that in my classes for University I had learned a bit about basic coding skills but never touched on networking. So I took a couple weeks to glean and try my hand at creating a basic program.

For my project it requires at least two python files running to work fully. The first can be started will be the server. Simply running chat_server.py in the terminal suffices and will set up the server on the localhost IP. Then in another terminal you will need to run the client side, chat_client.py. This will then start up your own connection to the server and allow for communiaction between the client and server.

Below is a 5 minute video going over some basics of what I used and found works along with a demenstration of basic functionality.

[Software Demo Video](https://youtu.be/wAc0e1TGQF0)

# Network Communication

I chose to do a Client Server aprouch for this netwrok. This allowed for me to see how the socket library and object could be used in python for different things.

I used TCP along with encryption to allow for error checking and safety with passing the messages back and forth.

# Development Environment

I chose to continue using VS Code for this project. It wasn't overly complicated in terms of coding requirements. Simply took the time for me to understand that basics of what a network is, and how I even start coding one. VS Code worked well and python had plenty of tutorials and descriptions about what a socket is and how you can start with the basics of using them.

# Useful Websites

I mainly focused of Geeks for Geeks and some youtube descriptions with tutorials to help me stumble through networking.
* [Geeks for Geeks](https://www.geeksforgeeks.org)
* [Tutorialspoint](https://www.tutorialspoint.com/python/python_network_programming.htm)
* [Stak Overflow](https://stackoverflow.com)

# Future Work

Additions I wish to make in the future
* GUI
* Ability to open and close the server on command
* Potentially have a Data Base to store and query from