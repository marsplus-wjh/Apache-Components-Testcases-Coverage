import scipy.stats as stats
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
#Zhongxu Huang
#Jun.24th.2019

# It's a threshold for significance level
alpha = 0.05

#This is a path list for all files
PATH2 = []
PATH2.append('/Users/donald/Desktop/Mutation_score/configuration/finaljacoco1.csv')
PATH2.append('/Users/donald/Desktop/Mutation_score/Collection/jacoco.csv')
PATH2.append('/Users/donald/Desktop/Mutation_score/digester/finaljacoco.csv')
PATH2.append('/Users/donald/Desktop/Mutation_score/Jxpath/finaljacoco.csv')
PATH2.append('/Users/donald/Desktop/Mutation_score/Codec/jacoco.csv')

# This function to read file and generate according lists.
def readfile2(path):
	with open(path,"rt", encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		branch_coverage = [row['BRANCH_COVERED'] for row in reader]
	with open(path,"rt", encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		branch_missed = [row['BRANCH_MISSED'] for row in reader]
	with open(path,"rt", encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		line_coverage = [row['LINE_COVERED'] for row in reader]
	with open(path,"rt", encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		line_missed = [row['LINE_MISSED'] for row in reader]
	with open(path,"rt", encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		mutation_score = [row['MUTATION_SCORE'] for row in reader]
	branch_coverage = list(map(int, branch_coverage))
	branch_missed = list(map(int, branch_missed))
	line_coverage = list(map(int, line_coverage))
	line_missed = list(map(int, line_missed))
	mutation_score = list(map(float, mutation_score))
	branch_coverage_percentage = list_percentage(branch_coverage,branch_missed)
	line_coverage_percentage = list_percentage(line_coverage,line_missed)
	return branch_coverage_percentage,line_coverage_percentage,mutation_score

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
        0 : "commons_configuration_mutation",
        1 : "commons_collections_mutation",
        2 : "commons_digester_mutation",
        3 : "commons-jxpath_mutation",
		4 : "commons-codec_mutation"
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
	totallist = []
	for i in range(len(list1)):
		if list1[i]+list2[i]==0:
			num =float('inf')
		else:
			num = list1[i]/(list1[i]+list2[i])
		totallist.append(num)
	return totallist

# main function
if __name__ == '__main__':
	for i in range(len(PATH2)):
		branch_coverage_percentage,line_coverage_percentage,mutation_score =readfile2(PATH2[i])
		correlation1, pvalue1 = spearman(branch_coverage_percentage, mutation_score)
		print("correlation = " + str(correlation1), "pvalue = " + str(pvalue1))
		isornotcorrect(pvalue1)
		correlation2, pvalue2 = spearman(line_coverage_percentage, mutation_score)
		print("correlation = " + str(correlation2), "pvalue = " + str(pvalue2))
		isornotcorrect(pvalue2)

		## The aim is to darw a graph and generate graoh.
		patches = []
		patches.append(mpatches.Patch(color='red', label="branch&&mutation score"))
		patches.append(mpatches.Patch(color='blue', label="statement&&mutation score"))
		patches.append(mpatches.Patch(color='red', label="r=" + str(("%.2f" % correlation1)) + ", p=" + str(
			("%.2f" % pvalue1))))
		patches.append(mpatches.Patch(color='blue', label="r=" + str(("%.2f" % correlation2)) + ", p=" + str(
			("%.2f" % pvalue2))))
		legend = plt.legend(handles=patches, fontsize="large", loc='best')
		nx1 = np.array(branch_coverage_percentage)
		ny1 = np.array(mutation_score)
		plt.scatter(nx1, ny1, color='red')
		nx2 = np.array(line_coverage_percentage)
		ny2 = np.array(mutation_score)
		plt.scatter(nx2, ny2, color='blue')
		## This step can save all png files.
		plt.savefig('%s.png' % (num_to_string(i)))
		# This step can show the graph is console.
		plt.show()


