# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 01:56:34 2020

@author: Zhiyue June Wei
"""

# Setup.py file, needed to be created in the parent directory
import setuptools

    
# Notice that, firstly, you need to pip install the packaege in the parent directory
# Then, you can use this package system-wide

setuptools.setup(
    name = "CrunchbaseAPI",
    version = "0.1.0",
    author = "ZhiyuJuneWei",
    author_email = "zhiyuewei0407@gmail.com",
    description = "A api for crunchbase data (organizations and people information",
    packages = ['CrunchbaseAPI'],
    license = 'Apache',
    url = "https://github.com/JuniusWei/cbapi",
    install_requires = ['pandas', 'requests'],
    platforms = ['any'],
    keywords = 'pandas, CrunchbaseAPI'
    )

