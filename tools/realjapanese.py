# -*- coding: utf-8 -*-
"""実際の日本語 / REAL JAPANESE — the five interludes.

At each level boundary the book stops teaching and shows what the level's
language does when people are actually using it.  One interlude per boundary
(N5 → N4 → N3 → N2 → N1), placed immediately after that level's Can-do map.

Every interlude has the same two anchors, because those two are the point:

  * a dialogue panel (``blocks.Dialogue``) — the language in use;
  * a 'why this sounds natural' block (``blocks.SpeechNote``) — the mechanism
    behind each choice, quoted line by line.

Everything else varies by level: the scene, the registers, and how much romaji
is printed (the level policy of R17/R20 — full at N5, gone by N1).

Honesty rules that hold for all five
------------------------------------
The dialogues are *editorial reconstructions*.  They are not transcripts, not
recordings, and not corpus examples — this edition queried no corpus.  Each
claim inside them carries one of the book's six confidence levels:

  公式        official document (文化審議会「敬語の指針」, 文化庁 surveys, JLPT)
  一般的な教育上の説明  the usual explanation in teaching materials
  編集上の整理  the editors' description of a pattern they wrote themselves
  要検証      not established — with the exact question left open

``HOWTO`` states this on the page, once, in 実際の日本語 ①; later interludes
carry a one-line pointer back to it instead of repeating it.
"""
from reportlab.platypus import (Paragraph, Spacer, PageBreak, NextPageTemplate,
                                CondPageBreak, KeepTogether)
import theme as T
from theme import guard
import blocks as B


def P(t, s='body', base='Body'):
    return Paragraph(guard(t, base), T.ST[s])


def H2(t):
    return B.SectionHead(t)


def H3(t):
    return [CondPageBreak(78), Paragraph(guard(t, 'BodyB'), T.ST['h3'])]


def H4(t):
    return [CondPageBreak(58), Paragraph(guard(t, 'SansB'), T.ST['h4'])]


def CALL(label, body, tone='indigo'):
    return [B.Callout(label, body, tone=tone), Spacer(1, 8)]


def VF(label, body):
    return [B.Verify(label, body), Spacer(1, 8)]


def TB(cap, hdr, rows, colw=None):
    out = [CondPageBreak(74)]
    if cap:
        out.append(Paragraph(guard(cap, 'SansB'), T.ST['tblcap']))
    out.append(B.make_table(hdr, rows, colw))
    out.append(Spacer(1, 10))
    return out


def DLG(turns, show_romaji=True):
    return [B.Dialogue(turns, show_romaji=show_romaji), Spacer(1, 12)]


def WHY(items):
    return [B.SpeechNote('なぜ ／ VÌ SAO NGHE TỰ NHIÊN ／ なぜ自然なのか', items),
            Spacer(1, 12)]


# The official text this feature leans on hardest.  Read in full for this
# edition on 2026-09-18 (bunka.go.jp, PDF, 77 pp.).
# Short inline form.  The full citation — and the fact that the whole 77-page
# text was read for this edition on 18/09/2026 — is printed once per interlude
# in its source box ('GIỚI HẠN CỦA MỤC NÀY') and again in R67 and the
# bibliography; repeating the full string under every item would bloat the page
# and read like boilerplate.
KEIGO_SHISHIN = '「敬語の指針」(文化審議会答申, 二〇〇七)'
FULL_KEIGO = ('文化審議会答申「敬語の指針」（平成19年2月2日, 文化庁, 全77頁）— '
              'đọc toàn văn cho ấn bản này ngày 18/09/2026')
SURVEY_FULL = ('文化庁「国語に関する世論調査」（平成18年2月調査）, dẫn trong '
               '「敬語の指針」第1章第2-2')

HOWTO = (
    'Năm mục 実際の日本語 nằm ở năm ranh giới bậc, ngay sau bản đồ năng lực. '
    'Chúng không dạy ngữ pháp mới. Chúng cho thấy ngữ pháp bạn đã học trông thế '
    'nào khi có người thật, mục đích thật và thời gian thật. Ba điều cần nói '
    'thẳng ngay từ đây. '
    '<b>Một: hội thoại trong năm mục này do ban biên tập soạn lại</b>, dựng theo '
    'các khuôn mẫu và quy tắc có nguồn — chủ yếu là 「敬語の指針」, các cuộc '
    'điều tra của 文化庁, và những mô tả ngữ pháp・dụng học phổ biến trong giáo '
    'trình. Chúng <b>không phải bản ghi âm và không phải trích từ corpus</b>: ấn '
    'bản này không truy vấn corpus nào. Vì vậy mục nào cũng ghi rõ chỗ nào có '
    'nguồn, chỗ nào là cách xếp đặt của người biên tập, chỗ nào còn phải kiểm '
    'chứng. <b>Hai: mỗi nhận định mang một trong sáu mức</b> — 公式 · 研究知見 · '
    '使用実態 · 一般的な教育上の説明 · 編集上の整理 · 要検証 — và mức được ghi '
    'ngay tại chỗ, không chỉ trong sổ đăng ký (R68). <b>Ba: romaji giảm dần '
    'theo bậc.</b> Mục ① và ② in romaji đầy đủ; ③ chỉ in ở những từ mới; ④ và ⑤ '
    'không in, đúng lộ trình đã nêu ở R17 và R20. Nếu bạn đọc mục ⑤ trước khi '
    'quen mặt chữ, hãy bắt đầu từ ①.')

# ===========================================================================
def real_japanese_1():
    """実際の日本語 ① — N5: a convenience store at 20:40."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('実際の日本語 ① ／ REAL JAPANESE — Cửa hàng tiện lợi ／ コンビニ'))
    F.append(P('Bậc N5 kết thúc ở trang trước. Cảnh đầu tiên là cảnh bạn sẽ gặp '
               'trong tuần đầu tiên ở Nhật: 20 giờ 40, một cửa hàng tiện lợi, một '
               'hộp cơm, một chai trà. Bạn đã có đủ ngữ pháp cho cảnh này. Điều '
               'còn thiếu là biết ai nói câu gì, và vì sao.', 'lead'))
    F += CALL('CÁCH ĐỌC MỤC NÀY ／ この欄の読み方', HOWTO, tone='gold')

    F += H3('① · 1  Bối cảnh')
    F.append(P('Nhân viên đứng sau quầy. Bạn đặt hộp cơm lên quầy, chưa nói gì. '
               'Những gì diễn ra sau đó là một cuộc trao đổi ngắn nhất có thể — '
               'ngắn hơn nhiều so với hội thoại trong giáo trình, và không vì thế '
               'mà kém lịch sự.'))
    F.append(P('Một điều về phía bạn trước khi đọc: bạn <b>không</b> cần nói nhiều. '
               'Trong cảnh này, ba câu của khách là đủ, và hai trong số đó chỉ có '
               'hai từ.'))

    F += H3('① · 2  Hội thoại')
    F += DLG([
        dict(sp='店員', ja='いらっしゃいませ。', ro='irasshaimase.',
             vi='(câu chào của nhân viên)'),
        dict(sp='客', ja='すみません、これ、お願いします。',
             ro='sumimasen, kore, onegaishimasu.',
             vi='Xin lỗi, cái này, cho tôi với ạ.'),
        dict(sp='店員', ja='お箸はお付けしますか。', ro='o-hashi wa o-tsuke shimasu ka.',
             vi='Anh/chị có lấy đũa không ạ?'),
        dict(sp='客', ja='大丈夫です。', ro='daijōbu desu.', vi='Không cần đâu ạ.'),
        dict(sp='店員', ja='レジ袋はご利用になりますか。',
             ro='reji-bukuro wa go-riyō ni narimasu ka.',
             vi='Anh/chị có dùng túi ni-lông không ạ?'),
        dict(sp='客', ja='いいえ、大丈夫です。', ro='iie, daijōbu desu.',
             vi='Không, không cần ạ.'),
        dict(sp='店員', ja='お弁当、温めますか。', ro='o-bentō, atatamemasu ka.',
             vi='Cơm hộp, anh/chị có muốn hâm không ạ?'),
        dict(sp='客', ja='お願いします。', ro='onegaishimasu.', vi='Vâng, làm ơn.'),
        dict(sp='店員', ja='お支払いは現金ですか、カードですか。',
             ro='o-shiharai wa genkin desu ka, kādo desu ka.',
             vi='Anh/chị trả tiền mặt hay thẻ ạ?'),
        dict(sp='客', ja='カードで。', ro='kādo de.', vi='Bằng thẻ.'),
        dict(sp='店員', ja='こちら、レシートです。ありがとうございました。',
             ro='kochira, reshīto desu. arigatō gozaimashita.',
             vi='Đây là hoá đơn ạ. Cảm ơn anh/chị.'),
        dict(sp='客', ja='どうも。', ro='dōmo.', vi='Cảm ơn.'),
    ])

    F += H3('① · 3  Vì sao nghe tự nhiên')
    F.append(P('Khối dưới đây dùng đúng thiết bị mà cuốn sách đã có từ ấn '
               'bản thứ nhất — những khung 「なぜ」 trả lời một câu hỏi duy '
               'nhất: vì sao cách nói này nghe tự nhiên. Ở các mục tra cứu '
               '(R28, R36, R44, R51) mỗi khung trả lời một câu hỏi. Ở đây, '
               'cùng thiết bị đó được mở ra theo từng dòng của một cuộc nói '
               'chuyện thật, để bạn thấy cơ chế hoạt động liên tục chứ không '
               'rời rạc.'))
    F += WHY([
        ('いらっしゃいませ',
         'Đây không phải câu chào gửi riêng cho bạn. Nó là tín hiệu cho cả gian '
         'hàng biết rằng nhân viên đã nhận ra có khách — trong nhiều cửa hàng nó '
         'được nói ra từ một quầy khác, hoặc qua loa, khi người nói không nhìn '
         'thấy bạn. Vì vậy bạn không phải đáp lại, và người Việt mới sang thường '
         'mất vài tuần để thôi cảm thấy có lỗi khi không đáp. <i>(編集上の整理)</i>'),
        ('お箸はお付けしますか。',
         'この お…します là dạng của <b>謙譲語Ⅰ</b> — dạng hạ hành động <i>của '
         'chính người nói</i> xuống, không nâng ai lên. Nhân viên hạ việc mình '
         'đưa đũa cho bạn. 「敬語の指針」第2章 liệt kê お(ご)……する là dạng chung '
         'của 謙譲語Ⅰ, và dạng này chỉ dựng được khi hành động là của mình: cũng '
         'tài liệu đó cảnh báo rằng dùng お…する cho hành động của <i>đối '
         'phương</i> là sai — phải là お持ちになりますか, không phải お持ちします'
         'か. Biết điều này thì bạn nghe được vì sao câu của nhân viên không hề '
         'hạ thấp bạn: nó chỉ đặt việc phục vụ ở phía người nói. '
         '<i>(公式 — ' + KEIGO_SHISHIN + ')</i>'),
        ('大丈夫です。',
         'Câu trả lời không có từ nào nghĩa là "không". Câu hỏi đã cung cấp động '
         'từ, nên 大丈夫です được hiểu là 「(お箸は)大丈夫です」 — "việc đó, ở '
         'trạng thái này, là ổn", tức là không cần. Cơ chế này (câu hỏi cấp phép '
         'cho sự lược bỏ) là chìa khoá của cả cảnh: phần lớn câu trả lời trong '
         'dịch vụ ngắn vì câu hỏi đã nói phần còn lại. <b>Nhưng</b> cùng một từ '
         'này có thể nghĩa "vâng, ổn" khi câu hỏi là về tình trạng của bạn '
         '(具合は大丈夫ですか). Nếu sợ nhầm, nói いいえ、大丈夫です — thêm một từ, '
         'hết mơ hồ. Xem thêm bảng R54.2 về hai nghĩa này. <i>(編集上の整理 · '
         '一般的な教育上の説明)</i>'),
        ('温めますか。→ お願いします。',
         'お願いします không phải "làm ơn" suông; nghĩa của nó là <i>đặt sự việc '
         'vào tay người đối diện</i>. Vì vậy nó nhận được mọi đề nghị mà không '
         'cần lặp lại động từ: hâm cơm, lấy đũa, gọi món, nhờ giữ hành lý. Đây '
         'là câu hữu dụng nhất trong mọi câu tiếng Nhật ở cửa hàng, và cũng là '
         'câu người học bỏ sót nhiều nhất. <i>(編集上の整理)</i>'),
        ('カードで。',
         'Câu bị cắt còn hai từ, nhưng <b>không</b> phải vì thân mật: câu hỏi ngay '
         'trước đã nói 「お支払いは…ですか」, nên カードで vẫn đang trả lời trong '
         'khung lịch sự です・ます mà nhân viên đã lập. Sự lược bỏ ở đây do ngữ '
         'cảnh cấp phép, không do hạ đăng ký. <i>(一般的な教育上の説明)</i>'),
        ('お箸 · お弁当 · お支払い · お会計',
         'Những お này là <b>美化語</b> — loại thứ năm trong năm loại kính ngữ '
         'của 「敬語の指針」. Nó không nâng người nào và không hạ ai: nó "làm đẹp" '
         'bản thân sự vật. Đó là lý do ngôn ngữ dịch vụ rắc お khắp nơi, và cũng '
         'là lý do お này không bắt buộc với bạn. <i>(公式 — ' + KEIGO_SHISHIN +
         ', 第2章第5)</i>'),
    ])
    F += CALL('MỘT CON SỐ CÓ NGUỒN ／ 出典のある数字',
              'Chuyện お có bắt buộc không đã được đếm. Trong 文化庁「国語に関する'
              '世論調査」(平成18年2月調査), hỏi người dân có nói お弁当 hay không: '
              'nam giới mọi thế hệ chỉ 10–30 % nói có, trong khi nữ giới mọi thế '
              'hệ ở mức 70–80 %. Điều đó cho thấy 美化語 là chuyện <b>tùy người, '
              'tùy vùng, tùy thế hệ</b> — không phải chuyện đúng/sai. Cảnh báo '
              'thường gặp ngược lại cũng đúng: tài liệu đó cũng ghi rằng nếu bạn '
              'buộc cả hai giới nói theo một khuôn thì chính là điều mà 「敬語の '
              '指針」第1章第2-2 gọi là quan niệm áp đặt theo giới tính và thế hệ, '
              'và nó dặn tránh cách áp đặt đó. <i>(公式 — ' + SURVEY_FULL + ')</i>',
              tone='teal')

    F += H3('① · 4  Giáo trình dạy gì — quầy thu ngân nói gì')
    F += TB('BẢNG RJ1.1 — CÙNG MỘT VIỆC, HAI CÁCH NÓI',
            ['Giáo trình (đúng ngữ pháp)', 'Ngoài quầy (mặc định của dịch vụ)',
             'Vì sao chọn cách thứ hai'],
            [['これをください。', 'これ、お願いします。',
              'ください là động từ "đưa cho tôi" — nói đúng, nhưng đặt trọng '
              'tâm vào việc nhận. お願いします đặt trọng tâm vào việc nhờ.'],
             ['はい、わかりました。', 'お願いします。／ はい。',
              'Nhận một đề nghị nhỏ không cần một mệnh đề đầy đủ; わかりました '
              'nghe như bạn đang xác nhận một chỉ thị.'],
             ['〜は要りません。', '大丈夫です。',
              'Từ chối trực tiếp một đề nghị nhỏ được, nhưng nghe khô hơn. Lưu ý '
              'tính hai nghĩa của 大丈夫です (mục ①·3).'],
             ['いくらですか。', '(giá đã in trên kệ) · 「お会計をお願いします。」',
              'Ở cửa hàng tiện lợi, câu bạn cần không phải câu hỏi giá mà là câu '
              'xin tính tiền.'],
             ['ありがとうございました。', 'どうも。',
              'Khách nói ngắn. Nói dài không sai — chỉ là rất ít người nói vậy. '
              '<i>(編集上の整理 — ấn bản này không đo tần suất.)</i>']],
            colw=[28, 32, 40])

    F += H3('① · 5  Dùng được ngay')
    F += TB('BẢNG RJ1.2 — NĂM CỤM ĐỦ DÙNG CẢ CẢNH',
            ['Cụm', 'Dùng khi', 'Đừng dùng khi'],
            [['これ、お願いします。', 'Chỉ vào món, đưa ra hiệu cho nhân viên.',
              'Khi cần nói rõ số lượng — lúc đó: これ、一つ、お願いします。'],
             ['お願いします。', 'Nhận một đề nghị; gọi món; nhờ một việc nhỏ.', '—'],
             ['大丈夫です。', 'Từ chối một đề nghị nhỏ.',
              'Khi câu hỏi là về tình trạng của bạn — dễ bị hiểu là "tôi ổn". '
              'Nói いいえ、大丈夫です.'],
             ['〜で（お願いします）。', 'Trả lời phương thức: カードで。／ 現金で。',
              '—'],
             ['すみません。', 'Gọi nhân viên; xin lỗi khi làm phiền.',
              '— (sáu việc của すみません: xem R54.1)']],
            colw=[22, 42, 36])

    F += VF('GIỚI HẠN CỦA MỤC NÀY ／ この欄の限界',
            '<b>Có nguồn:</b> ' + FULL_KEIGO + ' — các dạng kính ngữ (第2章) · '
            'con số về 美化語 (' + SURVEY_FULL + '). <b>Là xếp đặt của ban biên tập:</b> '
            'chức năng của いらっしゃいませ, cách đọc 大丈夫です trong ngữ cảnh '
            'này, hai bảng đối chiếu. <b>Không có nguồn và cần kiểm chứng:</b> '
            '(a) biến thể thật của từng chuỗi cửa hàng — 「お箸はお付けしますか」 · '
            '「お箸お付けしますか」 · 「お箸はご利用ですか」 đều tồn tại; ấn bản '
            'này không có nguồn nào đo được cái nào phổ biến hơn; (b) 「〜になり'
            'ます」 (こちら、○○円になります) — cách nói này được báo chí và các '
            'sách hướng dẫn 敬語 bàn nhiều, nhưng 「敬語の指針」 mà ấn bản này đã '
            'tra <b>không</b> xử lý riêng trường hợp này, nên sách không kết luận. '
            'Muốn chắc chắn, dùng でございます.')
    F.append(P('Mức của mục này: 公式 cho các dạng kính ngữ và con số · '
               '一般的な教育上の説明 cho cơ chế lược bỏ · 編集上の整理 cho toàn bộ '
               'hội thoại và hai bảng · 要検証 cho hai điểm ở khung trên.', 'caption'))
    return F


# ===========================================================================
def real_japanese_2():
    """実際の日本語 ② — N4: ordering and paying in a restaurant."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('実際の日本語 ② ／ REAL JAPANESE — Quán ăn ／ 飲食店'))
    F.append(P('Bậc N4 vừa kết thúc: bạn đã có 〜ていただく, 〜ておく, điều kiện, '
               'nhờ vả. Cảnh này dùng gần hết chúng, và dùng thêm một thứ mà giáo '
               'trình thường để sau: cách nói <b>quyết định</b> trước mặt người '
               'phục vụ.', 'lead'))
    F.append(P('Cách đọc mục này như mục ①: hội thoại do ban biên tập soạn lại, '
               'mỗi nhận định có mức.', 'caption'))

    F += H3('② · 1  Bối cảnh')
    F.append(P('Bốn người, một quán ăn gia đình lúc 12 giờ 20. Bạn là người gọi '
               'món. Trong cảnh này bạn phải làm ba việc bằng tiếng Nhật: hỏi ý '
               'nhân viên, chốt món, và trả tiền theo cách của bạn.'))

    F += H3('② · 2  Hội thoại')
    F += DLG([
        dict(sp='店員', ja='何名様ですか。', ro='nan-mei-sama desu ka.',
             vi='Anh/chị đi mấy người ạ?'),
        dict(sp='客', ja='四人です。', ro='yo-nin desu.', vi='Bốn người.'),
        dict(sp='店員', ja='こちらへどうぞ。', ro='kochira e dōzo.',
             vi='Mời anh/chị lối này.'),
        dict(sp='店員', ja='ご注文はお決まりですか。',
             ro='go-chūmon wa o-kimari desu ka.',
             vi='Anh/chị đã chọn món chưa ạ?'),
        dict(sp='客', ja='すみません、おすすめは何ですか。',
             ro='sumimasen, o-susume wa nan desu ka.',
             vi='Xin lỗi, món nào được giới thiệu ạ?'),
        dict(sp='店員', ja='そうですね、日替わり定食が人気です。',
             ro='sō desu ne, higawari teishoku ga ninki desu.',
             vi='Để xem, cơm phần theo ngày được ưa ạ.'),
        dict(sp='客', ja='じゃあ、それをお願いします。あと、生ビール一つ。',
             ro='jā, sore o onegaishimasu. ato, nama-bīru hitotsu.',
             vi='Vậy cho tôi món đó. Thêm một bia tươi.'),
        dict(sp='店員', ja='少々お待ちくださいませ。',
             ro='shōshō o-machi kudasaimase.', vi='Xin đợi một chút ạ.'),
        dict(sp='', ja='（thức ăn được mang ra）', vi=''),
        dict(sp='店員', ja='お待たせいたしました。日替わり定食でございます。',
             ro='o-matase itashimashita. higawari teishoku de gozaimasu.',
             vi='Xin lỗi đã để anh/chị đợi. Đây là cơm phần theo ngày ạ.'),
        dict(sp='客', ja='どうも。いただきます。', ro='dōmo. itadakimasu.',
             vi='Cảm ơn. Tôi dùng bữa.'),
        dict(sp='客', ja='すみません、お会計をお願いします。別々にできますか。',
             ro='sumimasen, o-kaikei o onegaishimasu. betsubetsu ni dekimasu ka.',
             vi='Xin lỗi, cho tôi tính tiền. Có thể tách riêng được không ạ?'),
        dict(sp='店員', ja='はい、できますよ。', ro='hai, dekimasu yo.',
             vi='Vâng, được ạ.'),
    ])

    F += H3('② · 3  Vì sao nghe tự nhiên')
    F += WHY([
        ('それをお願いします。／ 生ビール一つ。',
         'Hai cách nói hai mức khác nhau. それをお願いします là câu đầy đủ, dùng '
         'cho món chính. 生ビール一つ bỏ luôn trợ từ và động từ — trong quán, '
         'danh từ + số lượng là đủ, vì hành động "gọi" đã nằm trong ngữ cảnh. '
         'Người mới học thường nói 生ビールを一つください — đúng, nhưng dài hơn '
         'nhịp nói thật. <i>(編集上の整理)</i>'),
        ('おすすめは何ですか。',
         'Câu hỏi trực tiếp này <b>được</b> dùng với nhân viên, vì bạn đang hỏi '
         'thông tin, không đòi hỏi gì. Với cấp trên thì phải mềm hơn: 何かおすすめ'
         'はありますか, hoặc 〜でしょうか (R51, R44). Cùng một ý, hai mức lịch sự '
         'khác nhau theo người nghe, không theo nội dung. '
         '<i>(一般的な教育上の説明)</i>'),
        ('別々にできますか。',
         'Đây là câu hỏi về <b>quy định của quán</b>, không phải yêu cầu nhân viên '
         'làm gì, nên できますか vừa đủ và không cần kính ngữ nào. Nếu bạn muốn '
         'khung "nhờ vả": 別々にしていただけますか — vẫn đúng, và nghe như một '
         'lời nhờ. Đây là ví dụ rõ nhất của điều sẽ gặp suốt N3→N1: cùng một việc, '
         'chọn khung nào là chọn quan hệ. <i>(編集上の整理)</i>'),
        ('お待たせいたしました。',
         'So với お待たせしました, dạng いたす là <b>謙譲語Ⅱ（丁重語）</b> — nó '
         'không nâng ai, nó làm câu nói với <i>người nghe</i> trở nên trọng hơn. '
         'Tài liệu chính thức cũng ghi rõ: 「お(ご)……いたす」 mang cả hai tính chất, '
         '謙譲語Ⅰ (nâng người được hướng tới) và 謙譲語Ⅱ (trọng hoá người nghe) — '
         'vì vậy nó là dạng mạnh nhất trong nhóm お…する mà vẫn tự nhiên. '
         '<i>(公式 — ' + KEIGO_SHISHIN + ', 第2章第3【補足イ】)</i>'),
        ('でございます。',
         'でございます là 丁寧語, nhưng ở mức trọng hơn です・ます — tài liệu '
         'chính thức xếp nó <i>ngang mức</i> 謙譲語Ⅱ (丁重語). Đó là lý do các '
         'câu giới thiệu món của nhân viên kết thúc bằng でございます, và cũng là '
         'lý do nó an toàn hơn 「〜になります」. <i>(公式 — 同上, 第2章第4)</i>'),
        ('いただきます。',
         'Không phải câu tôn giáo; đây là 挨拶 cố định. Nhưng biết gốc của nó thì '
         'hiểu được vì sao nó đứng ở đầu bữa ăn: いただく là 謙譲語Ⅰ của もらう — '
         'nghĩa đen là "tôi nhận". Cùng động từ đó xuất hiện trong 〜ていただく, và '
         'đó chính là lý do dạng này nghe như một ân huệ: 「敬語の指針」ghi rõ '
         'いただく mang thêm nghĩa "được ban cho". Một câu chào, một mẫu ngữ pháp, '
         'một động từ. <i>(公式 — 同上, 第2章第2【補足】)</i>'),
        ('少々お待ちくださいませ。',
         'くださいませ là biến thể trọng hơn của ください, gắn chặt với ngôn ngữ '
         'dịch vụ. Người học không cần dùng nó; nhưng cần nhận ra nó, vì trong '
         'quán và cửa hàng bạn sẽ nghe nó liên tục. <i>(編集上の整理)</i>'),
    ])

    F += H3('② · 4  Giáo trình dạy gì — quán nói gì')
    F += TB('BẢNG RJ2.1 — GỌI MÓN VÀ TRẢ TIỀN',
            ['Giáo trình', 'Trong quán', 'Chênh lệch nằm ở đâu'],
            [['〜をください。', 'それをお願いします。',
              'ください nhận hàng; お願いします nhờ việc. Quán ăn là chỗ nhờ '
              'việc.'],
             ['何がおいしいですか。', 'おすすめは何ですか。',
              'おすすめ là từ cố định cho việc này; hỏi "cái gì ngon" nghe như '
              'hỏi một sự thật khách quan.'],
             ['お金を払いたいです。', 'お会計をお願いします。',
              'Danh từ hoá お会計 + お願いします — mẫu cố định, dùng luôn được.'],
             ['いくらですか。', '(hoá đơn) お会計は別々にお願いします。',
              'Trong quán bạn không hỏi giá, bạn gọi việc tính tiền.'],
             ['ありがとうございます。', 'ごちそうさまでした。',
              'Câu kết thúc bữa ăn không phải "cảm ơn" mà là "tôi đã được thết" — '
              'cùng họ いただく ở trên. <i>(編集上の整理)</i>']],
            colw=[24, 34, 42])

    F += H3('② · 5  Dùng được ngay')
    F += TB('BẢNG RJ2.2 — SÁU CỤM CHO CẢ BỮA ĂN',
            ['Cụm', 'Làm được gì', 'Ghi chú'],
            [['〜名です。', 'Trả lời câu hỏi số người.',
              '何名様ですか → 四人です. 人 và 名 đều đúng; 名 trang trọng hơn.'],
             ['おすすめは何ですか。', 'Nhờ nhân viên chọn giúp.', 'Đừng dùng với '
              'cấp trên; xem ②·3.'],
             ['〜をお願いします。', 'Chốt món, gọi thêm, gọi tính tiền.',
              'Mẫu câu hữu dụng nhất trong quán.'],
             ['〜を一つ。／ 〜一つ。', 'Gọi thêm một món.',
              'Danh từ + số lượng là đủ trong hội thoại.'],
             ['別々にできますか。', 'Hỏi quy định tách hoá đơn.',
              'Vẫn đúng nếu đổi thành 〜ていただけますか.'],
             ['お会計をお願いします。', 'Gọi tính tiền.', 'Rời quán: '
              'ごちそうさまでした。']],
            colw=[24, 36, 40])

    F += VF('GIỚI HẠN CỦA MỤC NÀY ／ この欄の限界',
            '<b>Có nguồn:</b> ' + FULL_KEIGO + ' — 謙譲語Ⅱ và でございます · いたす mang hai tính chất · '
            'いただく mang nghĩa "được ban cho" (' + KEIGO_SHISHIN + ', 第2章). '
            '<b>Là xếp đặt của ban biên tập:</b> toàn bộ hội thoại, mức độ trang '
            'trọng tương đối giữa các cách gọi món. <b>Cần kiểm chứng:</b> mức độ '
            'phổ biến của 生ビール一つ (bỏ trợ từ) so với 生ビールを一つ — cả hai '
            'đều gặp, ấn bản này không đo được tỉ lệ. Và các mẫu cố định của từng '
            'chuỗi quán ăn khác nhau rất nhiều: hãy nghe mẫu của chính quán bạn '
            'hay đến, đừng lấy mục này làm bản chuẩn duy nhất.')
    F.append(P('Mức của mục này: 公式 cho kính ngữ · 一般的な教育上の説明 cho một '
               'phần ②·3 · 編集上の整理 cho hội thoại và hai bảng · 要検証 cho các '
               'điểm ở khung trên.', 'caption'))
    return F


# ===========================================================================
def real_japanese_3():
    """実際の日本語 ③ — N3: asking, being refused, and ウチ/ソト."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('実際の日本語 ③ ／ REAL JAPANESE — Nhờ việc và bị từ chối ／ 依頼と断り'))
    F.append(P('N3 là bậc của 行間 — khoảng trống giữa các dòng. Cảnh này là chỗ '
               'khoảng trống đó quyết định: bạn nhờ một việc và bị từ chối, rồi '
               'phải nói câu tiếp theo. Giáo trình dạy câu nhờ. Câu thứ ba sau '
               'lời từ chối thì hầu như không giáo trình nào dạy.', 'lead'))
    F.append(P('Từ mục này, romaji chỉ còn in ở những từ mới. Cách đọc mục: như '
               'mục ①.', 'caption'))

    F += H3('③ · 1  Bối cảnh')
    F.append(P('Bạn là nhân viên năm thứ hai. 16 giờ 40, bạn cần một người cấp '
               'trên xem qua một tài liệu trước 18 giờ. Người đó là 田中, hơn bạn '
               'bốn tuổi, không phải cấp trên trực tiếp của bạn. Bạn chỉ có hai '
               'lượt để thuyết phục — không phải vì người ta khó tính, mà vì '
               'chiều nay ai cũng có việc.'))

    F += H3('③ · 2  Hội thoại — nhờ việc và nhận lời từ chối')
    F += DLG([
        dict(sp='私', ja='田中さん、ちょっとお願いがあるんですが。',
             vi='Anh Tanaka, em có chút việc muốn nhờ ạ.', note='〜んですが: nêu ra '
             'rằng có một việc, rồi dừng — lời nhờ còn chưa tới.'),
        dict(sp='田中', ja='うん、何？', vi='Ừ, gì thế?'),
        dict(sp='私', ja='この資料、今日中に目を通していただけますか。',
             vi='Tài liệu này, anh xem qua giúp em trong hôm nay được không ạ?',
             note='目を通す (めをとおす) = đọc lướt qua.'),
        dict(sp='田中', ja='今日中は… ちょっと難しいかな。午後は外出するんだよね。',
             vi='Trong hôm nay thì… hơi khó nhỉ. Chiều anh phải ra ngoài.'),
        dict(sp='私', ja='あ、そうですか。では、明日の朝でも大丈夫ですか。',
             vi='À, vâng ạ. Vậy sáng mai có được không ạ?'),
        dict(sp='田中', ja='明日の朝なら大丈夫。ごめんね、今日中は無理そう。',
             vi='Sáng mai thì được. Xin lỗi nhé, hôm nay chắc không kịp.'),
        dict(sp='私', ja='いえいえ、こちらこそ。明日の朝、お願いします。助かります。',
             vi='Không có gì ạ, em mới là người phải cảm ơn. Sáng mai nhờ anh ạ. '
                'Đỡ cho em quá.'),
    ], show_romaji=False)

    F += H3('③ · 3  Cảnh thứ hai — nói về người trong cùng công ty')
    F.append(P('Cùng buổi chiều đó, có điện thoại từ đối tác. Trong tiếng Việt '
               'bạn chỉ cần nói "sếp chưa về"; trong tiếng Nhật, chuyện ai được '
               'nâng lên, ai không, là chuyện ngữ pháp.'))
    F += DLG([
        dict(sp='取引先', ja='いつもお世話になっております。〇〇商事の佐藤です。',
             vi='Cảm ơn quý công ty vẫn luôn giúp đỡ. Tôi là Sato, công ty 〇〇.'),
        dict(sp='私', ja='お世話になっております。株式会社△△のグエンです。',
             vi='Cảm ơn anh. Tôi là Nguyễn, công ty △△.'),
        dict(sp='取引先', ja='田中部長はいらっしゃいますか。',
             vi='Anh Tanaka (trưởng phòng) có ở đó không ạ?',
             note='Người ngoài nâng 田中 lên bằng いらっしゃる — đúng, vì 田中 là '
                  'người phía bạn.'),
        dict(sp='私', ja='申し訳ございません、田中はただいま外出しております。'
                         '戻りましたら、こちらからお電話差し上げます。',
             vi='Xin lỗi anh, anh Tanaka hiện đang ra ngoài. Khi anh ấy về, tôi sẽ '
                'gọi lại ạ.',
             note='Phía mình thì KHÔNG nâng: 田中, không phải 田中部長でいらっしゃる。'),
    ], show_romaji=False)

    F += H3('③ · 4  Vì sao nghe tự nhiên')
    F += WHY([
        ('ちょっとお願いがあるんですが。',
         'Câu này không chứa lời nhờ nào cả. Nó chỉ báo rằng có một việc, rồi để '
         'người nghe chọn lượt tiếp theo. ん(の) + です khung hoá "có một chuyện", '
         'が để lửng. Vì vậy người nghe luôn có một lượt để nói "bây giờ hơi bận" '
         'mà không phải đối mặt với một yêu cầu đã hoàn chỉnh. Đây là cơ chế chung '
         'của 前置き trong tiếng Nhật, không phải một mẹo riêng. '
         '<i>(一般的な教育上の説明)</i>'),
        ('今日中は… ちょっと難しいかな。',
         'Ba lớp giảm nhẹ chồng lên nhau, và chúng làm ba việc khác nhau. '
         'は <b>khoanh phạm vi</b>: chỉ "trong hôm nay" là khó, không phải cả con '
         'người bạn nhờ. ちょっと <b>hạ mức</b>. かな <b>không khẳng định</b> — '
         'người nói còn để ngỏ. Rồi điều quan trọng nhất: lý do đưa ra là hoàn '
         'cảnh <i>của người nói</i> (午後は外出する), không phải đánh giá về lời '
         'nhờ của bạn. Người nghe không bị từ chối về mặt thể diện; việc của họ '
         'bị từ chối. <i>(編集上の整理)</i>'),
        ('では、明日の朝でも大丈夫ですか。',
         'Lượt này là lượt mà người học hay bỏ trống. Phản xạ tự nhiên của người '
         'mới học là hỏi "vì sao" hoặc dừng lại. Hỏi なぜ buộc người nói phải '
         'biện minh cho một câu họ vừa cố ý nói ra mềm — đúng cái họ tránh. Thay '
         'vào đó, đưa <b>một phương án mới, rẻ hơn cho họ</b>. でも ở đây nghĩa là '
         '"kể cả … (thì cũng được)" — bạn hạ yêu cầu xuống mức dễ chấp nhận hơn. '
         '<i>(編集上の整理)</i>'),
        ('明日の朝なら大丈夫。',
         'なら: điều kiện trở thành đề tài — "nếu là sáng mai thì ổn". So với '
         '明日の朝は大丈夫 ("còn sáng mai thì ổn" — は khoanh đề tài), なら kết '
         'câu ở đúng điều kiện bạn vừa đưa ra, nên câu trả lời nghe như một kết '
         'luận logic hơn là một ân huệ. Ở cảnh tiếp theo, 戻りましたら dùng cùng '
         'một phép: đặt điều kiện trước rồi mới hứa. <i>(一般的な教育上の説明)</i>'),
        ('田中部長はいらっしゃいますか。→ 田中は外出しております。',
         'Đây là nguyên tắc <b>(1) 自分側は立てない</b> của 「敬語の指針」: người '
         'phía mình, dù chức vụ cao hơn bạn, cũng <b>không</b> dùng 尊敬語 khi nói '
         'với người ngoài. Không phải vì coi nhẹ anh ấy, mà vì 尊敬語 là để nâng '
         '<i>phía người nghe</i>. Việc bạn đang tiếp đối tác được thực hiện bằng '
         'phần thứ hai của câu: 申し訳ございません, 外出しております (謙譲語Ⅱ おる), '
         '差し上げます — những dạng hạ phía mình và trọng hoá người nghe. Phiên '
         'bản sai thường gây ấn tượng kỳ lạ nhất với người bản ngữ: 田中部長は外出'
         'していらっしゃいます — tự nâng sếp nhà mình lên trước mặt đối tác. '
         '<i>(公式 — ' + KEIGO_SHISHIN + ', 第2章第6 (1))</i>'),
        ('先輩が遊びにいらっしゃった → 先輩が遊びに来た。',
         'Điều tinh tế thứ hai, cũng từ tài liệu đó: chỉ nâng người thứ ba khi '
         'người nghe <i>cũng</i> biết và cũng nhìn nhận người đó là người cần nâng. '
         'Kể cho một người bạn về một người bạn không quen: 「昨日、高校の時の先輩'
         'が遊びにいらっしゃった」 nghe không ổn; tài liệu chính thức khuyên dùng '
         '来た. Người học N3 hay chưa để ý dạng lỗi ngược này — rải 尊敬語 khắp nơi '
         'cho "chắc ăn". 敬語 không phải thuốc bổ. <i>(公式 — 同上, 第2章第6 (3)イ)'
         '</i>'),
    ])
    F += CALL('VÙNG MIỀN: KHÔNG CÓ KÍNH NGỮ KHÔNG CÓ NGHĨA LÀ KHÔNG LỊCH SỰ ／ 方言の敬語',
              'Cùng một tài liệu chính thức, ngay chương đầu, ghi hai điều mà người '
              'học ở Tokyo thường không được nói. Một: tiếng Kansai dùng <b>〜はる</b> '
              'như một dạng gần với 尊敬語, và nó dùng được cả với người trong nhà '
              'mình — ví dụ 「うちの父さん、家にいてはります」; trong tiếng chuẩn '
              'bạn sẽ không nâng bố mình trước người ngoài. Đây không phải lỗi, mà '
              'là một hệ thống khác có cách dùng khác. Hai: nhiều vùng Đông Bắc và '
              'Bắc Kantō không có đủ các dạng 尊敬語・謙譲語 mà tiếng chuẩn có, '
              'nhưng sự kính trọng được thể hiện bằng 文末表現 và ngữ điệu — ví dụ '
              '「そだなし・そだのう」. Kết luận của 文化審議会 rất rõ: đó là những '
              'phương tiện quý của địa phương, cần được giữ. Với người học, điều đó '
              'nghĩa là: 「không có kính ngữ = bất lịch sự」 là nhận định về '
              '<i>tiếng chuẩn</i>, không phải về tiếng Nhật. <i>(公式 — ' +
              KEIGO_SHISHIN + ', 第1章第2-1)</i>', tone='teal')

    F += H3('③ · 5  Giáo trình dạy gì — văn phòng nói gì')
    F += TB('BẢNG RJ3.1 — NHỜ, TỪ CHỐI, VÀ NÓI VỀ NGƯỜI CỦA MÌNH',
            ['Giáo trình (đúng)', 'Thực tế', 'Khác ở đâu'],
            [['来てください。', '来ていただけますか。／ 来てくださいませんか。',
              'ください là mệnh lệnh lịch sự. Ở N3 trở lên nó vẫn đúng, nhưng '
              'trong công việc nó là câu của người có quyền.'],
             ['無理です。', '今日中は、ちょっと難しいかな。',
              'Câu từ chối thẳng vẫn tồn tại; nhưng khi bạn cần nhờ vả lần sau, '
              'cách nói mềm giữ được quan hệ.'],
             ['理由を教えてください。', 'では、明日の朝でも大丈夫ですか。',
              'Hỏi lý do là điều hợp lý về logic và tốn kém về quan hệ. Người '
              'bản ngữ thường chuyển thẳng sang phương án mới.'],
             ['田中部長は外出しています。', '田中は外出しております。',
              'Không nâng người phía mình khi nói với người ngoài; dùng 謙譲語Ⅱ '
              'để trọng hoá người nghe.'],
             ['わかりません。', '確認して、あらためてご連絡します。',
              'Câu thật thà này đóng sập lượt nói. Câu sau vẫn đúng sự thật và '
              'mở ra một lượt mới. <i>(編集上の整理)</i>']],
            colw=[24, 34, 42])

    F += H3('③ · 6  Dùng được ngay')
    F += TB('BẢNG RJ3.2 — NĂM KHUÔN CHO VIỆC NHỜ VẢ',
            ['Khuôn', 'Dùng khi', 'Lưu ý'],
            [['〜んですが。', 'Mở đầu mọi lời nhờ.',
              'Không đặt động từ nhờ vào câu này; để lượt sau.'],
             ['〜ていただけますか。', 'Nhờ một việc, mức trung.',
              'いただく mang nghĩa "được ban cho" — nên nó nhờ, chứ không ra lệnh.'],
             ['〜ていただけませんか。', 'Nhờ một việc, mức cao hơn.',
              'Dạng phủ định nghe dè dặt hơn, vì nó thừa nhận việc từ chối.'],
             ['〜は、ちょっと難しいかな。', 'Từ chối mềm.',
              'Nếu bạn thay かな bằng です thì mềm hơn nữa nhưng mất phần "để ngỏ".'],
             ['では、〜でも大丈夫ですか。', 'Mở lại sau lời từ chối.',
              'Đây là lượt quan trọng nhất, và là lượt hay bị bỏ.']],
            colw=[26, 30, 44])

    F += VF('GIỚI HẠN CỦA MỤC NÀY ／ この欄の限界',
            '<b>Có nguồn:</b> ' + FULL_KEIGO + ' — 自分側は立てない · 第三者を立てる条件 · chức năng của '
            'お(ご)……いたす và いただく · 方言の敬語 (' + KEIGO_SHISHIN + ', 第1–2 '
            'chương). <b>Là xếp đặt của ban biên tập:</b> cách đọc ba lớp giảm nhẹ '
            'trong lời từ chối, vai trò của lượt thứ ba, toàn bộ hội thoại, hai '
            'bảng. <b>Cần kiểm chứng:</b> mức độ phổ biến của 〜んですが so với '
            'câu nhờ trực tiếp trong công sở Việt–Nhật khác nhau; mục này không '
            'khảo sát và không có số liệu. Đừng lấy 田中 làm khuôn cho mọi đồng '
            'nghiệp: quan hệ với người hơn bốn tuổi trong cùng nhóm khác với quan '
            'hệ với cấp trên trực tiếp.')
    F.append(P('Mức của mục này: 公式 cho kính ngữ và phần vùng miền · '
               '一般的な教育上の説明 cho 〜んですが và なら · 編集上の整理 cho hội '
               'thoại, lượt thứ ba và hai bảng · 要検証 cho điểm ở khung trên.',
               'caption'))
    return F


# ===========================================================================
def real_japanese_4():
    """実際の日本語 ④ — N2: a review meeting, and what is not said."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('実際の日本語 ④ ／ REAL JAPANESE — Cuộc họp ／ 会議'))
    F.append(P('N2 là bậc của 抽象を運ぶ — mang điều trừu tượng. Cảnh này cho thấy '
               'điều đó nghĩa là gì trong một cuộc họp có vấn đề: không ai nói '
               '"chúng tôi sai", nhưng mọi thông tin cần thiết đều đã được nói ra, '
               'kèm theo một điểm cần cấp trên quyết.', 'lead'))
    F.append(P('Không romaji ở mục này. Từ vựng khó được chú ngay dưới dòng. '
               'Cách đọc mục: như mục ①.', 'caption'))

    F += H3('④ · 1  Bối cảnh')
    F.append(P('Họp tiến độ dự án, 14 giờ, sáu người. Có một chậm trễ ở khâu kiểm '
               'thử. Người trình bày là thành viên phụ trách; người hỏi là trưởng '
               'phòng. Câu hỏi của trưởng phòng rất ngắn; câu trả lời dài, và trong '
               'đó có gần hết ngữ pháp N2.'))

    F += H3('④ · 2  Hội thoại')
    F += DLG([
        dict(sp='部長', ja='進捗のほう、どうですか。', vi='Tiến độ thế nào rồi?'),
        dict(sp='担当', ja='はい。開発は予定どおり進んでおりますが、テスト工程で'
                           '少し遅れが出ております。',
             vi='Vâng. Phần phát triển vẫn đúng kế hoạch, nhưng ở khâu kiểm thử có '
                'chút chậm.', note='工程 (こうてい) = khâu, công đoạn · 〜ております '
             '= 丁重語 của 〜ています.'),
        dict(sp='部長', ja='原因は。', vi='Nguyên nhân?'),
        dict(sp='担当', ja='外部の検証ツールの仕様変更が重なったためです。今週中に'
                           '代替の手順を固めまして、来週前半には巻き戻せる見込みです。',
             vi='Do thay đổi thông số của công cụ kiểm tra bên ngoài trùng vào cùng '
                'lúc. Trong tuần này sẽ chốt quy trình thay thế, dự kiến đầu tuần '
                'sau có thể bù lại.', note='巻き戻す (まきもどす) = bù lại, kéo về '
             'đúng tiến độ.'),
        dict(sp='部長', ja='影響は。', vi='Ảnh hưởng thì sao?'),
        dict(sp='担当', ja='リリース時期には影響が出ない範囲に収められると思い'
                           'ます。ただ、品質の面でどこまで許容できるか、ご相談'
                           'させていただければと思います。',
             vi='Tôi nghĩ có thể giữ trong phạm vi không ảnh hưởng tới thời điểm '
                'phát hành. Chỉ có điều, về mặt chất lượng thì có thể chấp nhận tới '
                'đâu, tôi muốn được tham vấn anh ạ.', note='許容 (きょよう) = '
             'chấp nhận, dung thứ.'),
        dict(sp='部長', ja='じゃあ、その線で進めて。必要なら早めに上げて。',
             vi='Vậy cứ theo hướng đó mà làm. Nếu cần thì báo lên sớm.'),
        dict(sp='担当', ja='承知しました。明日までに、判断が必要な点を整理して'
                           'お持ちします。',
             vi='Vâng ạ. Trước ngày mai tôi sẽ tổng hợp những điểm cần quyết và '
                'mang trình anh.'),
    ], show_romaji=False)

    F += H3('④ · 3  Vì sao nghe tự nhiên')
    F += WHY([
        ('〜ております',
         'Nguyên văn 「敬語の指針」liệt kê おる là dạng của <b>謙譲語Ⅱ（丁重語）</b> '
         '— loại kính ngữ trọng hoá <i>người nghe</i> trong khi nói về phía mình. '
         'Đó là lý do các báo cáo dùng 進んでおります · 出ております: câu không '
         'nâng phòng ban bạn lên, nó nâng người đang nghe. Nếu chỉ đọc です・ます '
         'thì câu không sai, nhưng âm điệu công việc mất đi — người nghe nhận ra '
         'ngay mức đăng ký. <i>(公式 — ' + KEIGO_SHISHIN + ', 第2章第3)</i>'),
        ('原因は。／ 影響は。',
         'Câu hỏi trong họp bị rút còn danh từ + は. Không phải cộc lốc: は khoanh '
         'đề tài, ngữ điệu lên ở cuối làm phần nghi vấn, và động từ 何ですか bị bỏ '
         'vì cả phòng đang nói về cùng một việc. Đây là phiên bản nói của hiện '
         'tượng bạn đã học ở R26 (lược bỏ và cấu trúc thông tin): cái bị bỏ luôn '
         'là cái người nghe đã có. <i>(編集上の整理)</i>'),
        ('重なったためです。',
         'Nguyên nhân được nêu bằng ためです cộng với một chủ thể không phải người: '
         '「仕様変更が重なった」 — các thay đổi "trùng vào nhau", không ai gây ra. '
         'Đây là cách nói phổ biến trong báo cáo công việc, và cũng là chỗ người '
         'học cần cảnh giác khi đọc: thông tin nhân quả thì có, nhưng chủ thể hành '
         'động bị đẩy ra ngoài khung. Đọc đúng kiểu câu này là kỹ năng N1 (xem '
         'chương 8). <i>(編集上の整理)</i>'),
        ('巻き戻せる見込みです。',
         '見込みです tuyên bố một <b>dự báo</b>, không phải một sự thật — nó thuộc '
         'nhóm phương tiện nhận thức ở R33. Ở đây nó làm đúng một việc: người nói '
         'đưa ra kế hoạch mà không tự nhận là chắc chắn, nên nếu tuần sau trượt, '
         'anh ta không nói sai. Người nghe quen với đăng ký này sẽ tự hiểu đó là '
         'cam kết ở mức dự báo. <i>(一般的な教育上の説明 · R33)</i>'),
        ('〜範囲に収められると思います。',
         'Chồng thêm một lớp: と思います. Nó không làm kế hoạch yếu đi; nó chuyển '
         'câu từ khẳng định sang <i>phán đoán của người nói</i> — và như vậy giữ '
         'chỗ cho người nghe sửa. Trong tiếng Nhật công việc, と思います thường '
         'xuất hiện ở chính chỗ người nói <i>đang cam kết</i>, không phải chỗ họ '
         'nghi ngờ. <i>(編集上の整理)</i>'),
        ('ご相談させていただければと思います。',
         'Đây là câu quan trọng nhất trong hội thoại, và dịch sát nghĩa thì nó vô '
         'hại: "tôi muốn được tham vấn". Việc nó làm lớn hơn thế: nó <b>đưa một '
         'điểm cần quyết lên bàn</b> mà không nói 決めてください. Người nói không '
         'có quyền quyết định mức chấp nhận chất lượng, và thay vì nói ra điều đó '
         'một cách trực tiếp, câu này biến việc xin ý kiến thành hành động của '
         'chính người nói (させていただく) — nên nó không áp lực ai. Cấp trên nhận '
         'đúng thông điệp và trả lời bằng một quyết định. <i>(編集上の整理)</i>'),
        ('〜のほう',
         '進捗のほう là cách nói bạn sẽ gặp liên tục trong hội thoại công việc. '
         'Nó không phải kính ngữ và không bắt buộc; nghĩa của nó mờ — khoảng '
         '\u201cv\u1ec1 ph\u1ea7n\u2026\u201d. 「敬語の指針」bàn về việc các bộ quy tắc dịch vụ bị dùng quá '
         'cứng, nhưng <b>không</b> xử lý riêng 〜のほう — vì vậy mục này không kết '
         'luận nó đúng hay sai, chỉ ghi nhận nó rất phổ biến trong nói. Trong văn '
         'bản viết, bỏ nó đi: 進捗はどうですか. <i>(要検証 — ấn bản này chưa tra '
         'được văn bản chính thức nào định chế 〜のほう.)</i>'),
        ('承知しました。',
         'Đây là câu nhận việc chuẩn trong công việc. 了解です nghe nhẹ hơn và '
         'được dùng rộng rãi giữa người ngang hàng; rất nhiều sách hướng dẫn nói '
         'không nên dùng với cấp trên, nhưng cách đánh giá này <b>thay đổi theo '
         'công ty</b> và mục này không tìm được nguồn chính thức nào định chế nó. '
         'Lời khuyên an toàn: khi chưa biết văn hoá nơi mình làm, dùng 承知しました '
         'và かしこまりました. <i>(要検証 — khác nhau theo nơi làm việc.)</i>'),
    ])
    F += CALL('ĐIỀU KHÔNG ĐƯỢC NÓI ／ 言われなかったこと',
              'Đọc lại hội thoại và để ý những gì <b>không</b> xuất hiện: không có '
              '"chúng tôi thất bại", không có "không kịp", không có "ai đã làm sai", '
              'không ai nói "できません". Ngược lại, mọi thông tin mà một cuộc họp '
              'cần đều đã có: chuyện gì (遅れ), ở đâu (テスト工程), vì sao (仕様変'
              '更), bao giờ xong (来週前半), ảnh hưởng (リリース時期には出ない範囲), '
              'và điểm cần quyết (品質の許容範囲). Điều bị bỏ là <i>phán đoán và '
              'quy trách nhiệm</i>, không phải dữ kiện. Nếu bạn mang cách nói của '
              'giáo trình — đầy đủ chủ ngữ, đầy đủ khẳng định — vào cuộc họp này, '
              'bạn sẽ nói nhiều hơn và truyền ít thông tin hơn. '
              '<i>(編集上の整理: đây là cách đọc hội thoại do ban biên tập soạn, '
              'không phải một luận điểm nghiên cứu.)</i>', tone='indigo')

    F += H3('④ · 4  Giáo trình dạy gì — cuộc họp nói gì')
    F += TB('BẢNG RJ4.1 — BÁO CÁO CÓ VẤN ĐỀ',
            ['Giáo trình', 'Trong họp', 'Khác ở đâu'],
            [['遅れています。', '遅れが出ております。',
              '出る làm chậm trễ thành việc "xuất hiện", không phải việc ai đó gây '
              'ra; おります nâng người nghe.'],
             ['間に合いません。', '来週前半には巻き戻せる見込みです。',
              'Câu thứ nhất kết thúc vấn đề; câu thứ hai kèm theo kế hoạch — điều '
              'người nghe cần.'],
             ['私の判断では大丈夫です。', '〜の範囲に収められると思います。',
              'と思います không hạ thấp năng lực; nó mở chỗ cho người nghe sửa.'],
             ['決めてください。', 'ご相談させていただければと思います。',
              'Cùng một việc — xin một quyết định — nhưng đặt thành hành động của '
              'người nói.'],
             ['では、よろしくお願いします。', 'その線で進めて。',
              'Lượt của cấp trên thường ngắn và ở dạng mệnh lệnh mềm; người dưới '
              'không cần mô phỏng nó. <i>(編集上の整理)</i>']],
            colw=[24, 34, 42])

    F += VF('GIỚI HẠN CỦA MỤC NÀY ／ この欄の限界',
            '<b>Có nguồn:</b> ' + FULL_KEIGO + ' — おる = 謙譲語Ⅱ（丁重語）và chức '
            'năng của お(ご)……いたす (第2章第3). <b>Là xếp đặt của ban biên tập:</b> '
            'vai trò của 見込みです và と思います, cách đọc "điều không được nói", '
            'toàn bộ hội thoại. <b>Cần kiểm chứng:</b> (a) 〜のほう — rất phổ biến '
            'trong nói, nhưng không có văn bản chính thức nào trong số ấn bản này đã '
            'tra định chế nó; (b) mức chấp nhận 了解です với cấp trên — khác nhau '
            'theo công ty và theo thế hệ; (c) mô tả về văn hoá họp công ty Nhật '
            'trong mục này chỉ dựa trên một hội thoại do ban biên tập viết, không '
            'phải khảo sát thực địa.')
    F.append(P('Mức của mục này: 公式 cho 丁重語 và お(ご)……いたす · '
               '一般的な教育上の説明 cho 見込みです · 編集上の整理 cho hội thoại, '
               'cách đọc và bảng · 要検証 cho 〜のほう và 了解です.', 'caption'))
    return F


# ===========================================================================
def real_japanese_5():
    """実際の日本語 ⑤ — N1: media Japanese, and why it is a genre."""
    F = [NextPageTemplate('body'), PageBreak()]
    F.append(H2('実際の日本語 ⑤ ／ REAL JAPANESE — Tiếng Nhật trên truyền thông ／ メディアの日本語'))
    F.append(P('Bậc N1 kết thúc ở trang trước. Cảnh cuối cùng không phải một nơi '
               'chốn mà là một buổi chiều: ba phút tin tức, một đoạn phỏng vấn, một '
               'quảng cáo, một cảnh phim. Bốn thứ đó nói bốn thứ tiếng Nhật khác '
               'nhau — và không thứ nào là tiếng Nhật bạn dùng khi nói chuyện.',
               'lead'))
    F.append(P('Không romaji ở mục này. Cần đối chiếu cách đọc: R17. Cách đọc mục: '
               'như mục ①.', 'caption'))

    F += H3('⑤ · 1  Bốn thể loại, bốn đăng ký')
    F += TB('BẢNG RJ5.1 — CÙNG MỘT NGÔN NGỮ, BỐN LUẬT VIẾT',
            ['Thể loại', 'Câu mẫu', 'Nó đang làm gì', 'Mang ra đời thường thì sao'],
            [['Tin tức (bản tin, báo)',
              '政府は〜と発表しました。／ 〜が明らかになりました。／ 〜を受けて、'
              '協議が続いています。',
              'である体 (không です・ます), 受身 để chủ thể hành động đứng ngoài '
              'khung, 体言止め cho tiêu đề, 「〜とみられます」 để quy một nhận định '
              'cho nguồn không tên.',
              'Bạn nghe như đang đọc báo cho người đối diện. Nhưng 〜とみられます '
              'thì <b>nên</b> học: nó là tín hiệu để bạn không đọc một phỏng đoán '
              'thành sự thật.'],
             ['Phỏng vấn, phát biểu',
              '〜わけですけれども／ 〜というふうに／ 〜させていただきました。',
              'Người nói vừa kể vừa tự bình luận về lời mình, giữ khoảng cách với '
              'phát ngôn trước công chúng.',
              'Trong hội thoại riêng, mật độ わけですけれども như vậy nghe như '
              'đang trả lời phỏng vấn.'],
             ['Quảng cáo',
              'さあ、走ろう。／ 新しくなった、あの味。／ 〜しませんか。',
              'Mệnh lệnh và khuyến dụ — những dạng bị hạn chế trong hội thoại — '
              'được phép, vì tiếng nói ở đây là của thương hiệu, không của một '
              'người đối diện.',
              'Câu mệnh lệnh với người thật là bất lịch sự. Đây là quyền của thể '
              'loại, không phải mẫu câu để dùng.'],
             ['Phim, anime',
              '俺が行くぜ。／ 〜ですわ。／ 〜だぞ。',
              '役割語 — phương tiện <b>hư cấu</b> để định vị nhân vật theo tuổi, '
              'tầng lớp, giới, vùng, chỉ trong vài âm tiết (R36).',
              'Người thật không nói như vậy theo tỉ lệ đó. Xem cảnh báo thường trực '
              'dưới bảng.']],
            colw=[14, 24, 32, 30])

    F += CALL('CẢNH BÁO THƯỜNG TRỰC ／ 常設の注意 — アニメ・マンガの日本語',
              'Tiếng Nhật trong anime, manga, phim và tiểu thuyết <b>không phải</b> '
              'tiếng Nhật đời thường. Nó là một hệ thống được thiết kế để khán giả '
              'nhận ra nhân vật ngay lập tức: 役割語. Ba khác biệt cố định, không '
              'bao giờ biến mất vì bạn xem nhiều hơn: (1) mật độ các dạng cực đoan '
              '(mệnh lệnh, 〜ぜ, 〜ですわ, cách gọi tên kiểu 貴様) cao hơn đời thật '
              'rất nhiều; (2) khác biệt nam/nữ trong hư cấu mạnh hơn khác biệt '
              'nam/nữ ngoài đời — chính 「敬語の指針」dặn tránh cách nghĩ áp đặt '
              'theo giới và thế hệ; (3) nhân vật nói trọn câu hơn người thật, vì '
              'khán giả phải nghe được nội dung. Học từ anime là học từ một bản vẽ '
              'kỹ thuật: hữu ích để nhận diện, sai lệch để bắt chước. '
              '<i>(編集上の整理 · 公式 cho điểm giới và thế hệ — ' + KEIGO_SHISHIN +
              ', 第1章第2-2 · xem thêm R36, R61)</i>', tone='gold')

    F += H3('⑤ · 2  Vì sao từng loại nghe tự nhiên — ở đúng chỗ của nó')
    F += WHY([
        ('政府は〜と発表しました。',
         'Tin tức không có người nghe cụ thể, và phải đọc lại được. Vì thế nó dùng '
         'である体 thay cho です・ます (dạng trung tính, không hướng tới ai), và '
         'dùng 受身 để câu không cần nêu chủ thể: 発表されました đặt sự việc lên '
         'trước, người làm ở ngoài khung. Cơ chế này bạn đã gặp ở R26 (lược bỏ và '
         'cấu trúc thông tin) và chương 3 (受身) — tin tức là ứng dụng dày đặc nhất '
         'của chúng. <i>(一般的な教育上の説明)</i>'),
        ('〜とみられます。／ 〜との見方もあります。',
         'Nhóm này quan trọng hơn cả phần còn lại của bản tin, vì nó quyết định bạn '
         'đọc đúng hay sai sự thật: nó gán một nhận định cho một nguồn <b>không '
         'được nêu tên</b>. 〜とみられます = "được cho là", 〜との見方もあります = '
         '"cũng có cách nhìn rằng". Đây là phương tiện nhận thức (R33) ở mức văn '
         'bản. Khi đọc tin Nhật, hãy đánh dấu ba dạng: 〜とみられる · 〜可能性がある '
         '· 〜との見方 — và không trích lại chúng như dữ kiện đã xác lập. '
         '<i>(一般的な教育上の説明)</i>'),
        ('公共の場の敬語は、手本として聞かれる。',
         'Điều này không phải nhận định của ban biên tập: 「敬語の指針」ghi rõ rằng '
         'cách dùng kính ngữ trên truyền hình・phát thanh và trong các thông báo ở '
         'nhà ga, trên phương tiện công cộng được công chúng nghe và <b>lấy làm '
         'mẫu</b>, nên những người trực tiếp làm công việc này cần lưu ý. Hệ quả '
         'cho người học: người Nhật cũng học đăng ký từ truyền thông, giống bạn. '
         'Nghĩa là bạn sẽ gặp tiếng Nhật của phát thanh viên trong đời sống — và '
         'nên biết nó là một đăng ký chuyên biệt, không phải chuẩn để nói theo. '
         '<i>(公式 — ' + KEIGO_SHISHIN + ', 第1章第2-5 · xem thêm R35 về thông báo '
         'nhà ga)</i>'),
        ('役割語',
         '役割語 không phải "tiếng Nhật cổ" hay "tiếng Nhật sai" — nó là một hệ '
         'thống có luật, và luật của nó là luật của hư cấu. Vì vậy mục này không '
         'in danh sách từ nào của nó: danh sách đó thay đổi theo tác phẩm và theo '
         'năm, còn cơ chế (một vài âm tiết định vị cả một kiểu người) thì không '
         'thay đổi. Muốn tra: R36, và chương 10 của phần N1. '
         '<i>(編集上の整理)</i>'),
        ('「〜わけですけれども」',
         'Nhận xét ở đây là của ban biên tập, không phải một quy tắc: người được '
         'phỏng vấn thường nói vừa phải ở dạng tường thuật vừa tự bình luận, nên '
         'câu trở thành nhiều tầng — điều chỉ được dạy rất muộn trong các giáo '
         'trình. <i>(編集上の整理 — không có số liệu; xem khung giới hạn.)</i>'),
        ('Thứ tự romaji kết thúc ở đây.',
         'Mục này không in romaji, đúng theo lộ trình: ① ② đầy đủ, ③ chỉ từ mới, '
         '④ ⑤ không. Đó không phải hình thức: một người đọc trôi chảy R17 thật sự '
         'đọc 政府は 〜 と発表しました nhanh hơn câu phiên âm của nó. Nếu '
         'bạn vẫn cần romaji ở mục này, hãy quay lại chương 1 của phần N5 và R17 — '
         'đó là chỗ đúng để luyện. <i>(編集上の整理 · chính sách ở R17, R20)</i>'),
    ])

    F += H3('⑤ · 3  Giáo trình dạy gì — truyền thông nói gì')
    F += TB('BẢNG RJ5.2 — NHẬN DIỆN ĐĂNG KÝ QUA DẤU HIỆU',
            ['Dấu hiệu trong câu', 'Bạn đang nghe thể loại nào', 'Mức độ tin cậy của nội dung'],
            [['である体, 〜と発表した, 受身',
              'Bản tin, văn bản hành chính, báo cáo.', 'Sự việc thường đúng; cách '
              'quy nguồn cần kiểm.'],
             ['〜とみられます, 〜との見方, 〜可能性がある',
              'Bản tin hoặc phân tích.', 'Chưa xác lập — là phỏng đoán của một '
              'nguồn không tên.'],
             ['です・ます + わけですけれども, 〜させていただく',
              'Phỏng vấn, phát biểu công khai.', 'Là phát ngôn có chủ đích; đừng '
              'đọc như mô tả trung tính.'],
             ['Mệnh lệnh, 体言止め, さあ',
              'Quảng cáo, khẩu hiệu.', 'Không phải câu mô tả; đừng lấy làm dữ kiện.'],
             ['役割語, 俺, 〜ぜ, 〜ですわ',
              'Hư cấu.', 'Không phải mẫu dữ liệu về người thật. '
              '<i>(編集上の整理)</i>']],
            colw=[30, 30, 40])

    F += VF('GIỚI HẠN CỦA MỤC NÀY ／ この欄の限界',
            '<b>Có nguồn:</b> ' + FULL_KEIGO + ' — kính ngữ trong truyền thông và '
            'thông báo công cộng được công chúng lấy làm mẫu; cảnh báo về cách nghĩ '
            'áp đặt theo giới và thế hệ (第1章第2-2, 第2-5). <b>Là xếp đặt của '
            'ban biên tập:</b> bảng bốn thể loại, cách đọc 〜とみられます, toàn bộ '
            'nhận xét về わけですけれども. <b>Cần kiểm chứng:</b> mật độ các dạng '
            'trên trong bản tin thật và trong lời nói thật — mục này không truy vấn '
            'corpus, nên <b>không</b> có tỉ lệ nào được nêu. Muốn có số liệu, phải '
            'đếm trên BCCWJ・CEJC hoặc một tập bản tin cụ thể, và ghi rõ tập đó.')
    F.append(P('Mức của mục này: 公式 cho hai điểm ở khung giới hạn · '
               '一般的な教育上の説明 cho tin tức và 〜とみられます · 編集上の整理 '
               'cho bảng, cảnh báo anime và phần còn lại · 要検証 cho mọi nhận xét '
               'về tần suất — mục này không nêu con số nào.', 'caption'))
    return F


# ===========================================================================
INTERLUDES = {
    'N5': real_japanese_1,
    'N4': real_japanese_2,
    'N3': real_japanese_3,
    'N2': real_japanese_4,
    'N1': real_japanese_5,
}


def bridge(level):
    """Flowables for the interlude that closes ``level`` (may be empty)."""
    fn = INTERLUDES.get(level)
    return list(fn()) if fn else []
