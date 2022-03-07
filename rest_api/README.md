## Manage Camera Commands

The following is a high-level design for how the commands can be sent to the Raspberry Pi that have access to the internet.
This design has three core components:
* The Raspberry Pi Cameras running a program that connects to the cloud
* The Cloud application (Vultr)
  * Rest API that passes commands from the client to the Pi's
  * Object Storage (S3) Stores images sent from the Pi's
* The Web Client (website) that allows users to send commands to the Pi's.

The Rest API and the Website will live on a single cloud server that costs $5 a month. And the Object storage is a managed service on Vultr that will cost $5 a month.

![](https://github.com/CloudSAMM/Pi_Image_Managers/blob/main/command_center.png "")
