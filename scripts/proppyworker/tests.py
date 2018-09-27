import os
import json
import codecs
import unittest
from unittest.mock import patch, Mock
import queue
from proppy import Proppy
from worker import consume

BASE_DIR = './'

class TestProppyWorker(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.estimator = Proppy()

  def not_test_predict(self):
    text = codecs.open(os.path.join(BASE_DIR, 'fixtures/article-text.txt'), 'r', 'utf-8').read()
    self.assertAlmostEqual(self.estimator.predict(text), 0.9971261040155768, places=3)
  
  def test_consume(self):
    article = json.load(codecs.open(os.path.join(BASE_DIR, 'fixtures/articles.json'), 'r', 'utf-8'))['data'][0]
    results = []
    def collect_result(topic, data):
      results.append((topic, data))
    producer = Mock()
    producer.produce.side_effect = collect_result
    options = Mock()
    options.out_topic = "proppy-article"
    consume(json.dumps(article), producer, self.estimator, options) 
    self.assertEqual(len(results), 1)
    self.assertEqual(results[0][0], "proppy-article")
    articleDct = json.loads(results[0][1])
    #self.assertAlmostEqual(articleDct['meta']['propaganda'], 0.010179571439545801, places=3)
