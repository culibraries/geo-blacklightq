#import ez_setup
# ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(name='geoblacklightq',
      version='0.0.7.746',
      packages=find_packages(),
      package_data={'geoblacklightq': [
          'tasks/templates/*.tmpl', 'geoblacklightq/tasks/templates/*.tmpl']},
      install_requires=[
          'requests==2.20.1',
          'xmltodict==0.11.0',
          'jinja2',
          'gsconfig-py3',
          'fiona',
          'mock',
          'rasterio'
      ],
      include_package_data=True,
      )


# 'fiona==1.7.12',
