from misago.profiles.decorators import profile_view
from misago.profiles.template import RequestContext
from misago.utils import make_pagination

@profile_view('user_posts')
def posts(request, user, page=0):
    queryset = user.post_set.filter(forum_id__in=request.acl.threads.get_readable_forums(request.acl)).filter(deleted=False).filter(moderated=False).select_related('thread', 'forum').order_by('-id')
    count = queryset.count()
    pagination = make_pagination(page, count, 12)
    return request.theme.render_to_response('profiles/posts.html',
                                            context_instance=RequestContext(request, {
                                             'profile': user,
                                             'tab': 'posts',
                                             'items_total': count,
                                             'items': queryset[pagination['start']:pagination['stop']],
                                             'pagination': pagination,
                                             }));
