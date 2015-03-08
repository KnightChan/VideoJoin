rd /s /q build
rd /s /q msi
python2 setup.py -q bdist -d msi
python2 setup.py -q bdist_msi -d msi
exit