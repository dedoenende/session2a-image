import os # operating module wrapper (wind+lin+mac)
from PIL import Image
# print(os.getcwd()) # get working directory

# directory
folder = "K:\\gradschools\\Courses\\python\\session2a-image\\raw"

#load an image
img_path = os.path.join(folder, "bird.jpg") # wrapper os 
img = Image.open(img_path) # load image

img.show() # show picture

print(img.size)
print(img.size, img.format, img.mode) # jped full color image

# tupol?? cannot be changed, between round brackets

filename, extension = os.path.splitext(img_path)# save to new extension, turn to png
print(filename)
print(extension)

outfile = filename + ".png" # create new file with new extension
print(outfile)

img.save(outfile, "PNG") # saves to same folder under diff extension

new_img_path = os.path.join(folder, "a_Python_will_eat_bird.png")
img.save(new_img_path, "PNG") # saves to same folder under diff extension, save under different name

os.remove(outfile) # remove this path file
os.remove(new_img_path) # remove this path file

# make a new folder
# new_folder = "K:\\gradschools\\Courses\\python\\session2a-image\\temp"
# os.mkdir(new_folder) # make a new folder

our_file = "copy" + extension
print(our_file)
print(os.path.join(new_folder, our_file))
img.save(os.path.join(new_folder, our_file))

print(os.listdir(folder))

# import shutil # get this package
#directory = "K:\\gradschools\\Courses\\python\\session2a-image\\raw"
#for files in os.listdir(directory): # copy all pics from raw folder to new folder by using for loop
 #   if files.endswith(".jpg"):
  #      shutil.copy(files, new_folder) # copy these to new destination
   #     else:
    #        print ("file does not exist", files)
     #       print(files)

# loop over to save images in new folder
for img in img_list:
    img_path = os.path.join(old_folder, img)
    img_open = Image.open(img_path)
    img.open.save(os.path.join(new_folder, img))