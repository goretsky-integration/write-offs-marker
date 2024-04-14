from faststream import FastStream
from faststream.rabbit import RabbitBroker

import handlers
from config import load_config_from_file

broker = RabbitBroker(load_config_from_file().message_queue_url)
app = FastStream(broker)

broker.include_router(handlers.router)
