from typing import Tuple, Any
from .handler import AbletonOSCHandler

class SceneHandler(AbletonOSCHandler):
    def __init__(self, manager):
        super().__init__(manager)
        self.class_identifier = "scene"
    def init_api(self):
        def create_scene_callback(func, *args):
            def scene_callback(params: Tuple[Any]):
                scene_index = params[1]
                scene = self.song.scene[scene_index]
                return func(scene, *args, params[1:])

            return scene_callback

        methods = [
            "fire",
            "fire_as_selected"
        ]
        properties_r = [
            "clip_slots",
            "color",
            "color_index",
            "is_empty",
            "is_triggered",
            "name",
            "tempo"
        ]
        properties_rw = [
            "color",
            "color_index",
            "name",
            "tempo"
        ]

        for method in methods:
            self.osc_server.add_handler("/live/scene/%s" % method,
                                        create_scene_callback(self._call_method, method))

        for prop in properties_r + properties_rw:
            self.osc_server.add_handler("/live/scene/get/%s" % prop,
                                        create_scene_callback(self._get_property, prop))
            self.osc_server.add_handler("/live/scene/start_listen/%s" % prop,
                                        create_scene_callback(self._start_listen, prop))
            self.osc_server.add_handler("/live/scene/stop_listen/%s" % prop,
                                        create_scene_callback(self._stop_listen, prop))
        for prop in properties_rw:
            self.osc_server.add_handler("/live/scene/set/%s" % prop,
                                        create_scene_callback(self._set_property, prop))
