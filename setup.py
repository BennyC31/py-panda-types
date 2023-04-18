import setuptools

setuptools.setup(
    include_package_data=True,
    name='py-panda-types',
    version='0.0.1',
    description='Package for bundling data files into one Data Frame.',
    install_requires=['pandas==2.0.0'],
    url='git@github.com:BennyC31/py-panda-types.git',
    author='Benjamin Calderaio, Jr.',
    author_email='bencalderaio@gmail.com',
    packages=['pypantypes'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.9.0',
        'Operating System :: OS Independent',
    ],
)