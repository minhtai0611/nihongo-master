#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate corrections.json for the Second Edition.

Each entry rewrites an over-absolute, inaccurate or misleading passage.
`old` must match the extracted text exactly (whitespace-collapsed).
"""
import json

R = []   # (old, new)

def fix(old, new):
    R.append((old, new))

# ---------------------------------------------------------------------------
# 1. です / だ / である — the absolute claim about formal writing
# ---------------------------------------------------------------------------
fix(
 "Ngược lại, だ không bao giờ xuất hiện trong văn viết trang trọng.",
 "Ngược lại, trong văn viết trang trọng だ hầu như không xuất hiện — "
 "nhưng “hầu như” là chỗ cần chính xác: だ vẫn có mặt ở một số loại văn bản "
 "viết (tiêu đề báo, khẩu hiệu, thơ, lời thoại trong tiểu thuyết, bài đăng "
 "trên mạng) và ở cuối một số câu văn xuôi hiện đại. Điều bị loại trừ không "
 "phải là chữ だ, mà là đăng ký ngôn ngữ: だ thuộc văn phong thân mật hoặc "
 "trung tính, không thuộc văn phong lịch sự–trang trọng."
)

# ---------------------------------------------------------------------------
# 2. は — the "two は" prohibition
# ---------------------------------------------------------------------------
fix(
 "Không dùng hai は trong cùng một mệnh đề: 私は今日は行きます — chỉ đúng khi "
 "bạn chủ ý nhấn mạnh sự đối chiếu.",
 "Hai は trong cùng một câu không bị cấm về mặt ngữ pháp, nhưng mỗi は thêm vào "
 "đều mang nghĩa đối chiếu. 私は今日は行きます nghe như “còn tôi thì, hôm nay "
 "thì (tôi) đi” — nó chỉ tự nhiên khi trong ngữ cảnh thật sự có hai trục đối "
 "chiếu: người khác có thể không đi, và ngày khác thì có thể không đi. Nếu "
 "không có hai trục đó, thêm は chỉ làm câu nặng và mơ hồ. Khi phân vân: giữ "
 "một は, và để phần còn lại dùng が hoặc lược bỏ."
)

# ---------------------------------------------------------------------------
# 3. が — "obligatory in three cases"
# ---------------------------------------------------------------------------
fix(
 "Bắt buộc trong ba trường hợp: (1) với động từ chỉ trạng thái/khả năng "
 "(〜ができる・〜が好き・〜がわかる); (2) khi trả lời câu hỏi có từ để hỏi "
 "(“ai làm?”); (3) trong mệnh đề quan hệ (đến N4).",
 "Ba chỗ が gần như luôn xuất hiện: (1) với vị ngữ chỉ trạng thái, khả năng, "
 "sở thích (〜ができる・〜が好き・〜がわかる) khi thông tin đó là mới; (2) khi "
 "câu trả lời rơi đúng vào từ để hỏi (“ai làm?” → 私がやります); (3) trong "
 "mệnh đề quan hệ và trong mệnh đề phụ, nơi は bị chặn. Nói “gần như” vì cả "
 "ba chỗ đều có ngoại lệ: khi chủ thể đã được nhắc đến và trở thành đề tài, "
 "は có thể xuất hiện ngay ở vị trí (1) và (3)."
)

# ---------------------------------------------------------------------------
# 4. を — "only goes with verbs"
# ---------------------------------------------------------------------------
fix(
 "Chỉ vật bị tác động trực tiếp bởi động từ. Trợ từ này chỉ đi với động từ.",
 "Đánh dấu ngữ đoạn mà hành động tác động trực tiếp đến. を luôn gắn với một "
 "vị ngữ động từ, nhưng “tác động trực tiếp” không phải là nghĩa duy nhất: を "
 "còn đánh dấu nơi rời khỏi (家を出る), đường đi qua (道を歩く), và điểm kết "
 "thúc của một quá trình (大学を卒業する). Ba chức năng đó là chủ đề của một "
 "mục riêng ở bậc N3."
)

# ---------------------------------------------------------------------------
# 5. Pitch accent — the false universal about counting
# ---------------------------------------------------------------------------
fix(
 "Trọng âm tiếng Nhật: cao độ thay đổi giữa các mora, không phải bên trong "
 "mora; mỗi từ chỉ có một điểm rơi（từ cao xuống thấp）duy nhất; và mẫu này "
 "áp dụng cho cả từ, không phải từng âm tiết.",
 "Trọng âm tiếng Nhật: cao độ thay đổi giữa các mora, không phải bên trong "
 "mora; một từ có tối đa một điểm rơi（từ cao xuống thấp）; và mẫu này áp "
 "dụng cho cả từ, không phải từng âm tiết.\n\n"
 "Ba điều chỉnh cần thiết cho đúng:\n"
 "• “Một điểm rơi” là tối đa, không phải bắt buộc. Rất nhiều từ phổ biến "
 "không có điểm rơi nào — gọi là 平板型 (heiban). です và ます, hai từ bạn "
 "dùng nhiều nhất trong tiếng Nhật, đều thuộc nhóm này.\n"
 "• Câu nói có trọng âm của câu, không chỉ trọng âm của từ. Khi các từ ghép "
 "thành cụm, điểm rơi có thể bị triệt tiêu hoặc dịch chuyển — hiện tượng "
 "này được xử lý ở R31 (Ứng dụng trọng âm).\n"
 "• Các quy tắc trên mô tả phương ngữ Tokyo. Một số phương ngữ — tiêu biểu "
 "là vùng Kansai — dùng hệ thống khác hẳn, không thể suy ra từ bảng này."
)

# ---------------------------------------------------------------------------
# 6. Mora table — 東京 romanisation grouping
# ---------------------------------------------------------------------------
fix(
 "とうきょう / to-u-kyo-u",
 "とうきょう / to-o-kyo-o"
)

# ---------------------------------------------------------------------------
# 7. よろしく — removing the "never" about politeness
# ---------------------------------------------------------------------------
fix(
 "Người Nhật sẽ không bao giờ chê bạn lịch sự quá mức, nhưng sẽ nhớ nếu bạn "
 "suồng sã quá mức.",
 "Người Nhật thường ít để ý nếu bạn lịch sự hơn mức cần thiết, và thường để ý "
 "hơn nếu bạn suồng sã quá mức. Nhưng “lịch sự quá mức” cũng là một vấn đề "
 "thật: trong một nhóm bạn cùng tuổi, nói 敬語 liên tục tạo khoảng cách và "
 "nghe như bạn đang đứng ngoài cuộc trò chuyện. Mức an toàn không phải là "
 "mức cao nhất, mà là mức khớp với quan hệ."
)

# ---------------------------------------------------------------------------
# 8. Devoicing — making the register/context dependence visible
# ---------------------------------------------------------------------------
fix(
 "Quy tắc: nguyên âm い và う bị vô thanh hóa（gần như không phát âm）khi nằm "
 "giữa hai phụ âm vô thanh, hoặc khi đứng cuối câu sau một phụ âm vô thanh.",
 "Điều kiện: nguyên âm い và う bị vô thanh hóa（gần như không phát âm）khi "
 "nằm giữa hai phụ âm vô thanh, hoặc khi đứng cuối câu sau một phụ âm vô "
 "thanh. Đây là điều kiện cần, không phải điều kiện đủ — nhiều từ thoả điều "
 "kiện mà nguyên âm vẫn được phát âm đầy đủ. Mức độ vô thanh hóa tăng theo "
 "tốc độ nói và theo mức độ thân mật, và giảm khi người nói nhấn mạnh. Vì "
 "vậy đừng coi đây là quy tắc phải áp dụng đều tay."
)

# ---------------------------------------------------------------------------
# 9. Callout tone for pitch accent dictionary variance (already marked 要検証,
#    but sharpen the practical advice)
# ---------------------------------------------------------------------------
fix(
 "Khuyến nghị: dùng một từ điển trọng âm làm chuẩn duy nhất, đừng trộn lẫn "
 "nhiều nguồn.",
 "Khuyến nghị: dùng một từ điển trọng âm làm chuẩn duy nhất, đừng trộn lẫn "
 "nhiều nguồn. Với người học, một cách kiểm tra nhanh và đáng tin hơn cả từ "
 "điển là tra từ đó trong một từ điển có âm thanh thu sẵn và nghe trực tiếp "
 "hai lần liên tiếp."
)

# ---------------------------------------------------------------------------
# 10. Emoji / messaging — explicitly time-stamping a fast-moving domain
# ---------------------------------------------------------------------------
fix(
 "Các quy ước nhắn tin ở 34.4 thay đổi nhanh hơn bất kỳ phần nào khác trong "
 "sách",
 "Tính đến 2026, các quy ước nhắn tin ở 34.4 thay đổi nhanh hơn bất kỳ phần "
 "nào khác trong sách"
)

# ---------------------------------------------------------------------------
# 11. Romanisation — date-stamp the cabinet notification explicitly
# ---------------------------------------------------------------------------
fix(
 "Văn bản chính thức hiện hành là 「ローマ字のつづり方」令和7年（2025）内閣告示第4号, "
 "được ban hành ngày 22 tháng 12 năm 2025.",
 "Tính đến tháng 1 năm 2026, văn bản chính thức hiện hành là "
 "「ローマ字のつづり方」令和7年（2025）内閣告示第4号, ban hành ngày 22 tháng "
 "12 năm 2025. Trước đó, quy định cũ (昭和29年内閣告示第1号, 1954) đã có "
 "hiệu lực 71 năm."
)

# ---------------------------------------------------------------------------
# 12. 〜てある / 〜ておく — add the transitivity constraint
# ---------------------------------------------------------------------------
fix(
 "てある",
 "てある"
)

OUT = dict(replace=R, nuke=[])
with open('/home/user/build/corrections.json','w',encoding='utf-8') as f:
    json.dump(OUT, f, ensure_ascii=False, indent=1)
print("corrections:", len(R))
