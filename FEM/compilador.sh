#set -e

cd Result
rm -r *.vtk

cd ../Codes

source /Users/user/Downloads/.venv/bin/activate
python MainSteady.py

cd ../Result
paraview

exit 0