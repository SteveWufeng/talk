# Sep 18, 2023
- 
*notes while surfing through open source applications for conferrence meeting*


## Communication Protocols Search:
* Real-Time Messaging Protocol (RTMP)
-
- A communication protocol for streaming audio, video, and data over internet.
- could be used for video conference
- (some sites claim that it is Dead protocol for Flash. no browsers support it. 
only support it for legacy reason)
- But some sais RMTP is still used in sites like youtube.

* Session Initiation Protocol (SIP)
- 
- Computer Language used is ASCII.
- Highly flexible and simple
- Resemble HTTP protocol
- Used to establish, modify and terminate multimedia sessions or calls.
- (looks more reliable)

* Conferencing Protocol H.233:
- 
- Computer Language uses Binary.
- complex and posibilities of delay.
- less flexible than SIP.
- 

* Protocol H.323:
-
- protocol suite that defines audio, visual, and data comunication over IP
network.

* Common Industrial Protocol (CIP):
- 
-

# Open Source Application Search: 

* Github (Simple Realtime Server) - WebRTC, RTPM, H.265
link to page:
```bash
https://github.com/ossrs/srs
https://ossrs.io/lts/en-us/
```
This is a simple, high-efficiency, real-time video server supporting RTMP,
WebRTC, HLS, HTP-FLV, SRT, MPEG-DASH, and GB288181.

- Eye catching things:
	- Live: Support timestamp correcting for long time(>4.6hours) publishing/playing. v1.0.0+
	- API: Support HTTP API(CN, EN) for system management. v1.0.0+
	- Frequent update almost monthly.

* Github (Telepresence) - SIP based:
link to page:
```bash
https://github.com/DoubangoTelecom/telepresence
```
Open source alternative to Google Hanouts.


* Github (Jitsi meet):
link to page:
```bash
https://github.com/jitsi/jitsi-meet
```
Secure, simple, scalable video conferences that you use as a standalone app or embed in your web application.
They have a demo deployment
```bash
https://jitsi.org/jitsi-meet/
https://meet.jit.si/
```
The demo show authentication, but we can customize it to not authenticate in the code.

**Supports closed caption AND translation**
```bash
https://meetrix.io/blog/webrtc/jitsi/How-to-enable-translation-jitsi-meet-front-jigassi-google-translate-api.html
```


* GIthub (webRTC)
link to page:
```bash
https://github.com/melvinchia3636/webRTC/
```
This is a simpler video chat app. They adapted from the tutorial:
```bash
https://fireship.io/lessons/webrtc-firebase-video-chat/
```
Looks like what we want, but they require a signalling server. in their example: firebase.
which may not be very permanent.


* Github (zipcall)
```bash
https://github.com/ianramzy/decentralized-video-chat/tree/4b92b8a538a982bf65219c9cc120f41e0b9145c1
```
Aqquired, Not an option


* Github (talk)
```bash
https://github.com/vasanthv/talk
```
This project does not require an external signalling server. Which is better than webRTC.
The signalling server is built-in.


## 9/22 meeting note:

In talk, try to make an button that establish a communication with an external. 