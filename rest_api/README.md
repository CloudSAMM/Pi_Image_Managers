## Manage Camera Commands

The following is a high-level design for how the commands can be sent to the remote Raspberry Pi's that have access to the internet.
This design has three core components:
* The Raspberry Pi Cameras running a program that connects to the cloud
* The Cloud application (Vultr)
  * Rest API that passes commands from the client to the Pi's
  * Object Storage (S3) Stores images sent from the Pi's
* The Web Client (website) that allows users to send commands to the Pi's.

The Rest API and the Website will live on a single cloud server that costs $5 a month. And the Object Storage (S3) is a managed service on Vultr that will cost $5 a month.

![](https://github.com/CloudSAMM/Pi_Image_Managers/blob/main/command_center2.png "")

### How Commands are sent to the remote Pi's
When a users wants to send a command to a Pi, they will be able to do so from the Web interface. When a command is sent from the Web interface, it will send a request to the Rest API with the details regarding the desired command. When the Rest API recives a command, it will store said command in order to relay the command to the Pi. The Pi's will be running a program on a continuous loop that makes requests to the Rest API on a 1 second interval. The requests will ping the Rest API to check if there is a command that needs to be executed. If there is a command that needs to be executed it will execute the command and then send a request back to the Rest API with the command execution status. Once the Rest API gets a command execution status, it will acknowledge that the command has already been executed so that the next time the Rest API receives a status check from a Pi it will return a response that indicates that there are no pending commands to be executed.
