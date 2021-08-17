<p align="center">
<a href="https://dscvit.com">
	<img src="https://user-images.githubusercontent.com/30529572/92081025-fabe6f00-edb1-11ea-9169-4a8a61a5dd45.png" alt="DSC VIT"/>
</a>
	<h2 align="center"> Cadmus </h2>
	<h4 align="center"> Automatically caption ASL videos using deep neural networks , using the data set provided in the paper- "Word-level Deep Sign Language Recognition from Video: A New Large-scale Dataset and Methods Comparison". The project aims at developing a browser extension which can provide live captioning to sign language within a video call. <h4>
</p>

---
[![Join Us](https://img.shields.io/badge/Join%20Us-Developer%20Student%20Clubs-red)](https://dsc.community.dev/vellore-institute-of-technology/)
[![Discord Chat](https://img.shields.io/discord/760928671698649098.svg)](https://discord.gg/498KVdSKWR)

[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](INSERT_LINK_FOR_DOCS_HERE) 
  [![UI ](https://img.shields.io/badge/User%20Interface-Link%20to%20UI-orange?style=flat-square&logo=appveyor)](INSERT_UI_LINK_HERE)


## Features
- [ ]  live captioning for sign language during video call.
- [ ]  All participants in the google meet or zoom meet first join the socket room through our extension
- [ ]  Our model translates the sign language into text in the client server using sockets, which is then broadcasted into the room.
- [ ]  Broadcasted text appears as subtitles for everyone present in the meeting.

<br>
	
## Architecture Overview
![img](https://github.com/sharanya02/cadmus/blob/master/media/architecture.png?raw=true)

## Usage

Let's see how to start the client server and start making predictions!
For linux users, first cd into the ```client-server``` directory, install the requirements from requirements.txt inside a virtual environment and then run-
```bash
sudo bash run.sh
```
Next, open another terminal in the same directory and make sure you're inside the virtual environment you previously created, then run-
```
python3 charserver.py <INSERT A NAME FOR THE SOCKET ROOM>
```
Now, one can use our extension to simply join the room to get all subtitles. After joining the room, the person who will be signing must go to the host settings on google meet or zoom, and then select the ```My Fake Webcam```option under camera, as shown below-
<br>
![img](https://github.com/sharanya02/cadmus/blob/master/media/camera.png?raw=true)																																	

## Contributors

<table>
	<tr align="center">
		<td>
		Sharanya Mukherjee
		<p align="center">
			<img src = "https://avatars.githubusercontent.com/u/59661067?s=400&u=380275c84d3c07dce16d669b01755d7f020d133a&v=4" width="150" height="150" alt="Sharanya Mukherjee (Insert Your Image Link In Src">
		</p>
			<p align="center">
				<a href = "https://github.com/sharanya02">
					<img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/>
				</a>
				<a href = "https://www.linkedin.com/in/sharanya02/">
					<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="LinkedIn"/>
				</a>
			</p>
		</td>
	</tr>
</table>

<p align="center">
	Made with :heart: by <a href="https://dscvit.com">DSC VIT</a>
</p>
