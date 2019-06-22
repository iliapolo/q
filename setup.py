#############################################################################
# Copyright (c) 2018 Eli Polonsky. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   * See the License for the specific language governing permissions and
#   * limitations under the License.
#
#############################################################################

from setuptools import setup

setup(
    name='q',
    version='1.8',
    author='Harel Ben-Attia',
    author_email='harelba@gmail.com',
    install_requires=[
        'six==1.11.0',
        'flake8==3.6.0'
    ],
    packages=[
        'bin'
    ],
    entry_points={
        'console_scripts': [
            'q2 = bin.qtextasdata:run_standalone'
        ]
    }
)
