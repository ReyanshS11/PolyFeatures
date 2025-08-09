import os

old_version = '0.0.27'

os.system("python setup.py sdist bdist_wheel")
os.system(f"del dist\polyfeatures-{old_version}-py3-none-any.whl")
os.system(f"del dist\polyfeatures-{old_version}.tar.gz")
os.system('twine upload dist/*')