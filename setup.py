from setuptools import setup, find_packages
import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.resolve()

PACKAGE_NAME='zenoh-ros-type'
VERSION='0.1.0'
DESCRIPTION='Common class for ROS 2 message used by Zenoh'
AUTHOR='ChenYing Kuo'
LICENSE='Apache-2.0'
EMAIL='evshary@gmail.com'
URL='https://github.com/evshary/zenoh-ros-type-python'

requirements = (ROOT_DIR / "requirements.txt").read_text(encoding="utf8")
REQUIREMENTS_PKG = [s.strip() for s in requirements.split("\n")]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      license=LICENSE,
      author_email=EMAIL,
      url=URL,
      install_requires=REQUIREMENTS_PKG,
      packages=find_packages(),
     )
