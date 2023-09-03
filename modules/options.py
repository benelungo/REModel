from modules.blender import *


class Options:
    """All available scene transformation options"""
    def get_options_dict(self):
        return dict(zip([getattr(self, obj).name for obj in dir(self) if "OPTION" in obj],
                        [{"func": getattr(self, obj).apply,
                          "type": getattr(self, obj).type}
                         for obj in dir(self) if "OPTION" in obj]))

    def get_options_list(self):
        positions = [[getattr(self, obj).position, getattr(self, obj).name] for obj in dir(self) if "OPTION" in obj]
        positions = sorted(positions, key=lambda l: l[0])
        return [position[1] for position in positions]

    # TODO: add option here
    class OPTIONResolution:
        name = "Resolution"
        type = "resolution"
        position = 0

        @staticmethod
        def apply(value): change_resolution(value[0], value[1])

    class OPTIONBackground:
        name = "Background"
        type = "folder"
        position = 1

        @staticmethod
        def apply(value): set_hdr_background(value)

    class OPTIONRotateUD:
        name = "Rotate (up/down)"
        type = "range"
        position = 2

        @staticmethod
        def apply(value): rotate_UD(value)

    class OPTIONRotateLR:
        name = "Rotate (left/right)"
        type = "range"
        position = 3

        @staticmethod
        def apply(value): rotate_LR(value)

    class OPTIONTransformX:
        name = "Transform X"
        type = "range"
        position = 4

        @staticmethod
        def apply(value): transformX(value)

    class OPTIONTransformY:
        name = "Transform Y"
        type = "range"
        position = 5

        @staticmethod
        def apply(value): transformY(value)

    class OPTIONTransformZ:
        name = "Transform Z"
        type = "range"
        position = 6

        @staticmethod
        def apply(value): transformZ(value)
