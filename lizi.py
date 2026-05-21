import pymysql

# 连接MySQL
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)
cursor = conn.cursor()

# 查看当前所有连接
cursor.execute("SHOW PROCESSLIST")
results = cursor.fetchall()
print("当前所有连接：")
for row in results:
    print(f"  ID: {row[0]}, User: {row[1]}, Host: {row[2]}, DB: {row[3]}, Command: {row[4]}, Time: {row[5]}")

# 获取自己的连接ID
cursor.execute("SELECT CONNECTION_ID()")
my_id = cursor.fetchone()[0]
print(f"\n当前连接ID: {my_id}")

# 关闭除了自己以外的所有连接
killed = 0
for row in results:
    if row[0] != my_id:  # 不杀自己
        try:
            cursor.execute(f"KILL {row[0]}")
            print(f"✅ 已杀掉连接 ID: {row[0]}")
            killed += 1
        except Exception as e:
            print(f"❌ 杀掉 ID {row[0]} 失败: {e}")

print(f"\n清理完毕，共关闭 {killed} 个连接")

# 确认剩余连接
cursor.execute("SHOW PROCESSLIST")
remaining = cursor.fetchall()
print(f"剩余连接数: {len(remaining)}")

cursor.close()
conn.close()  # 最后关掉自己
print("👋 当前连接也已关闭")
