#!/usr/bin/python
#sudo ports install ffmpeg pkg-config
#sudo pip install av

import av

#settings
#teststream = "./mega1.ts"
threshold = float(0.2) #Delay should be less than this (0.2 Recommended)


if __name__ == "__main__":
    video_time = float()
    audio_time = [] #More than 1 audio possible
    delay = float()
    print "Testing stream..."
    print teststream
    container = av.open(teststream)

    #Compute start time based on each stream time_base
    print "Checking audio-video delay...."
    for s in container.streams:
        if (s.type == 'audio'):
            audio_time.append( float(s.start_time * s.time_base))
        elif (s.type == 'video'):
            video_time = float(s.start_time * s.time_base)

    #Print the results 
    print "%d audio streams" % len(audio_time)
    print "Audio-Video delay (max):"
    for at in audio_time:
        delay = max(delay,abs(video_time - at))
    print "%f (s)" % delay

    #Doing this we let know other that something went wrong
    #For example we could use this script in monit
    if delay>= threshold:
        exit(1)

