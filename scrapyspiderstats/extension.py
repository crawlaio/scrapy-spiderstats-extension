# -*- coding: utf-8 -*-
import logging
import uuid
from datetime import datetime

from pymongo import MongoClient
from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.extensions.logstats import LogStats
from twisted.internet import task

logger = logging.getLogger(__name__)


class SpiderStats(LogStats):
    def __init__(self, client, stats_mongodb_db, stats_mongodb_col, *args, **kwargs):
        self.pagesprev = 0
        self.itemsprev = 0
        self.client = client
        self.db = self.client[stats_mongodb_db]
        self.col = self.db[stats_mongodb_col]
        super(SpiderStats, self).__init__(*args, **kwargs)

    @classmethod
    def from_crawler(cls, crawler):
        stats_mongodb_uri = crawler.settings.get("STATS_MONGODB_URI")
        stats_mongodb_db = crawler.settings.get("STATS_MONGODB_DB")
        stats_mongodb_col = crawler.settings.get("STATS_MONGODB_COL")
        client = MongoClient(stats_mongodb_uri)
        interval = crawler.settings.getfloat("LOGSTATS_INTERVAL")
        if not interval:
            raise NotConfigured
        o = cls(client, stats_mongodb_db, stats_mongodb_col, crawler.stats, interval)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        return o

    def spider_opened(self, spider):
        stats_id = uuid.uuid4().hex
        self.stats.set_value("stats_id", stats_id, spider=spider)
        self.stats.set_value("spider_name", spider.name, spider=spider)
        logger.info("Spider Stats ID: {0}".format(stats_id))
        self.task = task.LoopingCall(self.log, spider)
        self.task.start(self.interval)

    def log(self, spider):
        items = self.stats.get_value("item_scraped_count", 0)
        pages = self.stats.get_value("response_received_count", 0)
        irate = (items - self.itemsprev) * self.multiplier
        prate = (pages - self.pagesprev) * self.multiplier
        self.pagesprev, self.itemsprev = pages, items
        self.stats.set_value("pages", pages)
        self.stats.set_value("pagerate", prate)
        self.stats.set_value("items", items)
        self.stats.set_value("itemrate", irate)
        self.stats.set_value("record_time", datetime.utcnow())
        insert_item = {}
        for key, value in self.stats.get_stats().items():
            insert_item[str(key).replace(".", "-")] = value
        self.col.insert_one(insert_item)
        logger.info(self.stats.get_stats())

    def spider_closed(self, spider, reason):
        self.log(spider)
        if self.task and self.task.running:
            self.task.stop()
