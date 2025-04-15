import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import imageio.v2 as imageio

# makeframes
def makeframes(data_name, folder_name):
    df = pd.read_csv(data_name)
    df2 = pd.read_csv(data_name)
    for i in range(len(df['data'])):
        df['data'] = df2['data']
        df['data'][i+1:] = 0 
        plot = df.plot.bar(y='data', ylim=(0,1.1*max(df2['data'])), rot=0)
        fig = plot.get_figure()
        fig.savefig(folder_name + "/frame-"+str(i)+".png")
        print("Saved frame" + folder_name + "/frame-" + str(i) + ".png")

def exportgif(folder_name):
    image_folder = os.fsencode(folder_name)

    # Sort a list based on key
    def mysort(x): 
        return int(str(x).replace(folder_name+'/frame-','').replace('.png',''))

    filenames = []

    for file in os.listdir(image_folder):
        filename = os.fsdecode(file)
        if filename.endswith( ('.jpeg', '.png', '.gif', '.jpg') ):
            filenames.append(folder_name + '/' + filename)

    filenames.sort(key=mysort) # this iteration technique has no built in order, so sort the frames
    print(filenames)

    images = list(map(lambda filename: imageio.imread(filename), filenames))
    imageio.mimsave(os.path.join('gifplot.gif'), images, duration = 200) # modify the frame duration as needed

    print("Exported : gifplot.gif")

# main
if __name__ == '__main__':
    try:
        data_name = sys.argv[1]
        folder_name = sys.argv[2]
    except:
        print("Something went wrong.")
    else:
        print("plot-to-gif start")
        makeframes(data_name,folder_name)
        exportgif(folder_name)
        print("plot-to-gif end")