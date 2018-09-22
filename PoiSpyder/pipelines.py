# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class PoispyderPipeline(object):

    def process_item(self, item, spider):

        db = pymysql.connect(host="localhost", user="root",
                             password="admin", db="travel_notes", port=3306)
        cur = db.cursor()
        print("进入数据库")
        sql_insert = """insert into poi_info values(null, '%s', '%s',
                    '%d', '%d', '%s', '%s', '%s', '%s', '%s',
                     '%s', '%d', '%s')
                """ % (item['name'], item['parent'],
                       item['parent_rank'], item['mentioned_times'],
                       item['overview'], item['tickets'],
                       item['address'], item['open_time'],
                       item['tips'], item['best_time'],
                       item['comment_count'], item['wander_time'])
        print("插入语句：" + sql_insert)

        try:
            cur.execute(sql_insert)
            db.commit()
            print("提交修改")
        except Exception as e:
            print("异常出现" + e.__class__.__name__)
            db.rollback()
        finally:
            db.close()

        return item
