#!/usr/bin/env python2

import psycopg2
import time
from datetime import datetime

DBName = "news"


def get_top_three_articles():
    db, c = connect_database()

    '''
        get the most popular three articles of all time
    '''

    query = ("select articles.title, count(*) as num from articles, log " +
             "where articles.slug = split_part(log.path,  '/article/', 2)" +
             " group by articles.title order by num desc limit 3")

    c.execute(query)
    return c.fetchall()
    close_database(db)


def show_top_three_articles():
    rows = get_top_three_articles()

    '''
        format result and show top three articles with heading
    '''

    print "Top Three Articles "
    print "---------------------"

    for row in rows:
        print '\'{0}\' - {1} views'.format(*row)
    print "\n"


def get_popular_article_authors():
    db, c = connect_database()

    '''
        get most popular article authors of all time
    '''

    query = ("select authors.name, count(*) as num from articles, authors, " +
             " log where articles.author = authors.id and articles.slug = " +
             "split_part(log.path,  '/article/', 2) group by authors.name " +
             "order by num desc")

    c.execute(query)
    return c.fetchall()
    close_database(db)


def show_popular_article_authors():
    rows = get_popular_article_authors()

    '''
        format result and show most popular article authors with heading
    '''

    print "Most Popular Article Authors "
    print "-----------------------------"

    for row in rows:
        print '{0} - {1} views'.format(*row)
    print "\n"


def get_high_error_rate_info():
    db, c = connect_database()

    '''
        get date and error rate which is higher than 0.01
    '''

    query = ("select date, error_rate from error_rate_view where " +
             " error_rate > 0.01")

    c.execute(query)
    return c.fetchall()
    close_database(db)


def show_high_error_rate_info():
    rows = get_high_error_rate_info()

    '''
        format result and shows date and error rate which is more than 1%
    '''

    print "Error Rate Greater Than 1%"
    print "--------------------------"

    for row in rows:
        date = datetime.strptime('{0}'.format(*row), '%Y-%m-%d')
        error_rate = float('{1}'.format(*row))
        print '{0} - {1} error'.format(
            date.strftime('%B %d, %Y'),
            "{:.1%}".format(error_rate))
    print "\n"


def connect_database():
    db = psycopg2.connect(database=DBName)
    c = db.cursor()
    return db, c


def close_database(db):
    db.close()


def run_sql_file(filename):
    db, c = connect_database()
    file = open(filename, 'r')
    sql = " ".join(file.readlines())
    c.execute(sql)
    db.commit()


# run sql file to create a view 'error_rate_view'
run_sql_file("create_view.sql")

show_top_three_articles()
show_popular_article_authors()
show_high_error_rate_info()
