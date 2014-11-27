PACKAGE = "oklink"
NAME = "oklink"
DESCRIPTION = "oklink api python sdk"
AUTHOR = "liu tao"
AUTHOR_EMAIL = "support@oklink.com"
URL = "https://www.oklink.com"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    package_data=find_package_data(
            PACKAGE,
            only_in_packages=False
      ),
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    install_requires=[
        'httplib2>=0.8',
        'requests>=1.1.0',
        'oauth2client>=1.1',
    ],    
    zip_safe=False,
)