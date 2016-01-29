signals_available = ... # type: bool

class _FakeSignal(object):
    def __init__(self, name, doc=None): ...
    def _fail(self, *args, **kwargs): ...
class Namespace(object):
    def signal(self, name, doc=None) -> _FakeSignal: ...

template_rendered = ... # type: _FakeSignal
request_started = ... # type: _FakeSignal
request_finished = ... # type: _FakeSignal
request_tearing_down = ... # type: _FakeSignal
got_request_exception = ... # type: _FakeSignal
appcontext_tearing_down = ... # type: _FakeSignal
appcontext_pushed = ... # type: _FakeSignal
appcontext_popped = ... # type: _FakeSignal
message_flashed = ... # type: _FakeSignal