# -*- coding: UTF-8 -*-
"""
======================
@author:fangkun
@time:2020/5/13:17:33
======================
"""
import re
from scripts.handle_mysql import HandleMsql
HandleMsql().create_not_existesd_id()
class Context:
    '''

    '''

    not_existed_id_pattern = r'\${not_existed_id}'

    def not_existed_id_replace(self, data):
        if re.search(self.not_existed_id_pattern, data):
            do_mysql = HandleMsql.create_not_existesd_id()
            res3 = re.sub(self.not_existed_id_pattern, '15882223197', data)

            do_mysql.close()
