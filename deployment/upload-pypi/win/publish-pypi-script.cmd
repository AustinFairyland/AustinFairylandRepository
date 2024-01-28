pip install setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install --upgrade setuptools wheel -i https://pypi.tuna.tsinghua.edu.cn/simple
python setup.py sdist bdist_wheel
pip install twine -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install --upgrade twine -i https://pypi.tuna.tsinghua.edu.cn/simple
twine upload dist/*
