# Ubuntu Focal Zoneminder


See <https://www.youtube.com/watch?v=hUqMUhgytyc> to install zoneminder

See <https://youtu.be/Us20t1gQPOE> for an in-depth feature (not as technical)

# zoneminder testing

## set up webcams

https://gist.github.com/endolith/2052778

https://askubuntu.com/questions/348838/how-to-check-available-webcams-from-the-command-line

https://forums.zoneminder.com/viewtopic.php?t=23361


## list webcams

    apt install v4l2-ctl
    v4l2-ctl --list-devices

## temp fix for capturing issues

    sudo su
    chmod 777 /dev/video*
    chmod 777 /dev/media*

## other way??

<!-- https://github.com/gen2brain/cam2ip

    apt install jpeglib-dev
    go get -v github.com/gen2brain/cam2ip/cmd/cam2ip
    cam2ip -->

<!-- https://dominoc925.blogspot.com/2021/09/how-to-quickly-publish-rtsp-stream.html

    apt install v4l-utils

    ffmpeg \
        -f v4l2 \
        -re -stream_loop -1 \
        -i /dev/media1 \
        -c copy \
        -f rtsp \
        rtsp://0.0.0.0:8554/mystream -->


linux stream webcam to rstp

zoneminder v4l2

vlc v4l2