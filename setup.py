from setuptools import setup, find_packages

setup(
    name='row-confusion-matrix',
    version='0.1.0',
    author='Your Name',
    description='A row-based confusion matrix for classification problems',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/row-confusion-matrix',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
