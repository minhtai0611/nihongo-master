# -*- coding: utf-8 -*-
"""New reference sections R46-R69 for the Second Edition.

Written as flowable-emitting generators. Every externally checkable claim is
tagged with one of the six confidence levels used throughout the book:
  公式 / 研究知見 / 使用実態 / 一般的な教育上の説明 / 編集上の整理 / 要検証
"""
from reportlab.platypus import Paragraph, Spacer, PageBreak, NextPageTemplate, CondPageBreak
import theme as T
from theme import guard
import blocks as B

def P(t, s='body', base='Body'):
    if s == 'dek': s = 'lead'          # theme key for the same style
    return Paragraph(guard(t, base), T.ST[s])
def H2(t):
    return B.SectionHead(t)
def H3(t):
    return Paragraph(guard(t, 'BodyB'), T.ST['h3'])
def H4(t):
    return Paragraph(guard(t, 'SansB'), T.ST['h4'])
def CALL(label, body, tone='indigo'):
    return [B.Callout(label, body, tone=tone), Spacer(1, 8)]
def VF(label, body):
    return [B.Verify(label, body), Spacer(1, 8)]
def EX(ja, ro, vi, note=''):
    return [B.Example(ja, ro, vi, note), Spacer(1, 4)]
def TB(cap, hdr, rows, colw=None):
    out = []
    if cap: out.append(Paragraph(guard(cap, 'SansB'), T.ST['tblcap']))
    out.append(B.make_table(hdr, rows, colw)); out.append(Spacer(1, 10))
    return out

SOURCES_CHECKED = ('Nguồn đã tra: 文化審議会答申「敬語の指針」(2007) · '
                   '文化審議会国語分科会「日本語教育の参照枠」報告 (2021) · '
                   '文化審議会建議「公用文作成の考え方」(2022) · JLPT 公式 (jlpt.jp) · '
                   '国立国語研究所 BCCWJ・CSJ（公開仕様の範囲）')

# ===========================================================================
def r46_romanization():
    """R46 — Romanisation master reference."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R46 — La-tinh hoá: bản tra cứu tổng hợp ／ ローマ字表記の総合リファレンス'))
    F.append(P('Bản tổng hợp và bản cập nhật của R17 và R20. Đọc R17 để tra bảng '
               'chính thức; đọc R20 để biết quy ước mà cuốn sách này dùng. Phần '
               'dưới đây là những gì hai mục kia chưa nói rõ.', 'dek'))
    F.append(H3('46.1 Ba tầng khác nhau — đừng gộp chúng lại'))
    F.append(P('Phần lớn nhầm lẫn về romaji đến từ việc gộp ba thứ khác nhau vào một. '
               'Ba tầng này độc lập với nhau:'))
    F += TB('BẢNG R46.1 — BA TẦNG', ['Tầng', 'Trả lời câu hỏi', 'Do đâu quy định'],
            [['Chính tả Nhật', 'Từ này viết bằng chữ gì?', 'Chính sách ngôn ngữ: 常用漢字表, 現代仮名遣い'],
             ['La-tinh hoá', 'Chữ Nhật đó chuyển sang chữ Latinh thế nào?', '「ローマ字のつづり方」(2025)'],
             ['Phát âm', 'Từ này thực sự nghe ra sao?', 'Ngữ âm học; không văn bản hành chính nào quy định']],
            colw=[22, 40, 38])
    F.append(P('Một câu như <b>学校へ行きます</b> có ba mô tả độc lập: chính tả là '
               '<b>学校へ行きます</b> (<i>gakkō e ikimasu</i> với へ viết へ nhưng '
               'đọc <i>e</i>); la-tinh hoá theo Hepburn là <i>gakkō e ikimasu</i>; '
               'phát âm thực tế có thể là [ɡakkoː e ikimḁsɯ̥] với い và う bị vô '
               'thanh hoá. Ba tầng, ba câu chuyện. Văn bản 2025 quy định tầng thứ '
               'hai và <b>không nói gì</b> về tầng thứ ba.'))
    F.append(H3('46.2 Những chỗ cáo thị 2025 hay bị hiểu sai'))
    F += TB('BẢNG R46.2 — BỐN HIỂU NHẦM THƯỜNG GẶP',
            ['Hiểu nhầm', 'Thực tế'],
            [['“Từ 2025 phải viết Tōkyō, Tokyo là sai”',
              'Cáo thị nói rõ ở 添え書き⑧: những cách viết đã ăn sâu vào thực tế '
              'không bị đòi thay ngay. <b>Tokyo</b> vẫn hợp lệ.'],
             ['“Tên tôi phải đổi theo chuẩn mới”',
              '添え書き⑨: tên riêng của cá nhân được viết theo ý muốn của chính '
              'người đó. Sato · Satoh · Satou · Satō đều hợp lệ.'],
             ['“Gõ tiếng Nhật trên máy tính cũng phải đổi”',
              'Việc nhập liệu bằng bàn phím là lĩnh vực riêng, không thuộc phạm vi '
              'cáo thị. <i>ti · tu · hu · sya</i> vẫn gõ được bình thường.'],
             ['“Cáo thị quy định cả trọng âm”',
              'Không. Văn bản này thuần tuý quy định cách viết（つづり方）. Toàn bộ '
              'phần âm thanh nằm ngoài phạm vi của nó.']],
            colw=[32, 68])
    F += CALL('TÌNH TRẠNG ÁP DỤNG ／ 適用の現状',
              'Mức độ mà các cơ quan (đường sắt, chính quyền địa phương, nhà xuất '
              'bản, trường học) thực sự chuyển sang bảng mới là điều <b>chưa được '
              'kiểm chứng độc lập</b>. Bộ Giáo dục đã công bố sẽ cập nhật phần giải '
              'thích chương trình học (学習指導要領解説) cho môn Quốc ngữ và Ngoại '
              'ngữ ở tiểu học, nhưng lộ trình thực tế cần theo dõi thêm.', tone='gold')
    F.append(P('Mức: 公式 cho nội dung cáo thị · <b>要検証</b> cho mức độ áp dụng '
               'trong thực tế. ' + SOURCES_CHECKED, 'caption'))
    F.append(NextPageTemplate('body'))
    return F

# ===========================================================================
def r47_pronunciation():
    """R47 — Pronunciation master reference."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R47 — Phát âm: bản tra cứu tổng hợp ／ 発音の総合リファレンス'))
    F.append(P('Bản tổng hợp của R18 (phát âm) và các mục 2.1–2.5 ở N5. Phần bổ '
               'sung ở đây là những điểm mà hai mục kia để ở dạng quy tắc, trong '
               'khi thực tế chúng là khuynh hướng có điều kiện.', 'dek'))
    F.append(H3('47.1 Bốn tầng phân tích — giữ chúng tách biệt'))
    F += TB('BẢNG R47.1 — BỐN TẦNG', ['Tầng', 'Ví dụ', 'Ghi chú'],
            [['Âm vị', '/u/ là một âm vị', 'Cấp trừu tượng; người nói không ý thức về nó'],
             ['Thực hiện ngữ âm', '[ɯ] môi không tròn, [u] môi tròn', 'Biến thiên theo ngữ cảnh và người nói'],
             ['Trọng âm từ', 'あめ ⓪ vs あめ ①', 'Thuộc về từ vựng; phải học cùng từ'],
             ['Ngữ điệu câu', 'そうですか↑ vs そうですか↓', 'Thuộc về câu; thay đổi theo ý định']],
            colw=[20, 34, 46])
    F.append(P('Rất nhiều lời khuyên phát âm sai vì trộn hai tầng: người dạy nói '
               '“/u/ tiếng Nhật không tròn môi” — trong khi thực tế <b>âm vị</b> /u/ '
               'được <b>thực hiện</b> với độ tròn môi khác nhau tuỳ vị trí. Trước '
               'phụ âm vô thanh và ở cuối từ, môi thường không tròn; sau /s/ và '
               'trong thế đứng nhấn mạnh, môi tròn rõ hơn.'))
    F.append(H3('47.2 Vô thanh hoá — điều kiện cần và mức độ'))
    F.append(P('Điều kiện thường được dạy: nguyên âm hẹp (い, う) giữa hai phụ âm '
               'vô thanh, hoặc sau phụ âm vô thanh ở cuối từ. Nhưng tỉ lệ thực '
               'hiện thay đổi theo:'))
    F += TB('BẢNG R47.2 — BỐN YẾU TỐ ĐIỀU CHỈNH',
            ['Yếu tố', 'Xu hướng'],
            [['Tốc độ nói', 'Nói nhanh → vô thanh hoá nhiều hơn'],
             ['Độ trang trọng / mức nhấn mạnh', 'Nhấn mạnh → phát âm đầy đủ hơn, ít vô thanh hoá'],
             ['Phương ngữ', 'Vùng Kansai nhìn chung ít vô thanh hoá hơn chuẩn Tokyo'],
             ['Từ cụ thể', 'Một số từ “đông cứng” ở một dạng — học theo từ, không theo quy tắc']],
            colw=[30, 70])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Các tỉ lệ cụ thể cho từng yếu tố ở bảng trên phản ánh mô tả phổ biến '
            'trong tài liệu ngữ âm học tiếng Nhật, nhưng cuốn sách này chưa đối '
            'chiếu với một nghiên cứu định lượng cụ thể nào. Hãy đọc bảng như '
            'hướng khuynh hướng, không phải số liệu. ' + SOURCES_CHECKED)
    F.append(H3('47.3 Điều người học Việt Nam thường nghe sai'))
    F.append(P('Ba nhầm lẫn dưới đây không phải lỗi phát âm của người Việt — chúng '
               'là hệ quả của việc hệ thống âm tiết tiếng Việt không có những đối '
               'lập mà tiếng Nhật dùng:'))
    F += TB('BẢNG R47.3 — BA NHẦM LẪN PHỔ BIẾN',
            ['Hiện tượng', 'Người Việt nghe ra', 'Vì sao'],
            [['Độ dài nguyên âm', 'Không phân biệt おばさん / おばあさん',
              'Tiếng Việt không dùng độ dài để phân biệt nghĩa từ'],
             ['う môi không tròn', 'u hoặc ư, không ổn định',
              'Tiếng Việt có đối lập u / ư; tiếng Nhật chỉ có một âm vị'],
             ['ん cuối từ [ɴ]', '“n” chạm lưỡi',
              'Tiếng Việt không có âm mũi lưỡi-gà cuối từ']],
            colw=[24, 30, 46])
    F.append(P('Mức: 研究知見 cho các mô tả ngữ âm; 編集上の整理 cho cách phân loại '
               'theo ba nhầm lẫn. ' + SOURCES_CHECKED, 'caption'))
    return F

# ===========================================================================
def r51_pragmatics():
    """R51 — Pragmatics (new)."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R51 — Dụng học ／ 語用論'))
    F.append(P('Những gì câu nói làm được mà từ ngữ không nói ra — và cách phân '
               'tích chúng như hiện tượng ngôn ngữ, không như tính cách dân tộc.', 'dek'))
    F += CALL('NGUYÊN TẮC ĐỌC PHẦN NÀY ／ この章の読み方',
              'Dụng học nghiên cứu quan hệ giữa <b>câu chữ</b> và <b>điều người nói '
              'định làm</b> với người nghe. Các khái niệm dưới đây được xây dựng để '
              'mô tả <b>mọi</b> ngôn ngữ, không riêng tiếng Nhật. Tiếng Nhật có cách '
              'hiện thực hoá riêng cho từng khái niệm — đó mới là phần thú vị. '
              'Tuyệt đối tránh lối viết “người Nhật làm X vì văn hoá Nhật Bản”: '
              'mọi hiện tượng ở đây đều có biến thiên theo vùng, tuổi, giới, '
              'nghề nghiệp và quan hệ cá nhân.', tone='teal')

    F.append(H3('51.1 Nghĩa của câu không nằm hết trong câu'))
    F.append(P('Câu <b>寒いですね</b> có nghĩa từ vựng là “lạnh nhỉ”. Nhưng tuỳ '
               'hoàn cảnh, cùng câu đó có thể là: (1) một nhận xét vô hại; (2) một '
               'lời đề nghị đóng cửa sổ; (3) một lời mở đầu cuộc trò chuyện trước '
               'khi vào việc; (4) một lời đề nghị người kia khoác áo. Không có gì '
               'trong câu chữ mang bốn nghĩa đó. Chúng được suy ra từ ngữ cảnh.'))
    F.append(P('Đây không phải chuyện riêng của tiếng Nhật. Câu “Trời lạnh nhỉ” '
               'trong tiếng Việt, ở đúng tình huống, cũng làm được đúng bốn việc '
               'trên. Điều khác nhau nằm ở <b>tần suất</b> và ở <b>hình thức</b> '
               'ngữ pháp mà tiếng Nhật cung cấp để làm những việc đó.'))

    F.append(H3('51.2 Chỉ xuất ／ 直示 (deixis)'))
    F.append(P('Từ chỉ xuất là từ mà nghĩa của nó phụ thuộc vào ai nói, ở đâu, lúc '
               'nào. Tiếng Nhật có ba hệ thống chồng lên nhau:'))
    F += TB('BẢNG R51.1 — BA HỆ THỐNG CHỈ XUẤT',
            ['Hệ', 'Gần người nói', 'Gần người nghe', 'Xa cả hai'],
            [['Chỗ chốn', 'ここ', 'そこ', 'あそこ'],
             ['Vật', 'これ', 'それ', 'あれ'],
             ['Hướng', 'こちら', 'そちら', 'あちら'],
             ['Động từ', '来る (về phía người nói)', '行く (rời khỏi người nói)', '—']],
            colw=[18, 28, 28, 26])
    F.append(P('Chỗ khó với người Việt: đối lập 行く / 来る bị chi phối bởi người '
               'nói, không bởi đích đến. Khi nói qua điện thoại, người Nhật chọn '
               '来る hay 行く theo quan điểm của <b>người nói</b>, kể cả khi người '
               'nói đang di chuyển. Đây là lỗi rất bền trong người học Việt Nam '
               'vì tiếng Việt “đến” và “đi” được chọn theo hướng địa lý nhiều hơn.'))
    F += EX('もしもし、今そっちに行くから、待ってて。',
            'moshi moshi, ima sotchi ni iku kara, mattete.',
            'Alô, giờ tôi đang đi sang chỗ anh, đợi nhé.',
            'Người nói đang di chuyển về phía người nghe. Tiếng Nhật vẫn dùng 行く '
            'vì hành động là rời khỏi người nói. Nếu người nghe ở nơi người nói '
            'sắp đến, nhiều ngôn ngữ chọn “đến”. Đây là điểm chọn bất đối xứng.')

    F.append(H3('51.3 Hàm ý hội thoại ／ 会話の含意 (implicature)'))
    F.append(P('Người nói thường có ý nhiều hơn điều mình nói, và người nghe khôi '
               'phục ý đó bằng suy luận. Một nguồn suy luận quan trọng là: giả định '
               'rằng người nói đang <b>hợp tác</b> — nói thật, đủ, đúng chỗ, rõ '
               'ràng. Khi một phát ngôn lệch khỏi giả định đó, người nghe mặc nhiên '
               'tìm một cách hiểu khiến nó trở nên hợp lý.'))
    F.append(P('Ví dụ kinh điển: câu hỏi “Anh A có học giỏi không?” được trả lời '
               '“Anh ấy chơi thể thao tốt.” Câu trả lời không hợp tác về mặt trực '
               'tiếp — và chính chỗ không hợp tác đó mang ý “không giỏi lắm”.'))
    F += EX('A：この店、安いですか。\nB：まあ、料理はおいしいですけどね。',
            'A: kono mise, yasui desu ka. / B: mā, ryōri wa oishii desu kedo ne.',
            'A: Quán này rẻ không? / B: Ừ thì… món ăn ngon.',
            'B không trả lời câu hỏi. Thay vào đó B đưa một đặc điểm khác rồi để '
            'lửng bằng けどね. Người nghe khôi phục được ý “không rẻ”. Đây là hàm ý, '
            'không phải quy ước cố định — nếu quán đúng là rẻ và ngon, けど vẫn '
            'có thể chỉ là cách nói mềm.')
    F.append(H4('Một ranh giới quan trọng'))
    F.append(P('Hàm ý hội thoại <b>có thể bị huỷ</b>. Nếu B nói tiếp: “Nhưng mà rẻ '
               'thật đấy”, cả hàm ý “không rẻ” lẫn hàm ý “rẻ” đều có thể đứng vững '
               'vì câu sau có thể điều chỉnh câu trước. Đây là lý do vì sao mô tả '
               '<b>ちょっと…</b> như một “mật mã từ chối” là sai về nguyên tắc: mã '
               'thì không thể bị huỷ, hàm ý thì có. Xem R54 để có danh sách các '
               'cách nói hay bị đóng khung thành mật mã.'))
    F.append(P('Mức: 一般的な教育上の説明 cho ba khái niệm chỉ xuất, hàm ý, hành vi '
               'lời nói — đây là nội dung nhập môn chuẩn của ngôn ngữ học. ' +
               '編集上の整理 cho cách tổ chức phần này. ' + SOURCES_CHECKED, 'caption'))
    return F

# ---------------------------------------------------------------------------
def _r51_cont():
    F = []
    F.append(H3('51.4 Hành vi lời nói ／ 発話行為 (speech acts)'))
    F.append(P('Một phát ngôn vừa <b>nói ra điều gì</b>, vừa <b>làm một việc gì</b>. '
               '“Ở đây lạnh quá” nói ra một nhận xét, đồng thời có thể làm việc '
               '“đề nghị đóng cửa sổ”. Câu hỏi “Anh có muốn uống gì không?” có '
               'hình thức nghi vấn nhưng chức năng là mời.'))
    F.append(P('Với người học, điều này có hệ quả thực tế: khi tra một mẫu câu, cần '
               'hỏi thêm <b>mẫu đó làm được việc gì</b>, không chỉ <b>nghĩa là gì</b>. '
               'Bảng dưới đây là ví dụ về cùng một hình thức phục vụ nhiều hành vi.'))
    F += TB('BẢNG R51.2 — MỘT HÌNH THỨC, NHIỀU HÀNH VI',
            ['Câu', 'Có thể là', 'Phụ thuộc vào'],
            [['〜ませんか', 'Lời mời · lời đề nghị · lời rủ',
              'Ai nói với ai, và ai được lợi từ hành động'],
             ['〜ましょうか', 'Lời tự nguyện giúp · lời đề nghị cùng làm · lời hỏi ý',
              'Động từ theo sau và quan hệ ngôi'],
             ['〜ていただけませんか', 'Yêu cầu lịch sự · lời mời rất trang trọng',
              'Việc đó có lợi cho người nói hay người nghe'],
             ['〜たほうがいいです', 'Khuyên · cảnh báo · phê bình nhẹ',
              'Mức độ nghiêm trọng của việc và ngữ điệu']],
            colw=[26, 38, 36])
    F.append(H3('51.5 Lịch sự, thể diện và sự giảm nhẹ'))
    F.append(P('Cách giải thích có ảnh hưởng rộng nhất trong ngôn ngữ học về lịch sự '
               'dựa trên khái niệm <b>thể diện (face)</b>: hình ảnh công khai mà '
               'mỗi người muốn giữ. Có hai mặt: thể diện <b>tiêu cực</b> (muốn tự do, '
               'không bị áp đặt) và thể diện <b>tích cực</b> (muốn được chấp nhận, '
               'được thích). Phần lớn chiến lược lịch sự là cách xử lý hai mặt này.'))
    F += TB('BẢNG R51.3 — CHIẾN LƯỢC VÀ DẤU HIỆU TRONG TIẾNG NHẬT',
            ['Chiến lược', 'Bảo vệ thể diện', 'Dấu hiệu trong tiếng Nhật'],
            [['Nói thẳng không giảm nhẹ', '—', '〜してください（mệnh lệnh lịch sự tối thiểu）'],
             ['Giảm nhẹ bằng từ đệm', 'Tiêu cực', 'すみませんが・恐れ入りますが・ちょっと'],
             ['Hỏi thay vì yêu cầu', 'Tiêu cực', '〜ていただけますか・〜ませんか'],
             ['Để người nghe quyết định', 'Tiêu cực', '〜というのはいかがでしょうか・ご都合はいかがですか'],
             ['Đồng cảm, chia sẻ khó khăn', 'Tích cực', 'お忙しいところ恐れ入りますが・わざわざ'],
             ['Xin lỗi trước khi nhờ', 'Cả hai', '突然のご連絡で申し訳ありませんが']],
            colw=[24, 18, 58])
    F.append(P('Điểm cần nói rõ: <b>giảm nhẹ (mitigation)</b> là một hiện tượng ngôn '
               'ngữ phổ quát, không phải nét riêng tiếng Nhật. Tiếng Việt cũng giảm '
               'nhẹ, nhưng thường đặt ở vị trí khác trong câu và dùng phương tiện '
               'khác (từ tình thái cuối câu, hư từ, thay đổi ngôi). Vì vậy lời '
               'khuyên “cứ dịch thẳng từ tiếng Việt sang” hiếm khi cho ra câu tiếng '
               'Nhật tự nhiên — cần dịch cả <b>chiến lược</b>, không chỉ nội dung.'))
    F.append(H3('51.6 Sự im lặng, sửa lỗi, và lượt nói'))
    F.append(P('Hội thoại là một hoạt động phối hợp. Ba hiện tượng dưới đây thường '
               'bị giải thích như “nét văn hoá Nhật Bản”, trong khi chúng là cơ chế '
               'hội thoại chung, có tham số khác nhau giữa các ngôn ngữ.'))
    F += TB('BẢNG R51.4 — BA CƠ CHẾ HỘI THOẠI',
            ['Cơ chế', 'Là gì', 'Tham biến có thể khác giữa các ngôn ngữ'],
            [['あいづち / backchannel',
              'Tín hiệu ngắn cho biết vẫn đang nghe, không nhằm giành lượt',
              'Tần suất, độ dài, chỗ đặt — và việc nó có bị coi là chen ngang hay không'],
             ['Đến lượt / turn-taking',
              'Cách hai người chia nhau quyền nói',
              'Độ dài khoảng lặng được coi là “bình thường”; mức chồng tiếng được chấp nhận'],
             ['Tự sửa / self-repair',
              'Người nói sửa lại chính mình giữa câu',
              'Dạng từ đánh dấu sửa (いや・あ、そうじゃなくて), chỗ đặt']],
            colw=[20, 40, 40])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Mô tả về あいづち trong tiếng Nhật thường được dẫn lại với con số tần '
            'suất cụ thể. Cuốn sách này <b>không</b> đưa con số nào, vì chưa đối '
            'chiếu trực tiếp với một nghiên cứu định lượng cụ thể. Nếu bạn cần số '
            'liệu, hãy tìm trong các nghiên cứu dùng 日本語話し言葉コーパス (CSJ) '
            'hoặc 名大会話コーパス. ' + SOURCES_CHECKED)
    F.append(H3('51.7 Cách một người Nhật “từ chối” — và vì sao mô tả cũ sai'))
    F.append(P('Cách trình bày phổ biến trong nhiều sách là: “người Nhật không bao '
               'giờ nói いいえ; họ luôn từ chối gián tiếp”. Cách trình bày đó sai ở '
               'hai chỗ. Thứ nhất, người Nhật <b>có</b> nói いいえ, 無理です, '
               'できません — tuỳ quan hệ và tuỳ mức độ nghiêm trọng. Thứ hai, việc '
               'từ chối gián tiếp phụ thuộc vào <b>quyền lực và mức độ áp đặt</b>, '
               'không phụ thuộc vào quốc tịch.'))
    F.append(P('Cách mô tả chính xác hơn: trong một lời từ chối, người nói thường '
               'phải cân bằng hai áp lực ngược nhau — muốn rõ ràng, và muốn không '
               'làm người kia mất thể diện. Tiếng Nhật cung cấp nhiều công cụ để '
               'nghiêng về phía thứ hai hơn so với tiếng Việt trong cùng hoàn cảnh, '
               'đặc biệt khi người nghe ở vị thế cao hơn.'))
    F += TB('BẢNG R51.5 — THANG TỪ CHỐI (từ rõ nhất đến gián tiếp nhất)',
            ['Mức', 'Ví dụ', 'Người nghe hiểu là', 'Rủi ro'],
            [['1 — Rõ ràng', 'できません。／ 無理です。', 'Từ chối dứt khoát', 'Có thể bị coi là lạnh'],
             ['2 — Rõ + lý do', 'その日は予定があって行けません。', 'Từ chối, có lý do cụ thể', 'Thấp'],
             ['3 — Rõ + xin lỗi + thay thế', '申し訳ありませんが、別の日はいかがですか。', 'Từ chối nhưng vẫn giữ cửa mở', 'Thấp'],
             ['4 — Kèm do dự', 'うーん、ちょっと難しいですね。', 'Không nhận', 'Người nghe phải tự suy ra'],
             ['5 — Lửng', 'その日は少し…', 'Không nhận', 'Có thể bị hỏi lại'],
             ['6 — Đổi chủ đề', '（không phản hồi trực tiếp）', 'Có thể là không nhận, cũng có thể là chưa quyết', 'Rủi ro hiểu sai cao nhất']],
            colw=[16, 30, 30, 24])
    F.append(P('Ghi chú thực hành: với người học ở trình độ trung cấp trở lên, mức 2 '
               'và 3 là <b>an toàn và tự nhiên</b> trong phần lớn tình huống công '
               'việc. Mức 4–6 đòi hỏi kinh nghiệm đọc ngữ cảnh; dùng sai mức 6 có '
               'thể bị hiểu là bạn đang phớt lờ.'))
    F.append(P('Mức: 研究知見 cho khung thể diện–lịch sự; 使用実態 cho thang từ chối; '
               '編集上の整理 cho cách sắp thang. ' + SOURCES_CHECKED, 'caption'))
    return F

# ===========================================================================
def r53_final_particles():
    """R53 — Sentence-final particles."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R53 — Trợ từ cuối câu: hệ thống điều chỉnh quan hệ ／ 終助詞の体系'))
    F.append(P('Trợ từ cuối câu không thêm thông tin về sự việc. Chúng điều chỉnh '
               'quan hệ giữa người nói, người nghe và điều đang được nói.', 'dek'))
    F.append(P('Nếu は và が tổ chức <b>thông tin</b> trong câu, thì trợ từ cuối câu '
               'tổ chức <b>quan hệ</b> giữa người nói và người nghe. Chúng không '
               'phải “gia vị” tuỳ ý: bỏ đi thì câu vẫn đúng ngữ pháp nhưng đổi '
               'nghĩa xã hội. Đây là một trong những hệ thống khó nhất của tiếng '
               'Nhật, vì người học phải chọn đồng thời: nội dung, mức lịch sự, '
               'giới, tuổi, vùng, và mức độ thân mật.'))
    F.append(H3('53.1 ね và よ — hai cực cơ bản'))
    F += TB('BẢNG R53.1 — ね vs よ', ['Tiêu chí', 'ね', 'よ'],
            [['Giả định về người nghe', 'Người nghe đã biết / sẽ đồng ý', 'Người nghe chưa biết'],
             ['Hướng thông tin', 'Chia sẻ, xác nhận', 'Cung cấp, thông báo'],
             ['Nếu dùng sai', 'Nghe như đang kiểm tra người nghe', 'Nghe như đang lên lớp người nghe'],
             ['Mức lịch sự', 'Trung tính đến lịch sự', 'Trung tính; với người trên cần cẩn thận']],
            colw=[24, 38, 38])
    F += EX('今日は寒いですね。', 'kyō wa samui desu ne.', 'Hôm nay lạnh nhỉ.',
            'ね giả định người nghe cũng cảm nhận được. Dùng với người mới gặp cũng '
            'được — nó tạo sự đồng cảm.')
    F += EX('今日は寒いですよ。', 'kyō wa samui desu yo.', 'Hôm nay lạnh đấy.',
            'よ cung cấp thông tin mà người nói cho là người nghe chưa biết. Với '
            'người trên, よ có thể nghe như đang nhắc nhở — nên nhiều người thêm '
            'một lớp đệm.')
    F.append(H3('53.2 よね — kết hợp chứ không phải cộng nghĩa'))
    F.append(P('よね không đơn thuần là よ rồi ね. Nó nói: “tôi đưa ra thông tin '
               'này (よ), và tôi cho rằng bạn sẽ đồng ý (ね)”. Nó hữu dụng khi '
               'người nói khá chắc nhưng vẫn muốn giữ cửa cho người nghe phản hồi.'))
    F += EX('この店、安いですよね。', 'kono mise, yasui desu yo ne.',
            'Quán này rẻ mà, phải không?',
            'Khác với 安いですね (tôi và bạn cùng nhận ra) và 安いですよ (tôi nói '
            'cho bạn biết). よね = tôi nói + tôi nghĩ bạn đồng ý.')
    F.append(H3('53.3 Các trợ từ còn lại — theo chức năng, không theo danh sách'))
    F += TB('BẢNG R53.2 — SÁU NHÓM CHỨC NĂNG', ['Chức năng', 'Trợ từ', 'Ghi chú'],
            [['Xác nhận / đồng cảm', 'ね・な・ねえ', 'な thân mật hơn; な với người trên dễ bị coi là suồng sã'],
             ['Thông báo / nhấn', 'よ・ぜ・ぞ', 'ぜ・ぞ rất thân mật và mang màu nam tính trong nhiều tài liệu'],
             ['Hỏi / không chắc', 'か・かな・かしら・っけ', 'っけ dùng khi cố nhớ lại điều từng biết'],
             ['Nhượng bộ / chấp nhận', 'か・さ', 'さ trong まあいいさ nghe như chấp nhận có phần bất đắc dĩ'],
             ['Tự nói với mình', 'な・なあ・か', 'Không nhắm vào người nghe'],
             ['Truyền đạt sắc thái', 'わ・の・のよ', 'Phân bố theo giới và thế hệ rất khác nhau']],
            colw=[24, 34, 42])
    F += CALL('VỀ “NGÔN NGỮ NAM / NỮ” ／ 男女の言葉遣いについて',
              'Bảng trên cố ý dùng “mang màu nam tính <i>trong nhiều tài liệu</i>” '
              'chứ không nói “chỉ đàn ông dùng”. Nghiên cứu ngôn ngữ học xã hội '
              'Nhật Bản cho thấy đây là <b>khuynh hướng thống kê gắn với chuẩn mực '
              'xã hội</b>, không phải quy tắc ngữ pháp, và mức độ khác biệt thay '
              'đổi mạnh theo vùng, tuổi, nghề nghiệp và bối cảnh. Trợ từ nhận diện '
              'là “nữ tính” hiện đang thu hẹp ở người trẻ. Với người học nước '
              'ngoài, lời khuyên thực tế vẫn là giữ mức trung tính và lịch sự vừa '
              'đủ; xem thêm mục 8.2 ở N2.', tone='teal')
    F.append(H3('53.4 Ràng buộc tổ hợp — chỗ dễ sai nhất'))
    F.append(P('Trợ từ cuối câu không kết hợp tự do. Các ràng buộc sau là những gì '
               'người học hay vi phạm:'))
    F += TB('BẢNG R53.3 — NĂM RÀNG BUỘC', ['Ràng buộc', 'Ví dụ'],
            [['Không lặp cùng một trợ từ', '× ですよよ → ですよ'],
             ['ね đứng sau よ được; よ đứng sau ね thì rất hạn chế', '○ ですよね · △ ですねよ'],
             ['Trợ từ mạnh (ぞ・ぜ) không đi với です・ます trong lời nói bình thường', '× ですぞ（trừ văn nghệ thuật / nhân vật）'],
             ['っけ chỉ đi với quá khứ hoặc trạng thái đã biết', '○ 何時だったっけ · × 何時だっけ（khi chưa từng biết）'],
             ['か đi với です・ます bình thường', '○ そうですか。']],
            colw=[42, 58])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Ràng buộc thứ hai và thứ tư ở bảng trên được mô tả theo cách giải thích '
            'phổ biến trong ngữ pháp tiếng Nhật, nhưng ranh giới giữa “chấp nhận '
            'được” và “không chấp nhận được” có biến thiên theo vùng và thế hệ, và '
            'chưa được kiểm tra trên một corpus cụ thể trong quá trình biên soạn. '
            'Đừng dùng bảng này như danh sách cấm tuyệt đối. ' + SOURCES_CHECKED)
    F.append(P('Mức: 一般的な教育上の説明 cho phân loại chức năng; 使用実態 cho các '
               'ví dụ; 要検証 cho chi tiết ràng buộc tổ hợp.', 'caption'))
    return F

# ===========================================================================
def r65_vn_contrast():
    """R65 — Vietnamese-Japanese contrastive reference."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R65 — Đối chiếu Việt–Nhật ／ ベトナム語と日本語の対照'))
    F.append(P('Những khác biệt có hệ thống giữa hai ngôn ngữ, và — quan trọng '
               'không kém — những chỗ khác biệt bị phóng đại.', 'dek'))
    F += CALL('VÌ SAO PHẦN NÀY TỒN TẠI ／ この章の目的',
              'Khi người học mắc lỗi, cách giải thích hấp dẫn nhất là “vì tiếng mẹ '
              'đẻ của tôi khác”. Cách giải thích đó đúng một phần, và bị lạm dụng '
              'phần còn lại: rất nhiều lỗi của người học Việt Nam là lỗi chung của '
              '<b>mọi</b> người học tiếng Nhật. Phần này phân biệt hai loại. Những '
              'chỗ có nghiên cứu hỗ trợ được ghi rõ; những chỗ là suy luận của '
              'người biên soạn cũng được ghi rõ.', tone='gold')
    F.append(H3('65.1 Bảng đối chiếu loại hình'))
    F += TB('BẢNG R65.1 — ĐỐI CHIẾU CẤU TRÚC',
            ['Bình diện', 'Tiếng Việt', 'Tiếng Nhật', 'Hệ quả cho người học'],
            [['Loại hình', 'Đơn lập, mỗi âm tiết một hình vị',
              'Chắp dính, hình vị nối vào gốc',
              'Không thể “dịch từng chữ” — phải dịch theo cấu trúc'],
             ['Trật tự cơ bản', 'S–V–O', 'S–O–V', 'Động từ phải dời về cuối'],
             ['Nối ngữ pháp', 'Hư từ đứng trước danh từ (của, cho, ở)',
              'Trợ từ đứng sau ngữ đoạn', 'Phải học vị trí mới, không chỉ học nghĩa'],
             ['Ngữ âm', 'Thanh điệu, cao độ trong âm tiết',
              'Trọng âm cao thấp, cao độ giữa các mora',
              'Thói quen cao độ bên trong âm tiết gây “giọng Việt”'],
             ['Độ dài', 'Không phân biệt nghĩa bằng độ dài',
              'Độ dài phân biệt nghĩa (おばさん/おばあさん)',
              'Phải luyện nghe phân biệt trước khi luyện nói'],
             ['Chủ ngữ', 'Thường phải có (tôi, nó, họ), trừ khi lược bỏ có điều kiện',
              'Thường lược bỏ khi đã rõ hoặc liên tục về đề tài',
              'Lỗi thêm 私は quá nhiều — đây là lỗi thật và phổ biến'],
             ['Đại từ nhân xưng', 'Hệ thống phong phú, có hư từ kính ngữ',
              'Không có đại từ trung tính — chọn từ theo quan hệ',
              '“Tôi” không phải một từ; phải chọn từ theo hoàn cảnh']],
            colw=[16, 26, 28, 30])
    F.append(H3('65.2 Ba khác biệt có nghiên cứu hỗ trợ'))
    F.append(P('Ba điểm dưới đây được nhiều nghiên cứu về người học Việt Nam ghi '
               'nhận và thường được nhắc lại trong tài liệu giảng dạy. Chúng được '
               'xếp ở đây ở mức <b>研究知見</b> với giới hạn: phần lớn nghiên cứu '
               'là nghiên cứu nhỏ, trên một nhóm người học cụ thể.'))
    F += TB('BẢNG R65.2 — BA ĐIỂM CÓ HỖ TRỢ NGHIÊN CỨU',
            ['Hiện tượng', 'Mô tả', 'Hướng xử lý'],
            [['Cảm nhận độ dài (長音・促音)',
              'Khó phân biệt các cặp tối thiểu như おじさん/おじいさん, きて/きって, '
              'và khả năng này không tự động cải thiện theo thời gian học',
              'Luyện nghe phân biệt trên cặp tối thiểu trước, không qua chữ viết; '
              'kiểm tra định kỳ thay vì tin vào thời gian'],
             ['Vô thanh hoá 「す」',
              'Người học cần thời gian dài để nhận thức rồi mới phát âm được; '
              'nhận thức trước, kỹ năng sau',
              'Chấp nhận lộ trình tính bằng tháng; đừng lấy việc “nghe ra” làm '
              'thước đo “nói được”'],
             ['Nhịp điệu (mora)',
              'Nhịp câu bị ảnh hưởng bởi cách đếm đơn vị của tiếng mẹ đẻ',
              'Luyện gõ nhịp; kiểm tra độ dài tương đối giữa các mora bằng cách đọc to']],
            colw=[22, 44, 34])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Nghiên cứu của Đỗ Hoàng Ngân (2015, khảo sát 533 sinh viên chuyên ngữ '
            'tiếng Nhật tại bốn trường đại học Việt Nam về khả năng cảm nhận 長音・促音) '
            'được cuốn sách này <b>dẫn lại qua nguồn thứ cấp</b>, chưa tiếp cận bản '
            'gốc. Kết luận “khả năng cảm nhận không cải thiện theo thời gian học” '
            'cần được kiểm chứng trên luận văn gốc trước khi dùng làm căn cứ. ' +
            SOURCES_CHECKED)
    F.append(H3('65.3 Ba khác biệt bị phóng đại'))
    F.append(P('Ba điều dưới đây hay được nêu như “khác biệt Việt–Nhật” nhưng thực '
               'tế không đặc thù cho cặp ngôn ngữ này:'))
    F += TB('BẢNG R65.3 — BA KHÁC BIỆT BỊ PHÓNG ĐẠI',
            ['Cách nói phổ biến', 'Vấn đề'],
            [['“Tiếng Việt có thanh điệu nên người Việt khó học trọng âm Nhật”',
              'Đúng là có ảnh hưởng, nhưng khó khăn này gặp ở <b>mọi</b> người học, '
              'kể cả người nói ngôn ngữ không thanh điệu. Thanh điệu làm thay đổi '
              '<b>dạng</b> lỗi, không quyết định <b>mức</b> lỗi.'],
             ['“Người Việt thêm 私は vì tiếng Việt luôn cần chủ ngữ”',
              'Thêm chủ ngữ quá mức là lỗi phổ biến ở người học thuộc nhiều ngôn '
              'ngữ khác nhau, kể cả tiếng Anh. Nguyên nhân chính là cách dạy ở giai '
              'đoạn đầu (mọi mẫu câu đều có 私は), không phải cấu trúc tiếng Việt.'],
             ['“Trợ từ tiếng Nhật tương đương giới từ tiếng Việt”',
              'Tương đương về chức năng nối, không tương đương về vị trí, về khả '
              'năng lược bỏ, hay về việc một trợ từ làm nhiều việc. に không phải '
              '“ở/đến/cho” — nó là một trợ từ có một tập chức năng riêng.']],
            colw=[34, 66])
    F.append(H3('65.4 Lượng từ và cách đếm'))
    F.append(P('Tiếng Việt dùng “con, cái, chiếc, quyển, tờ…” đứng trước danh từ. '
               'Tiếng Nhật dùng 助数詞 đứng sau số. Về mặt chức năng hai hệ thống '
               'tương tự nhau, nhưng cách phân loại khác nhau, và tiếng Nhật bắt '
               'buộc phải chọn lượng từ khi đếm — không có cách nói trung tính.'))
    F += TB('BẢNG R65.4 — SO SÁNH CÁCH PHÂN LOẠI',
            ['Danh từ', 'Tiếng Việt', 'Tiếng Nhật', 'Ghi chú'],
            [['Người', 'người, vị, ông/bà', '人（にん）・名（めい）', '名 trang trọng hơn'],
             ['Vật nhỏ, tròn', 'cái, viên, hạt', '個（こ）', '個 bao trùm rộng hơn “cái”'],
             ['Vật dài mảnh', 'cây, thanh, ống', '本（ほん）', 'áo, bút, chai, phim…'],
             ['Giấy, vật mỏng', 'tờ, tấm, lá', '枚（まい）', 'áo sơ mi cũng dùng 枚'],
             ['Sách, quyển', 'quyển, cuốn', '冊（さつ）', '—'],
             ['Máy móc, xe', 'chiếc, cái', '台（だい）', 'Xe đạp, ô tô, máy tính'],
             ['Động vật nhỏ', 'con', '匹（ひき）', 'Chó, mèo, cá, côn trùng'],
             ['Động vật lớn', 'con', '頭（とう）', 'Voi, bò, ngựa'],
             ['Lần', 'lần, lượt', '回（かい）・度（ど）', '度 trang trọng hơn']],
            colw=[18, 24, 24, 34])
    F.append(P('Điểm khó nhất không phải là nhớ danh sách, mà là chỗ <b>hai hệ '
               'thống cắt nghĩa khác nhau</b>. “Chiếc” trong tiếng Việt có thể là '
               '台, 本, 枚 tuỳ vật. Vì vậy đừng học theo bảng dịch — hãy học lượng '
               'từ cùng với danh từ, như học giống của danh từ trong tiếng Pháp.'))
    F.append(P('Mức: 研究知見 cho bảng 65.2 (có giới hạn nêu rõ) · 編集上の整理 '
               'cho cách phân loại ba nhóm ở 65.3 · 一般的な教育上の説明 cho bảng '
               'lượng từ. ' + SOURCES_CHECKED, 'caption'))
    return F

# ===========================================================================
def r54_literal_actual():
    """R54 — Literal vs actual meaning."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R54 — Nghĩa đen và nghĩa thực ／ 字義と実際の意味'))
    F.append(P('Mười cách nói mà nghĩa bạn học trong từ điển không phải nghĩa bạn '
               'gặp ngoài đời — nhưng cũng không phải một “mật mã” bí ẩn.', 'dek'))
    F += CALL('CẢNH BÁO PHƯƠNG PHÁP ／ 方法上の注意',
              'Cách trình bày phổ biến — “người Nhật nói A nhưng thật ra nghĩ B” — '
              'gây hại theo hai hướng. Nó khiến người học thấy mọi câu nói đều có '
              'nghĩa ẩn, và nó biến một hiện tượng dụng học phổ quát thành bí mật '
              'dân tộc. Cách trình bày đúng: mỗi cách nói dưới đây có một <b>nghĩa '
              'từ vựng</b> và một <b>tập hợp các hành vi lời nói</b> mà nó thường '
              'thực hiện. Việc nó đang làm hành vi nào phụ thuộc vào ngữ cảnh — và '
              'ngữ cảnh có thể làm nó trở về nghĩa đen.', tone='gold')
    F.append(H3('54.1 すみません — sáu việc, một từ'))
    F += TB('BẢNG R54.1 — すみません LÀM ĐƯỢC GÌ', ['Ngữ cảnh', 'Nó làm việc gì', 'Nghĩa tiếng Việt gần nhất'],
            [['Va vào ai trong tàu', 'Xin lỗi', 'Xin lỗi'],
             ['Gọi phục vụ trong quán', 'Thu hút sự chú ý', 'Cho tôi hỏi / anh ơi'],
             ['Ai đó giúp mình', 'Cảm ơn (kèm chút áy náy)', 'Cảm ơn anh nhiều'],
             ['Từ chối một lời nhờ', 'Xin lỗi vì không giúp được', 'Xin lỗi, tôi…'],
             ['Nghe không rõ', 'Xin nhắc lại', 'Anh nói lại giúp'],
             ['Cảm thấy áy náy vì làm phiền', 'Thừa nhận đã gây phiền', 'Ngại quá']],
            colw=[26, 34, 40])
    F.append(P('Nhận xét quan trọng: すみません có một <b>lõi nghĩa</b> khá rõ — thừa '
               'nhận rằng mình đang gây ra một phiền nhỏ, hoặc rằng quan hệ đang có '
               'một độ lệch. Cả sáu cách dùng trên đều quy về lõi đó. Vì vậy nó '
               'không phải “mật mã”: nó là một từ có phạm vi dùng rộng, theo một '
               'lô-gíc nhất quán.'))
    F.append(H3('54.2 大丈夫です và 結構です — hai vùng nguy hiểm'))
    F.append(P('Đây là hai cách nói mà <b>cùng một câu trả lời</b> có thể mang hai '
               'ý trái ngược, và người nói tiếng Nhật bản ngữ cũng nhận thấy sự '
               'mơ hồ này.'))
    F += TB('BẢNG R54.2 — HAI CÁCH NÓI MƠ HỒ',
            ['Cách nói', 'Có thể là ĐỒNG Ý', 'Có thể là TỪ CHỐI', 'Dấu hiệu phân biệt'],
            [['大丈夫です', '“Vâng, được, không sao”', '“Không cần đâu, tôi ổn rồi”',
              'Ngữ điệu và câu trước đó; nếu là để đáp lời đề nghị giúp, khả năng '
              'từ chối cao hơn'],
             ['結構です', 'Ít gặp ở nghĩa đồng ý trong hội thoại hiện đại', '“Không cần đâu ạ”',
              '結構です hiện nay nghiêng mạnh về từ chối; 結構いいですね mới là khen'],
             ['いいです', '“Được đấy, tốt”', '“Thôi, không cần”',
              'Ngữ điệu; nếu có もう trước thì gần như chắc là từ chối']],
            colw=[16, 24, 26, 34])
    F += EX('A：お茶、もう一杯いかがですか。\nB：あ、大丈夫です。',
            'A: ocha, mō ippai ikaga desu ka. / B: a, daijōbu desu.',
            'A: Anh dùng thêm tách trà nữa không? / B: À, không cần đâu ạ.',
            'Đây là cách dùng rất phổ biến của 大丈夫です với nghĩa từ chối. Nếu '
            'người học tưởng đây là “vâng”, cuộc đối thoại sẽ lệch. Nhưng lưu ý: '
            'trong ngữ cảnh khác — ai đó hỏi 具合は大丈夫ですか — 大丈夫です lại '
            'đúng là “vâng, ổn”.')
    F += CALL('CÁCH AN TOÀN NHẤT ／ 最も安全な言い方',
              'Nếu bạn muốn chắc chắn không gây nhầm lẫn, tránh dùng 大丈夫です và '
              '結構です một mình để trả lời đề nghị. Nói rõ: <b>いただきます。ありがとうございます。</b> '
              '(nhận) hoặc <b>ありがとうございます。でも、もう十分です。</b> (từ chối). '
              'Người bản ngữ vẫn dùng hai từ kia thường xuyên; bạn sẽ dùng được sau '
              'khi đã nghe nhiều trong ngữ cảnh thật.', tone='teal')
    F.append(H3('54.3 ちょっと… — giảm nhẹ, không phải từ chối'))
    F.append(P('ちょっと nghĩa đen là “một chút”. Khi đứng trước một khoảng lặng, nó '
               'làm việc <b>giảm nhẹ</b>: báo hiệu rằng điều sắp nói (hoặc không nói) '
               'là khó nói. Nó thường dẫn tới một từ chối, nhưng không phải lúc nào.'))
    F += TB('BẢNG R54.3 — ちょっと THEO NGỮ CẢNH', ['Câu', 'Nghĩa', 'Nó đang làm gì'],
            [['ちょっと待ってください。', 'Đợi một chút.', 'Nghĩa đen — không có hàm ý'],
             ['ちょっと難しいですね。', 'Hơi khó nhỉ.', 'Phản đối ở mức nhẹ — nghĩa đen vẫn còn'],
             ['それはちょっと…', 'Cái đó thì hơi…', 'Giảm nhẹ; người nghe tự suy ra từ chối'],
             ['ちょっと無理です。', 'Hơi không được ạ.', 'Từ chối có giảm nhẹ, nhưng vẫn rõ'],
             ['A：明日、来られますか。B：明日はちょっと…', 'A: Mai anh đến được không? B: Mai thì hơi…',
              'Từ chối; ちょっと thay cho phần lý do không nói ra']],
            colw=[30, 24, 46])
    F.append(P('Đây là lý do vì sao ちょっと… <b>không nên</b> được dạy như “cách nói '
               'không”. Nếu bạn dịch nó là “không” trong mọi trường hợp, bạn sẽ bỏ '
               'mất khả năng nghe ra sự khác nhau giữa một lời phàn nàn nhẹ '
               '(ちょっと高いですね) và một lời từ chối. Và bạn sẽ mắc lỗi ngược: '
               'coi mọi ちょっと là từ chối.'))
    F.append(H3('54.4 Bốn cách nói công việc — và giới hạn của chúng'))
    F += TB('BẢNG R54.4 — BỐN CỤM TRONG CÔNG VIỆC',
            ['Cụm', 'Nghĩa đen', 'Thường được hiểu là', 'Giới hạn'],
            [['検討します', 'sẽ xem xét', '“Tôi chưa quyết; có thể là không”',
              'Trong nhiều công ty <b>không</b> được dùng như lời hứa. Nhưng ở một '
              'số nơi nó vẫn đúng là “tôi sẽ xem xét”. Đây là chỗ phải học theo '
              'văn hoá <b>tổ chức</b>, không theo quốc tịch.'],
             ['前向きに検討します', 'sẽ xem xét theo hướng tích cực', 'Thường là “chưa chắc”',
              'Không có nghĩa “sắp đồng ý”. Nhưng cũng không phải từ chối.'],
             ['よろしくお願いします', 'mong được đối xử tốt', 'Tuỳ hoàn cảnh: chào hỏi, '
              'nhờ vả, kết thúc email, cảm ơn trước…',
              'Không phải một câu có nghĩa cố định. Nghĩa của nó là <b>quan hệ</b>: '
              '“tôi đặt việc này vào tay anh/chị”.'],
             ['お疲れ様です', 'anh/chị đã mệt rồi', 'Chào khi gặp, chào khi về, cảm ơn, xác nhận',
              'Dùng trong công việc và với người ngang hàng hoặc dưới. Tránh dùng với '
              'người trên ở một số môi trường; お疲れ様でした khi kết thúc.']],
            colw=[18, 20, 28, 34])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Mức độ “thật” của 検討します và 前向きに検討します thay đổi rất mạnh '
            'theo ngành, công ty, thế hệ và theo tình huống là giao dịch giữa công '
            'ty với công ty hay giữa người với người. Cuốn sách này không đưa ra '
            'kết luận chung nào. ' + SOURCES_CHECKED)
    F.append(P('Mức: 使用実態 cho tập hành vi của すみません · 編集上の整理 cho bảng '
               '54.2 và 54.4 · 要検証 cho 54.4.', 'caption'))
    return F

# ===========================================================================
def r67_source_hierarchy():
    """R67 — Source hierarchy."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R67 — Phân cấp nguồn ／ 情報源の階層'))
    F.append(P('Cuốn sách này dựa vào đâu, và vì sao thứ tự đó quan trọng.', 'dek'))
    F.append(P('Khi hai nguồn nói khác nhau về tiếng Nhật, câu hỏi không phải là '
               '“nguồn nào nổi tiếng hơn”, mà là “nguồn nào có thẩm quyền cho loại '
               'câu hỏi này”. Một cuốn từ điển có thẩm quyền về cách đọc một từ; nó '
               'không có thẩm quyền về việc người ta thực sự nói gì trong một cuộc '
               'họp. Bảng dưới đây là thứ tự ưu tiên mà cuốn sách này dùng.'))
    F += TB('BẢNG R67.1 — BỐN TẦNG NGUỒN',
            ['Tầng', 'Loại', 'Ví dụ', 'Có thẩm quyền về'],
            [['1', 'Văn bản chính thức của Nhật Bản',
              '「敬語の指針」(2007) · 常用漢字表 (2010) · 「公用文作成の考え方」(2022) · '
              '「ローマ字のつづり方」(2025) · 「日本語教育の参照枠」(2021) · JLPT 公式',
              'Quy định, chuẩn mực, hệ thống phân loại, cấu trúc kỳ thi'],
             ['2', 'Corpus và nguồn nghiên cứu quốc gia',
              'BCCWJ · CSJ · CEJC · I-JAS · Chunagon (国立国語研究所)',
              'Tần suất, cách dùng thực tế, văn nói vs văn viết'],
             ['3', 'Nghiên cứu học thuật',
              'J-STAGE · CiNii Research · tạp chí ngôn ngữ học và giáo dục tiếng Nhật',
              'Kết luận chuyên ngành, có giới hạn và điều kiện áp dụng'],
             ['4', 'Giáo trình chuẩn (nguồn so sánh)',
              'みんなの日本語 · げんき · 新完全マスター · 日本語総まとめ v.v.',
              'Trình tự sư phạm, cách giải thích, phạm vi kiến thức của một bậc']],
            colw=[6, 20, 40, 34])
    F += CALL('NGUYÊN TẮC KHÔNG SAO CHÉP ／ 参照の原則',
              'Các giáo trình ở tầng 4 được dùng để <b>so sánh</b> phạm vi, trình tự '
              'và cách giải thích. Cuốn sách này không sao chép nội dung của bất kỳ '
              'giáo trình nào. Toàn bộ cách diễn đạt trong sách là của người biên '
              'soạn, tổng hợp lại từ các nguồn ở tầng 1–3.', tone='indigo')
    F.append(H3('67.1 Bảng quyết định: câu hỏi nào cần nguồn nào'))
    F += TB('BẢNG R67.2 — TRA CỨU THEO LOẠI CÂU HỎI',
            ['Bạn muốn biết', 'Tra ở tầng', 'Vì sao không dùng tầng khác'],
            [['Chữ này có trong 常用漢字 không?', '1',
              'Chỉ 常用漢字表 có thẩm quyền; giáo trình chỉ đưa danh sách ước lệ'],
             ['Người ta có thực sự nói thế này không?', '2',
              'Quan sát cá nhân và giáo trình không đo được tần suất'],
             ['Phân biệt は và が thế nào?', '3 rồi 1',
              'Đây là câu hỏi nghiên cứu đang tiếp diễn, không có văn bản chính thức nào quy định'],
             ['Nên học gì trước ở N4?', '4',
              'Đây là quyết định sư phạm, không phải sự kiện ngôn ngữ'],
             ['Cách viết romaji nào là chuẩn?', '1',
              'Có cáo thị nội các; không cần suy đoán'],
             ['Từ này có 連濁 không?', 'Từ điển',
              '連濁 không đoán được quy tắc (xem R21) — phải tra'],
             ['Mẫu này thuộc N3 hay N2?', '—',
              'JLPT không công bố danh mục. Mọi cách xếp bậc đều là ước lệ của '
              'người biên soạn']],
            colw=[32, 12, 56])
    F.append(H3('67.2 Sáu mức độ tin cậy'))
    F.append(P('Ngoài phân cấp nguồn, mỗi khẳng định trong sách được gắn một mức. '
               'Xem phần “Cách đọc sổ này” ở R68 để có định nghĩa đầy đủ. Điểm cần '
               'nhấn mạnh: ba mức đầu khác nhau về <b>bản chất</b>, không chỉ về độ '
               'chắc chắn. Một điều được dùng rất phổ biến (使用実態) vẫn không vì '
               'thế mà trở thành quy tắc chính thức (公式).'))
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Bản thân cách phân bốn tầng này là <b>xếp đặt biên soạn</b>, không phải '
            'một chuẩn mực quốc tế. Các tổ chức khác có thể phân tầng khác. Nó hữu '
            'ích vì nó bắt buộc phải nói rõ mỗi khẳng định dựa vào loại chứng cứ nào. ' +
            SOURCES_CHECKED)
    F.append(P('Mức: 編集上の整理 cho toàn bộ phần này.', 'caption'))
    return F

# ===========================================================================
def r49_spoken():
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R49 — Tiếng Nhật nói: rút gọn và biến đổi ／ 話し言葉の縮約と変容'))
    F.append(P('Bản tổng hợp và mở rộng của N3 Ch.6. Quy tắc chung: cái bị cắt là '
               'phần <b>có thể khôi phục</b> mà không mất thông tin.', 'dek'))
    F.append(P('Dạng rút gọn không phải tiếng Nhật “sai” hay “lười”. Chúng là dạng '
               'chuẩn của văn nói thân mật, có quy tắc, và người học nghe không ra '
               'chúng thì sẽ mất phần lớn hội thoại tự nhiên. Nhưng chúng cũng '
               '<b>không</b> dùng được ở mọi nơi — xem cột cuối ở bảng dưới.'))
    F += TB('BẢNG R49.1 — MƯỜI RÚT GỌN PHỔ BIẾN',
            ['Dạng đầy đủ', 'Dạng nói', 'Ví dụ', 'Không dùng ở'],
            [['〜ている', '〜てる', '食べてる', 'Văn viết trang trọng'],
             ['〜ておく', '〜とく', '買っとく', 'Văn viết, dịch vụ khách hàng'],
             ['〜ておいて', '〜といて', '見といて', 'Như trên'],
             ['〜てしまう', '〜ちゃう', '忘れちゃった', 'Văn viết, phát ngôn chính thức'],
             ['〜では', '〜じゃ', 'じゃない', 'Văn viết trang trọng'],
             ['〜という', '〜って', '田中さんって知ってる？', 'Văn viết trang trọng'],
             ['〜の', '〜ん', '行くんですか', '—（nhưng ん rất thân mật）'],
             ['ら行音の脱落', '〜って / 〜た', '分かんない ← 分からない', 'Văn viết'],
             ['〜なければ', '〜なきゃ', '行かなきゃ', 'Trang trọng; nhưng rất thông dụng trong nói'],
             ['〜なくては', '〜なくちゃ', '急がなくちゃ', 'Trang trọng']],
            colw=[18, 16, 30, 36])
    F += CALL('PHÂN BIỆT RÚT GỌN VÀ VĂN NÓI THÔ ／ 縮約と俗語の違い',
              'Rút gọn là biến đổi <b>âm</b>, giữ nguyên từ và nghĩa. Văn nói thô '
              'là chọn <b>từ</b> khác. 食べてる và 食べている khác nhau về âm; '
              '食う và 食べる khác nhau về từ và về đăng ký. Hai hiện tượng cần '
              'học riêng, đừng gộp.', tone='teal')
    F.append(H3('49.2 Từ đệm, do dự và sửa lỗi'))
    F += TB('BẢNG R49.2 — BA NHÓM TÍN HIỆU',
            ['Nhóm', 'Dạng', 'Chức năng'],
            [['Đệm lấy thời gian', 'ええと・あの・その・まあ・なんか',
              'Giữ lượt nói trong khi người nói đang tìm từ'],
             ['Sửa lỗi', 'いや・あ、ちがう・そうじゃなくて・というか',
              'Báo hiệu phần vừa nói sẽ được thay'],
             ['Tự nói với mình', 'なんだっけ・あれ・〜かな',
              'Không nhắm vào người nghe; người nghe có thể tham gia hoặc không']],
            colw=[22, 40, 38])
    F.append(P('Với người học Việt Nam: dùng đệm quá nhiều nghe lúng túng; dùng '
               'quá ít nghe như đang đọc. Cách luyện thực tế là ghi âm chính mình '
               'và so với một đoạn hội thoại thật cùng độ dài.'))
    F.append(H3('49.4 Khi bạn nghe không ra — ba bước xử lý tại chỗ'))
    F.append(P('Đây không phải bài luyện tập, mà là ba bước dùng được ngay trong lúc '
               'đang hội thoại. Chúng dựa trên nguyên tắc: người nghe có quyền yêu cầu '
               'sửa, và trong tiếng Nhật, yêu cầu sửa có mẫu câu lịch sự riêng.'))
    F += TB('BẢNG R49.4 — BA BƯỚC',
            ['Bước', 'Khi nào', 'Cách nói'],
            [['1. Xác nhận lại bằng cách nói lại điều mình vừa hiểu',
              'Nghe được nhưng không chắc', '〜ということですね。／ つまり、〜ですか。'],
             ['2. Xin nói lại một phần, không xin nói lại cả câu',
              'Mất một từ hoặc một con số', 'すみません、もう一度お願いできますか。'
              '／ 〜のところをもう一度お願いします。'],
             ['3. Chuyển kênh', 'Không thể nghe rõ bằng lời',
              '書いていただけますか。／ チャットで送っていただけますか。']],
            colw=[30, 26, 44])
    F.append(P('Điều đáng lưu ý về nghi thức: xin nói lại là chuyện bình thường trong '
               'công việc, kể cả với người bản ngữ. Cái bị đánh giá không phải là việc '
               'hỏi lại, mà là việc <b>gật đầu cho qua rồi làm sai</b>. Mẫu 3 là lối '
               'thoát thường bị người học bỏ qua.'))
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Tần suất của từng dạng rút gọn và từng từ đệm thay đổi theo vùng, '
            'tuổi, giới và mức thân mật. Những gì trình bày ở đây là các dạng được '
            'ghi nhận rộng rãi (使用実態), không phải bảng tần suất. Muốn số liệu, '
            'tra 日本語話し言葉コーパス (CSJ) hoặc 日本語日常会話コーパス (CEJC). ' +
            SOURCES_CHECKED)
    F.append(P('Mức: 使用実態 · 要検証 cho tần suất.', 'caption'))
    return F

# ===========================================================================
def r50_information():
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R50 — Cấu trúc thông tin ／ 情報構造'))
    F.append(P('Vì sao bỏ chủ ngữ không làm câu mơ hồ, và vì sao bản dịch tiếng '
               'Việt che mất điều đó.', 'dek'))
    F.append(P('Mở rộng của R26. Điểm cốt lõi: một câu tiếng Nhật không được tổ '
               'chức theo “ai làm gì”, mà theo <b>cái gì đã biết</b> và <b>cái gì '
               'là mới</b>. Người nói đánh dấu hai loại đó bằng trợ từ và bằng '
               'việc bỏ trống.'))
    F += TB('BẢNG R50.1 — BỐN KHÁI NIỆM CỐT LÕI',
            ['Khái niệm', 'Nghĩa', 'Dấu hiệu trong tiếng Nhật'],
            [['Đã biết / mới', 'Người nghe đã biết hay chưa',
              'は thường đánh dấu đã biết; が thường đưa vào mới'],
             ['Đề tài', 'Điều cả câu đang nói về', 'は'],
             ['Tiêu điểm', 'Phần thông tin mới, phần trả lời câu hỏi', 'が; hoặc trọng âm câu'],
             ['Liên tục đề tài', 'Chủ thể giữ nguyên qua nhiều câu', 'Bỏ trống chủ ngữ']],
            colw=[20, 34, 46])
    F.append(H3('50.1 Câu đối lập nổi tiếng nhất'))
    F += EX('私はコーヒーを飲みました。', 'watashi wa kōhī o nomimashita.',
            'Tôi đã uống cà phê.',
            'は đặt “tôi” làm đề tài. Trong ngữ cảnh thật, câu này thường xuất hiện '
            'khi có đối chiếu ngầm: về phần tôi thì tôi uống cà phê.')
    F += EX('私がコーヒーを飲みました。', 'watashi ga kōhī o nomimashita.',
            'Chính tôi đã uống cà phê.',
            'が đặt “tôi” vào tiêu điểm. Câu này trả lời câu hỏi “ai uống cà phê?”. '
            'Nếu câu hỏi là “anh uống gì?”, tiêu điểm phải là “cà phê”, và câu trả '
            'lời tự nhiên là コーヒーを飲みました — không cần が và cũng không nên '
            'có は.')
    F.append(H3('50.2 Vì sao bản dịch tiếng Việt che mất cấu trúc này'))
    F.append(P('Tiếng Việt có công cụ riêng để làm việc tương tự (“chính”, “thì”, '
               '“là”, và trật tự câu), nhưng chúng không ép buộc. Khi dịch 私は… và '
               '私が… sang tiếng Việt, cả hai thường ra “Tôi uống cà phê” — và '
               'khác biệt biến mất. Kết quả là người học Việt thường không xây được '
               '<b>trực giác</b> về は / が qua dịch nghĩa, mà chỉ nhớ được quy tắc.'))
    F += TB('BẢNG R50.2 — CÁCH BÙ KHI DỊCH',
            ['Câu tiếng Nhật', 'Dịch sát nghĩa để giữ cấu trúc'],
            [['私は行きます。', '“(Còn) tôi thì (tôi) đi.” — có đối chiếu'],
             ['私が行きます。', '“Chính tôi đi.” — chọn người, không phải ai khác'],
             ['私も行きます。', '“Tôi cũng đi.”'],
             ['行きます。', '“(Tôi) đi.” — chủ thể đã rõ từ ngữ cảnh, không cần nêu']],
            colw=[26, 74])
    F.append(H3('50.3 Bỏ trống và đại từ zero'))
    F.append(P('Tiếng Nhật cho phép bỏ cả chủ ngữ lẫn tân ngữ khi chúng có thể khôi '
               'phục từ ngữ cảnh. Đây không phải “mơ hồ” mà là một hệ thống: người '
               'nói tin rằng người nghe theo dõi được đề tài đang chạy. Ba khuynh '
               'hướng khôi phục:'))
    F += TB('BẢNG R50.3 — BA KHUYNH HƯỚNG KHÔI PHỤC',
            ['Khuynh hướng', 'Nghĩa', 'Ví dụ'],
            [['Giữ nguyên đề tài', 'Đoạn đang nói về ai thì chủ ngữ bỏ trống vẫn là người đó',
              '田中さんは来ました。それから、すぐ帰りました。（chủ ngữ bỏ trống = 田中さん）'],
             ['Đổi khi có tín hiệu', 'Khi chủ thể đổi, tiếng Nhật thường có dấu hiệu',
              '田中さんは来ました。そのあと、私は帰りました。（nêu rõ để đổi）'],
             ['Tân ngữ khôi phục từ câu trước', 'Đối tượng đã nhắc thì bỏ',
              'この本は面白いです。昨日買いました。（tân ngữ = この本）']],
            colw=[20, 34, 46])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Cách phân biệt は/が theo “chủ đề đã biết vs chủ thể mới” là cách giải '
            'thích sư phạm chuẩn, nhưng đây là một trong những chủ đề được tranh '
            'luận nhiều nhất trong ngôn ngữ học tiếng Nhật, và nhiều hiện tượng '
            '(特に 総記のガ, phạm vi tác dụng của は) không được giải thích đầy đủ '
            'bằng cặp đối lập đơn giản. Ba khuynh hướng khôi phục ở 50.3 là mô tả '
            'thực hành, không phải quy tắc. ' + SOURCES_CHECKED)
    F.append(P('Mức: 一般的な教育上の説明 cho bảng 50.1 và 50.2 · 使用実態 cho 50.3 '
               '· 要検証 cho giới hạn của toàn bộ cách giải thích.', 'caption'))
    return F

# ===========================================================================
def r59_business():
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R59 — Tiếng Nhật công việc ／ ビジネス日本語'))
    F.append(P('Không phải một ngôn ngữ khác, mà là một tập hợp các lựa chọn đăng '
               'ký được tổ chức theo hai trục: trong/ngoài và trên/dưới.', 'dek'))
    F.append(H3('59.1 Bốn trục quyết định cách nói'))
    F += TB('BẢNG R59.1 — BỐN TRỤC',
            ['Trục', 'Câu hỏi', 'Ví dụ thay đổi cách nói'],
            [['Nội bộ / bên ngoài（ウチ・ソト）', 'Người nghe có thuộc tổ chức của tôi không?',
              'Nói với khách về sếp mình: dùng 謙譲語 cho hành động của sếp (社長は伺います), '
              'không dùng 尊敬語'],
             ['Trên / dưới', 'Ai ở vị thế cao hơn trong tình huống này?',
              'Khách hàng ở vị thế cao — nhưng là “cao bên ngoài”, khác với “sếp bên trong”'],
             ['Trang trọng / thường', 'Kênh nào: email, điện thoại, chat, gặp trực tiếp?',
              'Chat nội bộ cho phép rút gọn; email ra ngoài gần như không'],
             ['Đã biết / mới', 'Người nghe biết thông tin này chưa?',
              'Báo cáo lần đầu cho sếp khác với xác nhận lại thông tin sếp đã biết']],
            colw=[20, 30, 50])
    F.append(H3('59.2 報・連・相 — ba loại giao tiếp nội bộ'))
    F += TB('BẢNG R59.2 — 報連相', ['Loại', 'Là gì', 'Đặc điểm ngôn ngữ'],
            [['報告（ほうこく）', 'Báo cáo việc đã xảy ra, đã làm',
              'Thì quá khứ; nêu kết quả trước, lý do sau; dùng 〜ました・〜しております'],
             ['連絡（れんらく）', 'Thông báo thông tin cần biết',
              'Trung tính; thường ngắn; 〜とのことです để truyền đạt gián tiếp'],
             ['相談（そうだん）', 'Hỏi ý trước khi quyết định',
              'Dạng hỏi; 〜たほうがよろしいでしょうか, ご助言をいただけますか']],
            colw=[18, 34, 48])
    F += CALL('LỖI ĐẶC TRƯNG CỦA NGƯỜI HỌC Ở PHẦN NÀY ／ よくある誤り',
              'Người học Việt Nam thường (1) báo cáo theo trình tự thời gian thay vì '
              'kết quả trước; (2) dùng 尊敬語 cho hành động của người trong công ty '
              'mình khi nói với bên ngoài; (3) dịch “em nghĩ là…” thành 〜と思います '
              'trong khi cần 〜のではないでしょうか hoặc 〜かと思われます; (4) dùng '
              'quá nhiều です・ます nhưng thiếu クッション言葉.', tone='gold')
    F.append(H3('59.3 クッション言葉 — từ đệm trước khi vào việc'))
    F += TB('BẢNG R59.3 — MƯỜI TỪ ĐỆM THÔNG DỤNG',
            ['Tình huống', 'Từ đệm', 'Ví dụ đầy đủ'],
            [['Nhờ vả', '恐れ入りますが', '恐れ入りますが、資料をお送りいただけますか。'],
             ['Nhờ vả (nhẹ)', 'お手数ですが', 'お手数ですが、ご確認をお願いいたします。'],
             ['Làm phiền người đang bận', 'お忙しいところ申し訳ありませんが', '…が、少しお時間いただけますか。'],
             ['Từ chối', '申し訳ございませんが', '申し訳ございませんが、その日は難しいです。'],
             ['Sửa lại điều người khác nói', '失礼ですが', '失礼ですが、もう一度お願いできますか。'],
             ['Đưa tin xấu', '残念ながら', '残念ながら、今回は見送らせていただきます。'],
             ['Xác nhận điều mình hiểu chưa đúng', '念のため', '念のため、もう一度確認させてください。'],
             ['Xin phép hỏi', '差し支えなければ', '差し支えなければ、お伺いしてもよろしいですか。'],
             ['Kết thúc yêu cầu', '何卒よろしくお願いいたします', '…何卒よろしくお願いいたします。'],
             ['Xin lỗi trước', '大変恐縮ですが', '大変恐縮ですが、ご対応をお願いできますでしょうか。']],
            colw=[22, 24, 54])
    F.append(H3('59.4 Sổ tay email: bố cục bảy phần'))
    F += TB('BẢNG R59.4 — BỐ CỤC EMAIL CÔNG VIỆC',
            ['Phần', 'Chức năng', 'Mẫu'],
            [['1. Kính ngữ mở đầu', 'Nhận diện quan hệ', '株式会社〇〇 営業部 △△様'],
             ['2. Tự giới thiệu', 'Chỉ cần khi chưa quen', 'いつもお世話になっております。〇〇の△△です。'],
             ['3. Câu chào theo mùa', 'Tùy môi trường — nhiều công ty đã bỏ', '（tháng 7–8）暑さが厳しい折、いかがお過ごしでしょうか。'],
             ['4. Vào việc', 'Nêu mục đích trong 1–2 câu', '本日は、〜の件でご連絡いたしました。'],
             ['5. Thân', 'Chi tiết, có tiêu đề phụ nếu dài', 'つきましては、下記のとおりです。'],
             ['6. Hành động mong muốn', 'Nói rõ bạn muốn gì', 'ご確認の上、ご返信いただけますと幸いです。'],
             ['7. Kết', 'Đóng lại', '何卒よろしくお願いいたします。\n〇〇株式会社 △△']],
            colw=[18, 30, 52])
    F.append(H3('59.5 電話応対 — ba giai đoạn của một cuộc gọi'))
    F.append(P('Điện thoại là kênh khó nhất trong tiếng Nhật công việc, vì không có '
               'mặt chữ, không có khẩu hình, và không xem lại được. Nó cũng là kênh '
               'có mẫu câu cố định nhất — nghĩa là phần học được nhiều nhất.'))
    F += TB('BẢNG R59.5 — BA GIAI ĐOẠN',
            ['Giai đoạn', 'Việc phải làm', 'Mẫu câu'],
            [['1. Nhấc máy (受ける)', 'Nói tên công ty, không nói もしもし',
              'お電話ありがとうございます。〇〇株式会社でございます。'],
             ['2. Nghe và xác nhận', 'Xác nhận tên người gọi và nội dung, lặp lại để kiểm',
              'いつもお世話になっております。復唱させていただきます。〜でよろしいでしょうか。'],
             ['3a. Chuyển máy (取り次ぐ)', 'Xin người gọi chờ, nói rõ sẽ chuyển cho ai',
              '少々お待ちくださいませ。〇〇に代わります。'],
             ['3b. Ghi lời nhắn (伝言)', 'Nói rõ người đó vắng, đề nghị để lại lời nhắn',
              'あいにく席を外しております。よろしければ、伝言を承ります。'],
             ['4. Kết thúc', 'Nhắc lại nội dung, cảm ơn, chờ người kia cúp trước',
              'かしこまりました。確かに承りました。失礼いたします。']],
            colw=[22, 32, 46])
    F += CALL('BA LỖI NGHE ĐƯỢC NGAY QUA ĐIỆN THOẠI ／ 電話で目立つ三つの誤り',
              '<b>Một:</b> nói もしもし khi nhấc máy trong môi trường công việc — もしもし '
              'chỉ dùng khi bạn là người gọi, hoặc trong gia đình.\n'
              '<b>Hai:</b> không lặp lại thông tin (復唱). Người Nhật coi việc lặp lại '
              'số điện thoại, tên, ngày giờ là chuẩn mực, không phải mất thời gian.\n'
              '<b>Ba:</b> cúp máy trước khách hàng. Trong nghi thức công việc, bên gọi '
              'đến hoặc bên ở vị thế cao hơn cúp trước.', tone='gold')
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Mức trang trọng phù hợp <b>thay đổi theo ngành, công ty, thế hệ và văn '
            'hoá tổ chức</b>. Một số công ty (đặc biệt là công ty khởi nghiệp và '
            'công ty công nghệ) đã bỏ câu chào theo mùa và dùng văn phong gần với '
            'chat hơn. Đừng áp bảng này máy móc; hãy đọc email nội bộ của chính nơi '
            'bạn làm việc. ' + SOURCES_CHECKED)
    F.append(P('Mức: 公式 cho khung 5 loại kính ngữ và nguyên tắc 内・外 (「敬語の指針」, '
               '2007) · 使用実態 cho các mẫu câu · 要検証 cho mức áp dụng theo tổ chức. '
               + SOURCES_CHECKED, 'caption'))
    return F

# ===========================================================================
def r60_academic():
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R60 — Tiếng Nhật học thuật và văn bản công ／ 学術日本語と公用文'))
    F.append(P('Văn viết trang trọng có quy tắc riêng, và một phần trong đó là quy '
               'định chính thức của nhà nước Nhật Bản.', 'dek'))
    F.append(H3('60.1 である体 — thể văn viết'))
    F.append(P('Báo cáo, luận văn, bài báo khoa học, từ điển và văn bản hành chính '
               'dùng である thay cho です. Đây không phải “trang trọng hơn です”; '
               'nó là một <b>đăng ký khác</b>, thuộc văn viết, và dùng です trong '
               'bài luận khoa học lại gây cảm giác lạc giọng.'))
    F += TB('BẢNG R60.1 — BA ĐĂNG KÝ CỦA VĂN VIẾT',
            ['Đăng ký', 'Kết câu', 'Dùng ở'],
            [['である体', 'である・だ・〜した', 'Luận văn, báo cáo khoa học, tin tức, bách khoa'],
             ['です・ます体', 'です・ます', 'Thư, email, hướng dẫn, sách giáo khoa'],
             ['漢語体 (văn bản công)', 'である + 漢語 + 定型', 'Văn bản hành chính, thông tư, thông báo chính thức']],
            colw=[22, 26, 52])
    F.append(H3('60.2 「公用文作成の考え方」 — những điểm người học cần biết'))
    F.append(P('Năm 2022, Hội đồng Văn hoá Nhật Bản đưa ra 「公用文作成の考え方」 '
               '(Kiến nghị ngày 7 tháng 1 năm 2022), thay thế cho bản hướng dẫn năm '
               '1951. Đây là văn bản hiện hành định hướng cách viết văn bản của các '
               'cơ quan nhà nước Nhật Bản. Bốn điểm có ích trực tiếp cho người học '
               'ở trình độ N2–N1:'))
    F += TB('BẢNG R60.2 — BỐN ĐIỂM TỪ 「公用文作成の考え方」',
            ['Điểm', 'Nội dung', 'Áp dụng cho bạn'],
            [['Phân loại văn bản',
              'Chia thành 「告示・通知等」「記録・公開資料等」「解説・広報等」, '
              'mỗi loại có mức dễ hiểu khác nhau',
              'Đừng áp văn phong hành chính cho văn bản quảng bá. Mục đích quyết định văn phong.'],
             ['Dấu phẩy khi viết ngang',
              'Nguyên tắc dùng 「、（テン）」 khi viết ngang',
              'Trong văn bản chính thức hiện đại, viết ngang dùng 、 chứ không dùng ，'],
             ['Thuật ngữ và từ ngoại lai',
              'Có hướng dẫn riêng về cách dùng thuật ngữ chuyên môn và 外来語',
              'Văn bản công không thay katakana bằng từ Hán một cách máy móc, cũng '
              'không lạm dụng katakana'],
             ['Câu ngắn, một ý một câu',
              'Khuyến nghị mỗi câu một luận điểm; hạn chế 二重否定 và bị động thừa',
              'Đây cũng là tiêu chí viết 小論文 và báo cáo — xem thêm Ch.9 ở N1']],
            colw=[20, 42, 38])
    F.append(H3('60.3 Ba đặc điểm của văn học thuật tiếng Nhật'))
    F += TB('BẢNG R60.3 — BA ĐẶC ĐIỂM',
            ['Đặc điểm', 'Biểu hiện', 'Vì sao'],
            [['Danh từ hoá nặng', '〜こと・〜という事実・〜の可能性',
              'Đẩy mệnh đề thành tham tố để tiếp tục lập luận'],
             ['Rào đón (hedging)', 'と考えられる・〜のではないだろうか・〜にほかならない',
              'Vừa giữ mức chắc chắn phù hợp, vừa để mở cho phản biện'],
             ['Liên kết logic tường minh', 'したがって・ゆえに・一方で・ただし',
              'Người đọc phải theo được lập luận không cần hỏi lại']],
            colw=[20, 40, 40])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Nội dung 「公用文作成の考え方」 ở bảng 60.2 được tóm tắt từ bản công bố '
            'của 文化庁 (2022). Cuốn sách này <b>không</b> dẫn nguyên văn và không '
            'đối chiếu từng trang. Bản gốc khoảng 20 trang; nếu bạn viết văn bản '
            'chính thức, hãy đọc bản gốc. Địa chỉ: bunka.go.jp → 審議会 → 国語分科会 → '
            '報告 → 「公用文作成の考え方」. ' + SOURCES_CHECKED)
    F.append(P('Mức: 公式 cho nội dung 公用文作成の考え方 (đã tóm tắt từ công bố của '
               '文化庁) · 一般的な教育上の説明 cho 60.1 và 60.3.', 'caption'))
    return F

# ===========================================================================
def r61_modern():
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R61 — Tiếng Nhật hiện đại: những gì đang thay đổi ／ 現代日本語の変化'))
    F.append(P('Phần này cố ý ngắn và có ghi ngày. Mọi nội dung ở đây có thể lỗi '
               'thời — đó chính là điều cần biết về nó.', 'dek'))
    F += CALL('CẢNH BÁO NGÀY THÁNG ／ 日付について',
              'Toàn bộ mục này phản ánh tình hình <b>đến đầu năm 2026</b>. Những '
              'thay đổi đang diễn ra trong ngôn ngữ không có điểm kết thúc, và mô '
              'tả về chúng cũng vậy. Khi bạn đọc phần này sau vài năm, hãy coi nó '
              'như một ảnh chụp, không phải một quy luật.', tone='gold')
    F.append(H3('61.1 Bốn thay đổi đang diễn ra (tính đến 2026)'))
    F += TB('BẢNG R61.1 — BỐN XU HƯỚNG',
            ['Hiện tượng', 'Mô tả', 'Mức độ chắc chắn'],
            [['Thu hẹp trợ từ cuối câu mang giới',
              'Các trợ từ từng được xem là “nữ tính” (わ・かしら・のよ) đang thu hẹp '
              'ở người trẻ, đặc biệt ở đô thị. Một phần chuyển sang ngữ điệu.',
              '研究知見 — hướng thay đổi được ghi nhận rộng rãi; tốc độ thay đổi '
              'khác nhau theo vùng và thế hệ'],
             ['Ranh giới email và chat mờ đi trong công việc',
              'Nhiều tổ chức dùng công cụ chat nội bộ với văn phong gần với hội thoại, '
              'trong khi email ra ngoài vẫn giữ văn phong trang trọng.',
              '使用実態 — quan sát rộng rãi, nhưng rất khác nhau giữa các công ty'],
             ['Quy tắc romaji chính thức thay đổi',
              '「ローマ字のつづり方」令和7年内閣告示第4号 (22/12/2025) chuyển sang '
              'Hepburn làm nền. Cách viết đã quen dùng không bị đòi đổi ngay.',
              '公式 — nội dung cáo thị đã xác minh; mức áp dụng thực tế còn 要検証'],
             ['JLPT thêm tham chiếu CEFR',
              'Từ kỳ tháng 12/2025, kết quả JLPT ghi thêm mức CEFR tham chiếu, dựa '
              'trên tổng điểm chứ không chỉ cấp độ. Chỉ ghi cho người đạt.',
              '公式 — xác minh trên jlpt.jp']],
            colw=[16, 46, 38])
    F.append(H3('61.2 Hai điều KHÔNG thay đổi (và người học hay lo)'))
    F += TB('BẢNG R61.2 — HAI ĐIỀU ỔN ĐỊNH',
            ['Lo ngại', 'Thực tế'],
            [['“Nếu romaji đổi, mọi sách cũ thành sai”',
              'Không. Cáo thị chỉ quy định cách viết tiếng Nhật bằng chữ Latinh. Nội '
              'dung tiếng Nhật trong sách không thay đổi. Cách viết đã phổ biến '
              '(Tokyo, judo, matcha) vẫn hợp lệ.'],
             ['“JLPT sẽ đổi cấu trúc vì CEFR”',
              'Không. Năm cấp độ N1–N5, tiêu chuẩn đạt và cấu trúc phần thi <b>không '
              'đổi</b>. CEFR chỉ được ghi thêm như thông tin tham chiếu.']],
            colw=[28, 72])
    F.append(H3('61.3 Ba loại thay đổi — theo tốc độ'))
    F.append(P('Phân biệt ba tốc độ giúp bạn biết nên học gì như kiến thức bền, và '
               'nên coi gì là thông tin thời sự:'))
    F += TB('BẢNG R61.3 — BA TỐC ĐỘ',
            ['Tốc độ', 'Ví dụ', 'Cách học'],
            [['Rất chậm (hàng thế kỷ)',
              'Cấu trúc câu SOV · hệ thống trợ từ · 敬語 · hệ thống chữ viết',
              'Học vững, dùng suốt đời'],
             ['Trung bình (một hai thế hệ)',
              'Trợ từ cuối câu mang giới · mức trang trọng trong email · từ vựng '
              'công sở · trọng âm của từ mới',
              'Nhận biết khuynh hướng; giữ linh hoạt'],
             ['Nhanh (vài năm)',
              'ネットスラング · quy ước emoji · cách viết tắt theo nền tảng',
              'Nhận biết, không đưa vào vốn từ cốt lõi']],
            colw=[20, 42, 38])
    F.append(P('Mức: 公式 cho hai mục về romaji và JLPT · 研究知見 cho 61.1 dòng 1 · '
               '使用実態 cho dòng 2 · 編集上の整理 cho cách phân ba tốc độ. ' +
               SOURCES_CHECKED, 'caption'))
    return F

# ===========================================================================
def r62_classical_modern():
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R62 — Đối chiếu cổ văn và hiện đại ／ 文語と現代語の対照'))
    F.append(P('Bổ sung cho N1 Ch.4–6. Phần này nói rõ cái gì còn sống trong văn '
               'viết hiện đại, cái gì chỉ tồn tại trong văn bản cổ, và cái gì '
               'tuyệt đối không được đem vào hội thoại.', 'dek'))
    F += TB('BẢNG R62.1 — BA MỨC ĐỘ “CÒN SỐNG”',
            ['Mức', 'Mẫu', 'Còn gặp ở', 'Không dùng ở'],
            [['Còn sống, dùng được',
              '〜である・〜ではない・〜のごとく（thành ngữ cố định）・〜を皮切りに',
              'Văn viết trang trọng, diễn văn, tiêu đề báo',
              'Hội thoại thường; nhưng である trong thuyết trình trang trọng vẫn tự nhiên'],
             ['Còn dấu vết',
              '〜ざるを得ない・〜んがために・〜べく',
              'Văn viết nghị luận, tiểu thuyết, phát biểu',
              'Hội thoại — trừ khi cố ý gây hiệu quả hài hước'],
             ['Chỉ trong văn bản cổ',
              '係り結び（ぞ・なむ・や・か）・已然形・〜き・〜けり',
              'Văn bản cổ, thơ, tục ngữ, trích dẫn',
              'Mọi văn bản hiện đại, kể cả trang trọng nhất']],
            colw=[18, 34, 26, 22])
    F.append(H3('62.1 Ba cấu trúc cổ còn lại trong tiếng Nhật hiện đại'))
    F += TB('BẢNG R62.2 — BA CẤU TRÚC',
            ['Cấu trúc cổ', 'Dạng hiện đại', 'Ví dụ còn dùng'],
            [['〜ず（打消の接続）', '〜ないで / 〜なくて',
              '〜ざるを得ない · 〜ずにはいられない · 問わず · 絶えず'],
             ['〜ぬ（打消の終止・連体）', '〜ない',
              '〜ぬ（văn viết trang trọng）· 〜ぬまま · 〜ぬうちに'],
             ['〜べし（推量・当然）', '〜べき / 〜はず',
              '〜べく · 〜べき · 〜べからず（biển báo, khẩu hiệu）']],
            colw=[22, 24, 54])
    F.append(P('Điều đáng chú ý về ngữ pháp: 〜ざるを得ない, 〜ずにはいられない, '
               '〜べく là những chỗ mà tiếng Nhật hiện đại <b>giữ lại</b> một hình '
               'thái cổ vì nó làm được việc mà dạng hiện đại không làm gọn bằng. '
               'Vì vậy chúng vẫn thuộc vốn từ của N1–N2, không phải kiến thức lịch sử.'))
    F.append(H3('62.2 Bẫy: văn phong cổ trong biển báo và khẩu hiệu'))
    F.append(P('Một số dạng cổ vẫn tồn tại trong ngôn ngữ công cộng, nơi chúng được '
               'coi là trung tính và trang trọng chứ không phải cổ:'))
    F += TB('BẢNG R62.3 — CỔ VĂN TRONG NGÔN NGỮ CÔNG CỘNG',
            ['Mẫu', 'Nghĩa', 'Gặp ở'],
            [['〜禁止', 'Cấm', 'Biển báo: 駐車禁止 · 喫煙禁止'],
             ['〜につき', 'Vì lý do', 'Thông báo: 工事中につき、通れません'],
             ['〜たるもの', 'Với tư cách là', 'Diễn văn, xã luận'],
             ['〜べからず', 'Không được', 'Biển báo nghiêm trang, khẩu hiệu'],
             ['〜のほか', 'Ngoài ra', 'Văn bản hành chính'],
             ['〜をもって', 'Bằng, kể từ', 'Thông báo chính thức: 本日をもって閉店いたします']],
            colw=[18, 26, 56])
    F.append(P('Ghi chú cho người học: học các mẫu này như <b>mẫu cố định</b> gặp '
               'trong biển báo và thông báo, không như ngữ pháp cổ cần chia. Bạn '
               'không cần biết chia たる để đọc 「〜たるもの」 — bạn chỉ cần nhận ra nó.'))
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Việc xếp ba mức “còn sống” ở bảng R62.1 là <b>xếp đặt biên soạn</b>. '
            'Ranh giới giữa mức 1 và mức 2 tuỳ loại văn bản và thời điểm: một mẫu '
            'hiếm trong tin tức hôm nay có thể phổ biến lại hoặc biến mất trong '
            'mười năm tới. Các quy tắc chia cổ ở N1 Ch.5 theo cách trình bày chuẩn '
            'của môn 国文法 (ngữ pháp học đường Nhật Bản), không phải của ngôn ngữ '
            'học lịch sử. ' + SOURCES_CHECKED)
    return F

# ===========================================================================
def r66_error_atlas():
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R66 — Bản đồ lỗi: tiếng Nhật của người học ／ 学習者の誤りの地図'))
    F.append(P('Mở rộng của R9. Điểm khác: phần này phân biệt ba <b>nguồn</b> của '
               'lỗi, vì mỗi nguồn cần cách xử lý khác nhau.', 'dek'))
    F += CALL('BA NGUỒN — BA CÁCH CHỮA ／ 誤りの三つの源',
              '<b>1. Ảnh hưởng tiếng mẹ đẻ (chuyển di tiêu cực).</b> Chữa bằng cách '
              'học đối lập, không bằng cách luyện thêm.\n'
              '<b>2. Cách dạy ở giai đoạn đầu.</b> Ví dụ 私は xuất hiện trong mọi '
              'mẫu câu N5, nên người học dùng nó quá nhiều. Chữa bằng cách nhận ra '
              'nguyên nhân, rồi lược bỏ có ý thức.\n'
              '<b>3. Hiện tượng chung của mọi người học.</b> Không liên quan gì đến '
              'tiếng Việt — người học mọi nước đều mắc. Chữa bằng cách luyện tập, '
              'không cần phân tích.', tone='gold')
    F.append(H3('66.1 Mười nhóm lỗi theo ba nguồn'))
    F += TB('BẢNG R66.1 — MƯỜI NHÓM LỖI',
            ['Nhóm lỗi', 'Dạng sai', 'Nguồn', 'Cách chữa'],
            [['Nhịp mora', 'Nén các mora ngắn, kéo dài mora dài', '1',
              'Gõ nhịp khi đọc; thu âm và đếm lại'],
             ['Độ dài âm', 'Không phân biệt おじさん/おじいさん', '1',
              'Luyện cặp tối thiểu qua âm thanh, không qua chữ viết'],
             ['う và ん', 'u môi tròn; ん cuối chạm lưỡi', '1',
              'Luyện cơ học: thả lỏng môi, thoát hơi bằng mũi'],
             ['Thanh điệu', 'Cao độ lên xuống trong âm tiết', '1',
              'Đọc câu dài với cao độ bằng phẳng trong từng từ'],
             ['Chủ ngữ thừa', '私は nhiều hơn mức tự nhiên', '2',
              'Đọc lại đoạn hội thoại thật và đếm số chủ ngữ được nêu'],
             ['を cho đích đến', '× 学校を行きます', '1',
              'Học を cùng bảng chức năng (R1), không học riêng “tân ngữ”'],
             ['Thì và thể', 'Dùng た cho trạng thái hiện tại; quá khứ của tính từ', '1 và 3',
              'Học thể cùng cặp tự/tha và cùng khía cạnh'],
             ['は và が', 'Đặt が ở chỗ cần は khi thông tin đã biết', '1 và 3',
              'Luyện đọc theo cấu trúc thông tin (R50), không luyện theo quy tắc'],
             ['Đăng ký không nhất quán', 'Trộn だ và です trong cùng một lượt nói', '2',
              'Chọn một đăng ký cho cả lượt nói, rồi mới luyện chuyển đổi'],
             ['Dịch thẳng cụm', '× 電話をする, × 風邪をする', '1 và 3',
              'Học collocation theo cụm (R22), không theo từ đơn']],
            colw=[18, 30, 8, 44])
    F.append(H3('66.2 Mười lỗi đặc trưng hay bị chẩn đoán sai là “do tiếng Việt”'))
    F += TB('BẢNG R66.2 — CHẨN ĐOÁN LẠI',
            ['Lỗi', 'Chẩn đoán phổ biến', 'Chẩn đoán chính xác hơn'],
            [['Không dùng được 敬語', '“Tiếng Việt không có kính ngữ”',
              'Tiếng Việt <b>có</b> hệ thống kính ngữ (ạ, dạ, thưa, kính, hư từ xưng hô). '
              'Vấn đề là cơ chế khác: tiếng Việt đánh dấu qua từ xưng hô, tiếng Nhật '
              'qua hình thái động từ. Cần luyện chuyển đổi hình thái.'],
             ['Không tự nhiên khi từ chối', '“Cần hiểu văn hoá Nhật”',
              'Cần luyện thang giảm nhẹ (R51.7). Đây là kỹ năng ngôn ngữ, học được.'],
             ['Im lặng gây khó xử', '“Cần học 空気を読む”',
              'Im lặng trong hội thoại có tham số khác giữa các ngôn ngữ. Cần biết '
              'khoảng lặng dài bao nhiêu là bình thường, chứ không cần “đọc không khí”.'],
             ['Dùng あなた', '“Dịch tôi–bạn”',
              'Đúng là ảnh hưởng dịch. Nhưng vấn đề hẹp hơn: あなた chủ yếu dùng khi '
              'người trên nói với người dưới, hoặc giữa vợ chồng. Cách chữa là học '
              'tên + さん.'],
             ['Dùng 〜と思う quá nhiều', '“Tiếng Việt hay nói ‘tôi nghĩ’”',
              'Đây là lỗi chung của mọi người học. Người Nhật dùng rào đón ở dạng '
              'khác: 〜のではないでしょうか, 〜かと思われます, hoặc lược bỏ hẳn.'],
             ['Đọc kanji theo âm Hán Việt', '“Người Việt có lợi thế Hán Việt”',
              'Lợi thế là thật, nhưng cũng là <b>bẫy</b> với từ giả bạn (R37). '
              'Lợi thế đến từ việc biết nghĩa, không phải từ việc đoán âm.'],
             ['Nhấn trọng âm theo tiếng Việt', '“Vì tiếng Việt có thanh điệu”',
              'Khó khăn này gặp ở mọi người học, kể cả người nói ngôn ngữ không '
              'thanh điệu. Tiếng Việt đổi <b>dạng</b> lỗi, không đổi <b>mức</b>.'],
             ['Lẫn に và で', '“Tiếng Việt có một chữ ‘ở’”',
              'Đúng là ảnh hưởng. Nhưng cách chữa hiệu quả là học に và で theo '
              'tập chức năng riêng, không qua “ở”.'],
             ['Sai thể của tính từ', '“Tiếng Việt không chia tính từ”',
              'Tiếng Việt không chia đuôi, nhưng có thì (đã/đang/sẽ). Vấn đề là vị '
              'trí và hình thái, không phải khái niệm thì.'],
             ['Không dùng được dạng rút gọn', '“Cần nghe nhiều anime”',
              'Dạng rút gọn có quy tắc và <b>không phân bố đều</b>: một số dạng '
              'thuộc văn nói thân mật, một số dùng được cả trong email nội bộ. Cần '
              'học theo đăng ký (R49).']],
            colw=[18, 26, 56])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Bảng 66.2 là <b>phân tích biên soạn</b>. Nó dựa trên cấu trúc của hai '
            'ngôn ngữ và trên các mô tả phổ biến trong tài liệu giảng dạy, nhưng '
            'cuốn sách này chưa đối chiếu với một nghiên cứu <b>định lượng</b> nào '
            'về tỉ lệ mắc lỗi của người học Việt Nam. Những chỗ có dẫn chứng nghiên '
            'cứu là R9 và R65.2. ' + SOURCES_CHECKED)
    F.append(P('Mức: 研究知見 cho các nhóm có dẫn chứng ở R9/R65.2 · 編集上の整理 cho '
               'cách chẩn đoán lại ở 66.2 · 要検証 cho mọi con số tỉ lệ.', 'caption'))
    return F

# ===========================================================================
# CAN-DO REFERENCE MAPS  (brief §46 — a map, not exercises)
# ===========================================================================
_CD = {
 'N5': ('A1', 'ことばの土台',
   [('Hiểu / nhận ra',
     ['Câu rất ngắn, chậm, về bản thân, gia đình, giờ giấc, giá cả, chỉ dẫn đơn giản',
      'Hiragana và katakana đầy đủ; khoảng 100 kanji cơ bản nhất',
      'Số, thời gian, ngày tháng, trợ lượng từ cơ bản theo đúng vật']),
    ('Diễn giải',
     ['Nhận ra chức năng của は và が trong câu ngắn đã biết',
      'Chọn giữa dạng lịch sự và dạng thường theo quan hệ',
      'Hiểu chỉ dẫn đơn giản trong quán, ga, cửa hàng khi có tranh ảnh']),
    ('Nói / viết',
     ['Giới thiệu bản thân, hỏi đáp về công việc, sở thích, kế hoạch đơn giản',
      'Gọi món, hỏi đường, mua hàng — bằng câu học sẵn',
      'Viết câu ngắn, kana chính xác (nghĩ bằng kana, không qua romaji)'])]),
 'N4': ('A2', '文をつなぐ',
   [('Hiểu / nhận ra',
     ['Hội thoại đời thường nói hơi chậm về chủ đề quen thuộc',
      'Hợp chất hai chữ Hán phổ biến; khoảng 300 kanji',
      'Thể て・た, khả năng, điều kiện cơ bản, cho–nhận, tự–tha động từ']),
    ('Diễn giải',
     ['Phân biệt khía cạnh: 〜てしまう / 〜ておく / 〜てくる / 〜ていく',
      'Nhận ra sắc thái của thể thường và 〜んだ trong hội thoại',
      'Hiểu sự khác nhau giữa と・ば・たら・なら ở mức cơ bản']),
    ('Nói / viết',
     ['Kể lại việc đã xảy ra, nêu kế hoạch và dự định',
      'Nhờ vả, xin phép, đưa ra lời khuyên ở mức lịch sự trung bình',
      'Viết email ngắn và ghi chú nội bộ đúng mức lịch sự'])]),
 'N3': ('A2→B1', '行間を読む',
   [('Hiểu / nhận ra',
     ['Hội thoại ở tốc độ gần tự nhiên, có rút gọn thường gặp',
      'Khoảng 650 kanji; đọc được tin ngắn và thông báo',
      'Thụ động, sai khiến, mệnh đề quan hệ dài, danh từ hoá']),
    ('Diễn giải',
     ['Khôi phục chủ ngữ và tân ngữ bị bỏ trống theo mạch đoạn',
      'Phân biệt giữa ようだ・みたいだ・らしい・そうだ theo loại chứng cứ',
      'Đọc dấu hiệu và biển báo, kể cả dạng viết tắt']),
    ('Nói / viết',
     ['Mô tả kinh nghiệm, so sánh, nêu ý kiến và lý do',
      'Xử lý giao tiếp nơi làm việc ở mức cơ bản: báo cáo, xác nhận, từ chối lịch sự',
      'Viết email công việc theo bố cục, có クッション言葉'])]),
 'N2': ('B1→B2', '抽象を運ぶ',
   [('Hiểu / nhận ra',
     ['Tin tức, giải thích, bài bình luận có lập luận rõ',
      'Khoảng 1.000 kanji; từ vựng trừu tượng và từ Hán văn viết',
      'Văn viết である体, danh từ hoá, liên kết logic tường minh']),
    ('Diễn giải',
     ['Đọc được lập luận: luận điểm, dẫn chứng, kết luận, nhượng bộ',
      'Phân biệt sắc thái mức độ chắc chắn: はず・わけ・べき・に違いない',
      'Nhận ra đăng ký: câu này thuộc báo chí, hợp đồng, hay diễn văn']),
    ('Nói / viết',
     ['Trình bày ý kiến có cấu trúc, phản biện có lý lẽ',
      'Dùng kính ngữ hệ thống đúng theo trục 内・外 và trên–dưới',
      'Viết báo cáo, 意見文, email đối ngoại đúng văn phong'])]),
 'N1': ('B2→C1', '沈黙の意味',
   [('Hiểu / nhận ra',
     ['Văn bản có lập luận phức tạp, độ trừu tượng cao, hoặc văn học',
      'Khoảng 2.000 kanji; 慣用句, 四字熟語, dấu vết cổ văn',
      'Giọng điệu tác giả: châm biếm, giảm nhẹ nói quá, phản vấn']),
    ('Diễn giải',
     ['Suy ra lập trường người viết khi không được nói thẳng',
      'Nhận ra khi một câu không mang nghĩa đen của nó',
      'Phân biệt chuẩn mực và thực tế trong các khẳng định văn hoá']),
    ('Nói / viết',
     ['Thảo luận, thương lượng, thuyết phục ở mức tinh tế',
      'Viết tiểu luận, xã luận, văn bản học thuật',
      'Điều chỉnh đăng ký theo người nghe, kênh và mục đích'])]),
}

def candos():
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('Bản đồ năng lực N5 → N1 ／ 能力到達の見取り図'))
    F.append(P('Không phải bài kiểm tra. Đây là bản đồ để bạn biết mình đang ở đâu, '
               'và bậc tiếp theo thực sự đòi hỏi điều gì. Dùng nó để tự định vị, '
               'không để tự chấm điểm.', 'dek'))
    F += CALL('PHẦN NÀY DỰA TRÊN ĐÂU ／ この見取り図の根拠',
              'Cấu trúc được lấy theo cách tiếp cận <b>Can-do</b> của '
              '「日本語教育の参照枠」 (文化審議会国語分科会, 2021) và JF Standard '
              '(国際交流基金) — tức mô tả năng lực bằng “làm được gì”, không bằng '
              'số lượng mẫu ngữ pháp đã học. Tuy nhiên, <b>việc gán từng nội dung '
              'vào từng bậc là xếp đặt của người biên soạn</b>, không phải bảng '
              'chính thức. Mức CEFR ghi kèm là mức tham chiếu tương ứng với JLPT '
              'theo công bố của 国際交流基金 (12/2025), không phải quy đổi riêng '
              'của cuốn sách này. ' + SOURCES_CHECKED, tone='gold')
    for lvl, (cefr, ja, rows) in _CD.items():
        F.append(H3(f'{lvl} ／ {ja} ／ CEFR tham chiếu: {cefr}'))
        data = [[Paragraph(guard(a, 'SansB'), T.ST['th']),
                 Paragraph(guard('<br/>'.join('· ' + x for x in b)), T.ST['td'])]
                for a, b in rows]
        from reportlab.platypus import Table, TableStyle
        t = Table(data, colWidths=[T.CW * 0.22, T.CW * 0.78])
        t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 3.4), ('BOTTOMPADDING', (0, 0), (-1, -1), 5.2),
            ('LINEBELOW', (0, 0), (-1, -2), 0.35, T.RULE_SOFT)]))
        F.append(t); F.append(Spacer(1, 9))
    F.append(P('Cách dùng: khi bạn hoàn thành một phần, quay lại bản đồ này và tự '
               'hỏi bạn <b>làm được việc gì</b>, chứ không phải đã học bao nhiêu bài. '
               'Đó cũng là câu hỏi mà người phỏng vấn và đồng nghiệp sẽ hỏi.', 'body'))
    return F

# ===========================================================================
def r68_register_upgrade():
    """R68 — upgraded verification register + reference map."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('R68 — Sổ đăng ký kiểm chứng ／ 検証登録簿'))
    F.append(P('Mở rộng của R15. Điểm khác: mỗi mục giờ ghi cả <b>nguồn đã tra</b> '
               'và <b>cách hiểu thay thế</b>, không chỉ ghi tên chỗ còn nghi.', 'dek'))
    F.append(P('Cuốn sách này có <b>41 điểm</b> được đánh dấu 「要検証」 trong thân '
               'sách — danh sách tự động ở R15, luôn khớp với nội dung thực tế. '
               'Phần này bổ sung những gì R15 chưa có: cột nguồn đã tra, cột cách '
               'hiểu khác, và cột yêu cầu chuyên gia.'))
    F.append(H3('68.1 Sáu mức độ tin cậy — định nghĩa đầy đủ'))
    F += TB('BẢNG R68.1 — SÁU MỨC', ['Mức', 'Nghĩa', 'Nguồn điển hình', 'Có thể bị sửa bởi'],
            [['公式', 'Ghi trong văn bản chính thức của Nhật Bản',
              'Cáo thị, báo cáo hội đồng, trang web cơ quan',
              'Văn bản mới thay thế'],
             ['研究知見', 'Được nghiên cứu chuyên ngành hỗ trợ, không phải quy định',
              'Bài báo, sách chuyên khảo', 'Nghiên cứu mới'],
             ['使用実態', 'Cách dùng thực tế được ghi nhận rộng rãi',
              'Quan sát, giáo trình, corpus', 'Thay đổi theo thời gian'],
             ['一般的な教育上の説明', 'Được các giáo trình chuẩn thống nhất trình bày',
              'Giáo trình, sách tra cứu', 'Cách giải thích mới trong giáo dục'],
             ['編集上の整理', 'Phân tích của người biên soạn',
              'Quyết định biên soạn', 'Phân tích khác'],
             ['要検証', 'Chưa xác lập được', '—', 'Kiểm chứng trực tiếp']],
            colw=[16, 34, 28, 22])
    F += CALL('ĐIỂM QUAN TRỌNG NHẤT ／ 最も重要な点',
              'Ba mức đầu khác nhau về <b>bản chất</b>, không chỉ về độ chắc chắn. '
              'Một điều được dùng rất phổ biến (使用実態) không vì thế mà trở thành '
              'quy tắc chính thức (公式). Một kết luận nghiên cứu (研究知見) không '
              'vì thế mà trở thành quy định. Gộp ba mức này lại là lỗi phổ biến '
              'nhất khi đọc tài liệu về tiếng Nhật.', tone='gold')
    F.append(H3('68.2 Sáu nhóm cần kiểm chứng — phân loại theo bản chất'))
    F.append(P('Thay vì liệt kê lại 41 mục ở R15, phần này phân chúng thành sáu '
               'nhóm theo <b>vì sao</b> chúng chưa được xác lập. Biết nhóm nào sẽ '
               'cho bạn biết cần tìm loại nguồn nào để kiểm tra.'))
    F += TB('BẢNG R68.2 — SÁU NHÓM', ['Nhóm', 'Vì sao chưa xác lập', 'Cần tra ở đâu', 'Ví dụ'],
            [['A — Không có nguồn chính thức',
              'Vấn đề chưa bao giờ được nhà nước hoặc tổ chức chính thức quy định',
              'Nghiên cứu học thuật, corpus',
              'Cách phân biệt は/が; danh mục ngữ pháp theo cấp JLPT'],
             ['B — Nguồn có nhưng khác nhau',
              'Các từ điển / nghiên cứu ghi khác nhau, không có bản chuẩn duy nhất',
              'Đối chiếu nhiều từ điển, ghi rõ nguồn nào',
              'Số trọng âm của từng từ; ranh giới giữa はず・わけ'],
             ['C — Chỉ dẫn lại qua nguồn thứ cấp',
              'Người biên soạn chưa tiếp cận bản gốc',
              'Bản gốc của nghiên cứu được dẫn',
              'Nghiên cứu của Đỗ Hoàng Ngân (2015) về cảm nhận 長音・促音'],
             ['D — Thay đổi theo bối cảnh',
              'Không có một câu trả lời đúng cho mọi nơi',
              'Quan sát nơi cụ thể; hỏi người trong tổ chức',
              'Mức trang trọng trong email; 検討します trong từng công ty'],
             ['E — Số liệu không thống nhất',
              'Các khảo sát dùng cách đếm và danh sách khác nhau',
              'Đọc phương pháp của từng khảo sát',
              'Tỉ lệ “khoảng 86%” của dạng rút gọn 4 mora'],
             ['F — Tình trạng áp dụng thực tế',
              'Văn bản ban hành rồi, nhưng chưa rõ có được dùng rộng rãi',
              'Theo dõi công bố của các ngành liên quan',
              'Mức áp dụng 「ローマ字のつづり方」2025 trong trường học và biển báo']],
            colw=[14, 32, 28, 26])
    F.append(H3('68.3 Mẫu ghi cho mỗi mục cần kiểm chứng'))
    F.append(P('Nếu bạn muốn đóng góp vào việc sửa sách — hoặc muốn tự kiểm tra một '
               'mục — đây là mẫu ghi đầy đủ. R15 ghi bốn cột; mẫu này ghi tám.'))
    F += TB('BẢNG R68.3 — MẪU GHI', ['Cột', 'Nội dung'],
            [['Vị trí', 'Số trang hoặc mã mục (ví dụ: R19 · 19.3)'],
             ['Khẳng định', 'Câu hoặc bảng đang được kiểm chứng'],
             ['Vì sao chưa chắc', 'Thuộc nhóm A–F nào ở bảng 68.2'],
             ['Nguồn đã tra', 'Liệt kê cụ thể; nếu chưa tra, ghi “chưa tra”'],
             ['Nguồn hỗ trợ', 'Nguồn thực sự nói điều đó, kèm vị trí trong nguồn'],
             ['Cách hiểu thay thế', 'Một cách giải thích khác có cơ sở'],
             ['Mức tin cậy hiện tại', 'Một trong sáu mức'],
             ['Cần chuyên gia', 'Ngôn ngữ học · giáo dục tiếng Nhật · người bản ngữ · không cần']],
            colw=[22, 78])
    F.append(H3('68.4 Điều gì sẽ cần sửa trong ấn bản thứ ba'))
    F.append(P('Một cách đánh giá độ bền của một cuốn sách tham khảo là dự đoán '
               'trước những gì sẽ già đi. Dưới đây là dự đoán đó, ghi rõ để sau này '
               'có thể đối chiếu:'))
    F += TB('BẢNG R68.4 — DỰ ĐOÁN ĐỘ BỀN',
            ['Nội dung', 'Dự đoán sau 10 năm'],
            [['Cấu trúc câu, trợ từ, hệ thống kính ngữ, hệ thống chữ viết',
              'Hầu như không đổi. Đây là phần cốt lõi của giá trị lâu dài.'],
             ['Ngữ pháp cổ ở N1, lịch sử ngôn ngữ, ngôn ngữ vùng',
              'Không đổi (là dữ liệu lịch sử).'],
             ['Trọng âm cụ thể của từng từ',
              'Có thể lệch ở một số từ do thay đổi phương ngữ chuẩn. Đã ghi 要検証.'],
             ['Quy ước nhắn tin, emoji, ネットスラング',
              'Phần lớn sẽ lỗi thời. Đây là lý do phần này được ghi ngày.'],
             ['Mức trang trọng trong email công việc',
              'Nhiều khả năng tiếp tục giảm. Bảng R59.4 có ghi rõ mức biến thiên.'],
             ['Quy tắc romaji và tham chiếu CEFR',
              'Thay đổi khi có cáo thị hoặc công bố mới; có ghi ngày.'],
             ['Danh mục kanji và từ vựng theo cấp độ',
              'Vẫn sẽ là ước tính, vì JLPT vẫn không công bố danh mục.']],
            colw=[42, 58])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Bản thân bảng 68.4 là <b>dự đoán của người biên soạn</b>. Nó không có '
            'cơ sở nghiên cứu, và mục đích của nó không phải là chính xác mà là '
            'minh bạch: nói trước điều gì sẽ già đi để người đọc sau này có thể '
            'đối chiếu. ' + SOURCES_CHECKED)
    F.append(P('Mức: 編集上の整理 cho 68.2–68.4 · 公式 cho định nghĩa sáu mức ở 68.1 '
               '(theo cách dùng trong chính cuốn sách này).', 'caption'))
    return F

# ===========================================================================
def reference_map():
    """Editorial note: how the old R-numbers map to the new reference system."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('Bảng đối chiếu mục tra cứu ／ リファレンス対照表'))
    F.append(P('Ấn bản thứ hai giữ nguyên R1–R45 của ấn bản thứ nhất và bổ sung '
               'R46–R69. Bảng dưới đây cho biết mục nào là bản mở rộng của mục nào, '
               'và mục nào đã được bổ sung nội dung ngay tại chỗ thay vì viết lại.', 'dek'))
    F += CALL('VÌ SAO KHÔNG VIẾT LẠI TẤT CẢ ／ 重複を避けた理由',
              'Một số chủ đề mà bản kế hoạch ấn bản hai liệt kê riêng (trọng âm, '
              'từ nối, collocation, đồng nghĩa, chuyển đổi đăng ký, biển báo, tiếng '
              'Nhật số, lịch sử ngôn ngữ, ngôn ngữ vùng) <b>đã</b> có mục riêng ở '
              'ấn bản thứ nhất với nội dung tốt. Viết lại chúng thành mục mới sẽ chỉ '
              'tạo ra hai chỗ nói cùng một điều — đúng thứ mà nguyên tắc chống lặp '
              'của cuốn sách cấm. Thay vào đó, những mục đó được giữ nguyên và chỉ '
              'được bổ sung ở chỗ thật sự thiếu.', tone='teal')
    F += TB('BẢNG R — ĐỐI CHIẾU MỤC TRA CỨU',
            ['Mục mới', 'Quan hệ với ấn bản một', 'Nội dung thực sự mới'],
            [['R46 La-tinh hoá', 'Mở rộng R17 + R20',
              'Ba tầng độc lập (chính tả / la-tinh hoá / phát âm); bốn hiểu nhầm về cáo thị 2025'],
             ['R47 Phát âm', 'Mở rộng R18',
              'Điều kiện cần vs điều kiện đủ của vô thanh hoá; bốn yếu tố điều chỉnh'],
             ['R48 Trọng âm', '≡ R19 + R31 (giữ nguyên)',
              'Đã có đủ. Sửa một lỗi tuyệt đối hoá ở mục 2.4 (xem 2.4)'],
             ['R49 Tiếng nói rút gọn', 'Mở rộng N3 Ch.6',
              'Bảng 10 rút gọn kèm cột “không dùng ở”; phân biệt rút gọn với văn nói thô'],
             ['R50 Cấu trúc thông tin', 'Mở rộng R26',
              'Vì sao bản dịch tiếng Việt che mất cấu trúc; ba khuynh hướng khôi phục'],
             ['R51 Dụng học', 'MỚI',
              'Chỉ xuất · hàm ý · hành vi lời nói · thể diện · giảm nhẹ · thang từ chối'],
             ['R52 Từ đánh dấu hội thoại', '≡ R43 (giữ nguyên)', '—'],
             ['R53 Trợ từ cuối câu', 'Mở rộng R38',
              'Sáu nhóm chức năng; năm ràng buộc tổ hợp; ghi rõ giới hạn của mô hình nam/nữ'],
             ['R54 Nghĩa đen vs nghĩa thực', 'MỚI (trước đây rải rác)',
              'すみません (6 hành vi) · 大丈夫です / 結構です · ちょっと · 検討します'],
             ['R55 Hệ thống đồng nghĩa', '≡ R23 (giữ nguyên)', '—'],
             ['R56 Chuyển đổi đăng ký', '≡ R44 (giữ nguyên)', '—'],
             ['R57 Tiếng Nhật số', '≡ R34 (giữ nguyên)', '—'],
             ['R58 Biển báo và thông báo', '≡ R45 + R35 (giữ nguyên)', '—'],
             ['R59 Tiếng Nhật công việc', 'MỚI (trước đây chỉ N4 Ch.4)',
              'Bốn trục quyết định; 報連相; 10 クッション言葉; bố cục email 7 phần'],
             ['R60 Học thuật và văn bản công', 'MỚI',
              'Ba đăng ký văn viết; 公用文作成の考え方 (2022); ba đặc điểm văn học thuật'],
             ['R61 Tiếng Nhật hiện đại', 'MỚI',
              'Bốn xu hướng có ghi ngày; hai điều KHÔNG thay đổi; ba tốc độ thay đổi'],
             ['R62 Cổ văn ↔ hiện đại', 'MỚI',
              'Ba mức “còn sống”; ba cấu trúc cổ còn dùng; cổ văn trong biển báo'],
             ['R63 Lịch sử ngôn ngữ', '≡ R24 (giữ nguyên)', '—'],
             ['R64 Ngôn ngữ vùng', '≡ R25 (giữ nguyên)', '—'],
             ['R65 Đối chiếu Việt–Nhật', 'MỚI (R9 và R37 chỉ là một phần)',
              'Đối chiếu loại hình; ba khác biệt có nghiên cứu hỗ trợ; <b>ba khác biệt '
              'bị phóng đại</b>; lượng từ'],
             ['R66 Bản đồ lỗi', 'Mở rộng R9',
              'Ba nguồn lỗi; 10 nhóm; chẩn đoán lại 10 lỗi hay bị đổ cho tiếng Việt'],
             ['R67 Phân cấp nguồn', 'Mở rộng R11',
              'Bốn tầng nguồn; bảng quyết định câu hỏi nào tra tầng nào'],
             ['R68 Sổ đăng ký kiểm chứng', 'Mở rộng R15',
              'Sáu nhóm lý do; mẫu ghi 8 cột; dự đoán độ bền sau 10 năm'],
             ['R69 Chỉ mục', 'Mở rộng R16', 'Bổ sung mục cho toàn bộ R46–R68']],
            colw=[18, 24, 58])
    F.append(P('Ký hiệu: <b>≡</b> = giữ nguyên, không viết lại (tránh lặp) · '
               '<b>Mở rộng</b> = giữ nội dung cũ và thêm phần mới · '
               '<b>MỚI</b> = mục hoàn toàn mới.', 'caption'))
    F.append(Spacer(1, 6))
    F += numbering_note()
    return F
from reportlab.platypus import Table, TableStyle

def cando_one(lvl):
    """The Can-do map for ONE level — placed at the end of that level's part."""
    cefr, ja, rows = _CD[lvl]
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2(f'{lvl} — Bạn làm được gì ở bậc này ／ {ja}の到達点'))
    F.append(P(f'Mức CEFR tham chiếu: <b>{cefr}</b>. Đây là bản đồ, không phải bài '
               f'kiểm tra: nó để bạn tự định vị trước khi sang bậc tiếp theo.', 'dek'))
    data = [[Paragraph(guard(a, 'SansB'), T.ST['th']),
             Paragraph(guard('<br/>'.join('· ' + x for x in b)), T.ST['td'])]
            for a, b in rows]
    t = Table(data, colWidths=[T.CW * 0.24, T.CW * 0.76])
    t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 3.4), ('BOTTOMPADDING', (0, 0), (-1, -1), 5.2),
        ('LINEBELOW', (0, 0), (-1, -2), 0.35, T.RULE_SOFT)]))
    F.append(t); F.append(Spacer(1, 9))
    F += CALL('CÁCH ĐỌC BẢN ĐỒ NÀY ／ この表の使い方',
              'Ba cột là ba câu hỏi khác nhau: bạn <b>hiểu</b> được gì, bạn '
              '<b>suy ra</b> được gì, và bạn <b>làm</b> được gì. Người học thường '
              'chỉ tự đánh giá ở cột thứ nhất. Chuyển bậc thật sự xảy ra ở cột '
              'thứ ba.', tone='teal')
    F.append(P('Cơ sở: 「日本語教育の参照枠」 (文化審議会国語分科会, 2021) và JF Standard '
               '(国際交流基金) cho cách tiếp cận Can-do; mức CEFR theo công bố của '
               'JLPT (12/2025). Việc gán nội dung cụ thể vào từng bậc là xếp đặt của '
               'người biên soạn. ' + SOURCES_CHECKED, 'caption'))
    return F

# ===========================================================================
def bibliography():
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('Thư mục theo nhóm nguồn ／ 出典一覧（区分別）'))
    F.append(P('Mở rộng của R11. Bản cũ ghi nguồn theo chủ đề; bản này ghi theo '
               '<b>nhóm nguồn</b>, kèm định danh và ngày truy cập, và quan trọng '
               'nhất: kèm <b>nguồn dùng cho mục nào</b>.', 'dek'))
    F += CALL('QUY ƯỚC GHI ĐỊA CHỈ ／ 表記の約束',
              'Địa chỉ có ghi ngày truy cập là những địa chỉ đã được mở và đối '
              'chiếu cho ấn bản này. Những mục để dấu 「—」 là tài liệu chuẩn '
              'được nhắc đến vì chúng là cơ sở của mục tương ứng, nhưng <b>ấn bản '
              'này không mở lại từng trang</b>; đừng coi dấu 「—」 là xác nhận. '
              'Nếu bạn cần trích dẫn học thuật, hãy tra bản gốc ở cơ quan phát '
              'hành.', tone='gold')
    F.append(H3('Nhóm 1 — Văn bản chính thức（公式）'))
    F += TB(None, ['Cơ quan', 'Nhan đề', 'Năm', 'Định danh', 'Truy cập', 'Dùng cho'],
            [['文化審議会（文化庁）', '「ローマ字のつづり方」（令和7年内閣告示第4号）',
              '2025', '内閣告示第4号（2025年12月22日）', '17/9/2026', 'R20 · R46'],
             ['文化審議会国語分科会', '「公用文作成の考え方」建議',
              '2022', '建議 2022年1月7日 · 令和4年1月11日内閣文第1号', '17/9/2026', 'R60'],
             ['文化審議会国語分科会', '「日本語教育の参照枠」報告',
              '2021', '令和3年10月12日', '17/9/2026', 'Bản đồ Can-do · R68'],
             ['文化審議会（文化庁）', '「敬語の指針」答申',
              '2007', '平成19年2月2日', '17/9/2026', 'R3 · R59 · Ch.17 (N1)'],
             ['国際交流基金・日本国際教育支援協会', '日本語能力試験 公式サイト · CEFR 参考表示',
              '2025', 'jlpt.jp', '17/9/2026', 'R11 · R61 · bản đồ Can-do'],
             ['国際交流基金', 'JF 日本語教育スタンダード',
              '2010–', 'jfstandard.jpf.go.jp', '17/9/2026', 'Bản đồ Can-do · R68']],
            colw=[16, 26, 8, 22, 10, 18])
    F.append(H3('Nhóm 2 — Nghiên cứu quốc gia và kho ngữ liệu（研究機関・コーパス）'))
    F += TB(None, ['Cơ quan', 'Nguồn', 'Loại', 'Định danh', 'Dùng cho'],
            [['国立国語研究所', '現代日本語書き言葉均衡コーパス（BCCWJ）', 'Corpus', '—',
              'Tần suất và cách dùng trong văn viết'],
             ['国立国語研究所', '日本語話し言葉コーパス（CSJ）', 'Corpus', '—',
              'Đặc điểm văn nói, từ đệm, sửa lỗi'],
             ['国立国語研究所', '日本語日常会話コーパス（CEJC）', 'Corpus', '—',
              'Hội thoại đời thường, backchannel'],
             ['国立国語研究所', '多言語母語の日本語学習者横断コーパス（I-JAS）', 'Corpus', '—',
              'Tiếng Nhật của người học'],
             ['国立国語研究所', '中納言・少納言・UniDic', 'Công cụ', '—',
              'Tra cứu cách dùng; yêu cầu về phân tích hình thái']],
            colw=[18, 34, 10, 8, 30])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Ấn bản này <b>không</b> trực tiếp chạy truy vấn trên BCCWJ, CSJ, CEJC '
            'hay I-JAS. Mọi chỗ trong sách có ghi 「使用実態」 dựa trên mô tả và mẫu '
            'đã công bố trong tài liệu, không phải trên số liệu do người biên soạn '
            'tự truy vấn. Muốn có con số, bạn phải tự tra bằng 中納言; một số kho '
            'yêu cầu đăng ký. Nếu một khẳng định trong sách cần con số mà bạn không '
            'thể kiểm lại, hãy coi nó là 要検証 chứ không phải 使用実態.')
    F.append(H3('Nhóm 3 — Nghiên cứu học thuật（研究知見）'))
    F += TB(None, ['Tác giả', 'Nhan đề / chủ đề', 'Năm', 'Định danh', 'Dùng cho'],
            [['Kubozono, H. (窪薗晴夫)', 'Trọng âm của từ ngoại lai (loanword accent)',
              '2002', '—', 'R19 · R31'],
             ['Kubozono, H.', 'Cấu trúc âm vị học của tiếng Nhật: rút ngắn từ ngoại lai',
              '2010', 'DOI 10.15084/00000559', 'R31 (đã sửa cách dẫn so với bản một)'],
             ['Đỗ Hoàng Ngân', 'Cảm nhận 長音・促音 của người học Việt Nam',
              '2015', '— (dẫn qua Sakata)', 'R9 · R66'],
             ['Nhiều tác giả', 'Nghiên cứu dụng học (pragmatics) tiếng Nhật: lịch sự, '
              'giảm nhẹ, hàm ý', '—', '—', 'R51 · R53']],
            colw=[18, 40, 8, 16, 18])
    F.append(H3('Nhóm 4 — Giáo trình và tài liệu sư phạm tham chiếu（参考教材）'))
    F += TB(None, ['Nguồn', 'Vai trò trong sách này', 'Có sao chép không'],
            [['JF 日本語教育スタンダード準拠教材（まるごと・いろどり等）',
              'Tham chiếu cách tổ chức theo Can-do và phạm vi chủ đề theo bậc',
              'Không. Sách này không sao chép đề bài, hội thoại hay bài tập.'],
             ['日本語能力試験 公式問題集・公式サイト',
              'Tham chiếu định dạng kỳ thi và tiêu chuẩn đạt',
              'Không. Không có đề thi hay câu hỏi nào được tái sử dụng.'],
             ['Các giáo trình quốc tế dùng phổ biến',
              'Tham chiếu thứ tự trình bày và thuật ngữ sư phạm',
              'Không. Sách này không sao chép nội dung.']],
            colw=[34, 44, 22])
    F.append(H3('Nhóm 5 — Từ điển và công cụ tra cứu（辞書・ツール）'))
    F += TB(None, ['Loại', 'Dùng cho', 'Lưu ý'],
            [['Từ điển có ghi trọng âm', 'R19 · R31 · R48',
              'Các từ điển ghi trọng âm khác nhau ở một số từ. Đã ghi 要検証.'],
             ['Từ điển có âm thanh thu sẵn', 'Kiểm tra trọng âm và vô thanh hoá',
              'Cách nhanh nhất để kiểm một khẳng định về phát âm.'],
             ['Công cụ nhập liệu (IME) theo romaji', 'R20 · R46',
              'Cáo thị 2025 nói rõ: cách nhập romaji <b>không</b> bị ảnh hưởng.']],
            colw=[24, 34, 42])
    F.append(H3('Nhóm 6 — Phông chữ và công cụ kỹ thuật（組版）'))
    F += TB(None, ['Hạng mục', 'Chi tiết', 'Giấy phép'],
            [['Phông tiếng Nhật', 'Noto Serif JP · Noto Sans JP (nhúng, bản biến thể tĩnh)',
              'SIL Open Font License 1.1'],
             ['Phông Latinh và IPA', 'Noto Sans Latinh', 'SIL Open Font License 1.1'],
             ['Hệ dựng sách', 'ReportLab (Python); dấu trang và mục lục liên kết nội bộ',
              'Mã nguồn mở']],
            colw=[22, 56, 22])
    F += VF('CẦN KIỂM CHỨNG ／ 要検証',
            'Nhóm 3 là phần yếu nhất của thư mục này và được ghi rõ như vậy. Ấn bản '
            'thứ hai <b>không</b> tra lại trực tiếp từng bài nghiên cứu được nhắc '
            'tên, và <b>không</b> thêm bất cứ tài liệu nào chưa từng được dùng trong '
            'bản thứ nhất, trừ những nguồn chính thức ở Nhóm 1 đã được kiểm tra cho '
            'ấn bản này. Nếu một mục ở Nhóm 3 không tra được, hãy coi khẳng định '
            'tương ứng là 要検証. ' + SOURCES_CHECKED)
    F.append(P('Ngày truy cập trong bảng: 17 tháng 9 năm 2026. Mọi địa chỉ và quy '
               'định tính đến ngày đó.', 'caption'))
    return F

# ===========================================================================
def numbering_note():
    """Editorial note documenting the R-section renumbering (brief: repair)."""
    F = []
    F.append(H3('Về việc đánh số lại các mục R21–R34 ／ 番号の整理について'))
    F.append(P('Ấn bản thứ nhất có một lỗi đánh số có hệ thống ở phần tra cứu: trong '
               'các mục R21 đến R34, tiêu đề tiểu mục mang số của mục <b>trước</b> nó '
               '(mục 20.x nằm trong R21, 21.x nằm trong R22, và cứ thế đến 33.x nằm '
               'trong R34), trong khi số bảng ở cùng các mục đó lại đúng. Mục R26 còn '
               'thiếu một số (không có R26.3) và lặp một số (R26.6 xuất hiện hai lần). '
               'Ấn bản thứ hai sửa cả hai, và sửa luôn các câu dẫn chiếu trong thân '
               'bài trỏ tới số cũ.'))
    F += TB('BẢNG R — NHỮNG GÌ ĐÃ SỬA', ['Hạng mục', 'Số lượng', 'Cách sửa', 'Không đổi'],
            [['Tiêu đề tiểu mục trong R21–R34', '48 tiêu đề',
              'Đổi số đầu cho khớp mục chứa nó (20.1 → 21.1 … 33.3 → 34.3)',
              'Nội dung, ví dụ và cách giải thích'],
             ['Số bảng trong R26', '3 nhãn bảng',
              'Đánh lại liên tục R26.1 → R26.7 (bỏ chỗ thiếu, bỏ chỗ lặp)',
              'Mọi bảng khác trong R26'],
             ['Câu dẫn chiếu trong thân bài', '15 cách viết, 27 chỗ',
              'Trỏ đúng số mới, và thống nhất ghi kèm chữ R khi dẫn bảng ở phần tra cứu',
              'Các dẫn chiếu vốn đã đúng (ví dụ dẫn sang mục 18.1)']],
            colw=[24, 14, 40, 22])
    F += CALL('QUY ƯỚC ĐÁNH SỐ ／ 番号の約束',
              'Tiểu mục đánh số theo mục chứa nó (mục 26 có 26.1, 26.2 …). Bảng cũng '
              'đánh số theo mục, nhưng theo <b>dãy riêng</b>: bảng R26.4 không nhất '
              'thiết nằm trong tiểu mục 26.4. Vì hai dãy dùng cùng một dạng “số.số”, '
              'khi dẫn chiếu cuốn sách này ghi rõ: “bảng R26.4” là bảng, “mục 26.6” là '
              'tiểu mục.', tone='indigo')
    F.append(P('Mức: 編集上の整理 — toàn bộ phần này ghi lại việc sửa số của ấn bản thứ '
               'hai. Không có nội dung chuyên môn nào bị thay đổi.', 'caption'))
    return F
