#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rrdtool
import time
import psutil

total_input = psutil.net_io_counters()[1]
total_output = psutil.net_io_counters()[0]
starttime = int(time.time())
update = rrdtool.updatev('/home/hgh/test/3/02/Flow.rrd',
        '%s:%s:%s' % (str(starttime),str(total_input),str(total_output))
        )
print 
print update
