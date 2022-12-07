from functools import partial
from typing import Tuple, Any
from .handler import AbletonOSCHandler

class SceneHandler(AbletonOSCHandler):
    def init_api(self):
        #--------------------------------------------------------------------------------
        # Init callbacks for Set: methods
        #--------------------------------------------------------------------------------
        for method in [
            "fire"

        ]:
            callback = partial(self._call_method, self.scene, method)
            self.osc_server.add_handler("/live/scene/%s" % method, callback)

        #--------------------------------------------------------------------------------
        # Init callbacks for Set: properties
        #--------------------------------------------------------------------------------
        properties_rw = [
            "name",
            "is_empty"
        ]
        properties_r = [
            "name",
            "is_empty"
        ]

        for prop in properties_r + properties_rw:
            self.osc_server.add_handler("/live/scene/get/%s" % prop, partial(self._get_property, self.scene, prop))
            self.osc_server.add_handler("/live/scene/start_listen/%s" % prop, partial(self._start_listen, self.scene, prop))
            self.osc_server.add_handler("/live/scene/stop_listen/%s" % prop, partial(self._stop_listen, self.scene, prop))
        for prop in properties_rw:
            self.osc_server.add_handler("/live/scene/set/%s" % prop, partial(self._set_property, self.scene, prop))


