# Example usage:

# class ExampleEvent(BaseEvent):
#
#     def __init__(self):
#         interval_minutes = 60  # Set the interval for this event
#         super().__init__(interval_minutes)
#
#     # Override the run() method
#     # It will be called once every {interval_minutes} minutes
#     async def run(self, client):
#         now = datetime.now()
#
#         if now.hour == 12:
#             msg = "It's high noon!"
#         else:
#             msg = f"It is {now.hour}:{now.minute}"
#
#         channel = get_channel(client, "general")
#         await client.send_message(channel, msg)


class BaseEvent:

    def __init__(self, interval_minutes):
        self.interval_minutes = interval_minutes

    async def run(self, client):
        raise NotImplementedError  # To be defined by every event
