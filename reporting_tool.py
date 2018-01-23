#!/usr/bin/env python

"""Log Anaylsys Project.

This module gets data from database and print out formatted results.
"""

import psycopg2
import time
from datetime import datetime

DBName = "news"


def get_top_three_articles():
    """Connect to a database and get the most popular three articles."""
    db, c = connect_database()

    query = ("""select articles.title, count(*) as num from articles,
         log where log.path = concat('/article/', articles.slug) and
         log.status='200 OK' group by articles.title order by num
         desc limit 3""")

    c.execute(query)
    results = c.fetchall()
    close_database(db)
    return results


def show_top_three_articles():
    """Format result and show top three articles with heading."""
    rows = get_top_three_articles()

    print "Top Three Articles "
    print "---------------------"

    for title, num in rows:
        print '\'{0}\' - {1} views'.format(title, num)
    print "\n"


def get_popular_article_authors():
    """Connect to a database and get most popular article authors."""
    db, c = connect_database()

    query = ("""select authors.name, count(*) as num from articles, authors,
                log where articles.author=authors.id and log.status='200 OK'
                and log.path=concat('/article/', articles.slug) group by
                authors.name order by num desc""")

    c.execute(query)
    results = c.fetchall()
    close_database(db)
    return results


def show_popular_article_authors():
    """Format result and show most popular article authors with heading."""
    rows = get_popular_article_authors()

    print "Most Popular Article Authors "
    print "-----------------------------"

    for name, num in rows:
        print '{0} - {1} views'.format(name, num)
    print "\n"


def get_high_error_rate_info():
    """Connect to a database and get date and error rate (>0.01)."""
    db, c = connect_database()

    query = ("""select date, error_rate from error_rate_view where
             error_rate > 0.01""")

    c.execute(query)
    results = c.fetchall()
    close_database(db)
    return results


def show_high_error_rate_info():
    """Format result and shows date and error rate which is more than 1%."""
    rows = get_high_error_rate_info()

    print "Error Rate Greater Than 1%"
    print "--------------------------"

    for err_date, err_pct in rows:
        print ("{:%B %d, %Y} - {:.1%} error ".format(err_date, err_pct))
    print "\n"


def connect_database():
    """Connect to database and return a database connection."""
    db = psycopg2.connect(database=DBName)
    c = db.cursor()
    return db, c


def close_database(db):
    """Close a database connection."""
    db.close()


def run_sql_file(filename):
    """Read sql file and execute queries."""
    db, c = connect_database()
    file = open(filename, 'r')
    sql = " ".join(file.readlines())
    c.execute(sql)
    db.commit()
    close_database(db)


# run sql file to create a view 'error_rate_view'
run_sql_file("create_view.sql")

show_top_three_articles()
show_popular_article_authors()
show_high_error_rate_info()
