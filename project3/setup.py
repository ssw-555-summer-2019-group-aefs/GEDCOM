from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name="project3",
            maintainer="AEFS",
            maintainer_email="",
            description="Travis set up for SSW 555 Summer 2019 GEDCOM group project",
            long_description="Travis set up for SSW 555 Summer 2019 GEDCOM group project",
            url="https://github.com/ssw-555-summer-2019-group-aefs/GEDCOM",
            download_url="",
            license="Stevens Institute of Technology",
            packages=PACKAGES)


if __name__ == '__main__':
    setup(**opts)