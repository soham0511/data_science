import matplotlib.pyplot as plt
import numpy as np
hours=[2,3,1,3,4,1,3,2,3,2]
activity=["college","play","ready","sleep","study","video game","travel","youtube","web series","waiting"]
explodes=[0.2,0,0,0,0,0,0,0.2,0,0]
plt.pie(hours,labels=activity,shadow=True,explode=explodes)
plt.show()
