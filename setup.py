from setuptools import find_packages, setup

setup(
    name="netbox-mikrotik",
    version="0.1.0.dev1",
    description="Sync IP-Addresses to Mikrotik Address Lists and more.",
    author="Julius Koenig",
    author_email="info@bastelquartier.de",
    license="GPL-3.0",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
