import matplotlib.pyplot as plt
import matplotlib as mp
import numpy as np
#vals is 2d matrix of numbers
"""
class nf(float):
    def __repr__(self):
        str = '%.1f' % (self.__float__(),)
        if str[-1] == '0':
            return '%.0f' % self.__float__()
        else:
            return '%.1f' % self.__float__()  
"""        
def plot2dgrid(vals,n):

    if n == "1":
        fig = mp.pyplot.figure(2)
        
        cmap2 = mp.colors.LinearSegmentedColormap.from_list('my_colormap',
                                                   ['blue','green','black','red'],
                                                   256)
        
        img2 = mp.pyplot.imshow(vals,interpolation='nearest',
                            cmap = cmap2,
                            origin='lower')
        
        mp.pyplot.colorbar(img2,cmap=cmap2)
        plt.title('2D-grid')
        plt.show()
    #fig.savefig("image2.png")
    #plt.contourf(vals)  
    
    if n == "2":
        CS = plt.contour(vals,10)
        plt.clabel(CS, inline=1, fontsize=10)
        plt.axis('scaled')
        plt.title('Countuour')
        
#plot2dgrid(np.random.rand(100,100)*10-5)
