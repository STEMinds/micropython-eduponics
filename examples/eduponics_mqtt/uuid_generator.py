"""
MicroPython MQTT Eduponics APP Client
https://github.com/STEMinds/micropython-eduponics
MIT License
Copyright (c) 2020 STEMinds

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import uuid

'''
There are 3 different ways to generate unique UUID, choose which one suitable for you.
'''

# make a UUID based on the host ID and current time, best option.
uuid_x = uuid.uuid1()
print(uuid_x)

# make a UUID using an MD5 hash of a namespace UUID and a name
uuid_y = uuid.uuid3(uuid.NAMESPACE_DNS, 'steminds.com')
print(uuid_y)

# make a random UUID
uuid_z = uuid.uuid4()
print(uuid_z)
