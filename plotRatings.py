import matplotlib.pyplot as plt
import numpy as np

# Sample data, to be replaced by real data from a SQL query
data = [
	[1,4,3,4,2,0,0,0,0,0,3,4,0,3],
	[3,3,3,3,4,4,4,1,1,1,2,2,2,0],
	[4,4,4,1,1,1,1,1,1,0,0,0,0,0]
]

# matplotlib is confusing; it knows it's a library for an object-oriented language,
# but it REALLY wants to be its own procedural language, so it breaks the pythonic 
# "everything is an object" convention and has too many subroutines and not enough 
# properties.
#
# For example, the "ax" object is an "axis" object, a subplot with a title, axis 
# labels, etc. to change the x-limits of the subplot to [-0.5,0.5], you don't do
#
# # ax.xlim = [-0.5,0.5]
#
# Instead, you have to do
#
# # ax.set_xlim([-0.5,0.5])
#
# which is 1) NOT the way the rest of your experience with Python works and 2) makes it 
# difficult to retrieve those values for later use (ax.xlim[0] doesn't exist, you have 
# to save that -0.5 in some other variable)
#
# That's just my little matplotlib rant, carry on.

fig = plt.figure(figsize=(4*len(data),3))	# width is proportional to the number of items we're plotting
superTitle = 'Student Ratings by Lab, Video, & Rubric Item'
# fig.suptitle(superTitle,fontsize=10)
for i in range(len(data)):
	ax = fig.add_subplot(1, len(data), i)
	ax.hist(data[i],histtype='stepfilled',alpha=0.45,bins=np.arange(-0.5,5.5,1),normed=True)
	ax.set_xticks(range(5))
	ax.set_title('Item '+str(i+1))
	ax.set_xticklabels(['P','F','G','VG','E'])
	ax.set_yticks([0,0.25,0.5,0.75,1])
	ax.set_yticklabels([])
	ax.set_ylim([0,1])
	ax.set_xlim([-0.5,4.5])
	ax.yaxis.tick_right()

plt.show()