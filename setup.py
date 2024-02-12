from setuptools import setup

setup(name='cbpi4-EasyEspFridge',
      version='0.0.1',
      description='Read Sensor Values from an EasyEsp device.',
      author='MiraeclVip',
      author_email='',
      url='https://github.com/MiracelVip/cbpi4-EasyEspFridge',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-EasyEspFridge': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-EasyEspFridge'],
     )