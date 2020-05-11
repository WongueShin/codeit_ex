from abc import ABC, abstractmethod

class MessageNotificationManager:
    """메시지 알림 관리 클래스"""

    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message):
        """새로 온 메시지 추가"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """모든 새 메시지 확인"""
        print("새로 온 메시지들:")

        for message in self.message_notifications:
            print(message.return_massage() + "\n")


class Message(ABC):
    @abstractmethod
    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content
        self.message_str = ''

    @abstractmethod
    def massage_addinfo(self) -> str:
        """return massage with short info"""
        self.message_str = f'{self.time}\n{self.sent_by}\n'
        return  self.message_str
    @abstractmethod
    def massage_addcontent(self) -> str:
        """return massage short info + content"""
        pass
    @abstractmethod
    def return_massage(self):
        self.massage_addinfo()
        self.massage_addcontent()
        return self.message_str

class KakaoTalkMessage(Message):
    """카카오톡 메시지 클래스"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        super().__init__(sent_by, time, content)

    def massage_addinfo(self):
        super().massage_addinfo()

    def massage_addcontent(self):
        self.message_str += self.content if len(self.content) <= self.notification_message_max_len else self.content[
                                                                                :self.notification_message_max_len] + "..."
    def return_massage(self):
        super().return_massage()
        return self.message_str




class FacebookMessage(Message):
    """페이스북 메시지 클래스"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        super().__init__(sent_by, time, content)
        self.location = location

    def massage_addinfo(self) -> str:
        """return massage with short info"""
        super().massage_addinfo()
        self.message_str += f'{self.location}\n'

    def massage_addcontent(self) -> str:
        """return massage short info + content"""
        self.message_str += self.content if len(self.content) <= self.notification_message_max_len else self.content[
                                                                                                          :self.notification_message_max_len] + "..."

    def return_massage(self):
        self.massage_addinfo()
        self.massage_addcontent()
        return self.message_str



class TextMessage(Message):
    """문자 메시지 클래스"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        super().__init__(sent_by, time, content)

    def massage_addinfo(self) -> str:
        """return massage with short info"""
        self.message_str= "{}, {}\n".format(self.sent_by, self.time)

    def massage_addcontent(self) -> str:
        """return massage short info + content"""
        self.message_str += self.content if len(self.content) <= self.notification_message_max_len else self.content[
                                                                                                          :self.notification_message_max_len] + "..."

    def return_massage(self):
        self.massage_addinfo()
        self.massage_addcontent()
        return self.message_str


    # 메시지 알림 관리 인스턴스 생성


message_notification_manager = MessageNotificationManager()

# 서로 다른 종류의 메시지 3개 생성
kakao_talk_message = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 30분", "나 오늘 놀러 못갈 거 같아, 미안!")
facebook_message = FacebookMessage("고대위", "서울시 성북구", "2019년 7월 1일 오후 11시 35분", "아니다, 갈게! 너네 어디서 놀고 있어?")
text_message = TextMessage("이영훈", "2019년 7월 2일 오전 12시 30분", "나도 놀러 갈게, 나 지금 출발")

# 메시지 알림 관리 인스턴스에 3개의 메시지를 추가
message_notification_manager.add_new_message(kakao_talk_message)
message_notification_manager.add_new_message(facebook_message)
message_notification_manager.add_new_message(text_message)

# 메시지 알림 관리 인스턴스에 있는 모든 메시지 출력
message_notification_manager.display_message_notifications()