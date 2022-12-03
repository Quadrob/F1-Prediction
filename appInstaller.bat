pyinstaller -F --log-level=INFO --noconfirm --noupx --onedir --nowindow ^
    --collect-all "xgboost" ^
    --hidden-import="sklearn.utils._cython_blas" ^
    --hidden-import="xgboost" ^
    --add-data "C:/Python/Lib/site-packages/customtkinter;customtkinter/" ^
    --add-data "C:/Python/Lib/site-packages/xgboost/VERSION;xgboost/" ^
    --add-data "C:/Python/xgboost/*;xgboost/" ^
    --icon "C:\Coding\PythonProjects\F1-Prediction\Assests\F1-logo.ico" ^
    F1Predict.py

echo d | xcopy "C:\Coding\PythonProjects\F1-Prediction\Assests" "C:\Coding\PythonProjects\F1-Prediction\dist\F1Predict\Assests"

timeout /t 300