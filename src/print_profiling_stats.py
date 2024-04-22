"""
@file profiling.py
@brief Script contains script to write profiling data to file.

@author
- Tomáš Lajda (xlajdat00)
@date April 22, 2024
"""

import pstats
import sys

p = pstats.Stats(sys.argv[1])
p.sort_stats('cumulative').print_stats()