import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def graphs(file,fps,sc,ff,d,center):
    df = pd.read_csv(file, index_col=False)
    df = pd.DataFrame(df, columns= ['cx','cy','n','v'])
    nn = []
    mnvl = []
    sdd = []
    #to get number of repeats
    for i in range(int(min(df["n"])),int(max(df["n"]))):
        c = df.loc[df['n'] == i]
        num = len(c["cx"])
        mnval = np.mean(c["cx"])
        nn.append(num)
        mnvl.append(mnval)
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    fig5, ax5 = plt.subplots()
    fig6, ax6 = plt.subplots()
    v = df["v"] #v
    cx = df["cx"] #cx
    n = df["n"] #frames
    t = n/fps
    x = cx
    v = v*sc
    ax1.plot(t,np.abs(np.array(x)-center)*sc,"rx")
    ax2.plot(t,v,"rx")
    ax4.plot(np.abs(np.array(x)-center)*sc,v,"rx")
    ax3.plot(np.linspace(1,len(nn),len(nn)),nn,"rx")
    ax5.plot(np.linspace(1,len(mnvl),len(mnvl)),(np.array(mnvl) - center)*sc,"b--")
    ax6.hist(np.abs((x-center)*sc),bins=100)
    print(d+"\\Making XDT for " +str(ff))
    ax1.set_ylabel("x-distance (cm)")
    ax1.set_xlabel("Time (s)")
    ax1.set_title("Graph of x-distance against Time of recording " + str(ff))
    ax1.grid()
    fig1.savefig(d+'\\XDT'+str(ff)+'.png')
    print("XDT done, making VT for " +str(ff))
    ax2.set_ylabel("Speed (cm per sec)")
    ax2.set_xlabel("Time (s)")
    ax2.set_title("Graph of speed against Time of recording " + str(ff))
    ax2.grid()
    fig2.savefig(d+'\\VT'+str(ff)+'.png')
    print("VT done, making MPPFT for " +str(ff))
    ax3.set_ylabel("Number of particles per frame")
    ax3.set_xlabel("Time (s)")
    ax3.set_title("Number of particles per frame against Time of recording " + str(ff))
    ax3.grid()
    fig3.savefig(d+'\\NPPFT'+str(ff)+'.png')
    print("NPPFT done, making VX for " +str(ff))
    ax4.set_ylabel("Speed (cm per sec)")
    ax4.set_xlabel("x-distance (cm)")
    ax4.set_title("Speed against x-distance of recording " + str(ff))
    ax4.grid()
    fig4.savefig(d+'\\VX'+str(ff)+'.png')
    fig5.savefig(d+'\\MN'+str(ff)+'.png')
    fig6.savefig(d+'\\hist'+str(ff)+'.png')
    print("VX done for " +str(ff))
    print("Number ppf: " + str(np.mean(nn)))