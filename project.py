from simple_blogger import Journalist
from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from simple_blogger.senders.TelegramSender import TelegramSender
from simple_blogger.senders.VkSender import VkSender
from datetime import datetime

class Project(Journalist):
    def __init__(self, **kwargs):
        super().__init__(            
            first_post_date=datetime(2025, 3, 6),
            text_generator=OpenAITextGenerator(),
            send_text_with_image=True,
            reviewer=TelegramSender(),
            senders=[
                TelegramSender(channel_id='@coffee_and_nerves'),
                VkSender(group_id='229838019')
            ],
            topic_word_limit=100,
            **kwargs)

    def _task_converter(self, item):
        return { 
                "topic": f"{item['topic']}",
                "category": f"{item['category']}",
                "topic_image": f"Нарисуй картинку, вдохновлённую темой '{item['topic']}' из области '{item['category']}'",
                "topic_prompt": f"Выбери рандомно актуальную проблему по теме '{item['topic']}' из области '{item['category']}', опиши проблему, как если бы рассказывал подруге, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее {self.topic_word_limit} слов",
            }
    
    def _system_prompt(self, _):
        return f'Ты - руководитель HR, лидер команды со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора'