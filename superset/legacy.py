# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Code related with dealing with legacy / change management"""
from typing import Any


def update_time_range(form_data: dict[str, Any]) -> None:
    """Move since and until to time_range."""
    if "since" in form_data or "until" in form_data:
        form_data["time_range"] = "{} : {}".format(
            form_data.pop("since", "") or "", form_data.pop("until", "") or ""
        )
