import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
#Zhongxu Huang
#Jun.24th.2019

# It's a threshold for significance level
alpha = 0.05

# This is list for calculating defect density.
TOTALPOST = []
##configutation
POST1= []
POST1.append(0.33)
POST1.append(0.15)
POST1.append(9.07)
POST1.append(2.83)
POST1.append(6.94)
##collection
POST2= []
POST2.append(0.56)
POST2.append(0.20)
POST2.append(0.79)
POST2.append(0.17)
POST2.append(3.90)
##digester
POST3= []
POST3.append(11.49)
POST3.append(0.34)
POST3.append(0.23)
POST3.append(3.95)
POST3.append(1.07)
##jxpath
POST4= []
POST4.append(2.93)
POST4.append(2.58)
POST4.append(0.35)
POST4.append(6.93)
POST4.append(0.14)
##Codec
POST5= []
POST5.append(1.14)
POST5.append(0.62)
POST5.append(4.90)
POST5.append(11.15)
POST5.append(0.89)
TOTALPOST.append(POST1)
TOTALPOST.append(POST2)
TOTALPOST.append(POST3)
TOTALPOST.append(POST4)
TOTALPOST.append(POST5)

#This is list for code change.
TOTALCHANGE =[]
##configutation
CHANGE1 = []
CHANGE1.append(3.02)
CHANGE1.append(19.45)
CHANGE1.append(0.77)
CHANGE1.append(2.83)
CHANGE1.append(0.86)
##collection
CHANGE2 = []
CHANGE2.append(1.77)
CHANGE2.append(10.01)
CHANGE2.append(20.29)
CHANGE2.append(211.70)
CHANGE2.append(1.54)
##digester
CHANGE3= []
CHANGE3.append(1.74)
CHANGE3.append(8.82)
CHANGE3.append(26.55)
CHANGE3.append(3.04)
CHANGE3.append(2.80)
##jxpath
CHANGE4= []
CHANGE4.append(13.33)
CHANGE4.append(17.41)
CHANGE4.append(25.75)
CHANGE4.append(2.02)
CHANGE4.append(7.35)
##Codec
CHANGE5= []
CHANGE5.append(2.64)
CHANGE5.append(6.41)
CHANGE5.append(3.26)
CHANGE5.append(0.81)
CHANGE5.append(4.48)
TOTALCHANGE.append(CHANGE1)
TOTALCHANGE.append(CHANGE2)
TOTALCHANGE.append(CHANGE3)
TOTALCHANGE.append(CHANGE4)
TOTALCHANGE.append(CHANGE5)

# it's spearman function
def spearman(x,y):
	correlation, pvalue = stats.spearmanr(x, y)
	return correlation,pvalue

# This is a function to determine the correlation value is correct or not.
def isornotcorrect(pva):
	if pva > alpha:
		print('Samples are uncorrelated')
	else:
		print('Samples are correlated')

# This is a function to name generated png
def num_to_string(num):
    numbers = {
        0 : "commons_configuration_5+6",
        1 : "commons_collections_5+6",
        2 : "commons_digester_5+6",
        3 : "commons-jxpath_5+6",
		4 : "commons-codec_5+6"
    }
    return numbers.get(num, None)

#This is a function to connect two difference list
def list_add(list1,list2):
    totallist = []
    for i in range(len(list1)):
        totallist.append(list1[i]+list2[i])
    return totallist

#This is a function to calculate the percentage of two lists
def list_percentage(list1,list2):
	num1 = 0
	num2 = 0
	for i in range(len(list1)):
		num1+=list1[i]
		num2+=list2[i]
	totalpre = num1/(num1+num2)
	return totalpre


# main function
if __name__ == '__main__':
	for i in range(len(TOTALPOST)):
		correlation1,pvalue1 = spearman(TOTALCHANGE[i],TOTALPOST[i])
		print("correlation = "+str(correlation1), "pvalue = "+str(pvalue1))
		isornotcorrect(pvalue1)

		## The aim is to darw a graph and generate graoh.
		patches = []
		patches.append(mpatches.Patch(color='red', label="code change&&defect"))
		patches.append(mpatches.Patch(color='red', label="r=" + str(("%.2f" % correlation1)) + ", p=" + str(
			("%.2f" % pvalue1)) ))
		legend  =   plt.legend(handles=patches, fontsize="large", loc='best')
		nx1 = np.array(TOTALCHANGE[i])
		ny1 = np.array(TOTALPOST[i])
		plt.scatter(nx1, ny1,color = 'red')
		## This step can save all png files.
		plt.savefig('%s.png' % (num_to_string(i)))
		#This step can show the graph is console.
		plt.show()



