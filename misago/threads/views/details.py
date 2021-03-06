from django.template import RequestContext
from misago.acl.utils import ACLError403, ACLError404
from misago.forums.models import Forum
from misago.threads.models import Thread, Post
from misago.threads.views.base import BaseView
from misago.views import error403, error404

class DetailsView(BaseView):
    def fetch_target(self, kwargs):
        self.thread = Thread.objects.get(pk=kwargs['thread'])
        self.forum = self.thread.forum
        self.proxy = Forum.objects.parents_aware_forum(self.forum)
        self.request.acl.forums.allow_forum_view(self.forum)
        self.request.acl.threads.allow_thread_view(self.request.user, self.thread)
        self.parents = Forum.objects.forum_parents(self.forum.pk, True)
        self.post = Post.objects.select_related('user').get(pk=kwargs['post'], thread=self.thread.pk)
        self.post.thread = self.thread
        self.request.acl.threads.allow_post_view(self.request.user, self.thread, self.post)
        self.request.acl.users.allow_details_view()

    def __call__(self, request, **kwargs):
        self.request = request
        self.forum = None
        self.thread = None
        self.post = None
        try:
            self.fetch_target(kwargs)
        except (Forum.DoesNotExist, Thread.DoesNotExist, Post.DoesNotExist):
            return error404(self.request)
        except ACLError403 as e:
            return error403(request, e.message)
        except ACLError404 as e:
            return error404(request, e.message)
        return request.theme.render_to_response('threads/details.html',
                                                {
                                                 'forum': self.forum,
                                                 'parents': self.parents,
                                                 'thread': self.thread,
                                                 'post': self.post,
                                                 },
                                                context_instance=RequestContext(request))