# -*- coding: utf-8 -*-
"""Front matter, TOC and back matter for the Second Edition."""
from reportlab.platypus import (Paragraph, Spacer, PageBreak, Flowable, Table,
                                TableStyle, KeepTogether, NextPageTemplate)
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
import theme as T
from theme import guard
import blocks as B

def P(t, s, base='Body'):
    return Paragraph(guard(t, base), T.ST[s])

def NextPageT(n):
    return NextPageTemplate(n)

# ------------------------------------------------------------------ colophon
def colophon():
    st = []
    st.append(NextPageT('plain'))
    st.append(P('THÔNG TIN XUẤT BẢN ／ 奥付', 'h2', 'BodyB'))
    st.append(Spacer(1, 4))
    rows = [
        ['Tên sách / 書名',
         '日本語 MASTER — N5 → N1\nGiáo trình và sách tra cứu tiếng Nhật cho người học Việt Nam'],
        ['Ấn bản / 版', 'Ấn bản thứ hai（第二版）, 2026.\nBản thứ nhất: 2025.'],
        ['Đối tượng', 'Người học tiếng Nhật nói tiếng Việt, từ sơ cấp (N5) đến cao cấp (N1).'],
        ['Cấu trúc', 'Một tập duy nhất. Năm phần theo cấp độ N5 → N1, tiếp theo là phần tra cứu R1–R69.'],
        ['Ngôn ngữ', 'Giải thích bằng tiếng Việt. Mọi cấu trúc, ví dụ và thuật ngữ giữ nguyên tiếng Nhật.'],
        ['Romaji', 'Kiểu Hepburn chỉnh sửa, có dấu trường âm (ā ī ū ē ō), theo '
                   '「ローマ字のつづり方」令和7年内閣告示第4号 (2025).'],
        ['Kiểu chữ / 書体', 'Shippori Mincho · Zen Old Mincho · Zen Kaku Gothic New (tiếng Nhật)\n'
                            'Noto Serif JP · Noto Sans JP (tiếng Việt, Latinh, IPA) — nhúng toàn bộ.'],
        ['Khổ sách / 判型', 'A4 (210 × 297 mm). Bố cục một cột, có số trang và dấu trang điều hướng.'],
        ['Sắp chữ', 'ReportLab (Python). Phông nhúng toàn bộ; dấu trang (bookmark) theo chương và mục.'],
    ]
    data = [[P(a, 'tdb', 'BodyB'), P(b, 'td')] for a, b in rows]
    t = Table(data, colWidths=[T.CW * 0.24, T.CW * 0.76])
    t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('LINEBELOW', (0, 0), (-1, -2), 0.35, T.RULE_SOFT)]))
    st.append(t)
    st.append(Spacer(1, 16))
    st.append(B.Callout('GIỚI HẠN CỦA CUỐN SÁCH ／ 本書の限界について',
        'Cuốn sách này được biên soạn tổng hợp từ các nguồn công khai đã được kiểm chứng, với sự '
        'trợ giúp của công cụ tính toán. <b>Nội dung chưa được hiệu đính bởi một giáo viên tiếng Nhật '
        'bản ngữ, một nhà ngôn ngữ học, hay một tổ chức giáo dục nào.</b> Mọi điểm mà người biên soạn '
        'không thể xác lập chắc chắn từ nguồn đã kiểm chứng đều được đánh dấu bằng khung '
        '「CẦN KIỂM CHỨNG ／ 要検証」 ngay tại chỗ, và được tập hợp lại trong Sổ đăng ký kiểm chứng '
        '(R68). Trước khi dùng một cách nói trong tình huống quan trọng — thi cử, phỏng vấn, giao tiếp '
        'công việc — hãy đối chiếu với giáo viên hoặc một tài liệu chuyên môn có uy tín.', tone='gold'))
    st.append(Spacer(1, 12))
    st.append(P('Nguyên tắc nguồn ／ 出典の方針', 'h3', 'BodyB'))
    for t_ in [
        'R67 (Phân cấp nguồn) và R68 (Sổ đăng ký kiểm chứng) chỉ liệt kê những tài liệu thực sự đã '
        'được truy cập và đối chiếu. Không có nguồn nào được tạo ra, suy đoán, hay trích dẫn cho có.',
        'Những thông tin phải dẫn qua nguồn thứ cấp được ghi rõ là như vậy, kèm mức độ tin cậy. '
        'Sáu mức được dùng trong sách: 公式 (văn bản chính thức) · 研究知見 (kết quả nghiên cứu) · '
        '使用実態 (thực tế dùng được ghi nhận) · 一般的な教育上の説明 (cách giải thích phổ biến trong '
        'giáo trình) · 編集上の整理 (xếp đặt của người biên soạn) · 要検証 (chưa xác lập được).',
        'Ba mức đầu khác nhau về <b>bản chất</b>, không chỉ khác nhau về độ chắc chắn. Một cách nói '
        'được dùng phổ biến (使用実態) không vì thế mà trở thành quy tắc chính thức (公式).',
    ]:
        st.append(P(t_, 'body'))
    st.append(NextPageT('body'))
    return st

# ------------------------------------------------------------------------ TOC
def toc_head():
    """Editorial note in front of the table of contents."""
    st = []
    h = B.SectionHead('Mục lục ／ 目次')
    h._bookmark = dict(key='toc-head', text='Mục lục ／ 目次', level=0)
    st.append(h)
    st.append(P('Mục lục này liệt kê sáu phần, các chương trong từng phần, và các mục '
                'tra cứu R1 → R69. Các tiểu mục (2.1, 18.4, 26.6 …) <b>không</b> in ở '
                'đây; chúng nằm trong bảng dấu trang (bookmark) của tệp PDF, mở bằng '
                'biểu tượng dấu trang trong trình đọc — ở đó bấm được trực tiếp. Số '
                'trang in ở đây là số trang thật, lấy từ chính cuốn sách này, không '
                'phải số của bản thảo.', 'lead'))
    st.append(Spacer(1, 10))
    return st

def toc_flow():
    from reportlab.platypus.tableofcontents import TableOfContents
    t = TableOfContents()
    t.dotsMinLevel = 0
    def LS(name, size, lead, font, left, color, sb, sa):
        return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead,
            textColor=color, leftIndent=left, firstLineIndent=0,
            spaceBefore=sb, spaceAfter=sa, alignment=TA_LEFT)
    t.levelStyles = [
        LS('t0', 12.0, 16.4, 'BodyB',  0, T.INDIGO,   10.0, 3.6),
        LS('t1', 10.0, 14.0, 'BodyB', 11, T.SUMI,      5.2, 1.8),
        LS('t2',  8.8, 12.4, 'Body',  24, T.INK_SOFT,  0.8, 0.8),
        LS('t3',  9.2, 13.4, 'SansB',  1, T.VERMILION, 7.0, 2.0),
    ]
    return t

# ----------------------------------------------------------------- back matter
def backmatter():
    st = []
    st.append(NextPageT('body'))
    st.append(PageBreak())
    f = B.SectionHead('Lời kết ／ おわりに')
    f._bookmark = dict(key='back-final', text='Lời kết ／ おわりに', level=1)
    st.append(f)
    st.append(P('Về ấn bản thứ hai ／ 第二版について', 'h3', 'BodyB'))
    for t_ in [
        'Ấn bản thứ nhất (2025) đặt ra kiến trúc của cuốn sách: một tập duy nhất, N5 → N1, giải thích '
        'bằng tiếng Việt, có sổ đăng ký kiểm chứng công khai. Ấn bản thứ hai giữ nguyên kiến trúc đó '
        'và làm bốn việc.',
        '<b>Một, sửa những chỗ sai và những chỗ tuyệt đối hóa quá mức.</b> Những câu dạng “không bao '
        'giờ”, “luôn luôn”, “chỉ có thể” đã được rà lại và chuyển thành khuynh hướng + ngữ cảnh + '
        'ngoại lệ ở những chỗ mà tiếng Nhật thực tế không cho phép khẳng định tuyệt đối. Một số ví dụ '
        'sai hoặc gây hiểu nhầm đã được thay. R66 (Bản đồ lỗi) ghi lại những chỗ đó.',
        '<b>Hai, bổ sung những mảng còn thiếu.</b> Dụng học (pragmatics), cấu trúc thông tin, phương '
        'pháp bóc tách câu dài, chuyển đổi đăng ký, tiếng Nhật số, văn bản thực tế ngoài đời, và một '
        'hệ thống nguồn — kiểm chứng có thể tra cứu được.',
        '<b>Ba, sửa bố cục.</b> Mục lục của ấn bản thứ nhất bị lỗi trình bày: số trang tách khỏi tiêu '
        'đề và dồn thành một khối số. Ấn bản này dựng lại mục lục theo đúng số trang thực tế, có liên '
        'kết nội bộ và dấu trang đầy đủ. Chỉ mục (R16) được dựng lại thành lưới ba cột thật, vì bản '
        'cũ bị tràn cột và xé dòng giữa các mục. Việc đánh số tiểu mục trong R21–R34 được sửa cho '
        'khớp với mục chứa nó. Những trang gần như trắng do ngắt trang được xử lý bằng cách để nội '
        'dung tự chảy, không chèn thêm chữ.',
        '<b>Bốn, nói rõ hơn về giới hạn.</b> Sổ đăng ký kiểm chứng (R68) giờ ghi cả nguồn đã tra, '
        'cách hiểu thay thế, và mức độ tin cậy — không chỉ liệt kê chỗ chưa chắc. Thư mục (Nhóm 1–6) '
        'tách theo loại nguồn, ghi kèm định danh, ngày truy cập và nguồn dùng cho mục nào.',
        '<b>Năm, sửa cách dẫn nguồn.</b> Bản thứ nhất có chỗ dẫn một nghiên cứu cho một luận điểm '
        'không phải luận điểm của nó. Ấn bản này sửa cách dẫn đó và ghi rõ việc sửa ở thư mục, Nhóm 3.',
    ]:
        st.append(P(t_, 'body'))
    st.append(Spacer(1, 8))
    st.append(B.Callout('ĐI TIẾP TỪ ĐÂY ／ ここから先へ',
        'Một cuốn sách tham khảo tốt nên cho bạn biết nó biết gì, và không biết gì. Nếu bạn phát hiện '
        'một chỗ sai, hãy đối chiếu với một nguồn chính thức trước khi lấy cuốn sách này làm căn cứ — '
        'rồi ghi lại. Đó cũng là cách cuốn sách này được sửa cho ấn bản thứ hai.', tone='indigo'))
    return st
