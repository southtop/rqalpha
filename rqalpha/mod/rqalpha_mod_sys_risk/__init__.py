# -*- coding: utf-8 -*-
#
# Copyright 2017 Ricequant, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click
from rqalpha.__main__ import cli

__config__ = {
    # available_cash: 查可用资金是否充足，默认开启
    "available_cash": True,
    # available_position: 检查可平仓位是否充足，默认开启
    "available_position": True,
    # short_stock: 允许裸卖空
    "short_stock": False,
}


def load_mod():
    from .mod import RiskManagerMod
    return RiskManagerMod()


"""
注入 --short-stock option
可以通过 `rqalpha run --short-stock` 来开启允许卖空
"""
cli_prefix = "mod__sys_plot__"

cli.commands['run'].params.append(
    click.Option(
        ("--short-stock", cli_prefix + "short_stock"),
        is_flag=True,
        help="[sys_risk]enable stock shorting"
    )
)
