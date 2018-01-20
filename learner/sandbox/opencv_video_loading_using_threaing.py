"""
파이선 openCV 스레드 사용 비디오 플레이 테스트
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, opencv 3.4.0

Visual Studio Code에서 실행 시 라이브러리 호출 문제로 Python:Terminal (integrated)로 실행하면 잘됨!

우어어어 멀티 프로세스 쓰면 눈에 보이는 성능 향상이 있는것 같닷! 이미지를 처리하는 과정이 많아질 수록 더 눈에 띄는듯!!

뭐야!!!!!! 왜 한글이 터미널에서 출력이 안되는건데!?!?!?!?!?!?!?!!?!?

이미지 읽는건 스레딩 안될려낭 ;ㅁ;.... 대실패 해버렸다... 핳

레퍼런스:
https://github.com/opencv/opencv/blob/master/samples/python/video_threaded.py

키보드 단축키:

    스페이스바 - 멀티프로세스 켜기/끄기
    ESC - 프로그램 종료~!

"""

from multiprocessing.pool import ThreadPool # 다중 CPU를 위한 멀티스레드 라이브러리 호출
from collections import deque # 기본적인 Deque 가능한 컨테이너를 만드는 클래스입니다.
import cv2 # 오픈쒸브이이! 투! 

print(__doc__) # 프로그램 설명을 콘솔에 표시. 어이야...왜 이거 한글이 깨지냐!!! !)@*(&$)*&!@#

VIDEO_FILE_PATH = 'c:/Users/yooer/Documents/GitHub/Image-Labeling-project/learner/resources/videos/20170923_153612.mp4' # 실행시킬 비디오파이이일!
class DummyThreadTask(object):
    """
    멀티프로세스 클래스의 함수이름만 똑같이 만든 가짜 멀티프로세스 클래스 
    만약 다른데서 사용하려면 꼭 from collections import deque 를 소환해주세욯~!
    """
    def __init__(self, data):
        """
        동작시킬 함수를 초기화

        Args:
            data: 동작할 함수를 넣어줍니다 ~! 담고 있는 것은 함수의 실행 결과물(반환값)이 될겁니다
        """
        DummyThreadTask.data = data
    def ready(self):
        """
        멀티 프로세스가 동작 준비됬다는 것 처럼 하고 맨날 준비됬다고 구라칠겁니다!
        """
        return True
    def get(self):
        """
        가지고 있는 함수의 결과물을 돌려줍니다~!
        """
        return DummyThreadTask.data

class Debugging(object):
    """
    디버깅 글자를 일일히 넣어주기 너무 귀찮아서 만들었습니닷.... 귀찮아요....
    """
    container = deque() # 프레임 저장할 컨테이너~
    frame = None # 프레임을 저장할 공간!
    _default_display_xy_position = 20 # 글자가 시작할 최초 위치!
    
    display_x = _default_display_xy_position # x축 글자가 시작할 위치
    display_y = _default_display_xy_position # y축 글자가 시작할 위치
    display_text_size = 2 # 글자의 두께 결정
    display_text_interval = 30
    def __init__(self, screen_pos_x, screen_pos_y):
        """
        처음에 글자가 시작할 위치를 지정해줍니다아아! 근데 만약 아무것도 안주면 최초 위치는 화면 좌측 상단의
        (20,20)위치에서 시작겁니다~
        
        Args:
            screen_pos_x: 글자가 시작할 최초 x축 좌표 위치
            screen_pos_y: 글자가 시작할 최초 y축 좌표 위치
        """

        # x축 좌표 초기화
        if screen_pos_x != Debugging._default_display_xy_position:
            Debugging.display_x = screen_pos_x
        else:
            Debugging.display_x = Debugging._default_display_xy_position
        # y축 좌표 초기화
        if screen_pos_y != Debugging._default_display_xy_position:
            Debugging.display_y = screen_pos_y
        else:
            Debugging.display_y = Debugging._default_display_xy_position

    def add(self, string):
        """
        적을 글자를 넣어둡니닷. 조심할것은 출력할 메세지를 쌓아두기 떄문에 만약 창내용을 처음부터 새로 쓰고 싶다면
        clear()를 써서 내용을 비워줘요오!
        
        Args:
            string: 적을 글자를 넣어줍니닷!
        """
        Debugging.container.append(string)
    def write_on_frame(self, frame):
        """
        받은 프레임에 디버깅용 글자를 적습니다
        원판은 회손하지 않으니 imshow 로 출력할때 잊지 말고 함수의 결과물을 복사해서 사용해요오오오오

        Args:
            frame: 글자를 그릴 화면을 출력합니다
        
        Return:
            frame: 글자가 써진 화면을 반환합니다~ 원판이랑 다르다는거!
        """
        Debugging.frame = frame.copy()
        
            


def draw_str(dst, target, s):
    """

    """
    x, y = target
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 0), thickness = 5, lineType=cv2.LINE_AA)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), lineType=cv2.LINE_AA)

def process_frame(frame, _):
    # some intensive computation...
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame = cv2.medianBlur(frame, 19)
    return frame, _

if __name__ == '__main__':
    cap = cv2.VideoCapture(VIDEO_FILE_PATH) # 동영상 불러오기!

    THREAD_COUNTS = cv2.getNumberOfCPUs()
    THREAD_POOL = ThreadPool(processes = THREAD_COUNTS)
    FRAME_BUFFER = deque()
    IS_THREAD_ENABLE = True
    IS_DEBUG_SCREEN_ENABLE = True
    while True:
        while len(FRAME_BUFFER) > 0 and FRAME_BUFFER[0].ready():
            res, t0 = FRAME_BUFFER.popleft().get()
            draw_str(res, (20, 50), u'Multiprocessing    :  ' + str(IS_THREAD_ENABLE))
            draw_str(res, (20, 20), u'Pending / Max pending      :  ' + str(len(FRAME_BUFFER)) + '/' + str(THREAD_COUNTS))
            cv2.imshow('threaded video', res)
        if len(FRAME_BUFFER) < THREAD_COUNTS:
            ret, frame = cap.read()
            if IS_THREAD_ENABLE == True:
                THREAD_TASKS = THREAD_POOL.apply_async(process_frame, (frame.copy(), 0))
            else:
                THREAD_TASKS = DummyThreadTask(process_frame(frame, 0))
            FRAME_BUFFER.append(THREAD_TASKS)
        USER_INPUT = cv2.waitKey(1)
        if USER_INPUT == ord('d'):
            IS_DEBUG_SCREEN_ENABLE = not IS_DEBUG_SCREEN_ENABLE
        if USER_INPUT == ord(' '):
            IS_THREAD_ENABLE = not IS_THREAD_ENABLE
        if USER_INPUT == 27:
            break
cv2.destroyAllWindows()