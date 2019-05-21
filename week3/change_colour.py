pixel = input("Please provide a pixel value: ")
channel = input("Please provide channel values or pixel value: ")

red = int(pixel[2:4], 16)
green = int(pixel[4:6], 16)
blue = int(pixel[6:8], 16)

if channel[0:2] == "0x":
    redchan = int(channel[2:4], 16)
    greenchan = int(channel[4:6], 16)
    bluechan = int(channel[6:8], 16)
    newred = red + redchan
    newgreen = green + greenchan
    newblue = blue + bluechan
else:
    channel = channel.split()
    chan = []
    for i in range(len(channel)):
        why = int(channel[i])
        chan.append(why)
    newred = red + chan[0]
    newgreen = green + chan[1]
    newblue = blue + chan[2]

if newred > 255 or newred < 0:
    newred = (newred % 256)
if newgreen > 255 or newgreen < 0:
    newgreen = (newgreen % 256)
if newblue > 255 or newblue < 0:
    newblue = (newblue % 256)

print("Your new pixel value is: 0x{:02x}{:02x}{:02x}".
      format(newred, newgreen, newblue))
