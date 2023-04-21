import setuptools

with open('README.md','r') as rfile:
        long_description = rfile.read()
setuptools.setup(
    
    include_package_data=True,
    name='py-panda-types',
    version='0.0.3',
    description='Package for bundling data files into one Data Frame.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
    url='https://github.com/BennyC31/py-panda-types.git',
    author='Benjamin Calderaio, Jr.',
    author_email='bencalderaio@gmail.com',
    packages=['pypantypes'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
)