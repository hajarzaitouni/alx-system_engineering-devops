# Processes and signals
This project concerns commands for processess and signals in __Bash__.

## General
In this particular project, we were able to:
* find a process’ PID.
* kill process.
* know what is a signal.

## Tasks
0. What is my PID
* Write a Bash script that displays its own PID.

1. List your processes
* Write a Bash script that displays a list of currently running processes.

2. Show your Bash PID
* write a Bash script that displays lines containing the bash word

3. Show your Bash PID made easy
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

4. To infinity and beyond
* Write a Bash script that displays To infinity and beyond indefinitely.

5. Don't stop me now!
* Write a Bash script that stops `4-to_infinity_and_beyond process`.

6. Stop me if you can
* Write a Bash script that stops `4-to_infinity_and_beyond process`.
	* Not allowed to use either `kill` or `killall`

7. Highlander
* Write a Bash script that displays:
	
	* `To infinity and beyond` indefinitely
	* With a `sleep 2` in between each iteration
	* `I am invincible!!!` when receiving a `SIGTERM` signal

8. Beheaded process
* Write a Bash script that kills the process `7-highlander`
