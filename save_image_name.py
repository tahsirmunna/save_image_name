import os

image_name=os.listdir("./train/") # get a list of image name from a folder

#save the image name as .txt file. Here I name it list.txt
with open("list.txt", "w") as f:
    for img in image_name:
        f.write(img+"\n") 
