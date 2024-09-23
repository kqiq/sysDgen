
   from setuptools import setup, find_packages

   setup(
       name="systemd_service_generator",
       version="0.1.0",
       packages=find_packages(),
       install_requires=[],
       entry_points={
           'console_scripts': [
               'sdg=systemd_service_generator.generator:main',
           ],
       },
       author="kqiq",
       author_email="kqiqerl@gmail.com",
       description="A tool to generate systemd service files from a configuration file.",
       long_description=open('README.md').read(),
       long_description_content_type='text/markdown',
       url="https://github.com/yourusername/systemd_service_generator",
       classifiers=[
           "Programming Language :: Python :: 3",
           "License :: OSI Approved :: MIT License",
           "Operating System :: OS Independent",
       ],
       python_requires='>=3.6',
   )