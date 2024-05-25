from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='truefloat',
  version='0.0.1',
  author='furryich',
  author_email='thesavea89@gmail.com',
  description='True float. Without strange num',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='your_url',
  packages=find_packages(),
  install_requires=[''],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='float truefloat',
  project_urls={
    'GitHub': 'https://github.com/UserForBruteer'
  },
  python_requires='>=3.6'
)