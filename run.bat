@echo off
:: Activate the Python environment
call webScrap\Scripts\activate

:: Run the Streamlit application on the desired port
call streamlit run main.py --server.port 3001

:: Pause to view any error messages or output
pause