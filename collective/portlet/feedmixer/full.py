from Acquisition import aq_acquire
from Products.Five.browser import BrowserView


class FullFeedView(BrowserView):

    @property
    def title(self):
        return self.context.title

    @property
    def entries(self):
        return aq_acquire(self, 'context').entries
