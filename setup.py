from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='reason',
    version='0.6.1',
    description='Easy-to-use NLP toolbox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alisoltanirad/reason',
    author='Ali Soltani Rad',
    author_email='soltaniradali@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Natural Language :: English',
    ],
    python_requires='>=3.7',
    install_requires=[
        'numpy'
    ],
)
