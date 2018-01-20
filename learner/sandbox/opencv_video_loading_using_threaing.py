"""
파이선 openCV 스레드 사용 비디오 플레이 테스트
저자 : 안광은 (yooer10ms@cu.ac.kr)
버전 : python 3.5.4, opencv 3.4.0

Superpixel 코드가 내장되어 있어서 실험해볼 수 있음! CPU의 코어 개수에 맞춰 동적으로 활용

주의사항으로는... CPU 너무 열일하게됨;;;; (노트북이 헤어드라이기가 된줄 ;ㅂ;)

TODO: 
    뭐야!!!!!! 왜 한글이 터미널에서 출력이 안되는건데!?!?!?!?!?!?!?!!?!?
    디버깅용 글자도 한글이 안되 ㅠㅠㅠㅠ putText가 ASCII만 지원한다니... 하아... 
    이미지 읽는건 스레딩 안될려낭 ;ㅁ;.... 대실패 해버렸다... 핳

레퍼런스:
https://github.com/opencv/opencv/blob/master/samples/python/video_threaded.py

키보드 단축키:

    t - 멀티 프로세싱 활성화
    탭 키 - 디버깅 창 표시
    스페이스바 - 일시정지
    ESC, q - 프로그램 종료~!

"""

from multiprocessing.pool import ThreadPool # 다중 CPU를 위한 멀티스레드 라이브러리 호출
from collections import deque # 기본적인 Deque 가능한 컨테이너를 만드는 클래스입니다.
import cv2 # 오픈쒸브이이! 투!
import numpy as np

print(__doc__) # 프로그램 설명을 콘솔에 표시. TODO:어이야...왜 이거 한글이 깨지냐!!! !)@*(&$)*&!@#

#VIDEO_FILE_PATH = u'D:/OneDrive/문서/GitHub/Image-Labeling-Project/learner/resources/videos/sample_video.mp4' # 실행시킬 비디오파이이일!
VIDEO_FILE_PATH = u'D:/OneDrive/문서/GitHub/Image-Labeling-Project/learner/resources/videos/sample_video_2.mp4' # 실행시킬 비디오파이이일!
IS_THREAD_ENABLE = False
IS_DEBUG_SCREEN_ENABLE = False
IS_PLAY_PAUSED = False
WINDOW_TITLE = 'Video Player with CPU Threading'
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
        self.data = data
    def ready(self):
        """
        멀티 프로세스가 동작 준비됬다는 것 처럼 하고 맨날 준비됬다고 구라칠겁니다!
        """
        return True
    def get(self):
        """
        가지고 있는 함수의 결과물을 돌려줍니다~!
        """
        return self.data
class TextOnScreen(object):
    """
    프레임에 디버깅 메세지를 넣어주는 클래스! 디버깅 글자를 일일이 넣어주니 눈아파요 ;ㅁ; 그래서 자동으로 만들었습니다

    x, y 좌표는 프레임에 디버깅 메세지를 적을 위치를 지정해줍니다 

    근데 만약 아무것도 안주면 최초 위치는 화면 좌측 상단의 (20,20)위치에서 시작할겁니다~

    아 그리고 지금은 한글 지원 안되요....;ㅅ; cv2.putText 함수가 ASCII만 지원해요..
    """
    frame = None # 원본 프레임을 저장할 공간!

    _font_size_ratio = 0.1 # 0.1 기준으로 커지는게 괜찮을것 같아서 10!
    _font_size_interval = 2 # 그냥 몇번 테스트 해봤는데 opencv 의 글자가 0.1 커지면 2정도 커지는게 적당히 보이더라구욯
    _container = deque() # 프레임 저장할 컨테이너~
    _frame = None # 디버깅 글자가 추가된 프레임을 저장할 공간~
    display_text_size = 1.0 # 글자의 크기
    display_text_interval = 20 # 글자 상하 간격
    display_text_thickness = 1 # 글자 굵기
    def __init__(self, screen_pos_x = None, screen_pos_y = None):
        """
        처음에 글자가 시작할 위치를 지정해줍니다아아! 근데 만약 아무것도 안주면 최초 위치는 화면 좌측 상단의 (20,20)위치에서 시작할겁니다~
        
        Args:

            screen_pos_x: 글자가 시작할 최초 x축 좌표 위치

            screen_pos_y: 글자가 시작할 최초 y축 좌표 위치
        """
        # x축 좌표 설정
        if screen_pos_x is not None:
            self.display_x = screen_pos_x
        else:
            self.display_x = 20 
        # y축 좌표 설정
        if screen_pos_y is not None:
            self.display_y = screen_pos_y
        else:
            self.display_y = 20

    def adjust_display_size(self, size):
        """
        글자의 크기를 조정합니다! 모니터 해상도마다 다를 수 있어서 보기 편하게 조정해줍니닷!
        
        Args:

            size: 조정할 사이즈를 입력해줍니다! int값으로 1~10정도? 사실 아직 제한이 없어요..
        """
        self.display_text_size += float(size * self._font_size_ratio)
        self.display_text_interval += size * self._font_size_interval
        self.display_y += size * 2 # 눈에 이상하지 않을 정도로(?) 글자가 상단에 잘리는거 없애기
        if self.display_y >= 40:
            self.display_text_thickness = int(self.display_y/20)
        else:
            self.display_text_thickness = 1
        print(self.display_y)

    def add(self, string):
        """
        적을 글자를 넣어둡니닷. 조심할것은 출력할 메세지를 쌓아두기 떄문에 만약 창내용을 처음부터 새로 쓰고 싶다면
        clear()를 써서 내용을 비워줘요오!

        아 그리고 문자열은 유니코드로 변경되어 저장됩니다~
        
        Args:

            string: 적을 글자를 넣어줍니닷!
        """
        self._container.append(string.encode('utf-8'))
    def write_on_frame(self, frame):
        """
        받은 프레임에 디버깅용 글자를 적습니다
        원판은 회손하지 않으니 imshow 로 출력할때 잊지 말고 함수의 결과물을 복사해서 사용해요오오오오

        출력해야될 문장이 너무 많으면 화면을 벗어날 수 있어요~!

        Args:
            frame: 글자를 그릴 화면을 출력합니다
        
        Return:
            frame: 글자가 써진 화면을 반환합니다~ 원판이랑 다르다는거!
        """
        _frame = frame.copy() # 원판을 살립시다! 즉 그냥 새로 하나 복사했습니닷
        for itr_container in range(0, len(self._container)): # 출력할 디버깅 메세지들을 하나씩 꺼내서 프레임에 씁니다
            _tmp_str = self._container.popleft() # 메세지 꺼내기~!
            _interval = self.display_text_interval * itr_container # 메세지 위아래 간격 만들기
            # 디버깅 메세지 쓰기~!
            cv2.putText(_frame, _tmp_str.decode('utf-8'), (self.display_x + 1, self.display_y + 1 + _interval), cv2.FONT_HERSHEY_PLAIN, self.display_text_size, (0, 0, 0), thickness = self.display_text_thickness, lineType=cv2.LINE_AA)
            cv2.putText(_frame, _tmp_str.decode('utf-8'), (self.display_x, self.display_y + _interval), cv2.FONT_HERSHEY_PLAIN, self.display_text_size, (255, 255, 255), thickness = self.display_text_thickness, lineType= cv2.LINE_AA)
        self._container.clear() # 글자 출력하면 디버깅 메세지 컨테이너 비우기
        return _frame # 디버깅 메세지가 적어진 프레임을 반환합니닷~
def process_frame(frame, _):
    """
    영상을 조작하기(?) 위한 함수~! 여기에다가 각 프레임에 적용할 필터나 기능을 추가하면 됨이이~!

    Args:

        frame: 영상의 프레임! 스레드에 들어가는 경우 개별적으로 처리해야 하기에 .copy()를 사용하여 넣어주기!

        _: frame 변수를 전부 분해해버리는 파이썬 변수 처리를 막기 위한 더미 변수

    Return:

        frame: 조작된(?) 프레임 반환~!

        None: frame 변수를 전부 분해해버리는 파이썬 변수 처리를 막기 위한 더미 변수

    레퍼런스:

        https://github.com/opencv/opencv_contrib/blob/master/samples/python2/seeds.py
    """
    height, width, channels = frame.shape
    num_iterations = 2
    num_superpixels = 400
    prior = 2
    num_levels = 4
    num_histogram_bins = 5
    seeds = None
    if not seeds:
        seeds = cv2.ximgproc.createSuperpixelSEEDS(width, height, channels, num_superpixels, num_levels, prior, num_histogram_bins)
        color_img = np.zeros((height,width,3), np.uint8)
        color_img[:] = (0, 0, 255)

    seeds.iterate(frame, num_iterations)

    # retrieve the segmentation result
    labels = seeds.getLabels()

    # labels output: use the last x bits to determine the color
    num_label_bits = 2
    labels &= (1<<num_label_bits)-1
    labels *= 1<<(16-num_label_bits)

    mask = seeds.getLabelContourMask(False)

    # stitch foreground & background together
    mask_inv = cv2.bitwise_not(mask)
    result_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    result_fg = cv2.bitwise_and(color_img, color_img, mask=mask)
    frame = cv2.add(result_bg, result_fg)
    return frame, None

"""
메인 프로그램 시작~!
"""
if __name__ == '__main__':
    VIDEO = cv2.VideoCapture(VIDEO_FILE_PATH) # 동영상 불러오기!
    THREAD_COUNTS = cv2.getNumberOfCPUs() # CPU 갯수 얻기
    THREAD_POOL = ThreadPool(processes = THREAD_COUNTS) # 스레드 활성화
    THREAD_CONTAINER = deque() # 스레드 결과를 담아두는 컨테이너
    DEBUGGER = TextOnScreen() # 디버깅 메세지용~!
    _pause_frame = None
    
    if VIDEO.isOpened is False: # 파일을 못찾는 경우 프로그램 끄기!
            print('Video is not loaded!')
            exit(1)
    while True:
        #사용자 키 입력받기
        USER_INPUT = cv2.waitKey(1) # 키 입력 대기 (밀리초 기준)
        if USER_INPUT is 9: # 디버깅 활성화 (tab키)
            IS_DEBUG_SCREEN_ENABLE = not IS_DEBUG_SCREEN_ENABLE
        if USER_INPUT is ord('+'): # 디버깅 글자 크기 키우기
            DEBUGGER.adjust_display_size(1)
        if USER_INPUT is ord('_'): # 디버깅 글자 크기 줄이기
            DEBUGGER.adjust_display_size(-1)
        if USER_INPUT is ord('t'): # 스레드 활성화
            IS_THREAD_ENABLE = not IS_THREAD_ENABLE
        if USER_INPUT is 27 or USER_INPUT is ord('q'): # 프로그램 끄기 (esc키, q키 )
            break
        if USER_INPUT is ord(' '): # 재생 일시 정지
            IS_PLAY_PAUSED = not IS_PLAY_PAUSED
        
        if IS_PLAY_PAUSED is not True: # 화면 재생하기~!
            # 스레드 작업
            while len(THREAD_CONTAINER) > 0 and THREAD_CONTAINER[0].ready(): # 작업해야될 스레드 개수가 다 찻다면 화면 잠깐 멈추고 출력하기
                frame, _ = THREAD_CONTAINER.popleft().get() # 컨테이너에서 프레임 가져오기
                _pause_frame = frame.copy() # 정지화면용으로 복사해두기
                if IS_DEBUG_SCREEN_ENABLE is True: # 디버그 메세지 추가하기
                    DEBUGGER.add('Multiprocessing    :  ' + str(IS_THREAD_ENABLE))
                    DEBUGGER.add('Pending / Max     :  ' + str(len(THREAD_CONTAINER)) + '/' + str(THREAD_COUNTS))
                cv2.imshow(WINDOW_TITLE, DEBUGGER.write_on_frame(frame)) # 화면 보여주기!
            if len(THREAD_CONTAINER) < THREAD_COUNTS: # 스레드에 공간이 있다면 작업 넣기~
             #일시정지 안 했을때만 작업하기~
                _, frame = VIDEO.read() # 비디오 프레임 읽어오기
                if frame is None: # 비디오가 다 끝나면 화면 출력 종료~! 
                    #TODO: 근데 어째 생각해보니 이렇게 작성하면 영상 다 출력했을 때 스레드에 프레임이 남아 있어도 화면에 안나오고 짤릴 수 있겠는..걸?
                    break
                if IS_THREAD_ENABLE is True: # 스레드 사용하면 프로세스 여러개 사용하기
                    THREAD_TASKS = THREAD_POOL.apply_async(process_frame, (frame.copy(),0)) # process_frame 함수를 거처서 결과를 가져오기~
                else: # 스레드가 꺼져있으면 그냥 프로세스 하나로 작업하기
                    THREAD_TASKS = DummyThreadTask(process_frame(frame, 0)) # process_frame 함수를 거처서 결과를 가져오기~
                THREAD_CONTAINER.append(THREAD_TASKS) # 프레임 추가하기
        else: # 정지화면 보여주기~ 키보드 입력은 먹힘!
            DEBUGGER.add('Play Paused') #일시 정지 화면 출력하기
            if IS_DEBUG_SCREEN_ENABLE is True: # 디버그 메세지 추가하기
                DEBUGGER.add('Multiprocessing    :  ' + str(IS_THREAD_ENABLE))
                DEBUGGER.add('Pending / Max     :  ' + str(len(THREAD_CONTAINER)) + '/' + str(THREAD_COUNTS))
            cv2.imshow(WINDOW_TITLE, DEBUGGER.write_on_frame(_pause_frame)) # 디버그 메세지 추가된 프레임 넣기
cv2.destroyAllWindows() # 화면 끄기