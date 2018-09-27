 #!/usr/bin/env python
import os, sys
import json
import datetime
import random
import traceback
from shared.kafka import kafka_producer, kafka_consumer, consume_forever
import logging
from proppy import Proppy
logging.basicConfig()
logger = logging.getLogger(__name__)

def logfriendly(article):
  return {k:v for (k,v) in article.items() if k not in {'text', 'snippet'}}

def estimate_propaganda_score(estimator, article):
  # FIXME: disabled because memory issue
  # value = estimator.predict(article['text'])
  value = random.randint(0, 1)
  if 'meta' in article:
    article['meta']['propaganda'] = value
  else:
    article['meta'] = {
      'propaganda': value
    }
  logger.info('propaganda for article {} is {}'.format(article['key'], value))
  return article

def consume(payload, producer, estimator, options):
  article = json.loads(payload)
  # --------------- 
  if type(article) == str:
    return
  # REMOVE ^^^^^^^^
  try:
    article = estimate_propaganda_score(estimator, article)
    producer.produce(options.out_topic, json.dumps(article))
  except KeyboardInterrupt as e:
    # user interrupt
    raise e
  except OperationalError as e:
    raise e
  except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    logger.error(traceback.format_exc())
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    logger.error(json.dumps({'name'   :'stanceworker',
                             'why'    : str(e),
                             'where': '{} {} {}'.format(exc_type, fname, exc_tb.tb_lineno),
                             'when'   : datetime.datetime.now().isoformat(),
                             'message': logfriendly(article)}, indent=4))
    if not options['test']:
      producer.produce('error', json.dumps({'name'    : 'stanceworker',   # <-- change the name to match your worker
                                            'why'     : str(e),
                                            'when'    : datetime.datetime.now().isoformat(),
                                            'message' : article}))

def Command(options):
  logger.setLevel(level=logging.INFO)
  if options.debug:
    logger.setLevel(level=logging.DEBUG)

  if options.test:
    logger.setLevel(level=logging.DEBUG)
    if not options.group_id.endswith("-test"):
      options.group_id += "-test"
    if not options.out_topic.endswith("-test"):
      options.out_topic += "-test"

  topics = [options.in_topic]
  logger.info('subscribe to topic %s with group id %s, will write to topic %s', options.in_topic, options.group_id, options.out_topic)

  consumer = kafka_consumer(group_id=options.group_id, timeout_ms=6000)

  producer = kafka_producer()

  # FIXME: disabled because memory issue
  # estimator = Proppy()
  estimator = None
  try:
    # consume_forever(consumer, topics, logger, callback, rewind=False, **kwargs)
    consume_forever(consumer, topics, logger, consume, rewind=options.rewind, producer=producer, estimator=estimator, options=options)
  except KeyboardInterrupt:
    print("Aborted by user", file=sys.stderr)

  consumer.close()

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='proppy worker - assign stance for articles')
  parser.add_argument('--timeout', type=int, default=6000, help='session timeout ms')
  parser.add_argument('--group-id', type=str, default=os.environ.get('GROUPID', 'proppy-worker-0'), help='group id, make sure test will use *-test group id')
  parser.add_argument('--in-topic', type=str, default=os.environ.get('INTOPIC', 'clustered-article'), help='kafka topic to read')
  parser.add_argument('--out-topic', type=str, default=os.environ.get('OUTTOPIC', 'proppy-article'), help='kafka topic to write')
  parser.add_argument('--test', action='store_true', default=False, help='test mode')
  parser.add_argument('--rewind', action='store_true', default=False, help='read from beginning of the queue, ignore last reading position')
  parser.add_argument('--debug', action='store_true', default=os.environ.get('DEBUG', 'FALSE') == 'TRUE', help='debug, more verbose logging')

  args = parser.parse_args()

  Command(args)
