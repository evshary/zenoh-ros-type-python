from setuptools import setup, find_packages
import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.resolve()

PACKAGE_NAME='zenoh-ros-type'
VERSION='0.2.2'
DESCRIPTION='Common class for ROS 2 message used by Zenoh'
LONG_DESCRIPTION = (ROOT_DIR / "README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"

AUTHOR='ChenYing Kuo'
LICENSE='Apache-2.0'
EMAIL='evshary@gmail.com'
URL='https://github.com/evshary/zenoh-ros-type-python'

requirements = (ROOT_DIR / "requirements.txt").read_text(encoding="utf8")
REQUIREMENTS_PKG = [s.strip() for s in requirements.split("\n")]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=EMAIL,
      url=URL,
      install_requires=REQUIREMENTS_PKG,
      packages=find_packages(),
     )
