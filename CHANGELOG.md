# WIP 0.5.0

Optimization:

* Move to `orjson` for json handling
* Move to `fasteruuid` for uuid generation
* Increase number of workers


Before (https://github.com/epoch8/amplitude-collector/actions/runs/6450075227/job/17509073693):

```
http_req_duration..............: avg=429.41ms min=50ms    med=429.41ms max=663.29ms p(90)=445.46ms p(95)=454.04ms
```

After (https://github.com/epoch8/amplitude-collector/actions/runs/6455384921/job/17522777436):

```
http_req_duration..............: avg=270.32ms min=56.97ms med=275.47ms max=499.49ms p(90)=383.73ms p(95)=407.69ms
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
