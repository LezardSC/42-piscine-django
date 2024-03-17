pip --version
mkdir -p local_lib
python3 -m pip install --target=local_lib --upgrade git+https://github.com/jaraco/path.git --log install_path.log
python3 my_program.py