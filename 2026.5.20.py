# #数据库的链接的基本使用
# import pymysql
# # 第1步：连接数据库
# conn = pymysql.connect(
#     host='localhost',      # 数据库地址（本地就是 localhost）
#     port=3306,             # MySQL 端口号，默认 3306
#     user='root',           # 用户名
#     password='123456',     # 密码（改成你自己的！）
#     database='company'     # 数据库名
# )
# # 第2步：创建游标（用来执行 SQL）
# cursor = conn.cursor()

# 第3步：执行 SQL 查询
# cursor.execute('''SELECT * FROM  employees
#                where salary > 8000 and salary < 10000 ''')
#执行插入
# sql="INSERT INTO employees (emp_name, salary,dept_id)" \
# " VALUES ('John', 9000,3)"
# cursor.execute(sql)
#执行批量插入
# sql="INSERT INTO employees (emp_name, salary,dept_id)" \
#     " VALUES (%s, %s, %s)"
# val=[
#     ('钱九', 18000,4),
    
# ]
# cursor.executemany(sql,val)

#执行更新,使用参数化更新

# sql="UPDATE employees SET salary = %s WHERE emp_name = %s"
# ud=(10000,'钱九')
# cursor.execute(sql,ud)
#删除
# sql="DELETE FROM employees WHERE emp_name = %s"
# ud=('钱九',)
# cursor.execute(sql,ud)
#开始事务,将Alice账户的500元转到Bob账户
# conn.begin()
# sql="UPDATE employees SET salary = salary - 500 " \
# "WHERE emp_name = %s"
# ud=('Alice',)
# cursor.execute(sql,ud)
# sql="UPDATE employees SET salary = salary + 500 " \
# "WHERE emp_name = %s"
# ud=('Bob',)
# cursor.execute(sql,ud)
# #提交事务
# conn.commit()
# #全部插入/fetchone/fetchmany/fetchall
# # 第4步：获取查询结果
# result = cursor.fetchall()
# print(result)
# # 第5步：关闭连接（先关游标，再关连接）
# cursor.close()
# conn.close()

# import pymysql

# # 连接数据库
# conn = pymysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='123456',
#     autocommit=True  # 自动提交，DML操作不用手动commit
# )

# # ====== 追踪当前数据库 ======
# current_db = None

# def create_database(conn, db_name):
#     """创建数据库"""
#     sql = f"CREATE DATABASE `{db_name}`"
#     cursor = conn.cursor()
#     try:
#         cursor.execute(sql)
#         print(f"✅ 数据库 [{db_name}] 创建成功！")
#     except pymysql.err.ProgrammingError as e:
#         if "1007" in str(e):
#             print(f"⚠️ 数据库 [{db_name}] 已存在，无需重复创建")
#         else:
#             print(f"❌ 创建失败: {e}")
#     finally:
#         cursor.close()

# def use_database(conn, db_name):
#     """选择/切换数据库"""
#     cursor = conn.cursor()
#     try:
#         cursor.execute(f"USE `{db_name}`")
#         print(f"✅ 已切换到数据库 [{db_name}]")
#         return db_name
#     except pymysql.err.ProgrammingError as e:
#         if "1049" in str(e):
#             print(f"⚠️ 数据库 [{db_name}] 不存在！请先创建")
#         else:
#             print(f"❌ 切换失败: {e}")
#         return None
#     finally:
#         cursor.close()

# def create_table(conn, table_name, columns):
#     """创建表"""
#     cursor = conn.cursor()
#     try:
#         sql = f"CREATE TABLE `{table_name}` ({columns})"
#         cursor.execute(sql)
#         print(f"✅ 表 [{table_name}] 创建成功！")
#     except pymysql.err.ProgrammingError as e:
#         if "1050" in str(e):
#             print(f"⚠️ 表 [{table_name}] 已存在，无需重复创建")
#         else:
#             print(f"❌ 创建失败: {e}")
#     finally:
#         cursor.close()

# def build_columns():
#     """交互式逐列添加字段，返回拼接好的字段字符串"""
#     columns_list = []  # 存放每一列的定义
#     print("\n--- 开始添加字段（输入 q 结束）---")
#     print("常用类型提示：INT, VARCHAR(n), DATE, DECIMAL(m,n), TEXT, DATETIME")

#     while True:
#         col_name = input("\n字段名（输入 q 结束）：").strip()
#         if col_name.lower() == 'q':
#             break
#         if not col_name:
#             print("⚠️ 字段名不能为空！")
#             continue

#         col_type = input("字段类型（如 INT, VARCHAR(20), DATE）：").strip()
#         if not col_type:
#             print("⚠️ 字段类型不能为空！")
#             continue

#         # 拼接约束条件
#         constraints = ""
#         print("约束选项（直接回车跳过）：")
#         pk = input("  是否主键？(y/n)：").strip().lower()
#         if pk == 'y':
#             constraints += " PRIMARY KEY"
#         nn = input("  是否非空？(y/n)：").strip().lower()
#         if nn == 'y':
#             constraints += " NOT NULL"
#         ai = input("  是否自增？(y/n)：").strip().lower()
#         if ai == 'y':
#             constraints += " AUTO_INCREMENT"
#         default = input("  默认值（回车跳过）：").strip()
#         if default:
#             constraints += f" DEFAULT '{default}'"  # 字符串类型加引号
#         comment = input("  字段注释（回车跳过）：").strip()
#         if comment:
#             constraints += f" COMMENT '{comment}'"

#         # 拼成完整的一列定义
#         one_col = f"`{col_name}` {col_type}{constraints}"
#         columns_list.append(one_col)
#         print(f"  ✅ 已添加：{one_col}")

#     if not columns_list:
#         return None

#     # 用逗号拼接所有列
#     result = ", ".join(columns_list)
#     print(f"\n📋 最终字段定义：\n   {result}")
#     return result

# while True:
#     print("\n1.创建数据库")
#     print("2.选择数据库")
#     print("3.创建表")
#     print("4.插入数据")
#     print("5.查询数据")
#     print("6.更新数据")
#     print("7.删除数据")
#     print("8.退出")
#     a = input("请输入对应的指令：")

#     if a == "1":
#         db = input("请输入创建的数据库名称：")
#         create_database(conn, db)

#     elif a == "2":
#         cursor = conn.cursor()
#         cursor.execute("SHOW DATABASES")
#         result = cursor.fetchall()
#         print("当前所有的数据库：")
#         for i in result:
#             print(f"  {i[0]}")
#         cursor.close()
#         db = input("请选择数据库：")
#         res = use_database(conn, db)
#         if res:
#             current_db = res  # ✅ 记录当前数据库

#     elif a == "3":
#         # ✅ 检查是否已选择数据库
#         if not current_db:
#             print("⚠️ 请先选择数据库！（选2）")
#             continue

#         # 展示当前已有的表
#         cursor = conn.cursor()
#         cursor.execute("SHOW TABLES")
#         result = cursor.fetchall()
#         print("当前所有的表格：")
#         for i in result:
#             print(f"  {i[0]}")
#         cursor.close()

#         table_name = input("请输入表格名称：")

#         # ✅ 交互式逐列添加字段
#         columns = build_columns()
#         if not columns:
#             print("⚠️ 未添加任何字段，取消建表")
#             continue

#         # 确认创建
#         confirm = input(f"确认创建表 [{table_name}]？(y/n)：").strip().lower()
#         if confirm == 'y':
#             create_table(conn, table_name, columns)
#         else:
#             print("❌ 已取消")

#     elif a == "4":
#         pass
#     elif a == "5":
#         pass
#     elif a == "6":
#         pass
#     elif a == "7":
#         pass
#     elif a == "8":
#         conn.close()  # ✅ 关闭连接
#         print("👋 已断开连接，再见！")
#         break
#     else:
#         print("输入错误，请重新输入！")

#封装数据库操作类
import pymysql
class DBHelper:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, autocommit=True)
        self.cursor = self.conn.cursor()
        self.current_db = None
    def add_user(self):   
        pass
    def get_user_by_id(self):
        pass
    def update_user_email(self):
        pass
    def delete_user(self):
        pass