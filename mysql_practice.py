"""
MySQL 课堂实战 —— Python + pymysql 完整练习
功能：
  1. 创建数据库
  2. 选择数据库
  3. 创建 user 表（id PK, username, gender ENUM默认男, phone）
  4. 插入 5 条用户数据
  5. 查询所有男性用户
  6. 修改手机号
  7. 删除 id=3 的数据
  8. 使用事务完成连续插入
  9. 退出
"""

import pymysql


# ==================== 函数定义区 ====================

def create_database(conn, db_name):
    """创建数据库"""
    sql = f"CREATE DATABASE `{db_name}`"
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        print(f"✅ 数据库 [{db_name}] 创建成功！")
    except pymysql.err.ProgrammingError as e:
        if "1007" in str(e):
            print(f"⚠️ 数据库 [{db_name}] 已存在，无需重复创建")
        else:
            print(f"❌ 创建失败: {e}")
    finally:
        cursor.close()


def use_database(conn, db_name):
    """选择/切换数据库"""
    cursor = conn.cursor()
    try:
        cursor.execute(f"USE `{db_name}`")
        print(f"✅ 已切换到数据库 [{db_name}]")
        return db_name
    except pymysql.err.ProgrammingError as e:
        if "1049" in str(e):
            print(f"⚠️ 数据库 [{db_name}] 不存在！请先创建")
        else:
            print(f"❌ 切换失败: {e}")
        return None
    finally:
        cursor.close()


def create_table(conn):
    """
    练习3: 创建 user 表
    结构: id(int,主键,自增), username(varchar),
          gender(enum类型,默认'男'), phone(varchar)
    """
    cursor = conn.cursor()
    try:
        # DROP IF EXISTS 避免重复创建报错
        cursor.execute("DROP TABLE IF EXISTS `user`")

        sql = """
        CREATE TABLE `user` (
            `id` INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户编号',
            `username` VARCHAR(20) NOT NULL COMMENT '用户名',
            `gender` ENUM('男', '女') DEFAULT '男' COMMENT '性别',
            `phone` VARCHAR(11) COMMENT '手机号'
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户信息表'
        """
        cursor.execute(sql)
        print("✅ user 表创建成功！表结构如下:")
        print("-" * 55)
        print(f"{'字段':<12} {'类型':<20} {'约束/默认'}")
        print("-" * 55)
        print(f"{'id':<12} {'INT':<20} {'PRIMARY KEY, 自增'}")
        print(f"{'username':<12} {'VARCHAR(20)':<20} {'NOT NULL'}")
        enum_str = 'ENUM("男","女")'
        default_str = "DEFAULT '男'"
        print(f"{'gender':<12} {enum_str:<20} {default_str}")
        print(f"{'phone':<12} {'VARCHAR(11)':<20} {''}")
        print("-" * 55)

    except pymysql.err.ProgrammingError as e:
        print(f"❌ 建表失败: {e}")
    finally:
        cursor.close()


def insert_data(conn):
    """
    练习4: 手动输入 5 条用户数据并插入
    循环5次，每次让用户输入 username / gender / phone
    注意: gender 字段有 DEFAULT '男', 所以不传也会自动填'男'
    """
    cursor = conn.cursor()
    users = []  # 用来收集用户输入的数据

    try:
        print("\n" + "=" * 40)
        print("  📝 开始录入数据（共 5 条）")
        print("=" * 40)

        for i in range(1, 6):
            print(f"\n--- 第 {i}/5 条 ---")
            name = input("  用户名: ").strip()
            if not name:
                print("  ⚠️ 用户名不能为跳过，重新输入")
                name = input("  用户名: ").strip()

            gender = input("  性别(男/女，直接回车默认=男): ").strip()
            if not gender:
                gender = "男"  # 空值就用默认值（和数据库 DEFAULT 对应）
            elif gender not in ("男", "女"):
                print(f"  ⚠️ '{gender}' 不合法，自动设为 '男'")
                gender = "男"

            phone = input("  手机号(11位，可留空): ").strip()
            if phone and len(phone) != 11:
                print(f"  ⚠️ 手机号长度 {len(phone)} 位，可能不标准，但仍然保存")

            users.append((name, gender, phone))
            print(f"  ✓ 已记录: {name} | {gender} | {phone or '(空)'}")

        # 所有数据收集完毕 → 批量插入
        print("\n📤 正在写入数据库...")
        sql = "INSERT INTO `user` (username, gender, phone) VALUES (%s, %s, %s)"
        cursor.executemany(sql, users)
        conn.commit()  # ⚠️ INSERT 必须 commit 才会保存！

        print(f"\n✅ 成功插入 {cursor.rowcount} 条数据:")
        for i, (name, gender, phone) in enumerate(users, 1):
            print(f"   {i}. {name} | {gender} | {phone or '(未填)'}")

    except Exception as e:
        conn.rollback()  # 出错就回滚
        print(f"❌ 插入失败，已回滚: {e}")
    finally:
        cursor.close()


def query_male_users(conn):
    """
    练习5: 查询所有男性用户
    演示 WHERE 条件查询 + fetchall 取结果
    """
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # 用 DictCursor 返回字典
    try:
        sql = "SELECT * FROM `user` WHERE gender = %s ORDER BY id"
        cursor.execute(sql, ("男",))

        results = cursor.fetchall()

        print(f"\n📋 男性用户列表 (共 {len(results)} 人):")
        print("=" * 50)

        if results:
            for row in results:
                print(f"  ID:{row['id']}  姓名:{row['username']}"
                      f"  性别:{row['gender']}  手机:{row['phone'] or '(未填写)'}")
        else:
            print("  （没有男性用户）")

        print("=" * 50 + "\n")

    finally:
        cursor.close()


def update_phone(conn):
    """
    练习6: 修改手机号
    根据 username 找到用户，修改其 phone 字段
    """
    cursor = conn.cursor()
    try:
        # 先显示当前所有用户供选择
        cursor.execute("SELECT id, username, phone FROM `user`")
        users = cursor.fetchall()
        if not users:
            print("⚠️ 表中还没有数据！请先插入数据")
            return

        print("\n当前用户列表:")
        for u in users:
            print(f"  ID:{u[0]}  {u[1]}  手机:{u[2] or '(未填)'}")

        name = input("\n要修改谁的手机号？输入用户名: ").strip()
        new_phone = input("输入新的手机号(11位): ").strip()

        # 更新操作（用参数化防SQL注入）
        sql = "UPDATE `user` SET phone = %s WHERE username = %s"
        cursor.execute(sql, (new_phone, name))

        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ 成功将 [{name}] 的手机号修改为 [{new_phone}]")
        else:
            print(f"❌ 未找到用户名为 [{name}] 的记录")

    except Exception as e:
        conn.rollback()
        print(f"❌ 修改失败: {e}")
    finally:
        cursor.close()


def delete_user(conn):
    """
    练习7: 删除 id=3 的数据
    演示: 先 SELECT 确认 → 再 DELETE → 用主键定位 → commit 提交
    """
    target_id = 3  # 题目要求删除 id=3

    cursor = conn.cursor()
    try:
        # 第一步：先查一下这条数据是否存在（安全确认）
        cursor.execute("SELECT * FROM `user` WHERE id = %s", (target_id,))
        target = cursor.fetchone()

        if not target:
            print(f"⚠️ ID={target_id} 的记录不存在或已被删除")
            return

        print(f"\n即将删除的记录: ID={target[0]}  {target[1]}  {target[2]}  {target[3]}")

        # 第二步：执行删除（用主键 id 精确定位，最安全）
        cursor.execute("DELETE FROM `user` WHERE id = %s", (target_id,))
        conn.commit()  # ⚠️ DELETE 必须 commit！

        print(f"✅ 成功删除 {cursor.rowcount} 条记录 (ID={target_id})")

    except Exception as e:
        conn.rollback()
        print(f"❌ 删除失败，已回滚: {e}")
    finally:
        cursor.close()


def transaction_insert(conn):
    """
    练习8: 使用事务完成连续插入（手动输入数据）
    演示: 多条 INSERT 作为"一个整体"，要么全部成功，要么全部失败
    事务四步骤: BEGIN → 多条SQL → COMMIT(成功) / ROLLBACK(失败)
    """
    cursor = conn.cursor()
    new_users = []

    try:
        print("\n" + "=" * 40)
        print("  🔄 事务插入模式")
        print("  （输入要插入的条数，然后逐条录入）")
        print("  全部录入后才一起提交！")
        print("=" * 40)

        # 让用户决定插入几条
        count_str = input("\n要插入几条数据？(输入数字): ").strip()
        if not count_str or not count_str.isdigit():
            count = 3  # 默认3条
            print(f"  输入无效，默认 {count} 条")
        else:
            count = int(count_str)
            if count < 1:
                count = 3

        # 逐条收集用户输入
        for i in range(1, count + 1):
            print(f"\n--- 第 {i}/{count} 条 ---")
            name = input("  用户名: ").strip()
            gender = input("  性别(男/女，回车默认=男): ").strip() or "男"
            phone = input("  手机号(11位，可留空): ").strip()

            new_users.append((name, gender, phone))
            print(f"  ✓ 已记录: {name} | {gender} | {phone or '(空)'}")

        # 开始执行事务插入
        print("\n📤 开始写入数据库...")

        sql = "INSERT INTO `user` (username, gender, phone) VALUES (%s, %s, %s)"

        for name, gender, phone in new_users:
            cursor.execute(sql, (name, gender, phone))
            print(f"  ✓ 执行插入: {name}")

        # 所有 SQL 都执行成功 → 提交事务
        conn.commit()
        print(f"\n✅ 事务提交成功！共插入 {cursor.rowcount} 条新数据")

        # 展示最终表中所有数据验证结果
        print("\n📋 当前 user 表全部数据:")
        cursor.execute("SELECT * FROM `user` ORDER BY id")
        rows = cursor.fetchall()
        for r in rows:
            phone_display = r[3] if r[3] else "(未填)"
            print(f"  ID:{r[0]}  {r[1]}  {r[2]}  {phone_display}")

    except Exception as e:
        # 任何一条出错 → 回滚整个事务（已插入的全部撤销）
        conn.rollback()
        print(f"\n❌ 事务回滚！（一条失败全部撤销）原因: {e}")
    finally:
        cursor.close()


# ==================== 主程序区 ====================

def main():
    """程序入口 - 主菜单循环"""

    # ① 建立连接（初始不指定 database）
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        charset='utf8mb4'
    )
    print("✅ MySQL 连接成功！\n")

    current_db = None  # 记录当前选择的数据库

    while True:
        print("=" * 45)
        print(f"   🗄️  MySQL 实战练习")
        print("=" * 45)
        print(f"   当前数据库: {current_db or '(未选择)'}")
        print("-" * 45)
        print("  1. 创建数据库")
        print("  2. 选择数据库")
        print("  3. 创建 user 表")
        print("  4. 插入 5 条数据")
        print("  5. 查询所有男性用户")
        print("  6. 修改手机号")
        print("  7. 删除 id=3 的数据")
        print("  8. 事务连续插入")
        print("  0. 退出")
        print("=" * 45)

        choice = input("\n请输入指令(0-8): ").strip()

        if choice == "1":
            db = input("输入数据库名称: ").strip()
            if db:
                create_database(conn, db)
                current_db = db  # 建完自动选中

        elif choice == "2":
            db = input("选择数据库: ").strip()
            if db:
                result = use_database(conn, db)
                if result:
                    current_db = result

        elif choice == "3":
            if not current_db:
                print("⚠️ 请先选择数据库！(选 1 或 2)")
                continue
            create_table(conn)

        elif choice == "4":
            if not current_db:
                print("⚠️ 请先选择数据库！")
                continue
            insert_data(conn)

        elif choice == "5":
            if not current_db:
                print("⚠️ 请先选择数据库！")
                continue
            query_male_users(conn)

        elif choice == "6":
            if not current_db:
                print("⚠️ 请先选择数据库！")
                continue
            update_phone(conn)

        elif choice == "7":
            if not current_db:
                print("⚠️ 请先选择数据库！")
                continue
            delete_user(conn)

        elif choice == "8":
            if not current_db:
                print("⚠️ 请先选择数据库！")
                continue
            transaction_insert(conn)

        elif choice == "0":
            break
        else:
            print("❓ 无效指令，请重新输入\n")

    # 程序退出时关闭连接
    conn.close()
    print("🔒 连接已关闭，再见！👋")


# 程序启动入口
if __name__ == "__main__":
    main()
