import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df2 = pd.read_csv('data.csv')
for i in range(len(df['date'])):
    df['data'] = df2['data']
    df['data'][i+1:] = 0 
    print(df['data'])
    plot = df.plot.bar(x='date', y='data', ylim=(0,1.1*max(df2['data'])), rot=0)
    #plt.show() # show plot if necessary
    fig = plot.get_figure()
    fig.savefig("frames/frame-"+str(i)+".png")
    print(str(i) + " : Saved frame frames/frame-" + str(i) + ".png")