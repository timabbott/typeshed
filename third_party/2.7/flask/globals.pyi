
from werkzeug.local import LocalStack, LocalProxy

_request_ctx_stack = ... # type: LocalStack
_app_ctx_stack = ... # type: LocalStack
current_app = ... # type: LocalProxy
request = ... # type: LocalProxy
session = ... # type: LocalProxy
g = ... # type: LocalProxy
