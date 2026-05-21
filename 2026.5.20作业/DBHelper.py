# -*- coding: utf-8 -*-
"""
DBHelper.py —— 通用数据库操作封装类

核心设计思路：
1. 封装复用：集中管理所有数据库交互逻辑，避免业务代码中重复写连接代码
2. 职责单一：只管"连库→执行→返回结果"，不管具体业务
3. 稳健性：写操作自带事务（commit / rollback），最后统一关闭连接，防止资源泄漏
"""

import pymysql


class DBHelper:
    """数据库助手类：负责 MySQL 连接的建立、查询、写入和关闭"""

    def __init__(self, host='localhost', user='root', pwd='123456', db='company', port=3306):
        """
        构造方法：初始化数据库连接和游标
        
        参数说明：
            host —— 数据库地址（本地一般是 'localhost' 或 '127.0.0.1'）
            user  —— MySQL 用户名（如 'root'）
            pwd   —— MySQL 密码
            db    —— 要使用的数据库名称（如 'didang'）
            port  —— 端口号，MySQL 默认 3306
        """
        # 建立 TCP 连接，charset 用 utf8mb4 支持中文和 emoji
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=pwd,
            database=db,
            charset='utf8mb4'
        )
        # 游标：用来执行 SQL 并获取结果的"光标"
        self.cursor = self.conn.cursor()

    def query(self, sql, params=None):
        """
        查询方法（SELECT）：执行查询语句并返回所有结果行
        
        参数：
            sql    —— SQL 语句字符串（可带占位符 %s）
            params —— 占位符对应的参数元组，防止 SQL 注入
        
        返回：
            元组组成的 tuple，每条记录是一个元组
        示例：((1, '张三', 'zhang@qq.com'), (2, '李四', ...))
        """
        self.cursor.execute(sql, params or ())  # params 为 None 时用空元组代替
        return self.cursor.fetchall()           # 取出全部结果

    def execute(self, sql, params=None):
        """
        执行方法（INSERT / UPDATE / DELETE）：带事务保护的写操作
        
        为什么需要事务？
          — commit()：确认修改，数据真正写入数据库
          — rollback()：出错时撤销，保证数据不会"写了一半"
        
        参数同 query()
        返回受影响的行数
        """
        try:
            # 第一步：通过游标发送 SQL 到 MySQL
            self.cursor.execute(sql, params or ())
            # 第二步：没有报错 → 提交事务（确认更改）
            self.conn.commit()
            return self.cursor.rowcount  # 返回影响了几行
        except Exception as e:
            # 出错了 → 回滚事务（撤销刚才的操作），然后抛出异常让调用方处理
            self.conn.rollback()
            raise e

    def close(self):
        """关闭游标和连接，释放资源（用完必须调！）"""
        self.cursor.close()
        self.conn.close()


# ==================== 使用示例 ====================
if __name__ == '__main__':
    # ① 创建 DBHelper 实例（默认参数已设置，可直接调用）
    db = DBHelper()  # host='localhost', user='root', pwd='123456', db='company'

    # ② 测试查询：看看 employees 表里有什么
    result = db.query('SELECT * FROM employees')
    print('查询结果:', result)

    # ③ 关闭连接（重要！不关会占用资源）
    db.close()
