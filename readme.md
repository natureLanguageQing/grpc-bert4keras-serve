# grpc bert4keras serve


requirements

```
grpclib 
protobuf
```
grpclib 简介 一款实现asyncio的python的grpc扩展库

以文本分类项目为例子

本教程运行目录为`example/text_classification`

第一步：通过`text_classification_proto_code_gen.sh`根据pb文件生成`text_classification_grpc.py`和`text_classification_pb2.py`

第二步：编写serve层代码

```
import asyncio

from grpclib.server import Server, Stream
from grpclib.utils import graceful_exit

from text_classification_grpc import GreeterBase
# generated by protoc
from text_classification_pb2 import TextClassifyRequest, TextClassifyReply


class Greeter(GreeterBase):

    async def SayTextClassify(self, stream: Stream[TextClassifyRequest, TextClassifyReply]) -> None:
        request = await stream.recv_message()
        assert request is not None
        message = f'Hello, {request.text}!'
        a = TextClassifyReply.Scores(negative=1.3, neutral=0.4, positive=0.8)
        await stream.send_message(TextClassifyReply(label=message, scores=a))


async def main(*, host: str = '127.0.0.1', port: int = 50052) -> None:
    server = Server([Greeter()])
    # Note: graceful_exit isn't supported in Windows
    with graceful_exit([server]):
        await server.start(host, port)
        print(f'Serving on {host}:{port}')
        await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())

```
第四步启动grpc服务的serve层
```
sh text_classification_serve.sh
```

测试结果
```100%|█████████████████████████████████████████████████████| 1000/1000 [00:14<00:00, 70.53it/s]```
测试环境
GPU
TITAN Xp
CPU
7核 Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz