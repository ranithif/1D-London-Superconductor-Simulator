#adding sliders to original code so you can see the change that changing the pentration depth or slab thickness does
#different materials have different london penetration thickness 
#could have used button feature in matplot lib but that would only show one other plot or a couple other plots and you wouldnt be able to see the conitnual gradual change
#so opted for sliders feature instead, it also makes the graphs a lot more interactive

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# to plot the 1D London Equation:
    #B(x) = B_0 * (cosh(x/lambda)/cosh(x/2*lambda))
    
B0 = 1 #external magnetic field strength
LP_init = 50*(10**-9) #  london penetration depth as it varies from around 20 -500 nm this is on thinner side
d = 500 * (10**-9) # thickness of superconducting slab
mu = (4*np.pi ) * (10**(-7)) #permeability of free space

x = np.linspace (-d/2,d/2,300)

def B(x,LP):
    return B0*(np.cosh(x/LP)/(np.cosh(d/(2*LP)))) #this plots the magnetics field inside the superconductor

def J(x,LP):
    return  (-B0/(mu*LP))*(np.sinh(x/LP)/np.cosh(d/(2*LP)))

fig, (plt1,plt2) = plt.subplots(1,2)


line1, = plt1.plot(x, B(x,LP_init),color = 'pink')
line2, = plt2.plot(x, J(x,LP_init), color = 'purple')

plt1.set_xlabel('position $x$ inside slab (m) ', fontsize = 7)
plt1.set_ylabel ('Magnetic Field $B$ (Tesla)')

plt2.set_xlabel('position $x$ inside slab (m)', fontsize=7)
plt2.set_ylabel('Current density (A/m^2)')

plt.subplots_adjust(bottom=0.25, wspace=0.35)

axLP = fig.add_axes([0.25,0.1,0.65,0.03])
LP_slider = Slider(ax = axLP, label = 'Penetration depth (m)',
                   valmin=20*(10**-9), valmax=500*(10**-9), valinit = LP_init)
#chose this penetration depth range^^ cos its the exected range for superconducting materials 

fig.LP_slider = LP_slider #prevents garbage collection

#so that the plot changes and updates as you change the values:
def update(val):

    current_lp = val
    line1.set_ydata(B(x, current_lp))
    line2.set_ydata(J(x, current_lp))
    
    # so that J(x) height resizes dynamically:
    plt1.relim()
    plt1.autoscale_view(scalex=False, scaley=True)
    plt2.relim()
    plt2.autoscale_view(scalex=False, scaley=True)
    
    fig.canvas.draw()
       
LP_slider.on_changed(update)
