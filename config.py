class settings:
    ClubInfo = [
        {
            "ClubName": "疯羽",
            "ClubPlatform": [
                {
                    "PlatformName": "likedong",
                    "ClubID": 342
                }
            ]
        },
        {
            "ClubName": "羽见",
            "ClubPlatform": [
                {
                    "PlatformName": "likedong",
                    "ClubID": 361
                }
            ]
        },
        {
            "ClubName": "鸽羽",
            "ClubPlatform": [
                {
                    "PlatformName": "shandong",
                    "ClubID": 7484
                }
            ]
        },
        {
            "ClubName": "浔羽",
            "ClubPlatform": [
                {
                    "PlatformName": "shandong",
                    "ClubID": 7784
                },
                {
                    "PlatformName": "likedong",
                    "ClubID": 576
                },
            ]
        },
    ]
    UrlInfo = {
        'likedong': 'https://api.like-sports.cn:8008/api-c/activities/clubActivities?clubId={}&pageNum=1',
        'shandong': 'https://www.shuote.top:8082/flash/activity/filterList?type=1&id={}&pageSize=10&pageNo=1&sportId=0'
    }
    sleep_time = 15 * 60
