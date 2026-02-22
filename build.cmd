@echo off
echo ==============================================
echo  Nuno Europolitics - Deployment and Build
echo ==============================================

:: Create Virtual Environment
echo [1/4] Creating Virtual Environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo [ERROR] Failed to create virtual environment. Ensure Python is in your PATH.
    pause
    exit /b %errorlevel%
)

:: Activate Virtual Environment
echo [2/4] Activating Virtual Environment...
call venv\Scripts\activate.bat

:: Install Requirements
echo [3/4] Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install requirements.
    pause
    exit /b %errorlevel%
)

:: Run the App
echo [4/4] Starting the application...
streamlit run app.py

echo Deployment complete.
pause
