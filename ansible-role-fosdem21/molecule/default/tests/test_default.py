"""Role testing files using testinfra."""

import pytest

#
# Test 1
#

# def test_boxes_installed(host):
#     p = host.package('boxes')
#     assert p.is_installed



#
# Test 2
#

# @pytest.mark.parametrize("cmd,expected", [
#     (
#         "echo 'welcome to FOSDEM 21'  | boxes -d columns", 
#         "",
#         # (' __^__                      __^__\n'
#         #  '( ___ )--------------------( ___ )\n'
#         #  ' | / | welcome to FOSDEM 21 | \ |\n'
#         #  ' |___|                      |___|\n'
#         #  '(_____)--------------------(_____)\n'),        
#     )
# ])
# def test_cowsay(host, cmd, expected):
#     cmd_executed = host.command(cmd)
#     # import pprint
#     # pp = pprint.PrettyPrinter(indent=4)
#     # pp.pprint(cmd_executed)
#     # pp.pprint(host)
#     print(cmd_executed.stdout)
#     assert cmd_executed.exit_status == 0
#     assert cmd_executed.stdout == expected


