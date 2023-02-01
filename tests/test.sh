# HOST="http://localhost:8000/collect"
# 'https://collector-test.perek.epoch8.ru/collect'
# HOST="https://amplitude-collector.stage.looky.dev/collect"
HOST="https://amplitude-collector.prod.looky.dev/collect"

curl $HOST \
  -H 'authority: collector-test.perek.epoch8.ru' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cross-origin-resource-policy: cross-origin' \
  -H 'origin: http://localhost:63104' \
  -H 'referer: http://localhost:63104/' \
  -H 'sec-ch-ua: "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' \
  --data-raw 'checksum=6c1664870462f856090d97c3c5fcaa81&client=a79cefed0b7076cf3998ef7578a18bf0&e=%5B%7B%22device_id%22%3A%226rPzaVUwYHquzptdsrrKff%22%2C%22user_id%22%3A%22test_user%22%2C%22timestamp%22%3A1667130418121%2C%22event_id%22%3A4%2C%22session_id%22%3A1667130418118%2C%22event_type%22%3A%22MyApp%20startup%22%2C%22version_name%22%3Anull%2C%22platform%22%3A%22Web%22%2C%22os_name%22%3A%22Chrome%22%2C%22os_version%22%3A%22106%22%2C%22device_model%22%3A%22Windows%22%2C%22device_manufacturer%22%3Anull%2C%22language%22%3A%22en-US%22%2C%22api_properties%22%3A%7B%7D%2C%22event_properties%22%3A%7B%22event_prop_1%22%3A10%2C%22event_prop_2%22%3Atrue%7D%2C%22user_properties%22%3A%7B%7D%2C%22uuid%22%3A%22fed3c7a5-30be-4c53-bade-6d3958e2d7ae%22%2C%22library%22%3A%7B%22name%22%3A%22amplitude-flutter%22%2C%22version%22%3A%223.10.0%22%7D%2C%22sequence_number%22%3A5%2C%22groups%22%3A%7B%7D%2C%22group_properties%22%3A%7B%7D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36%22%7D%5D&upload_time=1667130418122&v=2' \
  --compressed

curl $HOST \
  -H 'authority: collector-test.perek.epoch8.ru' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cross-origin-resource-policy: cross-origin' \
  -H 'origin: http://localhost:63104' \
  -H 'referer: http://localhost:63104/' \
  -H 'sec-ch-ua: "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' \
  --data-raw 'checksum=98a7f86a31d56f73f5ed9b232ef3cd35&client=a79cefed0b7076cf3998ef7578a18bf0&e=%5B%7B%22device_id%22%3A%226rPzaVUwYHquzptdsrrKff%22%2C%22user_id%22%3A%22test_user%22%2C%22timestamp%22%3A1667130418124%2C%22event_id%22%3A5%2C%22session_id%22%3A-1%2C%22event_type%22%3A%22Out%20of%20Session%20Event%22%2C%22version_name%22%3Anull%2C%22platform%22%3A%22Web%22%2C%22os_name%22%3A%22Chrome%22%2C%22os_version%22%3A%22106%22%2C%22device_model%22%3A%22Windows%22%2C%22device_manufacturer%22%3Anull%2C%22language%22%3A%22en-US%22%2C%22api_properties%22%3A%7B%7D%2C%22event_properties%22%3A%7B%7D%2C%22user_properties%22%3A%7B%7D%2C%22uuid%22%3A%22ef693225-d501-475d-b971-fc88ed15144a%22%2C%22library%22%3A%7B%22name%22%3A%22amplitude-flutter%22%2C%22version%22%3A%223.10.0%22%7D%2C%22sequence_number%22%3A6%2C%22groups%22%3A%7B%7D%2C%22group_properties%22%3A%7B%7D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36%22%7D%2C%7B%22device_id%22%3A%226rPzaVUwYHquzptdsrrKff%22%2C%22user_id%22%3A%22test_user%22%2C%22timestamp%22%3A1667130418127%2C%22event_id%22%3A6%2C%22session_id%22%3A-1%2C%22event_type%22%3A%22revenue_amount%22%2C%22version_name%22%3Anull%2C%22platform%22%3A%22Web%22%2C%22os_name%22%3A%22Chrome%22%2C%22os_version%22%3A%22106%22%2C%22device_model%22%3A%22Windows%22%2C%22device_manufacturer%22%3Anull%2C%22language%22%3A%22en-US%22%2C%22api_properties%22%3A%7B%22productId%22%3Anull%2C%22special%22%3A%22revenue_amount%22%2C%22quantity%22%3A1%2C%22price%22%3A21.9%7D%2C%22event_properties%22%3A%7B%7D%2C%22user_properties%22%3A%7B%7D%2C%22uuid%22%3A%220276e298-1234-4861-9d1a-3007e56a5d24%22%2C%22library%22%3A%7B%22name%22%3A%22amplitude-flutter%22%2C%22version%22%3A%223.10.0%22%7D%2C%22sequence_number%22%3A7%2C%22groups%22%3A%7B%7D%2C%22group_properties%22%3A%7B%7D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36%22%7D%2C%7B%22device_id%22%3A%226rPzaVUwYHquzptdsrrKff%22%2C%22user_id%22%3A%22test_user%22%2C%22timestamp%22%3A1667130418128%2C%22event_id%22%3A2%2C%22session_id%22%3A-1%2C%22event_type%22%3A%22%24identify%22%2C%22version_name%22%3Anull%2C%22platform%22%3A%22Web%22%2C%22os_name%22%3A%22Chrome%22%2C%22os_version%22%3A%22106%22%2C%22device_model%22%3A%22Windows%22%2C%22device_manufacturer%22%3Anull%2C%22language%22%3A%22en-US%22%2C%22api_properties%22%3A%7B%7D%2C%22event_properties%22%3A%7B%7D%2C%22user_properties%22%3A%7B%22%24set%22%3A%7B%22date%22%3A%2201.06.2020%22%2C%22name%22%3A%22Name%22%2C%22buildNumber%22%3A%221.1.1%22%7D%7D%2C%22uuid%22%3A%226a282c27-ada2-4cfc-b096-3b5d337ad0fc%22%2C%22library%22%3A%7B%22name%22%3A%22amplitude-flutter%22%2C%22version%22%3A%223.10.0%22%7D%2C%22sequence_number%22%3A8%2C%22groups%22%3A%7B%7D%2C%22group_properties%22%3A%7B%7D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36%22%7D%5D&upload_time=1667130418879&v=2' \
  --compressed

curl $HOST \
  -H 'authority: collector-test.perek.epoch8.ru' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cross-origin-resource-policy: cross-origin' \
  -H 'origin: http://localhost:63104' \
  -H 'referer: http://localhost:63104/' \
  -H 'sec-ch-ua: "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' \
  --data-raw 'checksum=e6cd69605e0fa4a46439f2e87ebcc757&client=a79cefed0b7076cf3998ef7578a18bf0&e=%5B%7B%22device_id%22%3A%226rPzaVUwYHquzptdsrrKff%22%2C%22user_id%22%3A%22test_user%22%2C%22timestamp%22%3A1667130434980%2C%22event_id%22%3A7%2C%22session_id%22%3A1667130434980%2C%22event_type%22%3A%22Dart%20Click%22%2C%22version_name%22%3Anull%2C%22platform%22%3A%22Web%22%2C%22os_name%22%3A%22Chrome%22%2C%22os_version%22%3A%22106%22%2C%22device_model%22%3A%22Windows%22%2C%22device_manufacturer%22%3Anull%2C%22language%22%3A%22en-US%22%2C%22api_properties%22%3A%7B%7D%2C%22event_properties%22%3A%7B%7D%2C%22user_properties%22%3A%7B%7D%2C%22uuid%22%3A%2252c0306f-f972-45e8-8055-9d05c940e809%22%2C%22library%22%3A%7B%22name%22%3A%22amplitude-flutter%22%2C%22version%22%3A%223.10.0%22%7D%2C%22sequence_number%22%3A9%2C%22groups%22%3A%7B%7D%2C%22group_properties%22%3A%7B%7D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36%22%7D%5D&upload_time=1667130434980&v=2' \
  --compressed

curl $HOST \
  -H 'authority: collector-test.perek.epoch8.ru' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cross-origin-resource-policy: cross-origin' \
  -H 'origin: http://localhost:63104' \
  -H 'referer: http://localhost:63104/' \
  -H 'sec-ch-ua: "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' \
  --data-raw 'checksum=72d23a4332a15318147ccc196c612744&client=a79cefed0b7076cf3998ef7578a18bf0&e=%5B%7B%22device_id%22%3A%226rPzaVUwYHquzptdsrrKff%22%2C%22user_id%22%3A%22test_user%22%2C%22timestamp%22%3A1667130441489%2C%22event_id%22%3A8%2C%22session_id%22%3A1667130441489%2C%22event_type%22%3A%22revenue_amount%22%2C%22version_name%22%3Anull%2C%22platform%22%3A%22Web%22%2C%22os_name%22%3A%22Chrome%22%2C%22os_version%22%3A%22106%22%2C%22device_model%22%3A%22Windows%22%2C%22device_manufacturer%22%3Anull%2C%22language%22%3A%22en-US%22%2C%22api_properties%22%3A%7B%22productId%22%3A%22specialProduct%22%2C%22special%22%3A%22revenue_amount%22%2C%22quantity%22%3A2%2C%22price%22%3A41.23%7D%2C%22event_properties%22%3A%7B%7D%2C%22user_properties%22%3A%7B%7D%2C%22uuid%22%3A%221d01d1aa-287d-4fc8-8325-084041cd3897%22%2C%22library%22%3A%7B%22name%22%3A%22amplitude-flutter%22%2C%22version%22%3A%223.10.0%22%7D%2C%22sequence_number%22%3A10%2C%22groups%22%3A%7B%7D%2C%22group_properties%22%3A%7B%7D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36%22%7D%5D&upload_time=1667130441490&v=2' \
  --compressed