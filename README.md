# Scrapy SpiderStats Extension

将 Spider Stats 存储到 MongoDB 的扩展，可以用于爬虫监控和统计。

## 安装

```shell script
pip install scrapy-spiderstats-extension
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
    "_id":"5fb23d9cbaf515d71d3a9c6c",
    "log_count/INFO":9,
    "start_time":"2020-11-16T08:51:40.705Z",
    "stats_id":"2b55df7b46a548269ca603bb7ad889b2",
    "spider_name":"test",
    "pages":0,
    "pagerate":0,
    "items":0,
    "itemrate":0,
    "record_time":"2020-11-16T08:51:40.706Z"
}
```


> 记录状态

```json
{
    "_id":"5fb23dd8baf515d71d3a9c6d",
    "log_count/INFO":12,
    "start_time":"2020-11-16T08:51:40.705Z",
    "stats_id":"2b55df7b46a548269ca603bb7ad889b2",
    "spider_name":"test",
    "pages":510,
    "pagerate":510,
    "items":0,
    "itemrate":0,
    "record_time":"2020-11-16T08:52:40.713Z",
    "log_count/DEBUG":1034,
    "scheduler/enqueued/redis":521,
    "scheduler/dequeued/redis":520,
    "downloader/request_count":520,
    "downloader/request_method_count/GET":520,
    "downloader/request_bytes":239235,
    "downloader/response_count":510,
    "downloader/response_status_count/200":510,
    "downloader/response_bytes":110675,
    "response_received_count":510,
    "downloader/exception_count":3,
    "downloader/exception_type_count/twisted-internet-error-TimeoutError":3,
    "retry/count":3,
    "retry/reason_count/twisted-internet-error-TimeoutError":3
}
```

> 完成状态

```json
{
    "_id":"5fb23e2ebaf515d71d3a9c6f",
    "log_count/INFO":16,
    "start_time":"2020-11-16T08:51:40.705Z",
    "stats_id":"2b55df7b46a548269ca603bb7ad889b2",
    "spider_name":"test",
    "pages":1000,
    "pagerate":6,
    "items":0,
    "itemrate":0,
    "record_time":"2020-11-16T08:54:06.125Z",
    "log_count/DEBUG":2015,
    "scheduler/enqueued/redis":1007,
    "scheduler/dequeued/redis":1007,
    "downloader/request_count":1007,
    "downloader/request_method_count/GET":1007,
    "downloader/request_bytes":463763,
    "downloader/response_count":1000,
    "downloader/response_status_count/200":1000,
    "downloader/response_bytes":216997,
    "response_received_count":1000,
    "downloader/exception_count":7,
    "downloader/exception_type_count/twisted.internet.error.TimeoutError":7,
    "retry/count":7,
    "retry/reason_count/twisted.internet.error.TimeoutError":7,
    "elapsed_time_seconds":145.420645,
    "finish_time":"2020-11-16T08:54:06.125Z",
    "finish_reason":"finished"
}
```