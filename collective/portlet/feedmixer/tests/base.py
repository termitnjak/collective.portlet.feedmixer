from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
from Testing import ZopeTestCase as ztc


@onsetup
def setup_product():
    """Set up additional products and ZCML required to test this product.

    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """

    # Load the ZCML configuration for this package and its dependencies

    fiveconfigure.debug_mode = True
    import collective.portlet.feedmixer
    zcml.load_config('configure.zcml', collective.portlet.feedmixer)
    fiveconfigure.debug_mode = False

    # We need to tell the testing framework that these products
    # should be available. This can't happen until after we have loaded
    # the ZCML.

    ztc.installPackage('collective.portlet.feedmixer')


# The order here is important: We first call the deferred function and then
# let PloneTestCase install it during Plone site setup

setup_product()
ptc.setupPloneSite(products=['collective.portlet.feedmixer'])


class TestCase(ptc.PloneTestCase):
    """Base class used for test cases
    """


class FunctionalTestCase(ptc.FunctionalTestCase):
    """Test case class used for functional (doc-)tests."""
