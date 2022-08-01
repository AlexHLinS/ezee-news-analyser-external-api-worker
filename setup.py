from setuptools import setup, find_packages

setup(name='ezee_naeaw',
      version='0.1a0',
      description='External API worker module for ezee-news-analyser product',
      long_description='External API worker module. Implement data gathering methods for ezee-news-analyser product',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.10',
          'Topic :: Tools'
      ],
      keywords='External API worker module ezee-news-analyser',
      url='https://github.com/AlexHLinS/ezee-news-analyser-external-api-worker',
      author='Alex Shkil',
      author_email='alexhlins@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'razdel>=0.5.0',
          'translate>=3.6.1',
          'requests>=2.28.0',
          'ujson>=5.3.0',
          'slovnet>=0.5.0',
          'newspaper3k==0.2.8'
      ],
      include_package_data=True,
      zip_safe=False)
