from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import numpy as np

radarColors = {
    'red': (
        (0,0.8,0.8),
        (0.04,0.8,0.8),
        (0.09,0.8,0.6),
        (0.13,0.6,0.4),
        (0.17,0.4,0.8),
        (0.22,0.8,0.6),
        (0.26,0.6,0.39),
        (0.3,0.39,0.02),
        (0.35,0.02,0),
        (0.39,0,0.01),
        (0.43,0.01,0.01),
        (0.48,0.01,0),
        (0.52,0,0),
        (0.57,0,0.99),
        (0.61,0.99,0.9),
        (0.65,0.9,0.99),
        (0.7,0.99,0.99),
        (0.74,0.99,0.83),
        (0.78,0.83,0.74),
        (0.83,0.74,0.97),
        (0.87,0.97,0.6),
        (0.91,0.6,0.99),
        (0.96,0.99,1),
        (1,1,1),
        ),
    'green': (
        (0,1,1),
        (0.04,1,0.6),
        (0.09,0.6,0.4),
        (0.13,0.4,0.2),
        (0.17,0.2,0.8),
        (0.22,0.8,0.6),
        (0.26,0.6,0.39),
        (0.3,0.39,0.91),
        (0.35,0.91,0.62),
        (0.39,0.62,0),
        (0.43,0,0.99),
        (0.48,0.99,0.77),
        (0.52,0.77,0.56),
        (0.57,0.56,0.97),
        (0.61,0.97,0.74),
        (0.65,0.74,0.58),
        (0.7,0.58,0),
        (0.74,0,0),
        (0.78,0,0),
        (0.83,0,0),
        (0.87,0,0.33),
        (0.91,0.33,0.99),
        (0.96,0.99,1),
        (1,1,1),
        ),
    'blue': (
        (0,1,1),
        (0.04,1,0.8),
        (0.09,0.8,0.6),
        (0.13,0.6,0.4),
        (0.17,0.4,0.6),
        (0.22,0.6,0.4),
        (0.26,0.4,0.39),
        (0.3,0.39,0.91),
        (0.35,0.91,0.96),
        (0.39,0.96,0.96),
        (0.43,0.96,0.01),
        (0.48,0.01,0),
        (0.52,0,0),
        (0.57,0,0.01),
        (0.61,0.01,0),
        (0.65,0,0),
        (0.7,0,0),
        (0.74,0,0),
        (0.78,0,0),
        (0.83,0,0.99),
        (0.87,0.99,0.78),
        (0.91,0.78,0.99),
        (0.96,0.99,1),
        (1,1,1),
        )
    }

radarColors = LinearSegmentedColormap('radarColors', radarColors)

#plt.imshow(np.random.random(100).reshape((10,10))*115-30, cmap=radarColors, vmin=-30, vmax=85)
#plt.colorbar()
#plt.show()
