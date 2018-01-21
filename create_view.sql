CREATE OR REPLACE VIEW error_rate_view AS
  (SELECT t1.date,
          t2.count/t1.count::float AS error_rate
   FROM
     (SELECT date(TIME),
             count(status)
      FROM log
      GROUP BY date(TIME)) t1
   JOIN
     (SELECT date(TIME),
             count(status)
      FROM log
      WHERE status != '200 OK'
      GROUP BY date(TIME)) t2 ON t1.date = t2.date);
