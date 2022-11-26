import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import precision_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

def score_classification(model, df, scaler):
    score = 0
    for circuit in df[df.season == 2022]['round'].unique():
        test = df[(df.season == 2022) & (df['round'] == circuit)]
        X_test = test.drop(['driver', 'podium'], axis = 1)
        X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
        y_test = test.podium

        prediction_df = pd.DataFrame(model.predict_proba(X_test), columns = ['proba_0', 'proba_1'])
        prediction_df['actual'] = y_test.reset_index(drop = True)
        prediction_df.sort_values('proba_1', ascending = False, inplace = True)
        prediction_df.reset_index(inplace = True, drop = True)
        prediction_df['predicted'] = prediction_df.index
        prediction_df['predicted'] = prediction_df.predicted.map(lambda x: 1 if x == 0 else 0)# TODO i think i can check for a different postion here
        
        score += precision_score(prediction_df.actual, prediction_df.predicted)

    model_score = score / df[df.season == 2022]['round'].unique().max()
    return model_score


def performLogisticRegression(df, scaler, X_train, y_train, comparison_dict):
    params={'penalty': ['l1', 'l2'],
            'solver': ['saga', 'liblinear'],
            'C': np.logspace(-3,1,20)}

    for penalty in params['penalty']:
        for solver in params['solver']:
            for c in params['C']:
                model_params = (penalty, solver, c)
                model = LogisticRegression(penalty = penalty, solver = solver, C = c, max_iter = 10000)
                model.fit(X_train, y_train)
                
                model_score = score_classification(model, df, scaler)
                print('logistic_regression score: ' + str(model_score))
                
                comparison_dict['model'].append('logistic_regression')
                comparison_dict['params'].append(model_params)
                comparison_dict['score'].append(model_score)


def performRandomForestClassifier(df, scaler, X_train, y_train, comparison_dict):
    params={'criterion': ['gini', 'entropy'],
            'max_features': [0.8, 'auto', None],
            'max_depth': list(np.linspace(5, 55, 26)) + [None]}

    for criterion in params['criterion']:
        for max_features in params['max_features']:
            for max_depth in params['max_depth']:
                model_params = (criterion, max_features, max_depth)
                model = RandomForestClassifier(criterion = criterion, max_features = max_features, max_depth = max_depth)
                model.fit(X_train, y_train)
                
                model_score = score_classification(model, df, scaler)
                print('random_forest_classifier score: ' + str(model_score))
                
                comparison_dict['model'].append('random_forest_classifier')
                comparison_dict['params'].append(model_params)
                comparison_dict['score'].append(model_score)


def performSupportVectorMachinesClassifier(df, scaler, X_train, y_train, comparison_dict):
    params={'gamma': np.logspace(-4, -1, 20),
            'C': np.logspace(-2, 1, 20),
            'kernel': ['linear', 'poly', 'rbf', 'sigmoid']} 

    for gamma in params['gamma']:
        for c in params['C']:
            for kernel in params['kernel']:
                model_params = (gamma, c, kernel)
                model = SVC(probability = True, gamma = gamma, C = c, kernel = kernel )
                model.fit(X_train, y_train)
                
                model_score = score_classification(model, df, scaler)
                print('svm_classifier score: ' + str(model_score))
                
                comparison_dict['model'].append('svm_classifier')
                comparison_dict['params'].append(model_params)
                comparison_dict['score'].append(model_score)


def performNeuralNetworkClassifier(df, scaler, X_train, y_train, comparison_dict):
    params={'hidden_layer_sizes': [(80,20,40,5), (75,25,50,10)], 
            'activation': ['identity', 'logistic', 'tanh', 'relu'], 
            'solver': ['lbfgs', 'sgd', 'adam', 'logistic'], 
            'alpha': np.logspace(-4,2,20)} 

    for hidden_layer_sizes in params['hidden_layer_sizes']:
        for activation in params['activation']:
            for solver in params['solver']:
                for alpha in params['alpha']:
                    model_params = (hidden_layer_sizes, activation, solver, alpha )
                    model = MLPClassifier(hidden_layer_sizes = hidden_layer_sizes, activation = activation, solver = solver, alpha = alpha, random_state = 1)
                    model.fit(X_train, y_train)

                    model_score = score_classification(model, df, scaler)
                    print('neural_network_classifier score: ' + str(model_score))

                    comparison_dict['model'].append('neural_network_classifier')
                    comparison_dict['params'].append(model_params)
                    comparison_dict['score'].append(model_score)
        
