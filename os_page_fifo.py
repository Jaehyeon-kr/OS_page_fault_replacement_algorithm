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


def Fifo(page_dim:int, page_list : list):

    lru_ = [ ] 
    seen_idx = { } # 사용시점
    
    
    last_seen_idx =  -1
    
    cnt = 0
    for num, i in enumerate(page_list):
        

        if len(lru_) == page_dim and i in lru_: # 프레임 다차있는 일반적인 상황에서 찾고자하는 메모리 i가 프레임에 존재할 때
            # fifo는 갱신안함
            continue
            # seen_idx[i] = num  # LRU는 hit해도 사용시점 갱신해야함
            
        elif len(lru_) < page_dim and i not in lru_: # 프레임 다차기전에 일단 프레임을 다 안채웠을떄
            lru_.append(i)
            last_seen_idx = len(lru_) + 1   
            seen_idx[i] = num   
            cnt += 1

        elif len(lru_) == page_dim and i not in lru_: # 프레임 다차있는 일반적인 상황에서 찾고자하는 메모리 i가 프레임에 존재하지 않을 때
            #가장 마지막에 참조된것을 가져온다 
            last_seen_num, seen_idx = min_seen(seen_idx) # (1, 0 ) (숫자, 마지막 조회 시점)
            #현재 그 교체대상의 위치를 가져온다.
            
            replace_idx = where_num(last_seen_num, lru_)

            lru_[replace_idx] = i #가장 마지막에 참조된것을 가져온다 
            seen_idx[i] = num
            cnt += 1
                
        elif len(lru_) < page_dim and i in lru_:
            continue  # hit이니까 그냥 넘어가기
        print(f'{num}| {i} | {lru_}')

    print("최종 페이지 fault 수:", cnt)    
            
print(page_list)
Fifo(3, page_list)