lenght = int(input())
width = int(input())
height = int(input())
percent = int(input())

volume = lenght*width*height/1000

print(volume - volume*percent/100)