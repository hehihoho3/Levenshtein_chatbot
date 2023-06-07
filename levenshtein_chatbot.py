import pandas as pd
import Levenshtein

# CSV 파일에서 응답을 로드하는 함수
def load_responses(file_path):
    responses = {}
    data = pd.read_csv(file_path)
    for _, row in data.iterrows():
        trigger = row['Q']  # 질문
        response = row['A']  # 대답
        responses[trigger] = response
    return responses

# 사용자 입력에 대한 가장 유사한 매치를 찾는 함수
def get_closest_match(user_input, responses):
    closest_match = None
    min_distance = float('inf')
    for key in responses.keys():
        distance = Levenshtein.distance(user_input, key)  # Levenshtein 거리 계산
        if distance < min_distance:
            min_distance = distance
            closest_match = key
    return closest_match

# 메인 함수
def main():
    # CSV 파일에서 응답 로드
    responses = load_responses('ChatbotData.csv')

    # 챗봇 메인 루프
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Chatbot: 안녕히 가세요!")
            break
        closest_match = get_closest_match(user_input.lower(), responses)
        if closest_match:
            print("Chatbot:", responses[closest_match])
        else:
            print("Chatbot: 죄송해요, 이해하지 못했습니다. 다른 방식으로 다시 말씀해 주세요.")
            
# 메인 함수 실행
if __name__ == '__main__':
    main()