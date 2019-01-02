from user_agents import parse

# Let's start from an old, non touch Blackberry device
ua_string = 'BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba'
user_agent = parse(ua_string)
user_agent.is_mobile # returns True
user_agent.is_tablet # returns False
user_agent.is_touch_capable # returns False
user_agent.is_pc # returns False
user_agent.is_bot # returns False
str(user_agent) # returns "BlackBerry 9700 / BlackBerry OS 5 / BlackBerry 9700"

# Now a Samsung Galaxy S3
ua_string = 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
user_agent = parse(ua_string)
user_agent.is_mobile # returns True
user_agent.is_tablet # returns False
user_agent.is_touch_capable # returns True
user_agent.is_pc # returns False
user_agent.is_bot # returns False
str(user_agent) # returns "Samsung GT-I9300 / Android 4.0.4 / Android 4.0.4"

# iPad's user agent string
ua_string = 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10'
user_agent = parse(ua_string)
user_agent.is_mobile # returns False
user_agent.is_tablet # returns True
user_agent.is_touch_capable # returns True
user_agent.is_pc # returns False
user_agent.is_bot # returns False
str(user_agent) # returns "iPad / iOS 3.2 / Mobile Safari 4.0.4"

# Kindle Fire's user agent string
ua_string = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true'
user_agent = parse(ua_string)
user_agent.is_mobile # returns False
user_agent.is_tablet # returns True
user_agent.is_touch_capable # returns True
user_agent.is_pc # returns False
user_agent.is_bot # returns False
str(user_agent) # returns "Kindle / Android / Amazon Silk 1.1.0-80"

# Touch capable Windows 8 device
ua_string = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)'
user_agent = parse(ua_string)
user_agent.is_mobile # returns False
user_agent.is_tablet # returns False
user_agent.is_touch_capable # returns True
user_agent.is_pc # returns True
user_agent.is_bot # returns False
str(user_agent) # returns "PC / Windows 8 / IE 10"