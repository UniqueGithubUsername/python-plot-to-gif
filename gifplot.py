import imageio.v2 as imageio
import os

path = 'frames/'
image_folder = os.fsencode(path)

# Sort a list based on key
def mysort(x): 
    return int(str(x).replace(path+'frame-','').replace('.png',''))

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png', '.gif', '.jpg') ):
        filenames.append(path + filename)

filenames.sort(key=mysort) # this iteration technique has no built in order, so sort the frames
print(filenames)

images = list(map(lambda filename: imageio.imread(filename), filenames))
imageio.mimsave(os.path.join('gifplot.gif'), images, duration = 200) # modify the frame duration as needed

print("Exported : gifplot.gif")