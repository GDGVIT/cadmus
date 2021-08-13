sudo apt install v4l2loopback-dkms;
sudo apt install ffmpeg;
sudo modprobe --remove v4l2loopback
sudo modprobe v4l2loopback card_label="My Fake Webcam" exclusive_caps=1
ffmpeg -stream_loop -1 -re -i /dev/video0 -vcodec rawvideo -threads 0 -f v4l2 $(ls -1 /dev/video* | tail -n 1)
