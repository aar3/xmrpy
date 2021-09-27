# Copyright 2021 Rashad Alston

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
# EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.

import logging
from xmrpy._config import config

LOG_FORMAT = "[%(asctime)s] %(levelname)s PID:%(process)s %(module)s L%(lineno)s - %(message)s"

logging.basicConfig(
    level=config.LOG_LEVEL,
    filename=config.LOG_FILE,
    format=LOG_FORMAT,
    datefmt="%Y/%m/%d %H:%M:%S",
)


console = logging.StreamHandler()
console.setLevel(config.LOG_LEVEL)
console.setFormatter(logging.Formatter(LOG_FORMAT))

logger = logging.getLogger("xmrpy")
logger.addHandler(console)
