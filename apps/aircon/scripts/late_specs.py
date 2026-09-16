"""Reviewed source-pixel adapter for storyboard frames 08–12.

Tuples use author_cards.py's existing schema.  All OCR ids refer to the
immutable atlas.ocr.json observation array.  ``plain_buttons`` marks native
text links whose hit targets should omit the normal button surface; the
author may consume this optional style hint.  ``extra_text`` captures the
one visible line Apple Vision missed and uses the normal source-pixel rect.
No whole-card or UI image crops are permitted here.
"""

SPECS = {
    8: dict(
        cards=[
            ('installation_booking', [28, 148, 572, 360]),
            ('calendar_updated', [28, 525, 572, 339]),
        ],
        buttons=[
            ('reschedule', [59, 416, 212, 63], False, [182], 'installation.open_slots'),
            ('cancel_booking', [333, 416, 209, 63], False, [183], 'installation.cancel'),
            ('acknowledge_calendar', [56, 775, 212, 63], False, [188], 'calendar.acknowledge'),
            ('undo_calendar', [333, 775, 209, 63], False, [189], 'calendar.undo'),
        ],
        icons=[
            ('wrench', [61, 177, 44, 46]),
            ('check', [529, 184, 32, 33]),
            ('calendar', [58, 548, 44, 47]),
        ],
        dock=[13, 882, 584, 141],
    ),
    9: dict(
        cards=[
            ('installation_booking', [18, 128, 467, 334]),
            ('calendar_undone', [18, 487, 468, 252]),
        ],
        buttons=[
            ('reschedule', [46, 374, 180, 63], False, [32], 'installation.open_slots'),
            ('cancel_booking', [271, 374, 177, 63], False, [33], 'installation.cancel'),
            ('restore_calendar', [121, 652, 233, 62], False, [36], 'calendar.restore'),
        ],
        icons=[
            ('wrench', [47, 152, 39, 39]),
            ('check', [429, 155, 29, 32]),
            ('calendar', [41, 514, 45, 47]),
        ],
        dock=[14, 845, 484, 151],
        skip=[40],  # Payment dock symbol misrecognized as ".|".
        extra_text=[
            dict(
                id='desktop_date',
                text='9月18日 周五',
                bounds=[29, 30, 125, 23],
                role='desktop_date',
                basis='Manual visual observation of frame 09; missing from atlas OCR',
            ),
        ],
    ),
    10: dict(
        cards=[('installation_arriving', [21, 128, 478, 631])],
        photos=[('technician_portrait', [48, 303, 159, 175])],
        buttons=[
            ('contact_technician', [49, 668, 193, 63], True, [95], 'navigation.technician'),
            ('view_booking', [276, 667, 188, 64], False, [96], 'navigation.booking'),
        ],
        icons=[('wrench', [51, 152, 39, 40])],
        lines=[[102, 528, 136, 3], [261, 528, 142, 3]],
        dots=[
            [79, 518, 21, 23, True],
            [236, 516, 26, 27, True],
            [402, 517, 23, 25, False],
        ],
        dock=[8, 844, 500, 152],
        skip=[92],  # Current progress ring is a native shape, not the glyph ◎.
        photo_clips={'technician_portrait': 'ellipse'},
    ),
    11: dict(
        cards=[
            ('payment_due', [18, 126, 459, 459]),
            ('installation_complete', [18, 603, 459, 220]),
        ],
        buttons=[
            ('source_service_order', [43, 451, 127, 34], False, [146], 'navigation.service_order'),
            ('pay_materials', [42, 502, 217, 59], True, [148], 'payment.pay'),
            ('withdraw_payment_request', [285, 501, 169, 59], False, [149], 'payment.cancel'),
            ('report_installation_issue', [130, 735, 228, 58], False, [152], 'navigation.service_feedback'),
        ],
        icons=[
            ('wallet', [48, 149, 44, 41]),
            ('wrench', [44, 630, 38, 41]),
        ],
        lines=[[47, 341, 400, 1]],
        dock=[13, 847, 487, 149],
        skip=[156],  # Shopping bag dock outline misrecognized as text.
        plain_buttons=['source_service_order'],
    ),
    12: dict(
        cards=[
            ('payment_complete', [22, 128, 564, 466]),
            ('installation_complete', [21, 610, 565, 222]),
        ],
        buttons=[
            ('source_service_order', [49, 462, 127, 35], False, [203], 'navigation.service_order'),
            ('view_payment_receipt', [55, 513, 333, 60], False, [204], 'navigation.payment_receipt'),
            ('view_service_order', [142, 748, 249, 59], False, [207], 'navigation.service_order'),
        ],
        icons=[
            ('wallet', [52, 154, 48, 43]),
            ('check', [500, 162, 33, 34]),
            ('wrench', [52, 641, 41, 40]),
        ],
        lines=[[53, 354, 490, 1]],
        dock=[13, 850, 584, 150],
        plain_buttons=['source_service_order'],
    ),
}

CORRECTIONS = {
    # Leading wrench was incorrectly included in OCR as the character 人.
    178: ('安装服务 · 预约成功', [124, 186, 252, 33]),
    # Source image corruption and OCR noise in the approved unbranded payee.
    145: ('收款方：安装服务团队', None),
    202: ('收款方：安装服务团队', None),
}
