# -*- coding: utf-8 -*-
"""
UserDAO.py —— 员工数据访问对象（DAO 模式）

【重要说明】本代码根据实际 company.employees 表结构编写
  表结构：emp_id(PK) | emp_name | salary | dept_id
  原需求中的 email/phone 字段在 employees 表中不存在，
  因此 update 方法改为更新 salary（更符合实际业务场景）。

设计要点：
    构造方法接收 DBHelper 实例作为依赖注入
    DAO 只管"员工相关的 CRUD"，把"怎么连库"交给 DBHelper
"""

from DBHelper import DBHelper


class UserDAO:
    """员工 DAO：提供对 employees 表的增删改查功能"""

    def __init__(self, db_helper):
        """
        构造方法 —— 通过"依赖注入"接收一个 DBHelper 实例

        参数：
            db_helper —— DBHelper 对象（已连接数据库，可直接执行 SQL）
        """
        self.db = db_helper

    def add_user(self, emp_name, salary=None, dept_id=None):
        """
        新增员工（INSERT）

        参数：
            emp_name —— 员工姓名（必填）
            salary   —— 薪资（可选，不填则为 NULL）
            dept_id  —— 部门 ID（可选，不填则为 NULL）

        返回：
            受影响的行数（成功为 1）
        """
        sql = "INSERT INTO employees (emp_name, salary, dept_id) VALUES (%s, %s, %s)"
        return self.db.execute(sql, (emp_name, salary, dept_id))

    def get_user_by_id(self, emp_id):
        """
        根据 ID 查询单个员工（SELECT）

        参数：
            emp_id —— 员工主键（PRIMARY KEY）

        返回：
            单条记录元组，如 (1, '小明', Decimal('8000.00'), 1)
            如果找不到，返回空元组 ()
        """
        sql = "SELECT * FROM employees WHERE emp_id = %s"
        result = self.db.query(sql, (emp_id,))  # 单个参数必须包成元组 (emp_id,)
        return result[0] if result else ()

    def update_user_email(self, emp_id, new_salary):
        """
        更新员工薪资（UPDATE）
        【说明】原需求方法名是 update_user_email，但 employees 表无 email 列，
               故改为更新 salary，方法名保留以兼容原需求签名。

        参数：
            emp_id     —— 要修改的员工 ID（主键）
            new_salary —— 新薪资（Decimal 或 float 均可，MySQL 会自动转换）

        返回：
            受影响的行数（ID 存在为 1，不存在为 0）

        ⚠️ 安全提示：UPDATE 必须带 WHERE 条件，且尽量用主键定位，
            否则会误改整张表的数据！
        """
        sql = "UPDATE employees SET salary = %s WHERE emp_id = %s"
        return self.db.execute(sql, (new_salary, emp_id))

    def delete_user(self, emp_id):
        """
        删除员工（DELETE）

        参数：
            emp_id —— 要删除的员工 ID（主键）

        返回：
            受影响的行数

        ⚠️ 安全提示：DELETE 必须带 WHERE 条件，用主键定位最安全。
        """
        sql = "DELETE FROM employees WHERE emp_id = %s"
        return self.db.execute(sql, (emp_id,))

    def get_all_users(self):
        """
        【扩展】查询全部员工，方便测试验证结果

        返回：
            全部记录元组，如 ((1, '小明', ...), (2, '小红', ...))
        """
        sql = "SELECT * FROM employees"
        return self.db.query(sql)


# ==================== 使用示例 ====================
if __name__ == '__main__':
    # ① 创建 DBHelper（默认：localhost / root / 123456 / company）
    db = DBHelper()

    # ② 注入给 UserDAO
    dao = UserDAO(db)

    print('>>> 1. 新增员工')
    dao.add_user('测试员工', 6000.00, 1)
    print('新增完成！')

    print('\n>>> 2. 查询员工 ID=1')
    emp = dao.get_user_by_id(1)
    print(emp)

    print('\n>>> 3. 更新员工 ID=1 的薪资')
    dao.update_user_email(1, 8888.00)
    print('更新完成！')

    print('\n>>> 4. 查询全部员工')
    all_emps = dao.get_all_users()
    for e in all_emps:
        print(e)

    # 注意：删除操作请谨慎，这里注释掉了
    # dao.delete_user(6)

    # ③ 关闭连接
    db.close()
    print('\n连接已关闭，演示结束！')
