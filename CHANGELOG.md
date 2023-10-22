# golang implementation

Naive implementation:
```
http_req_duration..............: avg=33.72ms  min=3.06ms  med=35.25ms max=95.07ms p(90)=45.38ms  p(95)=49.14ms
```

# 0.5.0

Optimization:

* Move to `orjson` for json handling
* Increase number of workers
* Migrate to Python 3.11
* Async Kafka client


Before (https://github.com/epoch8/amplitude-collector/actions/runs/6519807027/job/17706689675):

```
http_req_duration..............: avg=493.63ms min=56.78ms med=494.23ms max=712.02ms p(90)=509.06ms p(95)=512.46ms
```

After (https://github.com/epoch8/amplitude-collector/actions/runs/6519815420/job/17706708157):

```
http_req_duration..............: avg=56.66ms  min=19.92ms med=55.81ms max=112.05ms p(90)=65.73ms  p(95)=71.53ms
```

# 0.4.0

* Add `CLOUD_ENV` configuration option
* Add `KAFKA_TOPIC_CREATE` configuration option

# 0.2.5

* Add `ingest_uuid` to JSON parsing

# 0.2.4

* Add `ingest_uuid` field to message

# 0.2.3

* Fix `content-type` parsing

# 0.2.1, 0.2.2

* Add `KAFKA_USE_SSL` configuration option

# 0.2.0

* Support for `application/json` content-type

# 0.1.0

* Initial implementation
