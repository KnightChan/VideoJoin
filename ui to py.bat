for /r %%i in (*.ui) do (
	python2 -m PyQt4.uic.pyuic %%i -o %%~dpni.py
	
)	

pause