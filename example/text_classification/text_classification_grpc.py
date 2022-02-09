# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: text_classification.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import text_classification_pb2


class GreeterBase(abc.ABC):

    @abc.abstractmethod
    async def SayTextClassify(self, stream: 'grpclib.server.Stream[text_classification_pb2.TextClassifyRequest, text_classification_pb2.TextClassifyReply]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/TextClassify.Greeter/SayTextClassify': grpclib.const.Handler(
                self.SayTextClassify,
                grpclib.const.Cardinality.UNARY_UNARY,
                text_classification_pb2.TextClassifyRequest,
                text_classification_pb2.TextClassifyReply,
            ),
        }


class GreeterStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SayTextClassify = grpclib.client.UnaryUnaryMethod(
            channel,
            '/TextClassify.Greeter/SayTextClassify',
            text_classification_pb2.TextClassifyRequest,
            text_classification_pb2.TextClassifyReply,
        )
