from collective.portlet.feedmixer import FeedMixerMessageFactory as _
from zope.interface import implements
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

try:
    from zope.schema.interfaces import IVocabularyFactory
except ImportError:
    from zope.app.schema.vocabulary import IVocabularyFactory


class CacheTimeoutVocabulary(object):
    """Vocabulary factory for cache timeouts.
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary([
            SimpleTerm("300", title=_(u"5 minutes")),
            SimpleTerm("900", title=_(u"15 minutes")),
            SimpleTerm("1800", title=_(u"30 minutes")),
            SimpleTerm("3600", title=_(u"1 hour")),
            SimpleTerm("86400", title=_(u"24 hours")),
        ])

CacheTimeoutVocabularyFactory = CacheTimeoutVocabulary()
