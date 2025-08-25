# Copyright (c) 2025 Sensia Global
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
class Server:
    def __init__(self, host, port, unit, time_period, control_time_period, timeout, retries):
        self.host = host
        self.port = port
        self.unit = unit
        self.time_period = time_period
        self.control_time_period = control_time_period
        self.timeout = timeout
        self.retries = retries
        
