def decode_message(message, char_count):
    # 각 문자의 인코딩 값
    valid_codes = {
        '000000': 'A',
        '001111': 'B',
        '010011': 'C',
        '011100': 'D',
        '100110': 'E',
        '101001': 'F',
        '110101': 'G',
        '111010': 'H'
    }
    
    result = ""
    
    # 각 문자(6비트) 처리
    for i in range(char_count):
        start = i * 6
        code = message[start:start+6]
        
        # 정확히 일치하는 코드가 있는지 확인
        if code in valid_codes:
            result += valid_codes[code]
            continue
        
        # 1비트만 다른 코드 찾기
        found = False
        for valid_code, char in valid_codes.items():
            # 두 코드 간 다른 비트 수 계산
            diff_count = sum(1 for a, b in zip(code, valid_code) if a != b)
            if diff_count == 1:
                result += char
                found = True
                break
        
        # 해독 불가능한 문자
        if not found:
            return i + 1
    
    return result

# 입력 처리
char_count = int(input().strip())
message = input().strip()

# 결과 출력
print(decode_message(message, char_count))