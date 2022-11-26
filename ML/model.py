import pandas as pd
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

    
def performXGBoostDriver(X_train, y_train, X_test, y_test):
    model = XGBRegressor(random_state=7)
    model.fit(X_train,y_train)
    
    prediction_df = pd.DataFrame(model.predict(X_test), columns = ['results'])
    prediction_df['driver'] = y_test.reset_index(drop = True)
    prediction_df.sort_values('results', ascending = True, inplace = True)
    prediction_df.reset_index(inplace = True, drop = True)
    prediction_df['predicted'] = prediction_df.index
    prediction_df['predicted'] = prediction_df.predicted.map(lambda x: x + 1 if x >= 0 else -1)

    return prediction_df
    
def performXGBoostConstructor(X_train, y_train, X_test, y_test):
    model = XGBRegressor(random_state=7)
    model.fit(X_train,y_train)
    
    prediction_df = pd.DataFrame(model.predict(X_test), columns = ['results'])
    prediction_df['constructor'] = y_test.reset_index(drop = True)
    prediction_df.sort_values('results', ascending = True, inplace = True)
    prediction_df.reset_index(inplace = True, drop = True)
    prediction_df['predicted'] = prediction_df.index
    prediction_df['predicted'] = prediction_df.predicted.map(lambda x: x + 1 if x >= 0 else -1)

    return prediction_df


def performLinearRegressionDriver(X_train, y_train, X_test, y_test):
    model = LinearRegression(fit_intercept = True)
    model.fit(X_train, y_train)
    
    prediction_df = pd.DataFrame(model.predict(X_test), columns = ['results'])
    prediction_df['driver'] = y_test.reset_index(drop = True)
    prediction_df.sort_values('results', ascending = True, inplace = True)
    prediction_df.reset_index(inplace = True, drop = True)
    prediction_df['predicted'] = prediction_df.index
    prediction_df['predicted'] = prediction_df.predicted.map(lambda x: x + 1 if x >= 0 else -1)

    return prediction_df


def performLinearRegressionConstructor(X_train, y_train, X_test, y_test):
    model = LinearRegression(fit_intercept = True)
    model.fit(X_train, y_train)
    
    prediction_df = pd.DataFrame(model.predict(X_test), columns = ['results'])
    prediction_df['constructor'] = y_test.reset_index(drop = True)
    prediction_df.sort_values('results', ascending = True, inplace = True)
    prediction_df.reset_index(inplace = True, drop = True)
    prediction_df['predicted'] = prediction_df.index
    prediction_df['predicted'] = prediction_df.predicted.map(lambda x: x + 1 if x >= 0 else -1)

    return prediction_df
