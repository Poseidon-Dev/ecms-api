from distutils.core import setup


setup(
    name='ecmsapi',
    # package_dir='src',
    # packages=['ecmsapi'],
    version='0.1.4',
    license='MIT',
    description='A python integration to allow for quickly sending queries directly to the as400',
    author='Johnny Whitworth',
    author_email='jwhitworth@arizonapipeline.com',
    url='https://github.com/Poseidon-Dev/ecms-api',
    download_url='https://github.com/Poseidon-Dev/ecms-api/archive/refs/tags/v_0.1.1.zip',
    keywords=['ecms', 'cgc'],
    requires=[
        'pandas',
        'pyodbc',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
    ],
)
