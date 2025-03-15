from rest_framework.throttling import UserRateThrottle

class BobRateThrottle(UserRateThrottle):
    scope = 'bob'