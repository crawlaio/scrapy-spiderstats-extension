# Scrapy SpiderStats Extension

将 Spider Stats 存储到 MongoDB 的扩展，可以用于爬虫监控和统计.

## 安装

```shell script
pip3 install scrapy-spiderstats-extension
```

## 使用

在 `settings.py` 配置文件中开启 `SpiderStats` 

```python
EXTENSIONS = {
    "scrapyspiderstats.SpiderStats": 0
}
STATS_MONGODB_URI = "mongodb://localhost:27017"
STATS_MONGODB_DB = "scrapy"
STATS_MONGODB_COL = "spiderstats"
```

## 存储结果

> 启动状态

```json
{
    "_id": ObjectId("5fb23d9cbaf515d71d3a9c6c"),
    "log_count/INFO": NumberInt("9"),
    "start_time": ISODate("2020-11-16T08:51:40.705Z"),
    "StatsId": "2b55df7b46a548269ca603bb7ad889b2",
    "spider_name": "test",
    "pages": NumberInt("0"),
    "pagerate": 0,
    "items": NumberInt("0"),
    "itemrate": 0,
    "record_time": ISODate("2020-11-16T08:51:40.706Z")
}
```


> 记录状态

```json
{
    "_id": ObjectId("5fb23dd8baf515d71d3a9c6d"),
    "log_count/INFO": NumberInt("12"),
    "start_time": ISODate("2020-11-16T08:51:40.705Z"),
    "StatsId": "2b55df7b46a548269ca603bb7ad889b2",
    "spider_name": "test",
    "pages": NumberInt("510"),
    "pagerate": 510,
    "items": NumberInt("0"),
    "itemrate": 0,
    "record_time": ISODate("2020-11-16T08:52:40.713Z"),
    "log_count/DEBUG": NumberInt("1034"),
    "scheduler/enqueued/redis": NumberInt("521"),
    "scheduler/dequeued/redis": NumberInt("520"),
    "downloader/request_count": NumberInt("520"),
    "downloader/request_method_count/GET": NumberInt("520"),
    "downloader/request_bytes": NumberInt("239235"),
    "downloader/response_count": NumberInt("510"),
    "downloader/response_status_count/200": NumberInt("510"),
    "downloader/response_bytes": NumberInt("110675"),
    "response_received_count": NumberInt("510"),
    "downloader/exception_count": NumberInt("3"),
    "downloader/exception_type_count/twisted-internet-error-TimeoutError": NumberInt("3"),
    "retry/count": NumberInt("3"),
    "retry/reason_count/twisted-internet-error-TimeoutError": NumberInt("3")
}
```

> 完成状态

```json
{
    "_id": ObjectId("5fb23e2ebaf515d71d3a9c6f"),
    "log_count/INFO": NumberInt("16"),
    "start_time": ISODate("2020-11-16T08:51:40.705Z"),
    "StatsId": "2b55df7b46a548269ca603bb7ad889b2",
    "spider_name": "test",
    "pages": NumberInt("1000"),
    "pagerate": 6,
    "items": NumberInt("0"),
    "itemrate": 0,
    "record_time": ISODate("2020-11-16T08:54:06.125Z"),
    "log_count/DEBUG": NumberInt("2015"),
    "scheduler/enqueued/redis": NumberInt("1007"),
    "scheduler/dequeued/redis": NumberInt("1007"),
    "downloader/request_count": NumberInt("1007"),
    "downloader/request_method_count/GET": NumberInt("1007"),
    "downloader/request_bytes": NumberInt("463763"),
    "downloader/response_count": NumberInt("1000"),
    "downloader/response_status_count/200": NumberInt("1000"),
    "downloader/response_bytes": NumberInt("216997"),
    "response_received_count": NumberInt("1000"),
    "downloader/exception_count": NumberInt("7"),
    "downloader/exception_type_count/twisted.internet.error.TimeoutError": NumberInt("7"),
    "retry/count": NumberInt("7"),
    "retry/reason_count/twisted.internet.error.TimeoutError": NumberInt("7"),
    "elapsed_time_seconds": 145.420645,
    "finish_time": ISODate("2020-11-16T08:54:06.125Z"),
    "finish_reason": "finished"
}
```