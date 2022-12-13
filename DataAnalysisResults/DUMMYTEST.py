

import matplotlib.pyplot as plt
import pandas as pd

def plotBarGraph(dataframe, picturePath):
    # plt.bar(dataframe.name, dataframe.score, color ='maroon', width = 0.4)    
    fig = plt.figure()
    fig.clf()
    ax = fig.add_subplot(111)
    plt.setp(ax.get_xticklabels(), fontsize=10, rotation='vertical')
    plt.bar(dataframe.name, dataframe.score, color ='maroon', width = 0.4)    
    plt.xlabel("Machine Learning Model")
    plt.ylabel("Success Percentage %")
    plt.title("Comparison Of Machine Learning Models")
    plt.show()
    plt.savefig(picturePath)

df = pd.DataFrame([['linear_regression', 66.5656], ['random_forest_regressor', 51], 
                   ['svm_regressor', 54.5], ['neural_network_regressor', 61.89],
                   ['logistic_regression', 60.333], ['random_forest_classifier', 53],
                   ['svm_classifier', 55.1], ['neural_network_classifier', 58],
                   ['xgboost_regressor', 66.5656]], columns=['name', 'score'])

plotBarGraph(df, 'predictionComparisonReg.png')