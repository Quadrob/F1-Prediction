import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.metrics import precision_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor


def scoreRegression(model, df, scaler):
    score = 0
    for circuit in df[df.season == 2022]['round'].unique():
        test = df[(df.season == 2022) & (df['round'] == circuit)]
        X_test = test.drop(['driver', 'podium'], axis = 1)
        X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
        y_test = test.podium

        prediction_df = pd.DataFrame(model.predict(X_test), columns = ['results'])
        prediction_df['podium'] = y_test.reset_index(drop = True)
        prediction_df['actual'] = prediction_df.podium.map(lambda x: 1 if x == 1 else 0) # TODO i think i can check for a different postion here
        prediction_df.sort_values('results', ascending = True, inplace = True)
        prediction_df.reset_index(inplace = True, drop = True)
        prediction_df['predicted'] = prediction_df.index
        prediction_df['predicted'] = prediction_df.predicted.map(lambda x: 1 if x == 0 else 0)

        score += precision_score(prediction_df.actual, prediction_df.predicted)

    model_score = score / df[df.season == 2022]['round'].unique().max()
    return model_score


def performLinearRegression(df, scaler, X_train, y_train, comparison_dict):
    params={'fit_intercept': ['True', 'False']}
    for fit_intercept in params['fit_intercept']:
        model_params = (fit_intercept)
        model = LinearRegression(fit_intercept = fit_intercept)
        model.fit(X_train, y_train)
        
        model_score = scoreRegression(model, df, scaler)
        print('linear_regression score: ' + str(model_score))
                
        comparison_dict['model'].append('linear_regression')
        comparison_dict['params'].append(model_params)
        comparison_dict['score'].append(model_score)

    
def performRandomForestRegression(df, scaler, X_train, y_train, comparison_dict):
    params={'criterion': ['mse'],
            'max_features': [0.8, 'auto'],
            'max_depth': list(np.linspace(5, 55, 26))}

    for criterion in params['criterion']:
        for max_features in params['max_features']:
            for max_depth in params['max_depth']:
                model_params = (criterion, max_features, max_depth)
                model = RandomForestRegressor(criterion = criterion, max_features = max_features, max_depth = max_depth, random_state = 1)
                model.fit(X_train, y_train)
                
                model_score = scoreRegression(model, df, scaler)
                print('random_forest_regressor score: ' + str(model_score))
                
                comparison_dict['model'].append('random_forest_regressor')
                comparison_dict['params'].append(model_params)
                comparison_dict['score'].append(model_score)


def performSupportVectorMachineRegression(df, scaler, X_train, y_train, comparison_dict):
    params={'gamma': np.logspace(-4, -1, 10),
            'C': np.logspace(-2, 1, 10),
            'kernel': ['linear', 'poly', 'rbf', 'sigmoid']}

    for gamma in params['gamma']:
        for c in params['C']:
            for kernel in params['kernel']:
                model_params = (gamma, c, kernel)
                model = SVR(gamma = gamma, C = c, kernel = kernel)
                model.fit(X_train, y_train)

                model_score = scoreRegression(model, df, scaler)
                print('svm_regressor score: ' + str(model_score))
                
                comparison_dict['model'].append('svm_regressor')
                comparison_dict['params'].append(model_params)
                comparison_dict['score'].append(model_score)


def performNeuralNetworkRegression(df, scaler, X_train, y_train, comparison_dict):
    params={'hidden_layer_sizes': [(80,20,40,5), (75,30,50,10,3)], 
            'activation': ['identity', 'relu','logistic', 'tanh',], 
            'solver': ['lbfgs','sgd', 'adam'], 
            'alpha': np.logspace(-4,1,20)} 

    for hidden_layer_sizes in params['hidden_layer_sizes']:
        for activation in params['activation']:
            for solver in params['solver']:
                for alpha in params['alpha']:
                    model_params = (hidden_layer_sizes, activation, solver, alpha )
                    model = MLPRegressor(hidden_layer_sizes = hidden_layer_sizes, activation = activation, solver = solver, alpha = alpha, random_state = 1)
                    model.fit(X_train, y_train)

                    model_score = scoreRegression(model, df, scaler)
                    print('nn_regressor score: ' + str(model_score))

                    comparison_dict['model'].append('nn_regressor')
                    comparison_dict['params'].append(model_params)
                    comparison_dict['score'].append(model_score)


def performLinearRegressionTesting(df, scaler, X_train, y_train, season, round):
    model = LinearRegression(fit_intercept = True)
    model.fit(X_train, y_train)
    
    test = df[(df.season == season) & (df['round'] == round)]
    X_test = test.drop(['driver', 'podium'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test.podium

    prediction_df = pd.DataFrame(model.predict(X_test), columns = ['results'])
    prediction_df['podium'] = y_test.reset_index(drop = True)
    prediction_df['actual'] = prediction_df.podium.map(lambda x: 1 if x == 1 else 0) # TODO i think i can check for a different postion here
    prediction_df.sort_values('results', ascending = True, inplace = True)
    prediction_df.reset_index(inplace = True, drop = True)
    prediction_df['predicted'] = prediction_df.index
    prediction_df['predicted'] = prediction_df.predicted.map(lambda x: 1 if x == 0 else 0)
    prediction_df = pd.merge(prediction_df, test[['driver', 'podium', 'season', 'round']], how='inner', on=['podium'])

    return prediction_df

    
def performXGBoostTesting(df, scaler, X_train, y_train, season, round):
    model = XGBRegressor(random_state=7)
    model.fit(X_train,y_train)
    
    test = df[(df.season == season) & (df['round'] == round)]
    X_test = test.drop(['driver', 'podium'], axis = 1)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns)
    y_test = test.podium

    prediction_df = pd.DataFrame(model.predict(X_test), columns = ['results'])
    prediction_df['podium'] = y_test.reset_index(drop = True)
    prediction_df['actual'] = prediction_df.podium.map(lambda x: 1 if x == 1 else 0) # TODO i think i can check for a different postion here
    prediction_df.sort_values('results', ascending = True, inplace = True)
    prediction_df.reset_index(inplace = True, drop = True)
    prediction_df['predicted'] = prediction_df.index
    prediction_df['predicted'] = prediction_df.predicted.map(lambda x: 1 if x == 0 else 0)
    prediction_df = pd.merge(prediction_df, test[['driver', 'podium', 'season', 'round']], how='inner', on=['podium'])

    return prediction_df

    

