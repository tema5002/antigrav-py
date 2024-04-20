from setuptools import setup, find_packages
 
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 11",
    "Programming Language :: Python :: 3"
]
 
setup(
    name="antigrav",
    version="1.0",
    description="antigrav is basically JSON but supports complex numbers",
    long_description=open("README.txt").read(),
    url="",
    author="tema5002",
    author_email="xtema5002x@gmail.com",
    license=None,
    classifiers=classifiers,
    keywords="kreisi",
    packages=find_packages(),
    install_requires=[""],
    long_description_content_type=True
)