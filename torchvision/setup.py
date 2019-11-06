from setuptools import setup, find_packages

requirements = [
    'numpy==1.16.4',
    'torch==1.0.0'
]

setup(name='torchvision',
      version='0.3',
      description='dummy package',
      url='http://github.com/voca-ai/voca-packages/ctcclassifier',
      author='Nave Algarici',
      author_email='nave@voca.ai',
      license='VOCA',
      install_requires=requirements,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
