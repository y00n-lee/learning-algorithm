def solution(genres, plays):
    answer = []
    music_dict = {}
    genre_cnt = {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        music_dict[idx] = (genre, play)

        if genre_cnt.get(genre):
            genre_cnt[genre] += play

        else:
            genre_cnt[genre] = play

    genre_cnt = {v: k for k, v in genre_cnt.items()}
    # music_dict = {:() for i, (g, p) in music_dict.items()}

    max_gcnt = list(genre_cnt.keys())
    max_gcnt.sort(reverse=True)

    # 많이 재생된 장르 순으로 반복
    for m in max_gcnt:
        genre = genre_cnt.get(m)  # 많이 재생된 장르 이름
        # 장르별로 곡 모으기
        g_play = {i: p for i, (g, p) in music_dict.items() if g == genre}
        # 장르별 2곡씩 수록, 1곡만 있으면 하나만 수록
        n = 2 if len(g_play.values()) > 1 else 1

        for _ in range(n):
            max_play = max(g_play.values())
            for idx, play in g_play.items():
                # max_play = max(g_play.values())
                if max_play == play:
                    answer.append(idx)
                    g_play[idx] = -1
                    break

    return answer