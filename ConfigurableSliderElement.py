from _Framework.SliderElement import SliderElement


class ConfigurableSliderElement(SliderElement):
    """ Special Slider class that can be configured with custom on- and off-values.
    Not currently used elsewhere in this script, but fixed for correctness:
    the original referenced an unimported ButtonElement and an undefined
    `force` variable, which would have raised NameError if ever called. """
    __module__ = __name__
    __doc__ = ' Special Slider class that can be configured with custom on- and off-values '

    def __init__(self, msg_type, channel, identifier):
        super().__init__(msg_type, channel, identifier)
        self._last_active_value = None
        self._force_next_value = False

    def send_value(self, value, force=False):
        if value != self._last_active_value:
            super().send_value(value, force or self._force_next_value)
        self._last_active_value = value
        self._force_next_value = False
