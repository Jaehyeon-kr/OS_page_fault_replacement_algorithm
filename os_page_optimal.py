page_list = list(map(int,input().split(" ")))

page_len = len(page_list)


def min_seen(seen_idx_dict : dict):
    
    k = sorted(seen_idx_dict.items(), key=lambda x: x[1])
    print(k) 

    return k[0][0], dict(k[1:])  # 페이지번호, 나머지 dict

    
def where_num(num : int , frame : list):
    
    for n, i in enumerate(frame):
        if i == num:
            return n 
        else :
            pass 

    return -1 

def future_ref(timestep:int, page_list : list, now_frame: list):

    # page list는 주어진 순서
    # now_frame은 지금 프레임  
    
    page_list= page_list[timestep+1:]
    print(page_list) # 7 2 3 
    last = -1

    seen_= {} 
    for i in now_frame:
        idx= where_num(i, page_list)
        if idx == -1:
            seen_[i] = float('inf')  # 미래에 없으면 무한대로 설정
        else:
            seen_[i] = idx 
    seen_ = sorted(seen_.items(), key=lambda x:x[1], reverse=True)
    print(seen_)
    print(seen_[0][0])
    return seen_[0][0]

def optimal(page_dim:int, page_list : list):

    lru_ = [ ] 
    seen_idx = { } # 사용시점
    
    
    last_seen_idx =  -1
    
    cnt = 0
    for num, i in enumerate(page_list):
        

        if  i in lru_:
            continue  # hit이니까 그냥 넘어가기
    
            
        elif len(lru_) < page_dim and i not in lru_: # 프레임 다차기전에 일단 프레임을 다 안채웠을떄
            lru_.append(i)
            last_seen_idx = len(lru_) + 1   
            cnt += 1

        elif len(lru_) == page_dim and i not in lru_: # 프레임 다차있는 일반적인 상황에서 찾고자하는 메모리 i가 프레임에 존재하지 않을 때
            #가장 마지막에 참조된것을 가져온다 

            candidate_num = future_ref(num, page_list, lru_) # (1, 0 ) (숫자, 마지막 조회 시점)
            #현재 그 교체대상의 위치를 가져온다.
            
            replace_idx = where_num(candidate_num, lru_)

            lru_[replace_idx] = i #가장 마지막에 참조된것을 가져온다 
            cnt += 1
                

        print(f'{num}| {i} | {lru_}')

    print("최종 페이지 fault 수:", cnt)    
            
print(page_list)
optimal(3, page_list)