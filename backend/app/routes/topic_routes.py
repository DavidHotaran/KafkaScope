from fastapi import APIRouter

topic_router = APIRouter()


# topic CRUD operations


@topic_router.get("/topics")
def get_all_topics():
    pass


@topic_router.get("/topics/{topic:str}")
def get_topic_by_name(topic: str):
    pass


@topic_router.post("/topics")
def create_topic():
    pass


@topic_router.delete("topics/{topic:str}")
def delete_topic(topic: str):
    pass


# topic message operations


@topic_router.post("/topics/{topic:str}/messages/produce")
def produce_new_message_on_topic(topic: str):
    pass


@topic_router.get("/topics/{topic:str}/messages/view")
def view_messages_on_topic(topic: str):
    """View current messages on a topic, does NOT consume the messages. This is a read only glance."""  # noqa: E501
    pass
