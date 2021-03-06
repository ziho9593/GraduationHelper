def dict_select(user_id):
    '''
    maj_dict = {
        전공: [0.줄임말, 1.단일전공학점, 2.단일전공전필, 3.단일전공선필, 4.복수전공학점, 5.복수전공전필, 6.복수전공선필, 7.총이수학점]
        }
    '''
    if user_id in ['12', '13', '14', '15']:
        maj_dict = {
            # 지식정보서비스대학
            '경영정보전공': ['경정', 60, 7, 0, 45, 4, 0, 130],
            '회계세무전공': ['회세', 60, 9, 0, 45, 4, 0, 130],
            '무역학과': ['무역', 60, 9, 0, 45, 4, 0, 130],
            '경영학과': ['경영', 60, 9, 0, 45, 4, 0, 130],
            '법학과': ['법', 60, 1, 5, 42, 0, 5, 136],
            '행정학과': ['행정', 60, 1, 5, 42, 0, 5, 130],
            '경찰행정학과': ['경행', 60, 1, 5, 42, 0, 5, 130],
            '국제관계학과': ['국관', 60, 1, 5, 42, 0, 5, 130],
            '국제산업정보학과': ['국정', 60, 5, 0, 42, 5, 0, 130],
            '지식재산학과': ['지재', 60, 1, 5, 42, 0, 5, 130],
            '교정보호전공': ['교보', 60, 1, 5, 42, 0, 5, 130],
            '사회복지전공': ['사복', 60, 6, 0, 42, 6, 0, 130],
            '청소년전공': ['청년', 60, 4, 0, 42, 4, 0, 130],
            '경제전공': ['경제', 60, 5, 0, 42, 5, 0, 130],
            '응용통계전공': ['응통', 60, 6, 0, 42, 6, 0, 130],
            # 인문대학
            '유아교육과': ['유아', 60, 1, 5, 42, 0, 5, 130],
            '국어국문학과': ['국문', 60, 1, 0, 42, 0, 0, 130],
            '영어영문학과': ['영문', 60, 1, 0, 42, 0, 0, 130],
            '중어중문학과': ['중문', 60, 6, 0, 42, 5, 0, 130], # 전진탐 1, 전필and선필 5
            '사학과': ['사', 60, 1, 5, 42, 0, 5, 130],
            '문헌정보학과': ['문정', 60, 1, 5, 42, 0, 5, 130],
            '문예창작학과': ['문창', 60 ,1, 5, 42, 0, 5, 130],
            '독어독문전공': ['독문', 60, 1, 5, 42, 0, 5, 130],
            '프랑스어문전공': ['프문', 60, 1, 5, 42, 0, 5, 130],
            '일어일문전공': ['일문', 60, 1, 5, 42, 0, 5, 130],
            '러시아어문전공': ['러문', 60, 1, 5, 42, 0, 5, 130],
            # 융합과학대학
            '융합보안학과': ['융보', 60, 1, 0, 42, 0, 0, 130],
            '수학과': ['수', 60, 1, 10, 42, 0, 10, 130],
            '전자물리학과': ['전물', 60, 1, 10, 42, 0, 10, 130],
            '화학과': ['화', 60, 1, 10 ,42, 0, 10, 130],
            '생명과학전공': ['생과', 60, 1, 10, 42, 0, 10, 130],
            '식품생물공학전공': ['식생', 60, 1, 10, 42, 0, 10, 130],
            '컴퓨터공학부': ['컴공', 67, 1, 0, 42, 0, 0, 136],
            # 창의공과대학
            '토목공학과': ['토목', 67, 1, 0, 42, 0, 0, 136],
            '건축공학과': ['건축', 67, 6, 0, 42, 6, 0, 136],
            '도시ㆍ교통공학과': ['도교', 67, 1, 10, 42, 0, 10, 136],
            '신소재공학과': ['산재', 67, 1, 0, 42, 0, 0, 136],
            '환경에너지공학과': ['환에', 67, 1, 10, 42, 0, 10, 136],
            '화학공학과': ['화공', 67, 1, 10, 42, 0, 10, 136],
            '산업경영공학과': ['산경', 67, 1, 10, 42, 0, 10, 136],
            '전자공학과': ['전자', 67, 1, 10, 42, 0, 10, 136],
            '기계시스템공학과': ['기시', 67, 1, 10, 42, 0, 10, 136],
            '건축학과': ['건축', 120, 31, 0, 120, 31, 0, 170],
            # 예술체육대학
            '서양화학과': [''],
            '예술학과': [''],
            '서양화ㆍ미술경영학과': ['서미', 60, 1, 0, 42, 0, 0, 130],
            '서예ㆍ문자예술학과': [''],
            '한국화학과': [''],
            '한국화ㆍ서예학과': ['한서', 60, 1, 0, 42, 0, 0, 130],
            '도예학과': [''],
            '환경조각학과': [''],
            '입체조형학과': ['입체', 60, 1, 0, 42, 0, 0, 130],
            '체육학과': ['체육', 60, 1, 5, 42, 0, 5, 130],
            '시각정보디자인전공': ['시정', 60, 1, 0, 42, 0, 0, 130],
            '산업디자인전공': ['산디', 60, 1, 0, 42, 0, 0, 130],
            '장신구ㆍ금속디자인전공': ['장금', 60, 1, 0, 42, 0, 0, 130],
            '스포츠건강과학전공': ['스건', 60, 1, 0, 42, 0, 0, 130],
            '레저스포츠전공': ['레스', 60, 1, 5, 42, 0, 5, 130],
            '스포츠산업경영전공': ['스산', 60, 1, 0, 42, 0, 0, 130],
            '시큐리티매니지먼트학과': ['시큐', 60, 1, 0, 42, 0, 0, 130],
            # 관광문화대학
            '관광경영학과': ['관경', 60, 1, 5, 42, 0, 5, 130],
            '관광개발학과': ['관개', 60, 1, 5, 42, 0, 5, 130],
            '호텔경영학과': ['호경', 60, 1, 5, 42, 0, 5, 130],
            '외식ㆍ조리학과': ['외조', 60, 1, 5, 42, 0, 5, 130],
            '관광이벤트학과': ['관이', 60, 1, 5, 42, 0, 5, 130],
            '연기학과': ['연기', 60, 1, 5, 42, 0, 5, 130],
            '애니메이션학과': ['애니', 60, 6, 0, 42, 6, 0, 130],
            '애니메이션영상학과': ['애영', 60, 6, 0, 42, 6, 0, 130],
            '전자디지털음악학과': [],
            '실용음악학과': [],
            '영상학과': [],
            '언론미디어학과': [],
            '미디어영상': ['미디', 60, 1, 0, 42, 0, 0, 130],
            # 연계/융합전공
            '문화재관리': [],
            '형사사법': [],
            '경제정보': [],
            '심리': [],
            '관광스포츠산업융합전공': ['', 0, 0, 0, 42, 0, 6, 0],
            '동아시아': [],
            '창업융합전공': ['창융', 0, 0, 0, 42, 0, 0, 0],
            '커뮤니티': [],
            '융합데이터': ['융데'],
            '디자인비즈융합전공': ['디융'],
            '도시재생학': []
            }
    elif user_id == '16':
        maj_dict = {
            # 지식정보서비스대학
            '경영정보전공': ['경정', 60, 7, 0, 45, 4, 0, 130],
            '회계세무전공': ['회세', 60, 9, 0, 45, 4, 0, 130],
            '무역학과': ['무역', 60, 8, 0, 45, 5, 0, 130],
            '경영학과': ['경영', 60, 9, 0, 45, 4, 0, 130],
            '법학과': ['법', 60, 1, 5, 42, 0, 5, 136],
            '행정학과': ['행정', 60, 1, 5, 42, 0, 5, 130],
            '경찰행정학과': ['경행', 60, 1, 5, 42, 0, 5, 130],
            '국제관계학과': ['국관', 60, 1, 5, 42, 0, 5, 130],
            '국제산업정보학과': ['국정', 60, 5, 0, 42, 5, 0, 130],
            '지식재산학과': ['지재', 60, 1, 5, 42, 0, 5, 130],
            '교정보호전공': ['교보', 60, 1, 5, 42, 0, 5, 130],
            '사회복지전공': ['사복', 60, 6, 0, 42, 6, 0, 130],
            '청소년전공': ['청년', 60, 4, 0, 42, 4, 0, 130],
            '경제전공': ['경제', 60, 5, 0, 42, 5, 0, 130],
            '응용통계전공': ['응통', 60, 6, 0, 42, 6, 0, 130],
            # 인문대학
            '유아교육과': ['유아', 60, 1, 5, 42, 0, 5, 130],
            '국어국문학과': ['국문', 60, 1, 0, 42, 0, 0, 130],
            '영어영문학과': ['영문', 60, 1, 0, 42, 0, 0, 130],
            '중어중문학과': ['중문', 60, 6, 0, 42, 5, 0, 130], # 전진탐 1, 전필and선필 5
            '사학과': ['사', 60, 1, 5, 42, 0, 5, 130],
            '문헌정보학과': ['문정', 60, 1, 5, 42, 0, 5, 130],
            '문예창작학과': ['문창', 60 ,1, 5, 42, 0, 5, 130],
            '독어독문전공': ['독문', 60, 1, 5, 42, 0, 5, 130],
            '프랑스어문전공': ['프문', 60, 1, 5, 42, 0, 5, 130],
            '일어일문전공': ['일문', 60, 1, 5, 42, 0, 5, 130],
            '러시아어문전공': ['러문', 60, 1, 5, 42, 0, 5, 130],
            # 융합과학대학
            '융합보안학과': ['융보', 60, 1, 0, 42, 0, 0, 130],
            '수학과': ['수', 60, 1, 10, 42, 0, 10, 130],
            '전자물리학과': ['전물', 60, 1, 10, 42, 0, 10, 130],
            '화학과': ['화', 60, 1, 10 ,42, 0, 10, 130],
            '생명과학전공': ['생과', 60, 1, 10, 42, 0, 10, 130],
            '식품생물공학전공': ['식생', 60, 1, 10, 42, 0, 10, 130],
            '컴퓨터공학부': ['컴공', 67, 1, 0, 42, 0, 0, 136],
            # 창의공과대학
            '토목공학과': ['토목', 67, 1, 0, 42, 0, 0, 136],
            '건축공학과': ['건축', 67, 6, 0, 42, 6, 0, 136],
            '도시ㆍ교통공학과': ['도교', 67, 1, 10, 42, 0, 10, 136],
            '신소재공학과': ['산재', 67, 1, 0, 42, 0, 0, 136],
            '환경에너지공학과': ['환에', 67, 1, 10, 42, 0, 10, 136],
            '화학공학과': ['화공', 67, 1, 10, 42, 0, 10, 136],
            '산업경영공학과': ['산경', 67, 1, 10, 42, 0, 10, 136],
            '전자공학과': ['전자', 67, 1, 10, 42, 0, 10, 136],
            '기계시스템공학과': ['기시', 67, 1, 10, 42, 0, 10, 136],
            '건축학과': ['건축', 120, 31, 0, 120, 31, 0, 170],
            # 예술체육대학
            '서양화학과': [''],
            '예술학과': [''],
            '서양화ㆍ미술경영학과': ['서미', 60, 1, 0, 42, 0, 0, 130],
            '서예ㆍ문자예술학과': [''],
            '한국화학과': [''],
            '한국화ㆍ서예학과': ['한서', 60, 1, 0, 42, 0, 0, 130],
            '도예학과': [''],
            '환경조각학과': [''],
            '입체조형학과': ['입체', 60, 1, 0, 42, 0, 0, 130],
            '체육학과': ['체육', 60, 1, 5, 42, 0, 5, 130],
            '시각정보디자인전공': ['시정', 60, 1, 0, 42, 0, 0, 130],
            '산업디자인전공': ['산디', 60, 1, 0, 42, 0, 0, 130],
            '장신구ㆍ금속디자인전공': ['장금', 60, 6, 0, 42, 6, 0, 130],
            '스포츠건강과학전공': ['스건', 60, 1, 0, 42, 0, 0, 130],
            '레저스포츠전공': ['레스', 60, 1, 5, 42, 0, 5, 130],
            '스포츠산업경영전공': ['스산', 60, 1, 0, 42, 0, 0, 130],
            '시큐리티매니지먼트학과': ['시큐', 60, 1, 0, 42, 0, 0, 130],
            # 관광문화대학
            '관광경영학과': ['관경', 60, 1, 5, 42, 0, 5, 130],
            '관광개발학과': ['관개', 60, 1, 5, 42, 0, 5, 130],
            '호텔경영학과': ['호경', 60, 1, 5, 42, 0, 5, 130],
            '외식ㆍ조리학과': ['외조', 60, 1, 5, 42, 0, 5, 130],
            '관광이벤트학과': ['관이', 60, 1, 5, 42, 0, 5, 130],
            '연기학과': ['연기', 60, 1, 5, 42, 0, 5, 130],
            '애니메이션학과': ['애니', 60, 6, 0, 42, 6, 0, 130],
            '애니메이션영상학과': ['애영', 60, 6, 0, 42, 6, 0, 130],
            '전자디지털음악학과': [],
            '실용음악학과': [],
            '영상학과': [],
            '언론미디어학과': [],
            '미디어영상': ['미디', 60, 1, 0, 42, 0, 0, 130],
            # 연계/융합전공
            '문화재관리': [],
            '형사사법': [],
            '경제정보': [],
            '심리': [],
            '관광스포츠산업융합전공': ['', 0, 0, 0, 42, 0, 6, 0],
            '동아시아': [],
            '창업융합전공': ['창융', 0, 0, 0, 42, 0, 0, 0],
            '커뮤니티': ['', 0, 0, 0, 42, 0, 4, 0, 0, 0, 0],
            '융합데이터': ['융데', 0, 0, 0, 42, 0, 4, 0],
            '디자인비즈융합전공': ['디융', 0, 0, 0, 42, 0, 0, 0],
            '도시재생학': []
            }
    elif user_id == '17':
        maj_dict = {
            # 지식정보서비스대학
            '경영정보전공': ['경정', 60, 7, 0, 45, 4, 0, 130],
            '회계세무전공': ['회세', 60, 7, 0, 45, 4, 0, 130],
            '무역학과': ['무역', 60, 8, 0, 45, 5, 0, 130],
            '경영학과': ['경영', 60, 9, 0, 45, 4, 0, 130],
            '법학과': ['법', 60, 1, 5, 42, 0, 5, 136],
            '행정학과': ['행정', 60, 1, 5, 42, 0, 5, 130],
            '경찰행정학과': ['경행', 60, 1, 5, 42, 0, 5, 130],
            '국제관계학과': ['국관', 60, 1, 5, 42, 0, 5, 130],
            '국제산업정보학과': ['국정', 60, 6, 0, 42, 5, 0, 130],
            '지식재산학과': ['지재', 60, 1, 6, 42, 0, 5, 130],
            '교정보호전공': ['교보', 60, 1, 5, 42, 0, 5, 130],
            '사회복지전공': ['사복', 60, 6, 0, 42, 6, 0, 130],
            '청소년전공': ['청년', 60, 4, 0, 42, 4, 0, 130],
            '경제전공': ['경제', 60, 5, 0, 42, 5, 0, 130],
            '응용통계전공': ['응통', 60, 6, 0, 42, 6, 0, 130],
            # 인문대학
            '유아교육과': ['유아', 60, 1, 5, 42, 0, 5, 130],
            '국어국문학과': ['국문', 60, 8, 0, 42, 8, 0, 130],
            '영어영문학과': ['영문', 60, 4, 0, 42, 4, 0, 130],
            '중어중문학과': ['중문', 60, 1, 5, 42, 0, 5, 130],
            '사학과': ['사', 60, 4, 5, 42, 4, 5, 130],
            '문헌정보학과': ['문정', 60, 1, 5, 42, 0, 5, 130],
            '문예창작학과': ['문창', 60 ,1, 5, 42, 0, 5, 130],
            '독어독문전공': ['독문', 60, 1, 5, 42, 0, 5, 130],
            '프랑스어문전공': ['프문', 60, 1, 5, 42, 0, 5, 130],
            '일어일문전공': ['일문', 60, 3, 3, 42, 3, 3, 130],
            '러시아어문전공': ['러문', 60, 6, 7, 42, 6, 7, 130],
            # 융합과학대학
            '융합보안학과': ['융보', 60, 2, 10, 42, 2, 10, 130],
            '수학과': ['수', 60, 1, 10, 42, 8, 10, 130], # 다전공 필수 8과목/24학점
            '전자물리학과': ['전물', 60, 1, 10, 42, 0, 10, 130],
            '화학과': ['화', 60, 1, 10 ,42, 0, 10, 130],
            '생명과학전공': ['생과', 60, 1, 10, 42, 0, 10, 130],
            '식품생물공학전공': ['식생', 60, 1, 10, 42, 0, 10, 130],
            '컴퓨터공학부': ['컴공', 67, 1, 10, 42, 0, 10, 136],
            # 창의공과대학
            '토목공학과': ['토목', 67, 8, 0, 42, 8, 0, 136],
            '건축공학과': ['건축', 67, 5, 0, 42, 5, 0, 136],
            '도시ㆍ교통공학과': ['도교', 67, 1, 10, 42, 0, 10, 136],
            '신소재공학과': ['산재', 67, 9, 0, 42, 9, 0, 136],
            '환경에너지공학과': ['환에', 67, 1, 10, 42, 0, 10, 136],
            '화학공학과': ['화공', 67, 1, 10, 42, 0, 10, 136],
            '산업경영공학과': ['산경', 67, 8, 0, 42, 8, 0, 136],
            '전자공학과': ['전자', 67, 3, 10, 42, 3, 10, 136],
            '기계시스템공학과': ['기시', 67, 1, 12, 42, 0, 12, 136],
            '건축학과': ['건축', 110, 25, 0, 110, 25, 0, 160],
            # 예술체육대학
            '서양화학과': [''],
            '예술학과': [''],
            '서양화ㆍ미술경영학과': ['서미', 60, 1, 0, 42, 0, 0, 130],
            '서예ㆍ문자예술학과': [''],
            '한국화학과': [''],
            '한국화ㆍ서예학과': ['한서', 60, 1, 0, 42, 0, 0, 130],
            '도예학과': [''],
            '환경조각학과': [''],
            '입체조형학과': ['입체', 60, 1, 0, 42, 0, 0, 130],
            '체육학과': ['체육', 60, 1, 5, 42, 0, 5, 130],
            '시각정보디자인전공': ['시정', 60, 1, 0, 42, 0, 0, 130],
            '산업디자인전공': ['산디', 60, 1, 0, 42, 0, 0, 130],
            '장신구ㆍ금속디자인전공': ['장금', 60, 6, 0, 42, 6, 0, 130],
            '스포츠건강과학전공': ['스건', 60, 1, 0, 42, 0, 0, 130],
            '레저스포츠전공': ['레스', 60, 1, 5, 42, 0, 5, 130],
            '스포츠산업경영전공': ['스산', 60, 1, 0, 42, 0, 0, 130],
            '시큐리티매니지먼트학과': ['시큐', 60, 1, 0, 42, 0, 0, 130],
            # 관광문화대학
            '관광경영학과': ['관경', 60, 1, 5, 42, 0, 5, 130],
            '관광개발학과': ['관개', 60, 1, 5, 42, 0, 5, 130],
            '호텔경영학과': ['호경', 60, 1, 5, 42, 0, 5, 130],
            '외식ㆍ조리학과': ['외조', 60, 1, 5, 42, 0, 5, 130],
            '관광이벤트학과': ['관이', 60, 1, 5, 42, 0, 5, 130],
            '연기학과': ['연기', 60, 1, 5, 42, 0, 5, 130],
            '애니메이션학과': ['애니', 60, 5, 0, 42, 5, 0, 130],
            '애니메이션영상학과': ['애영', 60, 5, 0, 42, 5, 0, 130],
            '전자디지털음악학과': [],
            '실용음악학과': [],
            '영상학과': [],
            '언론미디어학과': [],
            '미디어영상': ['미디', 60, 1, 0, 42, 0, 0, 130],
            # 연계/융합전공
            '문화재관리': [],
            '형사사법': [],
            '경제정보': [],
            '심리': [],
            '관광스포츠산업융합전공': ['', 0, 0, 0, 42, 0, 6, 0],
            '동아시아': [],
            '창업융합전공': ['창융', 0, 0, 0, 42, 0, 0, 0],
            '커뮤니티': ['', 0, 0, 0, 42, 0, 4, 0, 0, 0, 0],
            '융합데이터': ['융데', 0, 0, 0, 42, 0, 4, 0],
            '디자인비즈융합전공': ['디융', 0, 0, 0, 42, 0, 0, 0],
            '도시재생학': []
            }
    elif user_id in ['18', '19', '20']:
        maj_dict = {
            # 지식정보서비스대학
            '경영정보전공': ['경정', 60, 7, 0, 45, 4, 0, 130, 2],
            '회계세무전공': ['회세', 60, 6, 0, 45, 4, 0, 130, 2],
            '무역학과': ['무역', 60, 8, 0, 45, 5, 0, 130, 0],
            '경영학과': ['경영', 60, 9, 0, 45, 4, 0, 130, 0],
            '법학과': ['법', 60, 1, 5, 42, 0, 5, 136, 0],
            '행정학과': ['행정', 60, 1, 5, 42, 0, 5, 130, 0],
            '경찰행정학과': ['경행', 60, 1, 5, 42, 0, 5, 130, 0],
            '국제관계학과': ['국관', 60, 1, 5, 42, 0, 5, 130, 0],
            '국제산업정보학과': ['국정', 60, 6, 0, 42, 5, 0, 130, 0],
            '지식재산학과': ['지재', 60, 1, 6, 42, 0, 5, 130, 0],
            '교정보호전공': ['교보', 60, 1, 5, 42, 0, 5, 130, 1],
            '사회복지전공': ['사복', 60, 5, 0, 42, 5, 0, 130, 1],
            '청소년전공': ['청년', 60, 4, 0, 42, 4, 0, 130, 1],
            '경제전공': ['경제', 60, 5, 0, 42, 5, 0, 130, 2],
            '응용통계전공': ['응통', 60, 7, 0, 42, 7, 0, 130, 2],
            # 인문대학
            '유아교육과': ['유아', 60, 1, 5, 42, 0, 5, 130, 0],
            '국어국문학과': ['국문', 60, 8, 0, 42, 8, 0, 130, 0],
            '영어영문학과': ['영문', 60, 4, 0, 42, 4, 0, 130, 0],
            '중어중문학과': ['중문', 60, 1, 5, 42, 0, 5, 130, 0],
            '사학과': ['사', 60, 4, 5, 42, 4, 5, 130, 0],
            '문헌정보학과': ['문정', 60, 1, 5, 42, 0, 5, 130, 0],
            '문예창작학과': ['문창', 60 ,1, 5, 42, 0, 5, 130, 0],
            '독어독문전공': ['독문', 60, 1, 5, 42, 0, 5, 130, 4],
            '프랑스어문전공': ['프문', 60, 1, 5, 42, 0, 5, 130, 4],
            '일어일문전공': ['일문', 60, 3, 3, 42, 3, 3, 130, 4],
            '러시아어문전공': ['러문', 60, 6, 4, 42, 6, 4, 130, 4],
            # 융합과학대학
            '융합보안학과': ['융보'],
            '수학과': ['수', 60, 1, 10, 42, 8, 10, 130, 0], # 다전공 필수 8과목/24학점
            '전자물리학과': ['전물', 60, 1, 10, 42, 0, 10, 130, 0],
            '화학과': ['화', 60, 1, 10 ,42, 0, 10, 130, 0],
            '생명과학전공': ['생과', 60, 1, 10, 42, 0, 10, 130, 0],
            '식품생물공학전공': ['식생', 60, 1, 10, 42, 0, 10, 130, 0],
            '컴퓨터공학부': ['컴공', 67, 1, 10, 42, 0, 10, 136, 0],
            # 창의공과대학
            '토목공학과': ['토목', 67, 8, 0, 42, 8, 0, 136, 0],
            '건축공학과': ['건축', 67, 5, 0, 42, 5, 0, 136, 0],
            '도시ㆍ교통공학과': ['도교', 67, 1, 10, 42, 0, 10, 136, 0],
            '신소재공학과': ['산재', 67, 9, 0, 42, 9, 0, 136, 0],
            '환경에너지공학과': ['환에', 67, 1, 10, 42, 0, 10, 136, 0],
            '화학공학과': ['화공', 67, 1, 10, 42, 0, 10, 136, 0],
            '산업경영공학과': ['산경', 67, 8, 0, 42, 8, 0, 136, 0],
            '전자공학과': ['전자', 67, 3, 10, 42, 3, 10, 136, 0],
            '기계시스템공학과': ['기시', 67, 1, 12, 42, 0, 12, 136, 0],
            '건축학과': ['건축', 110, 25, 0, 110, 25, 0, 160, 0],
            # 예술체육대학
            '서양화학과': [''],
            '예술학과': [''],
            '서양화ㆍ미술경영학과': ['서미', 60, 1, 0, 42, 0, 0, 130, 0],
            '서예ㆍ문자예술학과': [''],
            '한국화학과': [''],
            '한국화ㆍ서예학과': ['한서', 60, 1, 0, 42, 0, 0, 130, 0],
            '도예학과': [''],
            '환경조각학과': [''],
            '입체조형학과': ['입체', 60, 1, 0, 42, 0, 0, 130, 0],
            '체육학과': ['체육', 60, 1, 5, 42, 0, 5, 130, 0],
            '시각정보디자인전공': ['시정', 60, 7, 0, 42, 7, 0, 130, 6],
            '산업디자인전공': ['산디', 60, 1, 0, 42, 0, 0, 130, 6],
            '장신구ㆍ금속디자인전공': ['장금', 60, 7, 0, 42, 7, 0, 130, 6],
            '스포츠건강과학전공': ['스건', 60, 1, 0, 42, 0, 0, 130, 0],
            '레저스포츠전공': ['레스', 60, 1, 5, 42, 0, 5, 130, 0],
            '스포츠산업경영전공': ['스산', 60, 5, 0, 42, 5, 0, 130, 0],
            '시큐리티매니지먼트학과': ['시큐', 60, 1, 0, 42, 0, 0, 130, 0],
            # 관광문화대학
            '관광경영학과': ['관경', 60, 1, 5, 42, 0, 5, 130, 0],
            '관광개발학과': ['관개', 60, 1, 5, 42, 0, 5, 130, 0],
            '호텔경영학과': ['호경', 60, 1, 5, 42, 0, 5, 130, 0],
            '외식ㆍ조리학과': ['외조', 60, 1, 5, 42, 0, 5, 130, 0],
            '관광이벤트학과': ['관이', 60, 1, 5, 42, 0, 5, 130, 0],
            '연기학과': ['연기', 60, 1, 5, 42, 0, 5, 130, 0],
            '애니메이션학과': ['애니', 60, 5, 0, 42, 5, 0, 130, 0],
            '애니메이션영상학과': ['애영', 60, 5, 0, 42, 5, 0, 130, 0],
            '전자디지털음악학과': [],
            '실용음악학과': [],
            '영상학과': [],
            '언론미디어학과': [],
            '미디어영상': ['미디', 60, 1, 0, 42, 0, 0, 130, 0],
            # 연계/융합전공
            '문화재관리': [],
            '형사사법': [],
            '경제정보': [],
            '심리': [],
            '관광스포츠산업융합전공': ['', 0, 0, 0, 42, 0, 6, 0, 0],
            '동아시아': [],
            '창업융합전공': ['창융', 0, 0, 0, 42, 0, 0, 0, 0],
            '커뮤니티': ['', 0, 0, 0, 42, 0, 4, 0, 0, 0, 0],
            '융합데이터': ['융데', 0, 0, 0, 42, 2, 2, 0, 0],
            '디자인비즈융합전공': ['디융', 0, 0, 0, 42, 0, 0, 0, 0],
            '도시재생학': []
            }

    return maj_dict