import time
from django.http import HttpResponseForbidden
from django.core.cache import cache

class AccessLogsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        # get user ip address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        request.ip = ip

        # Getting User and there endpoint that visited
        user=request.user
        visit_count_key = f'visit_count_{user.id}'
        visit_count = cache.get(visit_count_key, default=0)
        restriction_key = f'restriction_{user.id}'
        restriction_timeout = 30
        request.gold='10 endPoints & Gold Member'
        request.Silver='7 endPoints & Silver Member'
        request.Bronze='5 endPoints & Bronze Member'
        request.Guest='2 endPoints & Guest Member'

        visit=[2]
        dict_group={2:'Guest',5:'Bronze',7:'Silver',10:"Gold"}

        # All Users
        user_groups=request.user.groups.all()

        # Gold Group
        if((user_groups.filter(name='Gold').exists()) and (user_groups.filter(name='Silver').exists())):
            visit.append(10)

        # Silver Group
        elif((user_groups.filter(name='Silver').exists()) and (user_groups.filter(name='Bronze').exists())):
            visit.append(7)

        # Gold Group
        elif((user_groups.filter(name='Gold').exists()) and (user_groups.filter(name='Bronze').exists())):
            visit.append(10)
           
        # Bronze Group Single Group User
        elif(user_groups.filter(name='Bronze').exists()):
            visit.append(5)

        # Gold Group Single Group User
        elif(user_groups.filter(name='Gold').exists()):
            visit.append(10)

        # Silver Group single Group User
        elif(user_groups.filter(name='Silver').exists()):
            visit.append(7)
            
        else: # without any Group
            visit.append(2)

        max_visits=max(visit)
        group=dict_group[max_visits]
        print(group)
        request.group=group

        if visit_count >= max_visits:
                if not cache.get(restriction_key):
                    cache.set(restriction_key, True, restriction_timeout)
                    return HttpResponseForbidden(f"Hi,{user} {group} Member Please try again after 30 Seconds. you're temparory blocked !!!")
        cache.set(visit_count_key, visit_count + 1)
        # OutGoing Traffic
        response = self.get_response(request)
        return response
    
