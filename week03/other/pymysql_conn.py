import pretty_errors
import pymysql

# 打开数据库链接

db = pymysql.connect("81.68.90.212","root","qcL_584652199","db1")

try:
    # 适用 cursor() 方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        # 使用 execute() 方法执行 SQL 查询
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f"fetch error {e}")

finally:
    # 关闭数据库连接
    db.close()
print(f"Database version : {result} ")

