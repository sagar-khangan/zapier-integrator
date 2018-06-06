# api
inp = {
    "fullName": "full name",
    "firstName": "firstname2",
    "lastName": "workersfdc",
    "email": "test2@org.com",
    "company": "org",
    "phone": "565756756",
    "address": "BKC",
    "state": "MH",
    "city": "mumbai",
    "country": "india",
    "zip": "411028",
    "directDial": 1233

}

# kafkas
packet = {
    "jobid": 123,
    "payload": {
        "leads": [
            1, 2, 3
        ],
        "provider": "hubspot", # salesforce or any other
        "connection": {
            "api": "https://hooks.zapier.com/hooks/catch/<app id>/azgzrh", # zapier webhook
            "method": "POST",
            "params": [
                {"key": "hapikey", "value": "demo"}
            ],
            "headers": [
                {"key": "content-type", "value": "x-www-form-urlencoded"},  #
                {"key": "cache-control", "value": "no-cache"}
            ]
        }
    }
}

