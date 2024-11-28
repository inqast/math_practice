import numpy as np

viewCount = np.array([7, 11, 10, 8, 4, 15, 15])
museumCount = np.array([0, 7, 8, 0, 6, 9, 10])
mythCount = np.array([14, 0, 17, 0, 19, 18, 20])

viewCosts = viewCount * 450
museumCosts = museumCount * 1300
mythCosts = mythCount * 750

print(viewCosts+museumCosts+mythCosts)