window.REVIEW_MANIFEST = {
  "schema_version": 1,
  "title": "空调到家 · 原生卡片评审",
  "built_at": "2026-09-13T04:37:10.331760+00:00",
  "rows": [
    {
      "number": 1,
      "id": "aircon-01",
      "title": "好物详情",
      "description": "查看空调规格、配送和安装服务",
      "surface": "购物应用",
      "branch": false,
      "base": "../cards/aircon-01/",
      "reference": "../cards/aircon-01/reference.png",
      "native": "../cards/aircon-01/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "e5c9a3849994440c84e00ca68a835e7b"
      },
      "run": {
        "id": "aircon-01",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-01",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "87fea6fa4c41a6fae036d99faccf95ddc538914298bf3d07e3bb4e545382b6f5",
          "reference_sha256": "f03b5010b6c87bc292045ae1a227a6822e3213a9f2f26757ed514e6f9646c196",
          "id": "aircon-01",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "product_photo",
              "role": "photo",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Image"
              ],
              "actual_widget": "Image",
              "issues": [],
              "repair": "Use an original or separately generated image asset with documented crop, fit and clipping."
            },
            {
              "id": "divider_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "buy",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "buy_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "buy_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_9",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "back_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "share_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "truck_icon_2",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "calendar_icon_3",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_1",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_2",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_4",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_5",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_6",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_7",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_8",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 4.576,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "f03b5010b6c87bc292045ae1a227a6822e3213a9f2f26757ed514e6f9646c196",
            "native_sha256": "b9bdd0ddcfe7448b0baa72521416b3010cb41845abbd92a42241a367a968ed36",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_1: text ink dimensions",
          "text_1: text color",
          "text_2: text color",
          "text_4: text color",
          "text_5: reference OCR text differs",
          "text_5: text ink position",
          "text_5: text ink dimensions",
          "text_5: text color",
          "text_6: text ink dimensions",
          "text_6: text color",
          "text_7: text color",
          "text_8: text color"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              19.5,
              0.0,
              366.5,
              776.0
            ],
            "actual_bounds": [
              19.5,
              0.0,
              366.5,
              776.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "product_photo",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              19.5,
              91.0,
              366.5,
              303.0
            ],
            "actual_bounds": [
              19.5,
              91.0,
              366.5,
              303.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Image",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_0",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              32.384765625,
              569.830258302583,
              337.8671875,
              0.7158671586715867
            ],
            "actual_bounds": [
              32.384765625,
              569.8302612304688,
              337.8671875,
              0.7158671617507935
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "buy",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              36.6796875,
              700.8339483394834,
              331.4248046875,
              50.82656826568265
            ],
            "actual_bounds": [
              36.6796875,
              700.8339233398438,
              331.4248,
              50.82657
            ],
            "parent": "beauty_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "立即购买",
            "enabled": true,
            "issues": []
          },
          {
            "id": "buy_surface",
            "native_id": "beauty_0_0_2_0",
            "expected_bounds": [
              36.6796875,
              700.8339483394834,
              331.4248046875,
              50.82656826568265
            ],
            "actual_bounds": [
              36.6796875,
              700.8339233398438,
              331.4248046875,
              50.826568603515625
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "buy_control",
            "native_id": "beauty_0_0_2_1",
            "expected_bounds": [
              36.6796875,
              700.8339483394834,
              331.4248046875,
              50.82656826568265
            ],
            "actual_bounds": [
              36.6796875,
              700.8339233398438,
              331.4248046875,
              50.826568603515625
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_9",
            "native_id": "beauty_0_0_2_2",
            "expected_bounds": [
              153.38183857449988,
              714.3035464169672,
              89.1594541960006,
              23.5
            ],
            "actual_bounds": [
              153.3818359375,
              714.3035278320312,
              89.159454,
              23.5
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Label",
            "visible": true,
            "text": "立即购买",
            "enabled": true,
            "issues": []
          },
          {
            "id": "back_icon_0",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              35.9638671875,
              50.11070110701107,
              22.90625,
              28.634686346863468
            ],
            "actual_bounds": [
              35.9638671875,
              50.11070251464844,
              22.90625,
              28.634685516357422
            ],
            "parent": "beauty_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "share_icon_1",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              340.9033203125,
              50.82656826568265,
              25.76953125,
              25.055350553505534
            ],
            "actual_bounds": [
              340.9033203125,
              50.826568603515625,
              25.76953125,
              25.05535125732422
            ],
            "parent": "beauty_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "truck_icon_2",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              37.3955078125,
              597.0332103321033,
              27.9169921875,
              24.339483394833948
            ],
            "actual_bounds": [
              37.3955078125,
              597.033203125,
              27.9169921875,
              24.3394832611084
            ],
            "parent": "beauty_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "calendar_icon_3",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              37.3955078125,
              645.7121771217712,
              27.201171875,
              26.487084870848708
            ],
            "actual_bounds": [
              37.3955078125,
              645.712158203125,
              27.201171875,
              26.487085342407227
            ],
            "parent": "beauty_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_1",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              39.974042391524634,
              14.566487076543691,
              140.84707816426572,
              16.0
            ],
            "actual_bounds": [
              39.97404098510742,
              14.566487312316895,
              140.84708,
              16.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月17日 周四 09:41",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_2",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              181.81527157974642,
              54.62970570110141,
              43.344322513641536,
              22.0
            ],
            "actual_bounds": [
              181.81527709960938,
              54.62970733642578,
              43.344322,
              22.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "好物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_4",
            "native_id": "beauty_0_0_9",
            "expected_bounds": [
              42.39481827615897,
              416.38478303271063,
              172.2220560333054,
              27.0
            ],
            "actual_bounds": [
              42.39481735229492,
              416.3847961425781,
              172.22206,
              27.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "1.5匹变频空调",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_5",
            "native_id": "beauty_0_0_10",
            "expected_bounds": [
              36.51873930586699,
              462.92099030223125,
              118.6406337030099,
              39.14694829545275
            ],
            "actual_bounds": [
              36.51873779296875,
              462.9209899902344,
              118.64063,
              39.14695
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "¥2,799",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_6",
            "native_id": "beauty_0_0_11",
            "expected_bounds": [
              45.08204301063163,
              521.7665217939164,
              277.472914814486,
              19.03587247037747
            ],
            "actual_bounds": [
              45.0820426940918,
              521.7665405273438,
              277.4729,
              19.035873
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "一级能效 · 冷暖两用 · 安静睡眠",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_7",
            "native_id": "beauty_0_0_12",
            "expected_bounds": [
              79.55708711120167,
              597.3124855051851,
              176.08040915525018,
              19.5
            ],
            "actual_bounds": [
              79.55709075927734,
              597.3125,
              176.08041,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "送货上门 · 专业安装",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_8",
            "native_id": "beauty_0_0_13",
            "expected_bounds": [
              79.13368011151866,
              648.307019898865,
              147.4917816961616,
              19.0
            ],
            "actual_bounds": [
              79.13368225097656,
              648.3070068359375,
              147.49178,
              19.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "周五 9月18日送达",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_9",
            "reference": [
              154.5,
              716.0,
              81.0,
              19.5
            ],
            "native": [
              154.5,
              716.0,
              81.0,
              19.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              244,
              249,
              247
            ],
            "native_color": [
              255,
              255,
              255
            ],
            "issues": []
          },
          {
            "id": "text_1",
            "reference": [
              40.5,
              16.5,
              139.0,
              12.0
            ],
            "native": [
              40.5,
              16.5,
              134.0,
              12.0
            ],
            "delta": [
              0.0,
              0.0,
              -5.0,
              0.0
            ],
            "reference_color": [
              84,
              84,
              84
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_2",
            "reference": [
              182.5,
              56.0,
              36.0,
              18.0
            ],
            "native": [
              182.5,
              56.0,
              36.0,
              17.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              29,
              28,
              28
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_4",
            "reference": [
              44.5,
              418.0,
              162.5,
              23.0
            ],
            "native": [
              44.5,
              418.0,
              162.5,
              23.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              19,
              19,
              18
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_5",
            "reference": [
              44.5,
              465.5,
              104.0,
              27.5
            ],
            "native": [
              38.0,
              468.5,
              111.0,
              34.0
            ],
            "delta": [
              -6.5,
              3.0,
              7.0,
              6.5
            ],
            "reference_color": [
              32,
              32,
              31
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink position",
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_6",
            "reference": [
              46.0,
              523.5,
              287.5,
              15.0
            ],
            "native": [
              46.0,
              523.5,
              270.5,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              -17.0,
              0.0
            ],
            "reference_color": [
              76,
              77,
              77
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_7",
            "reference": [
              80.0,
              599.0,
              169.0,
              15.5
            ],
            "native": [
              80.5,
              599.0,
              168.5,
              15.5
            ],
            "delta": [
              0.5,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              79,
              79,
              80
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_8",
            "reference": [
              80.0,
              650.0,
              140.5,
              15.0
            ],
            "native": [
              80.0,
              650.0,
              140.0,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              74,
              74,
              74
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              19.5,
              0.0,
              366.5,
              776.0
            ],
            "native": [
              19.5,
              0.0,
              366.5,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "product_photo",
            "reference": [
              19.5,
              91.0,
              366.5,
              303.0
            ],
            "native": [
              19.5,
              91.0,
              366.5,
              303.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "divider_0",
            "reference": [
              32.384765625,
              569.830258302583,
              337.8671875,
              0.7158671586715867
            ],
            "native": [
              32.384765625,
              569.8302612304688,
              337.8671875,
              0.7158671617507935
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "buy",
            "reference": [
              36.6796875,
              700.8339483394834,
              331.4248046875,
              50.82656826568265
            ],
            "native": [
              36.6796875,
              700.8339233398438,
              331.4248,
              50.82657
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "buy_surface",
            "reference": [
              36.6796875,
              700.8339483394834,
              331.4248046875,
              50.82656826568265
            ],
            "native": [
              36.6796875,
              700.8339233398438,
              331.4248046875,
              50.826568603515625
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "buy_control",
            "reference": [
              36.6796875,
              700.8339483394834,
              331.4248046875,
              50.82656826568265
            ],
            "native": [
              36.6796875,
              700.8339233398438,
              331.4248046875,
              50.826568603515625
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "back_icon_0",
            "reference": [
              35.9638671875,
              50.11070110701107,
              22.90625,
              28.634686346863468
            ],
            "native": [
              35.9638671875,
              50.11070251464844,
              22.90625,
              28.634685516357422
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "share_icon_1",
            "reference": [
              340.9033203125,
              50.82656826568265,
              25.76953125,
              25.055350553505534
            ],
            "native": [
              340.9033203125,
              50.826568603515625,
              25.76953125,
              25.05535125732422
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "truck_icon_2",
            "reference": [
              37.3955078125,
              597.0332103321033,
              27.9169921875,
              24.339483394833948
            ],
            "native": [
              37.3955078125,
              597.033203125,
              27.9169921875,
              24.3394832611084
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "calendar_icon_3",
            "reference": [
              37.3955078125,
              645.7121771217712,
              27.201171875,
              26.487084870848708
            ],
            "native": [
              37.3955078125,
              645.712158203125,
              27.201171875,
              26.487085342407227
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "back_icon_0",
            "second": "share_icon_1",
            "vertical_gap_reference": -27.918819188191883,
            "vertical_gap_native": -27.918819427490234,
            "left_alignment_delta": 0.0
          },
          {
            "first": "share_icon_1",
            "second": "product_photo",
            "vertical_gap_reference": 15.118081180811814,
            "vertical_gap_native": 15.118080139160156,
            "left_alignment_delta": 0.0
          },
          {
            "first": "product_photo",
            "second": "divider_0",
            "vertical_gap_reference": 175.83025830258305,
            "vertical_gap_native": 175.83026123046875,
            "left_alignment_delta": 0.0
          },
          {
            "first": "divider_0",
            "second": "truck_icon_2",
            "vertical_gap_reference": 26.487084870848662,
            "vertical_gap_native": 26.487074732780457,
            "left_alignment_delta": 0.0
          },
          {
            "first": "truck_icon_2",
            "second": "calendar_icon_3",
            "vertical_gap_reference": 24.339483394833977,
            "vertical_gap_native": 24.3394718170166,
            "left_alignment_delta": 0.0
          },
          {
            "first": "calendar_icon_3",
            "second": "buy",
            "vertical_gap_reference": 28.634686346863486,
            "vertical_gap_native": 28.634679794311523,
            "left_alignment_delta": 0.0
          },
          {
            "first": "buy_surface",
            "second": "buy_control",
            "vertical_gap_reference": -50.82656826568265,
            "vertical_gap_native": -50.826568603515625,
            "left_alignment_delta": 0.0
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-01/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-01/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-01/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-01/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-01/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-01/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/01.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-01/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-01/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-01/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-01/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 2,
      "id": "aircon-02",
      "title": "订单详情",
      "description": "演示订单已完成付款，查看配送安排",
      "surface": "购物应用",
      "branch": false,
      "base": "../cards/aircon-02/",
      "reference": "../cards/aircon-02/reference.png",
      "native": "../cards/aircon-02/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "c02469ae407d45ef8416f5978f3b8fce"
      },
      "run": {
        "id": "aircon-02",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-02",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "3e9e6e3eb5bd3c87655cfd315577ef301eaba42664a72c1ab0b0f835756adcd1",
          "reference_sha256": "e77a48d6c66c43b6e2342edf0907cc8369a52b9c8f968ef8ca1375546b40ae13",
          "id": "aircon-02",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "order_product",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "product_photo",
              "role": "photo",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Image"
              ],
              "actual_widget": "Image",
              "issues": [],
              "repair": "Use an original or separately generated image asset with documented crop, fit and clipping."
            },
            {
              "id": "text_48",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_49",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "order_details",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "divider_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "divider_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "person_icon_2",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "calendar_icon_3",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "wrench_icon_4",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_50",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_51",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_53",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_54",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "divider_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "back",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "back_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "back_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "view_logistics",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "view_logistics_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "view_logistics_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_61",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "support",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "support_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "support_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_62",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "back_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "check_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "step_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "step_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "step_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "text_44",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_46",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_47",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_55",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_56",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_57",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_58",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_59",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_60",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 4.541,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "e77a48d6c66c43b6e2342edf0907cc8369a52b9c8f968ef8ca1375546b40ae13",
            "native_sha256": "39a980a6b84fd7b4d7a81482e112843d08b8b8d4c4f431edea6437f5465c23b7",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_48: text color",
          "text_50: text color",
          "text_51: text color",
          "text_53: text color",
          "text_54: text color",
          "text_61: text color",
          "text_62: text color",
          "text_44: reference text missing or OCR unresolved",
          "text_46: text color",
          "text_47: text color",
          "text_56: text color",
          "text_58: text color",
          "text_60: text color",
          "3 extra reference text observations need classification"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              18.0,
              0.0,
              370.0,
              776.0
            ],
            "actual_bounds": [
              18.0,
              0.0,
              370.0,
              776.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "order_product",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              32.313346228239844,
              152.47970479704796,
              339.94197292069634,
              136.01476014760146
            ],
            "actual_bounds": [
              32.31334686279297,
              152.47970581054688,
              339.9419860839844,
              136.01475524902344
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "product_photo",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              47.5,
              179.5,
              89.5,
              87.5
            ],
            "actual_bounds": [
              47.5,
              179.5,
              89.5,
              87.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Image",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_48",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              151.4195741221683,
              192.57350437844758,
              118.72361844679502,
              20.201154945719605
            ],
            "actual_bounds": [
              151.41957092285156,
              192.57350158691406,
              118.72362,
              20.201155
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "1.5匹变频空调",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_49",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              299.3955619440599,
              240.26581193640516,
              61.01869964071637,
              20.0
            ],
            "actual_bounds": [
              299.39556884765625,
              240.26580810546875,
              61.0187,
              20.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "¥2,799",
            "enabled": true,
            "issues": []
          },
          {
            "id": "order_details",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              32.313346228239844,
              289.21033210332104,
              339.94197292069634,
              211.18081180811808
            ],
            "actual_bounds": [
              32.31334686279297,
              289.2103271484375,
              339.9419860839844,
              211.18081665039062
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_0",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              49.48936170212766,
              377.26199261992616,
              304.1586073500967,
              0.7158671586715867
            ],
            "actual_bounds": [
              49.48936080932617,
              377.2619934082031,
              304.1585998535156,
              0.7158671617507935
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_1",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              49.48936170212766,
              435.9630996309963,
              304.1586073500967,
              0.7158671586715867
            ],
            "actual_bounds": [
              49.48936080932617,
              435.9631042480469,
              304.1585998535156,
              0.7158671617507935
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "person_icon_2",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              53.06769825918762,
              308.53874538745384,
              22.901353965183752,
              23.62361623616236
            ],
            "actual_bounds": [
              53.06769943237305,
              308.53875732421875,
              22.90135383605957,
              23.62361717224121
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "calendar_icon_3",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              53.06769825918762,
              395.15867158671585,
              25.04835589941973,
              24.339483394833948
            ],
            "actual_bounds": [
              53.06769943237305,
              395.1586608886719,
              25.048355102539062,
              24.3394832611084
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "wrench_icon_4",
            "native_id": "beauty_0_0_1_4",
            "expected_bounds": [
              52.35203094777563,
              454.57564575645756,
              25.04835589941973,
              24.339483394833948
            ],
            "actual_bounds": [
              52.35203170776367,
              454.5756530761719,
              25.048355102539062,
              24.3394832611084
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_50",
            "native_id": "beauty_0_0_1_5",
            "expected_bounds": [
              94.56920382040958,
              310.3484369828183,
              38.74074266749092,
              17.12524059390529
            ],
            "actual_bounds": [
              94.56920623779297,
              310.34844970703125,
              38.74074,
              17.12524
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "Alex",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_51",
            "native_id": "beauty_0_0_1_6",
            "expected_bounds": [
              94.16739334732985,
              343.8013034259725,
              122.39752378934374,
              18.5
            ],
            "actual_bounds": [
              94.16739654541016,
              343.8013000488281,
              122.39752,
              18.5
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "家 · 海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_53",
            "native_id": "beauty_0_0_1_7",
            "expected_bounds": [
              94.61580344053961,
              400.77691099047223,
              209.67512262991679,
              18.0
            ],
            "actual_bounds": [
              94.61580657958984,
              400.77691650390625,
              209.67513,
              18.0
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "周五 9月18日 14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_54",
            "native_id": "beauty_0_0_1_8",
            "expected_bounds": [
              94.17167123580394,
              455.8934547760379,
              124.3153280370065,
              19.0
            ],
            "actual_bounds": [
              94.17166900634766,
              455.8934631347656,
              124.31533,
              19.0
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "到货后预约安装",
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_2",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              50.20502901353965,
              531.8892988929889,
              1.4313346228239845,
              99.50553505535055
            ],
            "actual_bounds": [
              50.20502853393555,
              531.8892822265625,
              1.4313346147537231,
              99.50553131103516
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "back",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              32.313346228239844,
              47.96309963099631,
              28.626692456479688,
              37.22509225092251
            ],
            "actual_bounds": [
              32.31334686279297,
              47.96310043334961,
              28.626692,
              37.225094
            ],
            "parent": "beauty_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "back_surface",
            "native_id": "beauty_0_0_3_0",
            "expected_bounds": [
              32.313346228239844,
              47.96309963099631,
              28.626692456479688,
              37.22509225092251
            ],
            "actual_bounds": [
              32.31334686279297,
              47.96310043334961,
              28.626691818237305,
              37.225093841552734
            ],
            "parent": "beauty_0_0_3",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "back_control",
            "native_id": "beauty_0_0_3_1",
            "expected_bounds": [
              32.313346228239844,
              47.96309963099631,
              28.626692456479688,
              37.22509225092251
            ],
            "actual_bounds": [
              32.31334686279297,
              47.96310043334961,
              28.626691818237305,
              37.225093841552734
            ],
            "parent": "beauty_0_0_3",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_logistics",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              36.6073500967118,
              693.6752767527674,
              151.72147001934235,
              52.25830258302583
            ],
            "actual_bounds": [
              36.60734939575195,
              693.67529296875,
              151.72147,
              52.2583
            ],
            "parent": "beauty_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "查看物流",
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_logistics_surface",
            "native_id": "beauty_0_0_4_0",
            "expected_bounds": [
              36.6073500967118,
              693.6752767527674,
              151.72147001934235,
              52.25830258302583
            ],
            "actual_bounds": [
              36.60734939575195,
              693.67529296875,
              151.72146606445312,
              52.25830078125
            ],
            "parent": "beauty_0_0_4",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_logistics_control",
            "native_id": "beauty_0_0_4_1",
            "expected_bounds": [
              36.6073500967118,
              693.6752767527674,
              151.72147001934235,
              52.25830258302583
            ],
            "actual_bounds": [
              36.60734939575195,
              693.67529296875,
              151.72146606445312,
              52.25830078125
            ],
            "parent": "beauty_0_0_4",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_61",
            "native_id": "beauty_0_0_4_2",
            "expected_bounds": [
              73.82901373798585,
              708.8773610906611,
              80.16975774868078,
              21.0
            ],
            "actual_bounds": [
              73.82901000976562,
              708.8773803710938,
              80.169754,
              21.0
            ],
            "parent": "beauty_0_0_4",
            "widget_type": "Label",
            "visible": true,
            "text": "查看物流",
            "enabled": true,
            "issues": []
          },
          {
            "id": "support",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              217.67117988394583,
              693.6752767527674,
              149.5744680851064,
              51.54243542435424
            ],
            "actual_bounds": [
              217.67117309570312,
              693.67529296875,
              149.57446,
              51.542435
            ],
            "parent": "beauty_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "联系客服",
            "enabled": true,
            "issues": []
          },
          {
            "id": "support_surface",
            "native_id": "beauty_0_0_5_0",
            "expected_bounds": [
              217.67117988394583,
              693.6752767527674,
              149.5744680851064,
              51.54243542435424
            ],
            "actual_bounds": [
              217.67117309570312,
              693.67529296875,
              149.574462890625,
              51.54243469238281
            ],
            "parent": "beauty_0_0_5",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "support_control",
            "native_id": "beauty_0_0_5_1",
            "expected_bounds": [
              217.67117988394583,
              693.6752767527674,
              149.5744680851064,
              51.54243542435424
            ],
            "actual_bounds": [
              217.67117309570312,
              693.67529296875,
              149.574462890625,
              51.54243469238281
            ],
            "parent": "beauty_0_0_5",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_62",
            "native_id": "beauty_0_0_5_2",
            "expected_bounds": [
              253.34553522231306,
              708.5841053369575,
              79.84668633968393,
              21.176877665799438
            ],
            "actual_bounds": [
              253.3455352783203,
              708.5841064453125,
              79.84669,
              21.176878
            ],
            "parent": "beauty_0_0_5",
            "widget_type": "Label",
            "visible": true,
            "text": "联系客服",
            "enabled": true,
            "issues": []
          },
          {
            "id": "back_icon_0",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              34.460348162475825,
              50.11070110701107,
              22.901353965183752,
              28.634686346863468
            ],
            "actual_bounds": [
              34.460350036621094,
              50.11070251464844,
              22.90135383605957,
              28.634685516357422
            ],
            "parent": "beauty_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "check_icon_1",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              39.47001934235976,
              108.81180811808117,
              28.626692456479688,
              28.634686346863468
            ],
            "actual_bounds": [
              39.47002029418945,
              108.81180572509766,
              28.626691818237305,
              28.634685516357422
            ],
            "parent": "beauty_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_0",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              45.195357833655706,
              522.5830258302583,
              12.88201160541586,
              12.88560885608856
            ],
            "actual_bounds": [
              45.19535827636719,
              522.5830078125,
              12.882011413574219,
              12.885608673095703
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_1",
            "native_id": "beauty_0_0_9",
            "expected_bounds": [
              45.195357833655706,
              572.6937269372694,
              12.88201160541586,
              12.88560885608856
            ],
            "actual_bounds": [
              45.19535827636719,
              572.6937255859375,
              12.882011413574219,
              12.885608673095703
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_2",
            "native_id": "beauty_0_0_10",
            "expected_bounds": [
              45.195357833655706,
              624.9520295202951,
              12.88201160541586,
              12.88560885608856
            ],
            "actual_bounds": [
              45.19535827636719,
              624.9520263671875,
              12.882011413574219,
              12.885608673095703
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_44",
            "native_id": "beauty_0_0_11",
            "expected_bounds": [
              34.83984996653305,
              12.59545711746588,
              153.00413814730743,
              19.19285022568063
            ],
            "actual_bounds": [
              34.83985137939453,
              12.595457077026367,
              153.00414,
              19.19285
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月17日 周四 09:45",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_46",
            "native_id": "beauty_0_0_12",
            "expected_bounds": [
              164.3962042203231,
              54.59207139825517,
              84.14867488535174,
              22.0
            ],
            "actual_bounds": [
              164.39620971679688,
              54.592071533203125,
              84.148674,
              22.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "订单详情",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_47",
            "native_id": "beauty_0_0_13",
            "expected_bounds": [
              82.06396233872607,
              113.55775354857026,
              62.56535161719153,
              21.5
            ],
            "actual_bounds": [
              82.06396484375,
              113.55775451660156,
              62.565353,
              21.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "已付款",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_55",
            "native_id": "beauty_0_0_14",
            "expected_bounds": [
              75.6604754821831,
              519.5769697991014,
              40.448782048112626,
              20.5
            ],
            "actual_bounds": [
              75.66047668457031,
              519.5769653320312,
              40.448784,
              20.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "下单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_56",
            "native_id": "beauty_0_0_15",
            "expected_bounds": [
              253.4606953803944,
              523.788841141364,
              104.99341290069201,
              16.5
            ],
            "actual_bounds": [
              253.460693359375,
              523.788818359375,
              104.993416,
              16.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月17日 09:40",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_57",
            "native_id": "beauty_0_0_16",
            "expected_bounds": [
              75.5724393841724,
              570.3876468917013,
              58.05053969707726,
              19.5
            ],
            "actual_bounds": [
              75.57244110107422,
              570.3876342773438,
              58.05054,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "已付款",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_58",
            "native_id": "beauty_0_0_17",
            "expected_bounds": [
              253.4193529546904,
              573.4475596409739,
              105.39666176670693,
              17.0
            ],
            "actual_bounds": [
              253.4193572998047,
              573.4475708007812,
              105.39666,
              17.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月17日 09:45",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_59",
            "native_id": "beauty_0_0_18",
            "expected_bounds": [
              75.14501788547467,
              620.783431754483,
              58.60215741392414,
              20.0
            ],
            "actual_bounds": [
              75.14501953125,
              620.783447265625,
              58.602158,
              20.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "待发货",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_60",
            "native_id": "beauty_0_0_19",
            "expected_bounds": [
              253.44168592056616,
              623.9348775294839,
              105.20832862183352,
              16.5
            ],
            "actual_bounds": [
              253.44168090820312,
              623.9348754882812,
              105.20833,
              16.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月17日 09:45",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_48",
            "reference": [
              153.0,
              194.5,
              110.0,
              16.0
            ],
            "native": [
              153.0,
              194.5,
              110.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              77,
              77,
              76
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_49",
            "reference": [
              300.0,
              243.5,
              54.0,
              16.0
            ],
            "native": [
              300.5,
              243.5,
              53.5,
              16.0
            ],
            "delta": [
              0.5,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              51,
              52,
              52
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_50",
            "reference": [
              95.0,
              312.0,
              32.0,
              13.0
            ],
            "native": [
              95.0,
              312.0,
              32.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              68,
              68,
              69
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_51",
            "reference": [
              95.5,
              345.5,
              114.0,
              14.5
            ],
            "native": [
              95.5,
              345.5,
              114.0,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              86,
              86,
              86
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_53",
            "reference": [
              95.5,
              402.5,
              202.5,
              14.0
            ],
            "native": [
              95.5,
              402.5,
              202.5,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              74,
              75,
              75
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_54",
            "reference": [
              95.5,
              457.5,
              116.5,
              15.0
            ],
            "native": [
              95.5,
              457.5,
              116.5,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              81,
              81,
              81
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_61",
            "reference": [
              75.0,
              710.5,
              72.5,
              17.0
            ],
            "native": [
              74.5,
              710.5,
              73.0,
              17.0
            ],
            "delta": [
              -0.5,
              0.0,
              0.5,
              0.0
            ],
            "reference_color": [
              80,
              104,
              86
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_62",
            "reference": [
              254.0,
              710.5,
              72.5,
              17.0
            ],
            "native": [
              254.0,
              710.5,
              72.5,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              82,
              97,
              87
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_44",
            "reference": null,
            "native": null,
            "delta": null,
            "reference_color": null,
            "native_color": null,
            "issues": [
              "reference text missing or OCR unresolved"
            ]
          },
          {
            "id": "text_46",
            "reference": [
              165.5,
              56.5,
              76.5,
              18.0
            ],
            "native": [
              165.5,
              56.5,
              76.5,
              17.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              28,
              28,
              28
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_47",
            "reference": [
              84.0,
              115.5,
              54.0,
              17.5
            ],
            "native": [
              84.0,
              115.5,
              54.0,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              58,
              99,
              58
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_55",
            "reference": [
              76.5,
              521.5,
              33.0,
              16.5
            ],
            "native": [
              77.0,
              521.5,
              32.5,
              15.5
            ],
            "delta": [
              0.5,
              0.0,
              -0.5,
              -1.0
            ],
            "reference_color": [
              47,
              49,
              48
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_56",
            "reference": [
              254.0,
              525.5,
              98.5,
              12.5
            ],
            "native": [
              254.0,
              525.5,
              98.5,
              12.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              160,
              161,
              160
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_57",
            "reference": [
              77.5,
              572.0,
              49.5,
              15.5
            ],
            "native": [
              77.5,
              572.0,
              49.5,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              61,
              62,
              61
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_58",
            "reference": [
              254.0,
              575.5,
              98.5,
              13.0
            ],
            "native": [
              254.0,
              575.5,
              98.5,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              159,
              159,
              159
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_59",
            "reference": [
              76.0,
              622.5,
              51.0,
              16.0
            ],
            "native": [
              76.0,
              622.5,
              51.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              130,
              129,
              129
            ],
            "native_color": [
              117,
              131,
              124
            ],
            "issues": []
          },
          {
            "id": "text_60",
            "reference": [
              254.0,
              626.0,
              98.5,
              12.5
            ],
            "native": [
              254.0,
              626.0,
              98.5,
              12.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              160,
              160,
              160
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              18.0,
              0.0,
              370.0,
              776.0
            ],
            "native": [
              18.0,
              0.0,
              370.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "order_product",
            "reference": [
              32.313346228239844,
              152.47970479704796,
              339.94197292069634,
              136.01476014760146
            ],
            "native": [
              32.31334686279297,
              152.47970581054688,
              339.9419860839844,
              136.01475524902344
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "product_photo",
            "reference": [
              47.5,
              179.5,
              89.5,
              87.5
            ],
            "native": [
              47.5,
              179.5,
              89.5,
              87.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "order_details",
            "reference": [
              32.313346228239844,
              289.21033210332104,
              339.94197292069634,
              211.18081180811808
            ],
            "native": [
              32.31334686279297,
              289.2103271484375,
              339.9419860839844,
              211.18081665039062
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "divider_0",
            "reference": [
              49.48936170212766,
              377.26199261992616,
              304.1586073500967,
              0.7158671586715867
            ],
            "native": [
              49.48936080932617,
              377.2619934082031,
              304.1585998535156,
              0.7158671617507935
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "divider_1",
            "reference": [
              49.48936170212766,
              435.9630996309963,
              304.1586073500967,
              0.7158671586715867
            ],
            "native": [
              49.48936080932617,
              435.9631042480469,
              304.1585998535156,
              0.7158671617507935
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "person_icon_2",
            "reference": [
              53.06769825918762,
              308.53874538745384,
              22.901353965183752,
              23.62361623616236
            ],
            "native": [
              53.06769943237305,
              308.53875732421875,
              22.90135383605957,
              23.62361717224121
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "calendar_icon_3",
            "reference": [
              53.06769825918762,
              395.15867158671585,
              25.04835589941973,
              24.339483394833948
            ],
            "native": [
              53.06769943237305,
              395.1586608886719,
              25.048355102539062,
              24.3394832611084
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "wrench_icon_4",
            "reference": [
              52.35203094777563,
              454.57564575645756,
              25.04835589941973,
              24.339483394833948
            ],
            "native": [
              52.35203170776367,
              454.5756530761719,
              25.048355102539062,
              24.3394832611084
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "divider_2",
            "reference": [
              50.20502901353965,
              531.8892988929889,
              1.4313346228239845,
              99.50553505535055
            ],
            "native": [
              50.20502853393555,
              531.8892822265625,
              1.4313346147537231,
              99.50553131103516
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "back",
            "reference": [
              32.313346228239844,
              47.96309963099631,
              28.626692456479688,
              37.22509225092251
            ],
            "native": [
              32.31334686279297,
              47.96310043334961,
              28.626692,
              37.225094
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "back_surface",
            "reference": [
              32.313346228239844,
              47.96309963099631,
              28.626692456479688,
              37.22509225092251
            ],
            "native": [
              32.31334686279297,
              47.96310043334961,
              28.626691818237305,
              37.225093841552734
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "back_control",
            "reference": [
              32.313346228239844,
              47.96309963099631,
              28.626692456479688,
              37.22509225092251
            ],
            "native": [
              32.31334686279297,
              47.96310043334961,
              28.626691818237305,
              37.225093841552734
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "view_logistics",
            "reference": [
              36.6073500967118,
              693.6752767527674,
              151.72147001934235,
              52.25830258302583
            ],
            "native": [
              36.60734939575195,
              693.67529296875,
              151.72147,
              52.2583
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "view_logistics_surface",
            "reference": [
              36.6073500967118,
              693.6752767527674,
              151.72147001934235,
              52.25830258302583
            ],
            "native": [
              36.60734939575195,
              693.67529296875,
              151.72146606445312,
              52.25830078125
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "view_logistics_control",
            "reference": [
              36.6073500967118,
              693.6752767527674,
              151.72147001934235,
              52.25830258302583
            ],
            "native": [
              36.60734939575195,
              693.67529296875,
              151.72146606445312,
              52.25830078125
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "support",
            "reference": [
              217.67117988394583,
              693.6752767527674,
              149.5744680851064,
              51.54243542435424
            ],
            "native": [
              217.67117309570312,
              693.67529296875,
              149.57446,
              51.542435
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "support_surface",
            "reference": [
              217.67117988394583,
              693.6752767527674,
              149.5744680851064,
              51.54243542435424
            ],
            "native": [
              217.67117309570312,
              693.67529296875,
              149.574462890625,
              51.54243469238281
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "support_control",
            "reference": [
              217.67117988394583,
              693.6752767527674,
              149.5744680851064,
              51.54243542435424
            ],
            "native": [
              217.67117309570312,
              693.67529296875,
              149.574462890625,
              51.54243469238281
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "back_icon_0",
            "reference": [
              34.460348162475825,
              50.11070110701107,
              22.901353965183752,
              28.634686346863468
            ],
            "native": [
              34.460350036621094,
              50.11070251464844,
              22.90135383605957,
              28.634685516357422
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "check_icon_1",
            "reference": [
              39.47001934235976,
              108.81180811808117,
              28.626692456479688,
              28.634686346863468
            ],
            "native": [
              39.47002029418945,
              108.81180572509766,
              28.626691818237305,
              28.634685516357422
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_0",
            "reference": [
              45.195357833655706,
              522.5830258302583,
              12.88201160541586,
              12.88560885608856
            ],
            "native": [
              45.19535827636719,
              522.5830078125,
              12.882011413574219,
              12.885608673095703
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_1",
            "reference": [
              45.195357833655706,
              572.6937269372694,
              12.88201160541586,
              12.88560885608856
            ],
            "native": [
              45.19535827636719,
              572.6937255859375,
              12.882011413574219,
              12.885608673095703
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_2",
            "reference": [
              45.195357833655706,
              624.9520295202951,
              12.88201160541586,
              12.88560885608856
            ],
            "native": [
              45.19535827636719,
              624.9520263671875,
              12.882011413574219,
              12.885608673095703
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "back",
            "second": "back_icon_0",
            "vertical_gap_reference": -35.07749077490775,
            "vertical_gap_native": -35.07749191870117,
            "left_alignment_delta": 1.2395921444863234e-06
          },
          {
            "first": "back_icon_0",
            "second": "check_icon_1",
            "vertical_gap_reference": 30.06642066420664,
            "vertical_gap_native": 30.066417694091797,
            "left_alignment_delta": -9.223155785775816e-07
          },
          {
            "first": "check_icon_1",
            "second": "order_product",
            "vertical_gap_reference": 15.033210332103316,
            "vertical_gap_native": 15.033214569091797,
            "left_alignment_delta": -3.1727656590874176e-07
          },
          {
            "first": "order_product",
            "second": "order_details",
            "vertical_gap_reference": 0.7158671586716139,
            "vertical_gap_native": 0.7158660888671875,
            "left_alignment_delta": 0.0
          },
          {
            "first": "order_details",
            "second": "step_0",
            "vertical_gap_reference": 22.191881918819178,
            "vertical_gap_native": 22.191864013671875,
            "left_alignment_delta": -1.9184164301577766e-07
          },
          {
            "first": "step_0",
            "second": "divider_2",
            "vertical_gap_reference": -3.5793357933579486,
            "vertical_gap_native": -3.579334259033203,
            "left_alignment_delta": -9.22315585683009e-07
          },
          {
            "first": "divider_2",
            "second": "step_1",
            "vertical_gap_reference": -58.701107011070064,
            "vertical_gap_native": -58.701087951660156,
            "left_alignment_delta": 9.22315585683009e-07
          },
          {
            "first": "step_1",
            "second": "step_2",
            "vertical_gap_reference": 39.37269372693718,
            "vertical_gap_native": 39.3726921081543,
            "left_alignment_delta": 0.0
          },
          {
            "first": "step_2",
            "second": "view_logistics",
            "vertical_gap_reference": 55.83763837638376,
            "vertical_gap_native": 55.8376579284668,
            "left_alignment_delta": -1.1436713265311482e-06
          },
          {
            "first": "view_logistics",
            "second": "support",
            "vertical_gap_reference": -52.25830258302583,
            "vertical_gap_native": -52.2583,
            "left_alignment_delta": -6.087282855560261e-06
          },
          {
            "first": "person_icon_2",
            "second": "divider_0",
            "vertical_gap_reference": 45.099630996309955,
            "vertical_gap_native": 45.099618911743164,
            "left_alignment_delta": -2.065986912214157e-06
          },
          {
            "first": "divider_0",
            "second": "calendar_icon_3",
            "vertical_gap_reference": 17.180811808118108,
            "vertical_gap_native": 17.180800318717957,
            "left_alignment_delta": 2.065986912214157e-06
          },
          {
            "first": "calendar_icon_3",
            "second": "divider_1",
            "vertical_gap_reference": 16.46494464944648,
            "vertical_gap_native": 16.4649600982666,
            "left_alignment_delta": -2.065986912214157e-06
          },
          {
            "first": "divider_1",
            "second": "wrench_icon_4",
            "vertical_gap_reference": 17.896678966789693,
            "vertical_gap_native": 17.896681666374207,
            "left_alignment_delta": 1.6527895283502403e-06
          },
          {
            "first": "back_surface",
            "second": "back_control",
            "vertical_gap_reference": -37.22509225092251,
            "vertical_gap_native": -37.225093841552734,
            "left_alignment_delta": 0.0
          },
          {
            "first": "view_logistics_surface",
            "second": "view_logistics_control",
            "vertical_gap_reference": -52.25830258302583,
            "vertical_gap_native": -52.25830078125,
            "left_alignment_delta": 0.0
          },
          {
            "first": "support_surface",
            "second": "support_control",
            "vertical_gap_reference": -51.54243542435424,
            "vertical_gap_native": -51.54243469238281,
            "left_alignment_delta": 0.0
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-02/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-02/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-02/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-02/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-02/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-02/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/02.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-02/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-02/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-02/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-02/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 3,
      "id": "aircon-03",
      "title": "桌面订单卡",
      "description": "订单应用在桌面显示订单状态",
      "surface": "系统桌面",
      "branch": false,
      "base": "../cards/aircon-03/",
      "reference": "../cards/aircon-03/reference.png",
      "native": "../cards/aircon-03/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "e92ca8ec1be74d608c9d5fe704a7d0e9"
      },
      "run": {
        "id": "aircon-03",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-03",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "1777c206305ce793954dca0884f803521a96c117693300a6c957cd7e4af6856b",
          "reference_sha256": "ea9fbe0de1e6bd529d655839ec606c3e5375caff6bfada9f0d88696134c6e0d6",
          "id": "aircon-03",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "order_card",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "product_photo",
              "role": "photo",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Image"
              ],
              "actual_widget": "Image",
              "issues": [],
              "repair": "Use an original or separately generated image asset with documented crop, fit and clipping."
            },
            {
              "id": "view_order",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "view_order_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "view_order_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_110",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "collapse",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "collapse_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "collapse_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_111",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "order_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_105",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_106",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_107",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_108",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_109",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_103",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_104",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_112",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_113",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_114",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_115",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_116",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 5.329,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "ea9fbe0de1e6bd529d655839ec606c3e5375caff6bfada9f0d88696134c6e0d6",
            "native_sha256": "a243087aa24f8d27b7ca32e9e68c8417e47ca15108cb9fbecd8fb5a9541ae230",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_111: text color",
          "text_106: text color",
          "text_107: text color",
          "text_108: text color",
          "text_109: text color",
          "text_103: text color",
          "text_112: text color",
          "text_113: text color",
          "text_114: text color",
          "text_115: text color",
          "text_116: text color"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              16.0,
              0.0,
              373.5,
              776.0
            ],
            "actual_bounds": [
              16.0,
              0.0,
              373.5,
              776.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "order_card",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              35.9961759082218,
              167.7644894204232,
              324.9378585086042,
              376.9346826126955
            ],
            "actual_bounds": [
              35.996177673339844,
              167.76449584960938,
              324.9378662109375,
              376.9346923828125
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "product_photo",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              55.5,
              246.5,
              98.5,
              98.5
            ],
            "actual_bounds": [
              55.5,
              246.5,
              98.5,
              98.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Image",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_order",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              56.70650095602294,
              469.7405703771849,
              133.54588910133842,
              48.544618215271385
            ],
            "actual_bounds": [
              56.70650100708008,
              469.7405700683594,
              133.54588,
              48.544617
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "查看订单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_order_surface",
            "native_id": "beauty_0_0_0_1_0",
            "expected_bounds": [
              56.70650095602294,
              469.7405703771849,
              133.54588910133842,
              48.544618215271385
            ],
            "actual_bounds": [
              56.70650100708008,
              469.7405700683594,
              133.54588317871094,
              48.54461669921875
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_order_control",
            "native_id": "beauty_0_0_0_1_1",
            "expected_bounds": [
              56.70650095602294,
              469.7405703771849,
              133.54588910133842,
              48.544618215271385
            ],
            "actual_bounds": [
              56.70650100708008,
              469.7405700683594,
              133.54588317871094,
              48.54461669921875
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_110",
            "native_id": "beauty_0_0_0_1_2",
            "expected_bounds": [
              85.04122622323818,
              483.02155582476684,
              80.81428743420736,
              21.5
            ],
            "actual_bounds": [
              85.04122924804688,
              483.02154541015625,
              80.814285,
              21.5
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "查看订单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "collapse",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              220.96080305927342,
              469.7405703771849,
              114.26386233269598,
              48.544618215271385
            ],
            "actual_bounds": [
              220.96080017089844,
              469.7405700683594,
              114.26386,
              48.544617
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "收起",
            "enabled": true,
            "issues": []
          },
          {
            "id": "collapse_surface",
            "native_id": "beauty_0_0_0_2_0",
            "expected_bounds": [
              220.96080305927342,
              469.7405703771849,
              114.26386233269598,
              48.544618215271385
            ],
            "actual_bounds": [
              220.96080017089844,
              469.7405700683594,
              114.26386260986328,
              48.54461669921875
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "collapse_control",
            "native_id": "beauty_0_0_0_2_1",
            "expected_bounds": [
              220.96080305927342,
              469.7405703771849,
              114.26386233269598,
              48.544618215271385
            ],
            "actual_bounds": [
              220.96080017089844,
              469.7405700683594,
              114.26386260986328,
              48.54461669921875
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_111",
            "native_id": "beauty_0_0_0_2_2",
            "expected_bounds": [
              257.78741701953413,
              483.7859966764461,
              40.035480978982584,
              20.5
            ],
            "actual_bounds": [
              257.78741455078125,
              483.7860107421875,
              40.03548,
              20.5
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Label",
            "visible": true,
            "text": "收起",
            "enabled": true,
            "issues": []
          },
          {
            "id": "order_icon_0",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              60.27724665391969,
              191.32290708371664,
              32.136711281070745,
              32.12511499540018
            ],
            "actual_bounds": [
              60.27724838256836,
              191.32290649414062,
              32.13671112060547,
              32.12511444091797
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_105",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              109.99347940153123,
              197.79885333075654,
              120.40245669620035,
              21.0
            ],
            "actual_bounds": [
              109.99347686767578,
              197.79885864257812,
              120.40246,
              21.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "订单 · 已付款",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_106",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              169.05524777988424,
              267.8082162844657,
              117.350191308305,
              20.0
            ],
            "actual_bounds": [
              169.0552520751953,
              267.8082275390625,
              117.35019,
              20.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "1.5匹变频空调",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_107",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              169.69196664957389,
              309.475685127965,
              67.28553346437025,
              21.0
            ],
            "actual_bounds": [
              169.6919708251953,
              309.4756774902344,
              67.28553,
              21.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "¥2,799",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_108",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              58.0310512998521,
              376.54718658113813,
              125.79680299848464,
              21.720251040543904
            ],
            "actual_bounds": [
              58.03105163574219,
              376.54718017578125,
              125.79681,
              21.720251
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "预计周五送达",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_109",
            "native_id": "beauty_0_0_0_8",
            "expected_bounds": [
              57.82994515026223,
              416.42705380282047,
              107.8809639701624,
              18.5
            ],
            "actual_bounds": [
              57.8299446105957,
              416.42706298828125,
              107.88097,
              18.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "来自购物订单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              16.0,
              661.7773689052437,
              373.5,
              114.22263109475621
            ],
            "actual_bounds": [
              16.0,
              661.77734375,
              373.5,
              114.2226333618164
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              39.01345602294455,
              670.486844526219,
              68.26408795411089,
              68.23945538178472
            ],
            "actual_bounds": [
              39.01345443725586,
              670.48681640625,
              68.26409149169922,
              68.23945617675781
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              49.7256931166348,
              684.0507819687213,
              46.839613766730395,
              44.681037718491254
            ],
            "actual_bounds": [
              49.72569274902344,
              684.05078125,
              46.83961486816406,
              44.68103790283203
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              126.78595602294455,
              670.486844526219,
              68.26408795411089,
              68.23945538178472
            ],
            "actual_bounds": [
              126.78595733642578,
              670.48681640625,
              68.26409149169922,
              68.23945617675781
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              214.5584560229445,
              670.486844526219,
              68.26408795411089,
              68.23945538178472
            ],
            "actual_bounds": [
              214.55845642089844,
              670.48681640625,
              68.26409149169922,
              68.23945617675781
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_1_4",
            "expected_bounds": [
              225.27069311663476,
              684.0507819687213,
              46.839613766730395,
              44.681037718491254
            ],
            "actual_bounds": [
              225.27069091796875,
              684.05078125,
              46.83961486816406,
              44.68103790283203
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_1_5",
            "expected_bounds": [
              302.3309560229445,
              670.486844526219,
              68.26408795411089,
              68.23945538178472
            ],
            "actual_bounds": [
              302.3309631347656,
              670.48681640625,
              68.26409149169922,
              68.23945617675781
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_1_6",
            "expected_bounds": [
              313.04319311663477,
              684.0507819687213,
              46.839613766730395,
              44.681037718491254
            ],
            "actual_bounds": [
              313.0431823730469,
              684.05078125,
              46.83961486816406,
              44.68103790283203
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_103",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              44.381646296932104,
              26.718706975554362,
              104.5952416370661,
              18.0
            ],
            "actual_bounds": [
              44.38164520263672,
              26.718706130981445,
              104.595245,
              18.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月17日 周四",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_104",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              41.20444199148308,
              60.45924573310922,
              101.64164057119383,
              31.5
            ],
            "actual_bounds": [
              41.20444107055664,
              60.45924758911133,
              101.64164,
              31.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "09:46",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_112",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              54.55453428965638,
              738.0603153879359,
              36.37593614531091,
              18.5
            ],
            "actual_bounds": [
              54.554534912109375,
              738.060302734375,
              36.375935,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_113",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              139.24668586048773,
              695.9163574455233,
              32.80652494504185,
              24.0
            ],
            "actual_bounds": [
              139.24668884277344,
              695.9163818359375,
              32.806526,
              24.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "17",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_114",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              137.27360545226375,
              738.8694921409943,
              34.9841313367003,
              17.0
            ],
            "actual_bounds": [
              137.2736053466797,
              738.8695068359375,
              34.98413,
              17.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_115",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              225.6003966312072,
              738.2100253313249,
              34.10708259328741,
              18.0
            ],
            "actual_bounds": [
              225.60040283203125,
              738.2100219726562,
              34.107082,
              18.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_116",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              311.0583083357868,
              737.992015987206,
              35.811422371783806,
              18.5
            ],
            "actual_bounds": [
              311.0583190917969,
              737.9920043945312,
              35.811424,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_110",
            "reference": [
              86.0,
              485.0,
              73.0,
              17.5
            ],
            "native": [
              86.0,
              485.0,
              73.0,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              244,
              248,
              245
            ],
            "native_color": [
              255,
              255,
              255
            ],
            "issues": []
          },
          {
            "id": "text_111",
            "reference": [
              259.0,
              485.5,
              32.5,
              16.5
            ],
            "native": [
              259.0,
              485.5,
              32.5,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              112,
              114,
              113
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_105",
            "reference": [
              111.0,
              199.5,
              112.5,
              17.0
            ],
            "native": [
              111.0,
              199.5,
              112.5,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              54,
              54,
              53
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_106",
            "reference": [
              170.5,
              269.5,
              109.0,
              16.0
            ],
            "native": [
              170.5,
              269.5,
              109.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              73,
              73,
              73
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_107",
            "reference": [
              170.5,
              313.0,
              60.0,
              17.0
            ],
            "native": [
              170.5,
              313.0,
              60.0,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              16,
              16,
              16
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_108",
            "reference": [
              59.0,
              378.5,
              118.5,
              17.5
            ],
            "native": [
              59.0,
              378.5,
              118.0,
              17.5
            ],
            "delta": [
              0.0,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              30,
              29,
              30
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_109",
            "reference": [
              58.5,
              418.0,
              101.0,
              14.5
            ],
            "native": [
              58.5,
              418.0,
              101.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              113,
              113,
              113
            ],
            "native_color": [
              117,
              131,
              124
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_103",
            "reference": [
              45.0,
              28.5,
              97.0,
              14.0
            ],
            "native": [
              45.0,
              28.5,
              97.0,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              81,
              85,
              83
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_104",
            "reference": [
              43.0,
              62.5,
              94.5,
              27.5
            ],
            "native": [
              43.0,
              62.5,
              92.5,
              27.5
            ],
            "delta": [
              0.0,
              0.0,
              -2.0,
              0.0
            ],
            "reference_color": [
              58,
              70,
              64
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_112",
            "reference": [
              56.0,
              739.5,
              29.0,
              14.5
            ],
            "native": [
              56.0,
              739.5,
              29.0,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              95,
              104,
              101
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_113",
            "reference": [
              141.5,
              697.5,
              24.0,
              20.0
            ],
            "native": [
              141.5,
              697.5,
              24.0,
              18.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -2.0
            ],
            "reference_color": [
              98,
              105,
              100
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_114",
            "reference": [
              140.0,
              740.5,
              26.5,
              13.0
            ],
            "native": [
              140.0,
              740.5,
              26.5,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              80,
              88,
              85
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_115",
            "reference": [
              226.5,
              739.5,
              28.0,
              14.0
            ],
            "native": [
              226.5,
              739.5,
              28.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              97,
              105,
              102
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_116",
            "reference": [
              312.0,
              739.5,
              29.0,
              14.5
            ],
            "native": [
              312.0,
              739.5,
              29.0,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              101,
              108,
              106
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              16.0,
              0.0,
              373.5,
              776.0
            ],
            "native": [
              16.0,
              0.0,
              373.5,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "order_card",
            "reference": [
              35.9961759082218,
              167.7644894204232,
              324.9378585086042,
              376.9346826126955
            ],
            "native": [
              35.996177673339844,
              167.76449584960938,
              324.9378662109375,
              376.9346923828125
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "product_photo",
            "reference": [
              55.5,
              246.5,
              98.5,
              98.5
            ],
            "native": [
              55.5,
              246.5,
              98.5,
              98.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "view_order",
            "reference": [
              56.70650095602294,
              469.7405703771849,
              133.54588910133842,
              48.544618215271385
            ],
            "native": [
              56.70650100708008,
              469.7405700683594,
              133.54588,
              48.544617
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "view_order_surface",
            "reference": [
              56.70650095602294,
              469.7405703771849,
              133.54588910133842,
              48.544618215271385
            ],
            "native": [
              56.70650100708008,
              469.7405700683594,
              133.54588317871094,
              48.54461669921875
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "view_order_control",
            "reference": [
              56.70650095602294,
              469.7405703771849,
              133.54588910133842,
              48.544618215271385
            ],
            "native": [
              56.70650100708008,
              469.7405700683594,
              133.54588317871094,
              48.54461669921875
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "collapse",
            "reference": [
              220.96080305927342,
              469.7405703771849,
              114.26386233269598,
              48.544618215271385
            ],
            "native": [
              220.96080017089844,
              469.7405700683594,
              114.26386,
              48.544617
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "collapse_surface",
            "reference": [
              220.96080305927342,
              469.7405703771849,
              114.26386233269598,
              48.544618215271385
            ],
            "native": [
              220.96080017089844,
              469.7405700683594,
              114.26386260986328,
              48.54461669921875
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "collapse_control",
            "reference": [
              220.96080305927342,
              469.7405703771849,
              114.26386233269598,
              48.544618215271385
            ],
            "native": [
              220.96080017089844,
              469.7405700683594,
              114.26386260986328,
              48.54461669921875
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "order_icon_0",
            "reference": [
              60.27724665391969,
              191.32290708371664,
              32.136711281070745,
              32.12511499540018
            ],
            "native": [
              60.27724838256836,
              191.32290649414062,
              32.13671112060547,
              32.12511444091797
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              16.0,
              661.7773689052437,
              373.5,
              114.22263109475621
            ],
            "native": [
              16.0,
              661.77734375,
              373.5,
              114.2226333618164
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              39.01345602294455,
              670.486844526219,
              68.26408795411089,
              68.23945538178472
            ],
            "native": [
              39.01345443725586,
              670.48681640625,
              68.26409149169922,
              68.23945617675781
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              49.7256931166348,
              684.0507819687213,
              46.839613766730395,
              44.681037718491254
            ],
            "native": [
              49.72569274902344,
              684.05078125,
              46.83961486816406,
              44.68103790283203
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              126.78595602294455,
              670.486844526219,
              68.26408795411089,
              68.23945538178472
            ],
            "native": [
              126.78595733642578,
              670.48681640625,
              68.26409149169922,
              68.23945617675781
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              214.5584560229445,
              670.486844526219,
              68.26408795411089,
              68.23945538178472
            ],
            "native": [
              214.55845642089844,
              670.48681640625,
              68.26409149169922,
              68.23945617675781
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              225.27069311663476,
              684.0507819687213,
              46.839613766730395,
              44.681037718491254
            ],
            "native": [
              225.27069091796875,
              684.05078125,
              46.83961486816406,
              44.68103790283203
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              302.3309560229445,
              670.486844526219,
              68.26408795411089,
              68.23945538178472
            ],
            "native": [
              302.3309631347656,
              670.48681640625,
              68.26409149169922,
              68.23945617675781
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              313.04319311663477,
              684.0507819687213,
              46.839613766730395,
              44.681037718491254
            ],
            "native": [
              313.0431823730469,
              684.05078125,
              46.83961486816406,
              44.68103790283203
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "order_card",
            "second": "dock",
            "vertical_gap_reference": 117.07819687212509,
            "vertical_gap_native": 117.07815551757812,
            "left_alignment_delta": -1.7651180428401858e-06
          },
          {
            "first": "order_icon_0",
            "second": "product_photo",
            "vertical_gap_reference": 23.051977920883175,
            "vertical_gap_native": 23.051979064941406,
            "left_alignment_delta": -1.728648669541144e-06
          },
          {
            "first": "product_photo",
            "second": "view_order",
            "vertical_gap_reference": 124.7405703771849,
            "vertical_gap_native": 124.74057006835938,
            "left_alignment_delta": 5.105713540842771e-08
          },
          {
            "first": "view_order",
            "second": "collapse",
            "vertical_gap_reference": -48.544618215271385,
            "vertical_gap_native": -48.544617,
            "left_alignment_delta": -2.9394321074960317e-06
          },
          {
            "first": "view_order_surface",
            "second": "view_order_control",
            "vertical_gap_reference": -48.544618215271385,
            "vertical_gap_native": -48.54461669921875,
            "left_alignment_delta": 0.0
          },
          {
            "first": "collapse_surface",
            "second": "collapse_control",
            "vertical_gap_reference": -48.544618215271385,
            "vertical_gap_native": -48.54461669921875,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -68.23945538178472,
            "vertical_gap_native": -68.23945617675781,
            "left_alignment_delta": 2.899169928127776e-06
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -68.23945538178472,
            "vertical_gap_native": -68.23945617675781,
            "left_alignment_delta": -9.155273090755145e-07
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -68.23945538178472,
            "vertical_gap_native": -68.23945617675781,
            "left_alignment_delta": 6.713867179541921e-06
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -54.67551793928246,
            "vertical_gap_native": -54.67549133300781,
            "left_alignment_delta": -7.479432468926461e-06
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -44.681037718491254,
            "vertical_gap_native": -44.68103790283203,
            "left_alignment_delta": -1.8310546465727384e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -44.681037718491254,
            "vertical_gap_native": -44.68103790283203,
            "left_alignment_delta": -8.544921882958079e-06
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-03/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-03/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-03/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-03/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-03/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-03/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/03.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-03/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-03/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-03/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-03/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 4,
      "id": "aircon-04",
      "title": "物流更新",
      "description": "物流应用更新预计送达时间",
      "surface": "系统桌面",
      "branch": false,
      "base": "../cards/aircon-04/",
      "reference": "../cards/aircon-04/reference.png",
      "native": "../cards/aircon-04/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "7eac2409717742218be10a71c730293f"
      },
      "run": {
        "id": "aircon-04",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-04",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "61624bcf5632a3480c64ead2bf811e514971d90f45a1d47b6fffb3ae13562687",
          "reference_sha256": "ef12a7ded90c10cf85feb9e81c7457d8cdf84616ad2f8c0b91cf7fcf6a8e63ad",
          "id": "aircon-04",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "logistics_card",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "divider_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "courier",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "courier_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "courier_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_169",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "delivery_time",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "delivery_time_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "delivery_time_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_170",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "truck_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "home_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "step_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "step_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "step_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "text_162",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_163",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_164",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_165",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_166",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_167",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_168",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_212",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_160",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_161",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_171",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_172",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_173",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_174",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_213",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 6.542,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "ef12a7ded90c10cf85feb9e81c7457d8cdf84616ad2f8c0b91cf7fcf6a8e63ad",
            "native_sha256": "5e14338db6803c85c5f30659f8b7007354be24cfc6e062f42be818a513c2bf7e",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_169: text color",
          "text_170: text color",
          "text_162: text color",
          "text_163: text ink dimensions",
          "text_163: text color",
          "text_165: text color",
          "text_166: text color",
          "text_167: reference OCR text differs",
          "text_167: text ink position",
          "text_167: text ink dimensions",
          "text_167: text color",
          "text_212: text color",
          "text_160: text color",
          "text_171: text color",
          "text_172: reference text missing or OCR unresolved",
          "text_173: text color",
          "text_174: text color",
          "text_213: text color",
          "1 extra reference text observations need classification"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              0.0,
              42.0,
              406.0,
              692.0
            ],
            "actual_bounds": [
              0.0,
              42.0,
              406.0,
              692.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "logistics_card",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              17.846153846153847,
              187.28176795580112,
              364.57142857142856,
              384.23204419889504
            ],
            "actual_bounds": [
              17.846153259277344,
              187.28176879882812,
              364.5714416503906,
              384.2320556640625
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_0",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              67.56043956043956,
              358.05156537753226,
              251.75824175824175,
              1.9116022099447516
            ],
            "actual_bounds": [
              67.56044006347656,
              358.05157470703125,
              251.75823974609375,
              1.911602258682251
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "courier",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              38.879120879120876,
              503.33333333333337,
              138.94505494505495,
              43.32965009208103
            ],
            "actual_bounds": [
              38.879119873046875,
              503.3333435058594,
              138.94505,
              43.32965
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "联系配送员",
            "enabled": true,
            "issues": []
          },
          {
            "id": "courier_surface",
            "native_id": "beauty_0_0_0_1_0",
            "expected_bounds": [
              38.879120879120876,
              503.33333333333337,
              138.94505494505495,
              43.32965009208103
            ],
            "actual_bounds": [
              38.879119873046875,
              503.3333435058594,
              138.94505310058594,
              43.32965087890625
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "courier_control",
            "native_id": "beauty_0_0_0_1_1",
            "expected_bounds": [
              38.879120879120876,
              503.33333333333337,
              138.94505494505495,
              43.32965009208103
            ],
            "actual_bounds": [
              38.879119873046875,
              503.3333435058594,
              138.94505310058594,
              43.32965087890625
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_169",
            "native_id": "beauty_0_0_0_1_2",
            "expected_bounds": [
              65.60733494511243,
              515.770501910413,
              90.21949312157888,
              18.5
            ],
            "actual_bounds": [
              65.60733795166016,
              515.7705078125,
              90.21949,
              18.5
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "联系配送员",
            "enabled": true,
            "issues": []
          },
          {
            "id": "delivery_time",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              210.96703296703296,
              503.33333333333337,
              130.65934065934064,
              43.32965009208103
            ],
            "actual_bounds": [
              210.96702575683594,
              503.3333435058594,
              130.65935,
              43.32965
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "修改时间",
            "enabled": true,
            "issues": []
          },
          {
            "id": "delivery_time_surface",
            "native_id": "beauty_0_0_0_2_0",
            "expected_bounds": [
              210.96703296703296,
              503.33333333333337,
              130.65934065934064,
              43.32965009208103
            ],
            "actual_bounds": [
              210.96702575683594,
              503.3333435058594,
              130.6593475341797,
              43.32965087890625
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "delivery_time_control",
            "native_id": "beauty_0_0_0_2_1",
            "expected_bounds": [
              210.96703296703296,
              503.33333333333337,
              130.65934065934064,
              43.32965009208103
            ],
            "actual_bounds": [
              210.96702575683594,
              503.3333435058594,
              130.6593475341797,
              43.32965087890625
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_170",
            "native_id": "beauty_0_0_0_2_2",
            "expected_bounds": [
              241.45789794991273,
              515.975466362635,
              71.95172789494816,
              18.5
            ],
            "actual_bounds": [
              241.45790100097656,
              515.9754638671875,
              71.95173,
              18.5
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Label",
            "visible": true,
            "text": "修改时间",
            "enabled": true,
            "issues": []
          },
          {
            "id": "truck_icon_0",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              36.967032967032964,
              212.1325966850829,
              36.967032967032964,
              26.762430939226522
            ],
            "actual_bounds": [
              36.96703338623047,
              212.13259887695312,
              36.96703338623047,
              26.76243019104004
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "home_icon_1",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              37.6043956043956,
              428.78084714548805,
              19.758241758241756,
              19.753222836095766
            ],
            "actual_bounds": [
              37.60439682006836,
              428.7808532714844,
              19.758241653442383,
              19.753223419189453
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_0",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              59.912087912087905,
              351.6795580110497,
              14.659340659340659,
              14.655616942909761
            ],
            "actual_bounds": [
              59.912086486816406,
              351.6795654296875,
              14.659340858459473,
              14.655616760253906
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_1",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              182.9230769230769,
              350.4051565377532,
              18.483516483516482,
              18.478821362799266
            ],
            "actual_bounds": [
              182.92308044433594,
              350.4051513671875,
              18.483516693115234,
              18.47882080078125
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_2",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              312.30769230769226,
              351.6795580110497,
              14.659340659340659,
              14.655616942909761
            ],
            "actual_bounds": [
              312.30767822265625,
              351.6795654296875,
              14.659340858459473,
              14.655616760253906
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_162",
            "native_id": "beauty_0_0_0_8",
            "expected_bounds": [
              89.64849936487842,
              214.98118695648202,
              110.07348831301708,
              19.5
            ],
            "actual_bounds": [
              89.64849853515625,
              214.98118591308594,
              110.07349,
              19.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "物流 · 配送中",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_163",
            "native_id": "beauty_0_0_0_9",
            "expected_bounds": [
              40.39139027867892,
              264.3022552801514,
              204.69876097275252,
              25.0
            ],
            "actual_bounds": [
              40.39139175415039,
              264.30224609375,
              204.69876,
              25.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "周五 14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_164",
            "native_id": "beauty_0_0_0_10",
            "expected_bounds": [
              38.91779244249657,
              301.3671006791659,
              142.58574328053757,
              19.0
            ],
            "actual_bounds": [
              38.91779327392578,
              301.3670959472656,
              142.58574,
              19.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "空调正在送往你家",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_165",
            "native_id": "beauty_0_0_0_11",
            "expected_bounds": [
              47.69552190525411,
              379.7550399311466,
              48.5462777073411,
              17.0
            ],
            "actual_bounds": [
              47.69552230834961,
              379.7550354003906,
              48.546276,
              17.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "已发货",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_166",
            "native_id": "beauty_0_0_0_12",
            "expected_bounds": [
              168.3206967059823,
              379.20780486304994,
              50.86823536163987,
              17.5
            ],
            "actual_bounds": [
              168.32069396972656,
              379.2077941894531,
              50.868237,
              17.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "配送中",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_167",
            "native_id": "beauty_0_0_0_13",
            "expected_bounds": [
              67.17218878026414,
              427.9086768187458,
              131.07518376643543,
              19.58596127963557
            ],
            "actual_bounds": [
              67.17218780517578,
              427.90869140625,
              131.07518,
              19.58596
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "家 · 海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_168",
            "native_id": "beauty_0_0_0_14",
            "expected_bounds": [
              38.93919294004609,
              460.5248509364716,
              97.52527656101167,
              17.6791182626931
            ],
            "actual_bounds": [
              38.93919372558594,
              460.52484130859375,
              97.525276,
              17.67912
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "来自购物订单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_212",
            "native_id": "beauty_0_0_0_15",
            "expected_bounds": [
              296.81526191873087,
              379.2911058416071,
              49.8879968356069,
              17.5
            ],
            "actual_bounds": [
              296.8152770996094,
              379.2911071777344,
              49.887997,
              17.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "已送达",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              0.0,
              633.3222836095765,
              406.0,
              100.67771639042358
            ],
            "actual_bounds": [
              0.0,
              633.322265625,
              406.0,
              100.67771911621094
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              25.988461538461536,
              640.9432044198895,
              72.25907692307692,
              72.24072191528546
            ],
            "actual_bounds": [
              25.988462448120117,
              640.9431762695312,
              72.25907897949219,
              72.24072265625
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              35.5489010989011,
              653.0500184162063,
              53.1381978021978,
              51.21309760589319
            ],
            "actual_bounds": [
              35.54890060424805,
              653.050048828125,
              53.13819885253906,
              51.213096618652344
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              121.39846153846153,
              640.9432044198895,
              72.25907692307692,
              72.24072191528546
            ],
            "actual_bounds": [
              121.3984603881836,
              640.9431762695312,
              72.25907897949219,
              72.24072265625
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              216.8084615384615,
              640.9432044198895,
              72.25907692307692,
              72.24072191528546
            ],
            "actual_bounds": [
              216.80845642089844,
              640.9431762695312,
              72.25907897949219,
              72.24072265625
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_1_4",
            "expected_bounds": [
              226.36890109890106,
              653.0500184162063,
              53.1381978021978,
              51.21309760589319
            ],
            "actual_bounds": [
              226.368896484375,
              653.050048828125,
              53.13819885253906,
              51.213096618652344
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_1_5",
            "expected_bounds": [
              312.2184615384615,
              640.9432044198895,
              72.25907692307692,
              72.24072191528546
            ],
            "actual_bounds": [
              312.2184753417969,
              640.9431762695312,
              72.25907897949219,
              72.24072265625
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_1_6",
            "expected_bounds": [
              321.77890109890103,
              653.0500184162063,
              53.1381978021978,
              51.21309760589319
            ],
            "actual_bounds": [
              321.7789001464844,
              653.050048828125,
              53.13819885253906,
              51.213096618652344
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_160",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              24.3171483743138,
              65.90206368501089,
              94.22202012847313,
              16.062647932212496
            ],
            "actual_bounds": [
              24.317148208618164,
              65.90206146240234,
              94.22202,
              16.062649
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月18日 周五",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_161",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              20.85000626261639,
              95.95406794149645,
              89.93501967353444,
              28.0
            ],
            "actual_bounds": [
              20.850006103515625,
              95.95407104492188,
              89.93502,
              28.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "14:20",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_171",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              45.09057936442751,
              704.435936575599,
              35.890196048970935,
              17.5
            ],
            "actual_bounds": [
              45.090579986572266,
              704.4359130859375,
              35.890198,
              17.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_172",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              125.85654037783272,
              663.5159286861366,
              40.3951164012642,
              28.820813617799093
            ],
            "actual_bounds": [
              125.85653686523438,
              663.5159301757812,
              40.395115,
              28.820814
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "18",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_173",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              133.49300281851367,
              705.2455597012912,
              33.30149983592784,
              16.0
            ],
            "actual_bounds": [
              133.4929962158203,
              705.2455444335938,
              33.3015,
              16.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_174",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              228.76489460254317,
              705.0431759080776,
              33.476236185880815,
              17.0
            ],
            "actual_bounds": [
              228.764892578125,
              705.0431518554688,
              33.476234,
              17.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_213",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              322.75975874358886,
              704.5977145504949,
              35.11225525251117,
              17.5
            ],
            "actual_bounds": [
              322.759765625,
              704.5977172851562,
              35.112255,
              17.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_169",
            "reference": [
              66.5,
              517.5,
              82.5,
              14.5
            ],
            "native": [
              66.5,
              517.5,
              82.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              87,
              107,
              92
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_170",
            "reference": [
              242.0,
              517.5,
              65.0,
              14.5
            ],
            "native": [
              242.0,
              517.5,
              64.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              95,
              95,
              95
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_162",
            "reference": [
              90.5,
              217.0,
              101.5,
              15.5
            ],
            "native": [
              90.5,
              217.0,
              101.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              40,
              39,
              39
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_163",
            "reference": [
              41.5,
              266.5,
              207.0,
              21.0
            ],
            "native": [
              41.5,
              266.5,
              197.0,
              21.0
            ],
            "delta": [
              0.0,
              0.0,
              -10.0,
              0.0
            ],
            "reference_color": [
              29,
              29,
              29
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_164",
            "reference": [
              40.5,
              303.0,
              134.0,
              15.0
            ],
            "native": [
              40.5,
              303.0,
              134.5,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.5,
              0.0
            ],
            "reference_color": [
              60,
              60,
              59
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_165",
            "reference": [
              49.0,
              381.5,
              41.0,
              13.0
            ],
            "native": [
              49.0,
              381.5,
              41.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              71,
              71,
              71
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_166",
            "reference": [
              169.5,
              381.0,
              42.5,
              13.5
            ],
            "native": [
              169.5,
              381.0,
              42.5,
              13.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              74,
              74,
              74
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_167",
            "reference": [
              42.0,
              429.5,
              150.5,
              15.5
            ],
            "native": [
              68.5,
              430.0,
              124.5,
              15.0
            ],
            "delta": [
              26.5,
              0.5,
              -26.0,
              -0.5
            ],
            "reference_color": [
              82,
              83,
              83
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink position",
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_168",
            "reference": [
              40.0,
              462.5,
              90.0,
              13.5
            ],
            "native": [
              40.0,
              462.5,
              90.0,
              13.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              122,
              122,
              123
            ],
            "native_color": [
              117,
              131,
              124
            ],
            "issues": []
          },
          {
            "id": "text_212",
            "reference": [
              298.5,
              381.0,
              42.0,
              13.5
            ],
            "native": [
              298.5,
              381.0,
              42.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              86,
              86,
              86
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_160",
            "reference": [
              25.0,
              68.0,
              87.0,
              12.0
            ],
            "native": [
              25.0,
              68.0,
              87.0,
              12.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              76,
              81,
              78
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_161",
            "reference": [
              24.0,
              98.0,
              79.5,
              24.0
            ],
            "native": [
              24.0,
              98.0,
              79.5,
              24.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              58,
              71,
              64
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_171",
            "reference": [
              46.5,
              706.0,
              28.0,
              13.5
            ],
            "native": [
              46.5,
              706.0,
              28.0,
              13.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              90,
              103,
              98
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_172",
            "reference": null,
            "native": null,
            "delta": null,
            "reference_color": null,
            "native_color": null,
            "issues": [
              "reference text missing or OCR unresolved"
            ]
          },
          {
            "id": "text_173",
            "reference": [
              136.0,
              707.0,
              25.0,
              12.0
            ],
            "native": [
              136.0,
              707.0,
              25.0,
              12.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              91,
              102,
              97
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_174",
            "reference": [
              229.5,
              706.5,
              27.0,
              13.0
            ],
            "native": [
              229.5,
              706.5,
              27.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              96,
              105,
              100
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_213",
            "reference": [
              323.5,
              706.0,
              28.0,
              13.5
            ],
            "native": [
              323.5,
              706.5,
              28.0,
              13.0
            ],
            "delta": [
              0.0,
              0.5,
              0.0,
              -0.5
            ],
            "reference_color": [
              96,
              109,
              104
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              0.0,
              42.0,
              406.0,
              692.0
            ],
            "native": [
              0.0,
              42.0,
              406.0,
              692.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "logistics_card",
            "reference": [
              17.846153846153847,
              187.28176795580112,
              364.57142857142856,
              384.23204419889504
            ],
            "native": [
              17.846153259277344,
              187.28176879882812,
              364.5714416503906,
              384.2320556640625
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "divider_0",
            "reference": [
              67.56043956043956,
              358.05156537753226,
              251.75824175824175,
              1.9116022099447516
            ],
            "native": [
              67.56044006347656,
              358.05157470703125,
              251.75823974609375,
              1.911602258682251
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "courier",
            "reference": [
              38.879120879120876,
              503.33333333333337,
              138.94505494505495,
              43.32965009208103
            ],
            "native": [
              38.879119873046875,
              503.3333435058594,
              138.94505,
              43.32965
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "courier_surface",
            "reference": [
              38.879120879120876,
              503.33333333333337,
              138.94505494505495,
              43.32965009208103
            ],
            "native": [
              38.879119873046875,
              503.3333435058594,
              138.94505310058594,
              43.32965087890625
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "courier_control",
            "reference": [
              38.879120879120876,
              503.33333333333337,
              138.94505494505495,
              43.32965009208103
            ],
            "native": [
              38.879119873046875,
              503.3333435058594,
              138.94505310058594,
              43.32965087890625
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "delivery_time",
            "reference": [
              210.96703296703296,
              503.33333333333337,
              130.65934065934064,
              43.32965009208103
            ],
            "native": [
              210.96702575683594,
              503.3333435058594,
              130.65935,
              43.32965
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "delivery_time_surface",
            "reference": [
              210.96703296703296,
              503.33333333333337,
              130.65934065934064,
              43.32965009208103
            ],
            "native": [
              210.96702575683594,
              503.3333435058594,
              130.6593475341797,
              43.32965087890625
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "delivery_time_control",
            "reference": [
              210.96703296703296,
              503.33333333333337,
              130.65934065934064,
              43.32965009208103
            ],
            "native": [
              210.96702575683594,
              503.3333435058594,
              130.6593475341797,
              43.32965087890625
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "truck_icon_0",
            "reference": [
              36.967032967032964,
              212.1325966850829,
              36.967032967032964,
              26.762430939226522
            ],
            "native": [
              36.96703338623047,
              212.13259887695312,
              36.96703338623047,
              26.76243019104004
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "home_icon_1",
            "reference": [
              37.6043956043956,
              428.78084714548805,
              19.758241758241756,
              19.753222836095766
            ],
            "native": [
              37.60439682006836,
              428.7808532714844,
              19.758241653442383,
              19.753223419189453
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "step_0",
            "reference": [
              59.912087912087905,
              351.6795580110497,
              14.659340659340659,
              14.655616942909761
            ],
            "native": [
              59.912086486816406,
              351.6795654296875,
              14.659340858459473,
              14.655616760253906
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_1",
            "reference": [
              182.9230769230769,
              350.4051565377532,
              18.483516483516482,
              18.478821362799266
            ],
            "native": [
              182.92308044433594,
              350.4051513671875,
              18.483516693115234,
              18.47882080078125
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_2",
            "reference": [
              312.30769230769226,
              351.6795580110497,
              14.659340659340659,
              14.655616942909761
            ],
            "native": [
              312.30767822265625,
              351.6795654296875,
              14.659340858459473,
              14.655616760253906
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              0.0,
              633.3222836095765,
              406.0,
              100.67771639042358
            ],
            "native": [
              0.0,
              633.322265625,
              406.0,
              100.67771911621094
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              25.988461538461536,
              640.9432044198895,
              72.25907692307692,
              72.24072191528546
            ],
            "native": [
              25.988462448120117,
              640.9431762695312,
              72.25907897949219,
              72.24072265625
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              35.5489010989011,
              653.0500184162063,
              53.1381978021978,
              51.21309760589319
            ],
            "native": [
              35.54890060424805,
              653.050048828125,
              53.13819885253906,
              51.213096618652344
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              121.39846153846153,
              640.9432044198895,
              72.25907692307692,
              72.24072191528546
            ],
            "native": [
              121.3984603881836,
              640.9431762695312,
              72.25907897949219,
              72.24072265625
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              216.8084615384615,
              640.9432044198895,
              72.25907692307692,
              72.24072191528546
            ],
            "native": [
              216.80845642089844,
              640.9431762695312,
              72.25907897949219,
              72.24072265625
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              226.36890109890106,
              653.0500184162063,
              53.1381978021978,
              51.21309760589319
            ],
            "native": [
              226.368896484375,
              653.050048828125,
              53.13819885253906,
              51.213096618652344
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              312.2184615384615,
              640.9432044198895,
              72.25907692307692,
              72.24072191528546
            ],
            "native": [
              312.2184753417969,
              640.9431762695312,
              72.25907897949219,
              72.24072265625
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              321.77890109890103,
              653.0500184162063,
              53.1381978021978,
              51.21309760589319
            ],
            "native": [
              321.7789001464844,
              653.050048828125,
              53.13819885253906,
              51.213096618652344
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "logistics_card",
            "second": "dock",
            "vertical_gap_reference": 61.80847145488036,
            "vertical_gap_native": 61.808441162109375,
            "left_alignment_delta": 5.868765029504175e-07
          },
          {
            "first": "truck_icon_0",
            "second": "step_1",
            "vertical_gap_reference": 111.51012891344381,
            "vertical_gap_native": 111.51012229919434,
            "left_alignment_delta": 3.1020615267607354e-06
          },
          {
            "first": "step_1",
            "second": "step_0",
            "vertical_gap_reference": -17.20441988950276,
            "vertical_gap_native": -17.20440673828125,
            "left_alignment_delta": -4.946530538063598e-06
          },
          {
            "first": "step_0",
            "second": "step_2",
            "vertical_gap_reference": -14.655616942909761,
            "vertical_gap_native": -14.655616760253906,
            "left_alignment_delta": -1.2659764507816362e-05
          },
          {
            "first": "step_2",
            "second": "divider_0",
            "vertical_gap_reference": -8.283609576427226,
            "vertical_gap_native": -8.283607482910156,
            "left_alignment_delta": 1.4588073014465408e-05
          },
          {
            "first": "divider_0",
            "second": "home_icon_1",
            "vertical_gap_reference": 68.81767955801105,
            "vertical_gap_native": 68.81767630577087,
            "left_alignment_delta": 7.126357601805466e-07
          },
          {
            "first": "home_icon_1",
            "second": "courier",
            "vertical_gap_reference": 54.79926335174955,
            "vertical_gap_native": 54.79926681518555,
            "left_alignment_delta": -2.221746761676968e-06
          },
          {
            "first": "courier",
            "second": "delivery_time",
            "vertical_gap_reference": -43.32965009208103,
            "vertical_gap_native": -43.32965,
            "left_alignment_delta": -6.2041230250997614e-06
          },
          {
            "first": "courier_surface",
            "second": "courier_control",
            "vertical_gap_reference": -43.32965009208103,
            "vertical_gap_native": -43.32965087890625,
            "left_alignment_delta": 0.0
          },
          {
            "first": "delivery_time_surface",
            "second": "delivery_time_control",
            "vertical_gap_reference": -43.32965009208103,
            "vertical_gap_native": -43.32965087890625,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -72.24072191528546,
            "vertical_gap_native": -72.24072265625,
            "left_alignment_delta": -2.059936520026895e-06
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -72.24072191528546,
            "vertical_gap_native": -72.24072265625,
            "left_alignment_delta": -3.9672851244176854e-06
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -72.24072191528546,
            "vertical_gap_native": -72.24072265625,
            "left_alignment_delta": 1.8920898440910605e-05
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -60.1339079189687,
            "vertical_gap_native": -60.13385009765625,
            "left_alignment_delta": -1.4297988400358008e-05
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -51.21309760589319,
            "vertical_gap_native": -51.213096618652344,
            "left_alignment_delta": -4.11987301163208e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -51.21309760589319,
            "vertical_gap_native": -51.213096618652344,
            "left_alignment_delta": 3.6621094068323146e-06
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-04/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-04/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-04/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-04/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-04/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-04/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/04.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-04/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-04/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-04/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-04/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 5,
      "id": "aircon-05",
      "title": "预约安装",
      "description": "商品送达，安装服务提供预约入口",
      "surface": "系统桌面",
      "branch": false,
      "base": "../cards/aircon-05/",
      "reference": "../cards/aircon-05/reference.png",
      "native": "../cards/aircon-05/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "b5cee3210f584529b4c728cc57181330"
      },
      "run": {
        "id": "aircon-05",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-05",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "dc42ff1c89ce9715b0e66cecdf6945ab6e22305c84d51a3ebae10e16b207e1b5",
          "reference_sha256": "d92a3dfb2bf65359e74b6d8c600a8bcf1e2e1cd0079dadc4b184e332590de78b",
          "id": "aircon-05",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "installation_card",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "product_photo",
              "role": "photo",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Image"
              ],
              "actual_widget": "Image",
              "issues": [],
              "repair": "Use an original or separately generated image asset with documented crop, fit and clipping."
            },
            {
              "id": "choose_time",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "choose_time_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "choose_time_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_19",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "defer",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "defer_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "defer_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_20",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "wrench_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "check_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_13",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_14",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_15",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_16",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_17",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_18",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_11",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_12",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_21",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_22",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_23",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_24",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_25",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 6.791,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "d92a3dfb2bf65359e74b6d8c600a8bcf1e2e1cd0079dadc4b184e332590de78b",
            "native_sha256": "4d340037dd3ed3d70c6c0a5869a02903f40978a799044308c8ca7753ab707880",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_20: text color",
          "text_13: text color",
          "text_14: text color",
          "text_15: text color",
          "text_16: text color",
          "text_17: reference OCR text differs",
          "text_17: text ink dimensions",
          "text_18: text color",
          "text_11: text color",
          "text_21: text color",
          "text_22: text color",
          "text_23: text color",
          "text_24: text color",
          "text_25: text color"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              8.5,
              0.0,
              389.0,
              776.0
            ],
            "actual_bounds": [
              8.5,
              0.0,
              389.0,
              776.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "installation_card",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              21.416015625,
              116.28599412340843,
              354.05078125,
              515.3065621939276
            ],
            "actual_bounds": [
              21.416015625,
              116.28599548339844,
              354.05078125,
              515.3065795898438
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "product_photo",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              36.5,
              336.0,
              122.5,
              111.0
            ],
            "actual_bounds": [
              36.5,
              336.0,
              122.5,
              111.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Image",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "choose_time",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              37.37109375,
              557.8687561214496,
              154.232421875,
              51.68266405484819
            ],
            "actual_bounds": [
              37.37109375,
              557.8687744140625,
              154.23242,
              51.682663
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "选择时间",
            "enabled": true,
            "issues": []
          },
          {
            "id": "choose_time_surface",
            "native_id": "beauty_0_0_0_1_0",
            "expected_bounds": [
              37.37109375,
              557.8687561214496,
              154.232421875,
              51.68266405484819
            ],
            "actual_bounds": [
              37.37109375,
              557.8687744140625,
              154.232421875,
              51.68266296386719
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "choose_time_control",
            "native_id": "beauty_0_0_0_1_1",
            "expected_bounds": [
              37.37109375,
              557.8687561214496,
              154.232421875,
              51.68266405484819
            ],
            "actual_bounds": [
              37.37109375,
              557.8687744140625,
              154.232421875,
              51.68266296386719
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_19",
            "native_id": "beauty_0_0_0_1_2",
            "expected_bounds": [
              72.74300301729573,
              570.4108405741206,
              91.460561730315,
              24.0
            ],
            "actual_bounds": [
              72.74300384521484,
              570.4108276367188,
              91.46056,
              24.0
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "选择时间",
            "enabled": true,
            "issues": []
          },
          {
            "id": "defer",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              211.357421875,
              558.6287952987268,
              134.478515625,
              50.92262487757101
            ],
            "actual_bounds": [
              211.357421875,
              558.6287841796875,
              134.47852,
              50.922626
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "暂不预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "defer_surface",
            "native_id": "beauty_0_0_0_2_0",
            "expected_bounds": [
              211.357421875,
              558.6287952987268,
              134.478515625,
              50.92262487757101
            ],
            "actual_bounds": [
              211.357421875,
              558.6287841796875,
              134.478515625,
              50.92262649536133
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "defer_control",
            "native_id": "beauty_0_0_0_2_1",
            "expected_bounds": [
              211.357421875,
              558.6287952987268,
              134.478515625,
              50.92262487757101
            ],
            "actual_bounds": [
              211.357421875,
              558.6287841796875,
              134.478515625,
              50.92262649536133
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_20",
            "native_id": "beauty_0_0_0_2_2",
            "expected_bounds": [
              237.53814123755774,
              573.6487748469794,
              81.9763576690062,
              21.0
            ],
            "actual_bounds": [
              237.53814697265625,
              573.6488037109375,
              81.97636,
              21.0
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Label",
            "visible": true,
            "text": "暂不预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "wrench_icon_0",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              39.650390625,
              139.84720861900098,
              33.4296875,
              34.20176297747307
            ],
            "actual_bounds": [
              39.650390625,
              139.8472137451172,
              33.4296875,
              34.20176315307617
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "check_icon_1",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              38.890625,
              513.026444662096,
              19.75390625,
              19.761018609206662
            ],
            "actual_bounds": [
              38.890625,
              513.0264282226562,
              19.75390625,
              19.761018753051758
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_13",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              89.30356550306573,
              146.2573316910605,
              156.41451030066602,
              21.5
            ],
            "actual_bounds": [
              89.3035659790039,
              146.25732421875,
              156.4145,
              21.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "安装服务 · 待预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_14",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              38.26801973392962,
              207.02741667347686,
              146.50720269843558,
              29.0
            ],
            "actual_bounds": [
              38.26802062988281,
              207.0274200439453,
              146.5072,
              29.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "空调已送达",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_15",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              38.05145037482281,
              255.65162284239256,
              180.52626233567491,
              21.506664480033972
            ],
            "actual_bounds": [
              38.051448822021484,
              255.65162658691406,
              180.52626,
              21.506664
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "请选择上门安装时间",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_16",
            "native_id": "beauty_0_0_0_8",
            "expected_bounds": [
              38.2043947268983,
              293.62036054086155,
              198.17079614070934,
              21.050375959268525
            ],
            "actual_bounds": [
              38.20439529418945,
              293.620361328125,
              198.17079,
              21.050377
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "王师傅 · 安装服务团队",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_17",
            "native_id": "beauty_0_0_0_9",
            "expected_bounds": [
              37.64415143816866,
              468.21679626495325,
              161.48654018385744,
              27.048630052168587
            ],
            "actual_bounds": [
              37.64414978027344,
              468.216796875,
              161.48654,
              27.04863
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "家 海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_18",
            "native_id": "beauty_0_0_0_10",
            "expected_bounds": [
              71.03965015804589,
              514.7420419039811,
              165.85488895657952,
              18.5
            ],
            "actual_bounds": [
              71.0396499633789,
              514.7420654296875,
              165.85489,
              18.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "已送达 · 周五 15:20",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              17.6171875,
              658.9539666993145,
              370.765625,
              117.04603330068561
            ],
            "actual_bounds": [
              17.6171875,
              658.9539794921875,
              370.765625,
              117.04603576660156
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              40.10625,
              667.6792164544564,
              68.47615625,
              68.50081096963761
            ],
            "actual_bounds": [
              40.10625076293945,
              667.67919921875,
              68.47615814208984,
              68.50080871582031
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              51.502734375,
              682.1199608227229,
              45.6831875,
              43.4195181194907
            ],
            "actual_bounds": [
              51.50273513793945,
              682.1199340820312,
              45.683189392089844,
              43.419517517089844
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              127.236171875,
              667.6792164544564,
              68.47615625,
              68.50081096963761
            ],
            "actual_bounds": [
              127.23617553710938,
              667.67919921875,
              68.47615814208984,
              68.50080871582031
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              214.36609374999998,
              667.6792164544564,
              68.47615625,
              68.50081096963761
            ],
            "actual_bounds": [
              214.3660888671875,
              667.67919921875,
              68.47615814208984,
              68.50080871582031
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_1_4",
            "expected_bounds": [
              225.76257812499998,
              682.1199608227229,
              45.6831875,
              43.4195181194907
            ],
            "actual_bounds": [
              225.7625732421875,
              682.1199340820312,
              45.683189392089844,
              43.419517517089844
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_1_5",
            "expected_bounds": [
              301.496015625,
              667.6792164544564,
              68.47615625,
              68.50081096963761
            ],
            "actual_bounds": [
              301.4960021972656,
              667.67919921875,
              68.47615814208984,
              68.50080871582031
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_1_6",
            "expected_bounds": [
              312.8925,
              682.1199608227229,
              45.6831875,
              43.4195181194907
            ],
            "actual_bounds": [
              312.8924865722656,
              682.1199340820312,
              45.683189392089844,
              43.419517517089844
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_11",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              30.007753608026736,
              22.663390339388435,
              108.04606733832121,
              18.5
            ],
            "actual_bounds": [
              30.007753372192383,
              22.66339111328125,
              108.04607,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月18日 周五",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_12",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              27.92567941308339,
              57.54527165071097,
              90.33244389187226,
              30.0
            ],
            "actual_bounds": [
              27.92568016052246,
              57.54527282714844,
              90.33244,
              30.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "15:25",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_21",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              51.232837343551694,
              733.8854385960858,
              37.44223649987249,
              18.5
            ],
            "actual_bounds": [
              51.23283767700195,
              733.8854370117188,
              37.442238,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_22",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              138.24511035863293,
              690.8034113587373,
              33.65161064760842,
              25.0
            ],
            "actual_bounds": [
              138.2451171875,
              690.8034057617188,
              33.65161,
              25.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "18",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_23",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              136.76373317560137,
              734.6195152448497,
              36.59490621687722,
              17.5
            ],
            "actual_bounds": [
              136.76373291015625,
              734.6195068359375,
              36.594906,
              17.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_24",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              230.31889030784336,
              734.0535818458366,
              36.613814093170504,
              18.5
            ],
            "actual_bounds": [
              230.3188934326172,
              734.0535888671875,
              36.613815,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_25",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              321.88772203993807,
              733.7872979632167,
              37.2352495493568,
              19.0
            ],
            "actual_bounds": [
              321.8877258300781,
              733.7872924804688,
              37.23525,
              19.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_19",
            "reference": [
              74.0,
              572.0,
              82.5,
              20.0
            ],
            "native": [
              74.0,
              572.0,
              82.5,
              19.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              245,
              249,
              246
            ],
            "native_color": [
              255,
              255,
              255
            ],
            "issues": []
          },
          {
            "id": "text_20",
            "reference": [
              238.5,
              575.5,
              73.5,
              17.0
            ],
            "native": [
              238.5,
              575.5,
              73.5,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              128,
              128,
              128
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_13",
            "reference": [
              90.5,
              148.0,
              148.0,
              17.5
            ],
            "native": [
              90.5,
              148.0,
              148.0,
              16.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              88,
              89,
              89
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_14",
            "reference": [
              40.5,
              208.5,
              140.5,
              25.0
            ],
            "native": [
              40.5,
              208.5,
              137.5,
              25.0
            ],
            "delta": [
              0.0,
              0.0,
              -3.0,
              0.0
            ],
            "reference_color": [
              21,
              21,
              20
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_15",
            "reference": [
              39.0,
              257.5,
              172.0,
              17.5
            ],
            "native": [
              39.0,
              257.5,
              172.0,
              17.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              76,
              76,
              76
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_16",
            "reference": [
              39.5,
              295.5,
              190.0,
              17.0
            ],
            "native": [
              39.5,
              295.5,
              190.0,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              72,
              72,
              72
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_17",
            "reference": [
              40.5,
              471.0,
              151.5,
              18.5
            ],
            "native": [
              39.5,
              470.0,
              154.0,
              22.5
            ],
            "delta": [
              -1.0,
              -1.0,
              2.5,
              4.0
            ],
            "reference_color": [
              58,
              57,
              58
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink dimensions"
            ]
          },
          {
            "id": "text_18",
            "reference": [
              72.5,
              516.5,
              158.0,
              14.5
            ],
            "native": [
              72.5,
              516.5,
              158.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              83,
              83,
              84
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_11",
            "reference": [
              31.0,
              24.5,
              100.5,
              14.5
            ],
            "native": [
              31.0,
              24.5,
              100.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              95,
              100,
              99
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_12",
            "reference": [
              31.0,
              59.5,
              80.0,
              26.0
            ],
            "native": [
              31.0,
              59.5,
              80.0,
              25.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              48,
              60,
              55
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_21",
            "reference": [
              52.5,
              735.5,
              30.0,
              14.5
            ],
            "native": [
              52.5,
              735.5,
              30.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              90,
              100,
              94
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_22",
            "reference": [
              140.5,
              692.5,
              25.0,
              21.0
            ],
            "native": [
              140.5,
              692.5,
              25.0,
              19.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -2.0
            ],
            "reference_color": [
              74,
              81,
              77
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_23",
            "reference": [
              139.5,
              736.5,
              27.5,
              13.5
            ],
            "native": [
              139.5,
              736.5,
              27.5,
              13.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              101,
              110,
              106
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_24",
            "reference": [
              231.0,
              735.5,
              29.5,
              14.5
            ],
            "native": [
              231.0,
              735.5,
              29.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              112,
              118,
              115
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_25",
            "reference": [
              322.5,
              735.5,
              30.0,
              15.0
            ],
            "native": [
              323.0,
              735.5,
              29.5,
              14.5
            ],
            "delta": [
              0.5,
              0.0,
              -0.5,
              -0.5
            ],
            "reference_color": [
              113,
              121,
              119
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              8.5,
              0.0,
              389.0,
              776.0
            ],
            "native": [
              8.5,
              0.0,
              389.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "installation_card",
            "reference": [
              21.416015625,
              116.28599412340843,
              354.05078125,
              515.3065621939276
            ],
            "native": [
              21.416015625,
              116.28599548339844,
              354.05078125,
              515.3065795898438
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "product_photo",
            "reference": [
              36.5,
              336.0,
              122.5,
              111.0
            ],
            "native": [
              36.5,
              336.0,
              122.5,
              111.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "choose_time",
            "reference": [
              37.37109375,
              557.8687561214496,
              154.232421875,
              51.68266405484819
            ],
            "native": [
              37.37109375,
              557.8687744140625,
              154.23242,
              51.682663
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "choose_time_surface",
            "reference": [
              37.37109375,
              557.8687561214496,
              154.232421875,
              51.68266405484819
            ],
            "native": [
              37.37109375,
              557.8687744140625,
              154.232421875,
              51.68266296386719
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "choose_time_control",
            "reference": [
              37.37109375,
              557.8687561214496,
              154.232421875,
              51.68266405484819
            ],
            "native": [
              37.37109375,
              557.8687744140625,
              154.232421875,
              51.68266296386719
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "defer",
            "reference": [
              211.357421875,
              558.6287952987268,
              134.478515625,
              50.92262487757101
            ],
            "native": [
              211.357421875,
              558.6287841796875,
              134.47852,
              50.922626
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "defer_surface",
            "reference": [
              211.357421875,
              558.6287952987268,
              134.478515625,
              50.92262487757101
            ],
            "native": [
              211.357421875,
              558.6287841796875,
              134.478515625,
              50.92262649536133
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "defer_control",
            "reference": [
              211.357421875,
              558.6287952987268,
              134.478515625,
              50.92262487757101
            ],
            "native": [
              211.357421875,
              558.6287841796875,
              134.478515625,
              50.92262649536133
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "wrench_icon_0",
            "reference": [
              39.650390625,
              139.84720861900098,
              33.4296875,
              34.20176297747307
            ],
            "native": [
              39.650390625,
              139.8472137451172,
              33.4296875,
              34.20176315307617
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "check_icon_1",
            "reference": [
              38.890625,
              513.026444662096,
              19.75390625,
              19.761018609206662
            ],
            "native": [
              38.890625,
              513.0264282226562,
              19.75390625,
              19.761018753051758
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              17.6171875,
              658.9539666993145,
              370.765625,
              117.04603330068561
            ],
            "native": [
              17.6171875,
              658.9539794921875,
              370.765625,
              117.04603576660156
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              40.10625,
              667.6792164544564,
              68.47615625,
              68.50081096963761
            ],
            "native": [
              40.10625076293945,
              667.67919921875,
              68.47615814208984,
              68.50080871582031
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              51.502734375,
              682.1199608227229,
              45.6831875,
              43.4195181194907
            ],
            "native": [
              51.50273513793945,
              682.1199340820312,
              45.683189392089844,
              43.419517517089844
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              127.236171875,
              667.6792164544564,
              68.47615625,
              68.50081096963761
            ],
            "native": [
              127.23617553710938,
              667.67919921875,
              68.47615814208984,
              68.50080871582031
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              214.36609374999998,
              667.6792164544564,
              68.47615625,
              68.50081096963761
            ],
            "native": [
              214.3660888671875,
              667.67919921875,
              68.47615814208984,
              68.50080871582031
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              225.76257812499998,
              682.1199608227229,
              45.6831875,
              43.4195181194907
            ],
            "native": [
              225.7625732421875,
              682.1199340820312,
              45.683189392089844,
              43.419517517089844
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              301.496015625,
              667.6792164544564,
              68.47615625,
              68.50081096963761
            ],
            "native": [
              301.4960021972656,
              667.67919921875,
              68.47615814208984,
              68.50080871582031
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              312.8925,
              682.1199608227229,
              45.6831875,
              43.4195181194907
            ],
            "native": [
              312.8924865722656,
              682.1199340820312,
              45.683189392089844,
              43.419517517089844
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "installation_card",
            "second": "dock",
            "vertical_gap_reference": 27.361410381978544,
            "vertical_gap_native": 27.361404418945312,
            "left_alignment_delta": 0.0
          },
          {
            "first": "wrench_icon_0",
            "second": "product_photo",
            "vertical_gap_reference": 161.95102840352595,
            "vertical_gap_native": 161.95102310180664,
            "left_alignment_delta": 0.0
          },
          {
            "first": "product_photo",
            "second": "check_icon_1",
            "vertical_gap_reference": 66.02644466209597,
            "vertical_gap_native": 66.02642822265625,
            "left_alignment_delta": 0.0
          },
          {
            "first": "check_icon_1",
            "second": "choose_time",
            "vertical_gap_reference": 25.081292850146934,
            "vertical_gap_native": 25.081327438354492,
            "left_alignment_delta": 0.0
          },
          {
            "first": "choose_time",
            "second": "defer",
            "vertical_gap_reference": -50.922624877570954,
            "vertical_gap_native": -50.922653234375,
            "left_alignment_delta": 0.0
          },
          {
            "first": "choose_time_surface",
            "second": "choose_time_control",
            "vertical_gap_reference": -51.68266405484819,
            "vertical_gap_native": -51.68266296386719,
            "left_alignment_delta": 0.0
          },
          {
            "first": "defer_surface",
            "second": "defer_control",
            "vertical_gap_reference": -50.92262487757101,
            "vertical_gap_native": -50.92262649536133,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -68.50081096963761,
            "vertical_gap_native": -68.50080871582031,
            "left_alignment_delta": 2.899169928127776e-06
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -68.50081096963761,
            "vertical_gap_native": -68.50080871582031,
            "left_alignment_delta": -8.54492185453637e-06
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -68.50081096963761,
            "vertical_gap_native": -68.50080871582031,
            "left_alignment_delta": -8.544921882958079e-06
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -54.06006660137116,
            "vertical_gap_native": -54.06007385253906,
            "left_alignment_delta": 1.4190673823577526e-05
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -43.4195181194907,
            "vertical_gap_native": -43.419517517089844,
            "left_alignment_delta": -5.645751912197738e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -43.4195181194907,
            "vertical_gap_native": -43.419517517089844,
            "left_alignment_delta": -8.544921882958079e-06
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-05/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-05/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-05/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-05/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-05/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-05/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/05.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-05/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-05/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-05/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-05/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 6,
      "id": "aircon-06",
      "title": "展开时段",
      "description": "安装服务时段与个人日历关联，等待选择",
      "surface": "系统桌面",
      "branch": false,
      "base": "../cards/aircon-06/",
      "reference": "../cards/aircon-06/reference.png",
      "native": "../cards/aircon-06/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "a6a507bc2bf642e2b6f6d42dae127fd7"
      },
      "run": {
        "id": "aircon-06",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-06",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "0e546956afde92a8a191a2a4fabaede50a91e2bbf9bab45412ae9a8d9894fe1f",
          "reference_sha256": "82cc625de2350b642ba41741252bd39306ea86628270eb720e53b5a395ff5087",
          "id": "aircon-06",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "installation_card",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "divider_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "close",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "close_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "close_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "saturday",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "saturday_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "saturday_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_69",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "sunday",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "sunday_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "sunday_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_70",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "conflict_slot",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "conflict_slot_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "conflict_slot_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_71",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_72",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "afternoon",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "afternoon_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "afternoon_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_73",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_74",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "confirm_booking",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "confirm_booking_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "confirm_booking_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_77",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "close_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "home_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "step_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "step_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "text_66",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_67",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_75",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_76",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_64",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_65",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_78",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_79",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_80",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_81",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_82",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 7.036,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "82cc625de2350b642ba41741252bd39306ea86628270eb720e53b5a395ff5087",
            "native_sha256": "d3e6ea8bf85ef10f907c388fedd8bad7557a7da2d82dae057549cc2da17d9f49",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_70: text color",
          "text_71: text color",
          "text_73: text ink dimensions",
          "text_73: text color",
          "text_74: reference text missing or OCR unresolved",
          "text_66: text color",
          "text_67: text color",
          "text_75: reference OCR text differs",
          "text_75: text ink position",
          "text_75: text ink dimensions",
          "text_75: text color",
          "text_76: text ink dimensions",
          "text_76: text color",
          "text_64: text color",
          "text_78: text color",
          "text_79: text color",
          "text_80: text color",
          "text_81: text color",
          "text_82: text color",
          "2 extra reference text observations need classification"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              7.0,
              0.0,
              392.0,
              776.0
            ],
            "actual_bounds": [
              7.0,
              0.0,
              392.0,
              776.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "installation_card",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              20.647969052224372,
              109.9902248289345,
              363.9458413926499,
              561.3294232649072
            ],
            "actual_bounds": [
              20.647968292236328,
              109.99022674560547,
              363.9458312988281,
              561.3294067382812
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_0",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              41.11992263056093,
              543.8826979472141,
              316.936170212766,
              0.7585532746823069
            ],
            "actual_bounds": [
              41.11992263793945,
              543.8826904296875,
              316.9361572265625,
              0.7585532665252686
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "close",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              330.76015473887816,
              125.16129032258064,
              40.94390715667312,
              40.961876832844574
            ],
            "actual_bounds": [
              330.7601623535156,
              125.16129302978516,
              40.94391,
              40.961876
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "close_surface",
            "native_id": "beauty_0_0_0_1_0",
            "expected_bounds": [
              330.76015473887816,
              125.16129032258064,
              40.94390715667312,
              40.961876832844574
            ],
            "actual_bounds": [
              330.7601623535156,
              125.16129302978516,
              40.94390869140625,
              40.961875915527344
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "close_control",
            "native_id": "beauty_0_0_0_1_1",
            "expected_bounds": [
              330.76015473887816,
              125.16129032258064,
              40.94390715667312,
              40.961876832844574
            ],
            "actual_bounds": [
              330.7601623535156,
              125.16129302978516,
              40.94390869140625,
              40.961875915527344
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "saturday",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              39.603481624758224,
              217.70478983382208,
              156.19342359767893,
              46.271749755620725
            ],
            "actual_bounds": [
              39.60348129272461,
              217.7047882080078,
              156.19342,
              46.27175
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "周六 9月19日",
            "enabled": true,
            "issues": []
          },
          {
            "id": "saturday_surface",
            "native_id": "beauty_0_0_0_2_0",
            "expected_bounds": [
              39.603481624758224,
              217.70478983382208,
              156.19342359767893,
              46.271749755620725
            ],
            "actual_bounds": [
              39.60348129272461,
              217.7047882080078,
              156.19342041015625,
              46.271751403808594
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "saturday_control",
            "native_id": "beauty_0_0_0_2_1",
            "expected_bounds": [
              39.603481624758224,
              217.70478983382208,
              156.19342359767893,
              46.271749755620725
            ],
            "actual_bounds": [
              39.60348129272461,
              217.7047882080078,
              156.19342041015625,
              46.271751403808594
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_69",
            "native_id": "beauty_0_0_0_2_2",
            "expected_bounds": [
              65.89503300957745,
              231.59964901761208,
              110.39935986837351,
              20.009267302539367
            ],
            "actual_bounds": [
              65.89503479003906,
              231.5996551513672,
              110.39936,
              20.009268
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Label",
            "visible": true,
            "text": "周六 9月19日",
            "enabled": true,
            "issues": []
          },
          {
            "id": "sunday",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              214.752417794971,
              217.70478983382208,
              149.36943907156675,
              46.271749755620725
            ],
            "actual_bounds": [
              214.75241088867188,
              217.7047882080078,
              149.36945,
              46.27175
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "周日 9月20日",
            "enabled": true,
            "issues": []
          },
          {
            "id": "sunday_surface",
            "native_id": "beauty_0_0_0_3_0",
            "expected_bounds": [
              214.752417794971,
              217.70478983382208,
              149.36943907156675,
              46.271749755620725
            ],
            "actual_bounds": [
              214.75241088867188,
              217.7047882080078,
              149.36944580078125,
              46.271751403808594
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "sunday_control",
            "native_id": "beauty_0_0_0_3_1",
            "expected_bounds": [
              214.752417794971,
              217.70478983382208,
              149.36943907156675,
              46.271749755620725
            ],
            "actual_bounds": [
              214.75241088867188,
              217.7047882080078,
              149.36944580078125,
              46.271751403808594
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_70",
            "native_id": "beauty_0_0_0_3_2",
            "expected_bounds": [
              238.27117128131826,
              232.64030374689673,
              106.90887199831079,
              18.5
            ],
            "actual_bounds": [
              238.2711639404297,
              232.6403045654297,
              106.908875,
              18.5
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "Label",
            "visible": true,
            "text": "周日 9月20日",
            "enabled": true,
            "issues": []
          },
          {
            "id": "conflict_slot",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              39.603481624758224,
              283.6989247311828,
              326.0348162475822,
              91.02639296187684
            ],
            "actual_bounds": [
              39.60348129272461,
              283.69891357421875,
              326.03482,
              91.02639
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "09:00-11:00",
            "enabled": false,
            "issues": []
          },
          {
            "id": "conflict_slot_surface",
            "native_id": "beauty_0_0_0_4_0",
            "expected_bounds": [
              39.603481624758224,
              283.6989247311828,
              326.0348162475822,
              91.02639296187684
            ],
            "actual_bounds": [
              39.60348129272461,
              283.69891357421875,
              326.0348205566406,
              91.0263900756836
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "conflict_slot_control",
            "native_id": "beauty_0_0_0_4_1",
            "expected_bounds": [
              39.603481624758224,
              283.6989247311828,
              326.0348162475822,
              91.02639296187684
            ],
            "actual_bounds": [
              39.60348129272461,
              283.69891357421875,
              326.0348205566406,
              91.0263900756836
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": false,
            "issues": []
          },
          {
            "id": "text_71",
            "native_id": "beauty_0_0_0_4_2",
            "expected_bounds": [
              58.980400230006985,
              306.28808936822514,
              131.75047149987455,
              20.0
            ],
            "actual_bounds": [
              58.98040008544922,
              306.2880859375,
              131.75047,
              20.0
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "Label",
            "visible": true,
            "text": "09:00-11:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_72",
            "native_id": "beauty_0_0_0_4_3",
            "expected_bounds": [
              58.399296287338515,
              336.9350172832188,
              131.22099893851902,
              19.51474352314349
            ],
            "actual_bounds": [
              58.399295806884766,
              336.9350280761719,
              131.221,
              19.514744
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "Label",
            "visible": true,
            "text": "与项目例会冲突",
            "enabled": true,
            "issues": []
          },
          {
            "id": "afternoon",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              39.603481624758224,
              386.10361681329425,
              326.0348162475822,
              91.78494623655914
            ],
            "actual_bounds": [
              39.60348129272461,
              386.1036071777344,
              326.03482,
              91.78494
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "afternoon_surface",
            "native_id": "beauty_0_0_0_5_0",
            "expected_bounds": [
              39.603481624758224,
              386.10361681329425,
              326.0348162475822,
              91.78494623655914
            ],
            "actual_bounds": [
              39.60348129272461,
              386.1036071777344,
              326.0348205566406,
              91.78494262695312
            ],
            "parent": "beauty_0_0_0_5",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "afternoon_control",
            "native_id": "beauty_0_0_0_5_1",
            "expected_bounds": [
              39.603481624758224,
              386.10361681329425,
              326.0348162475822,
              91.78494623655914
            ],
            "actual_bounds": [
              39.60348129272461,
              386.1036071777344,
              326.0348205566406,
              91.78494262695312
            ],
            "parent": "beauty_0_0_0_5",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_73",
            "native_id": "beauty_0_0_0_5_2",
            "expected_bounds": [
              59.5522730984901,
              409.45642518022237,
              129.1516232741311,
              20.0
            ],
            "actual_bounds": [
              59.55227279663086,
              409.4564208984375,
              129.15163,
              20.0
            ],
            "parent": "beauty_0_0_0_5",
            "widget_type": "Label",
            "visible": true,
            "text": "14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_74",
            "native_id": "beauty_0_0_0_5_3",
            "expected_bounds": [
              53.28156977555914,
              438.4140175799203,
              85.3671306411637,
              22.816148960769105
            ],
            "actual_bounds": [
              53.28157043457031,
              438.4140319824219,
              85.367134,
              22.816149
            ],
            "parent": "beauty_0_0_0_5",
            "widget_type": "Label",
            "visible": true,
            "text": "日历空闲",
            "enabled": true,
            "issues": []
          },
          {
            "id": "confirm_booking",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              38.845261121856865,
              598.4985337243402,
              325.2765957446809,
              53.857282502443795
            ],
            "actual_bounds": [
              38.84526062011719,
              598.49853515625,
              325.27658,
              53.85728
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "确认预约",
            "enabled": false,
            "issues": []
          },
          {
            "id": "confirm_booking_surface",
            "native_id": "beauty_0_0_0_6_0",
            "expected_bounds": [
              38.845261121856865,
              598.4985337243402,
              325.2765957446809,
              53.857282502443795
            ],
            "actual_bounds": [
              38.84526062011719,
              598.49853515625,
              325.2765808105469,
              53.85728073120117
            ],
            "parent": "beauty_0_0_0_6",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "confirm_booking_control",
            "native_id": "beauty_0_0_0_6_1",
            "expected_bounds": [
              38.845261121856865,
              598.4985337243402,
              325.2765957446809,
              53.857282502443795
            ],
            "actual_bounds": [
              38.84526062011719,
              598.49853515625,
              325.2765808105469,
              53.85728073120117
            ],
            "parent": "beauty_0_0_0_6",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": false,
            "issues": []
          },
          {
            "id": "text_77",
            "native_id": "beauty_0_0_0_6_2",
            "expected_bounds": [
              154.29194753479035,
              613.5750856532991,
              91.16669793366202,
              23.73047018563889
            ],
            "actual_bounds": [
              154.2919464111328,
              613.5750732421875,
              91.166695,
              23.73047
            ],
            "parent": "beauty_0_0_0_6",
            "widget_type": "Label",
            "visible": true,
            "text": "确认预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "close_icon_0",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              342.13346228239845,
              137.29814271749754,
              18.197292069632496,
              18.205278592375365
            ],
            "actual_bounds": [
              342.1334533691406,
              137.2981414794922,
              18.19729232788086,
              18.205278396606445
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "home_icon_1",
            "native_id": "beauty_0_0_0_8",
            "expected_bounds": [
              41.87814313346229,
              504.4379276637341,
              21.230174081237912,
              20.480938416422287
            ],
            "actual_bounds": [
              41.878143310546875,
              504.43792724609375,
              21.230175018310547,
              20.480937957763672
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_0",
            "native_id": "beauty_0_0_0_9",
            "expected_bounds": [
              319.38684719535786,
              313.28250244379274,
              26.537717601547392,
              26.549364613880744
            ],
            "actual_bounds": [
              319.3868408203125,
              313.2825012207031,
              26.537717819213867,
              26.54936408996582
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_1",
            "native_id": "beauty_0_0_0_10",
            "expected_bounds": [
              319.38684719535786,
              415.6871945259042,
              26.537717601547392,
              26.549364613880744
            ],
            "actual_bounds": [
              319.3868408203125,
              415.68719482421875,
              26.537717819213867,
              26.54936408996582
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_66",
            "native_id": "beauty_0_0_0_11",
            "expected_bounds": [
              44.17976130363518,
              134.09146072981298,
              135.88784401600316,
              23.82733043705785
            ],
            "actual_bounds": [
              44.17975997924805,
              134.09146118164062,
              135.88785,
              23.82733
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "选择安装时间",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_67",
            "native_id": "beauty_0_0_0_12",
            "expected_bounds": [
              44.21470279917181,
              176.94956016246113,
              61.00972467318581,
              21.0
            ],
            "actual_bounds": [
              44.21470260620117,
              176.94955444335938,
              61.009724,
              21.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "王师傅",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_75",
            "native_id": "beauty_0_0_0_13",
            "expected_bounds": [
              68.8553837102447,
              506.3919684657309,
              137.43190942673203,
              20.36562318584025
            ],
            "actual_bounds": [
              68.85538482666016,
              506.3919677734375,
              137.43192,
              20.365623
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "家 · 海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_76",
            "native_id": "beauty_0_0_0_14",
            "expected_bounds": [
              45.167026811008384,
              560.9905079893273,
              217.7310024500977,
              19.0
            ],
            "actual_bounds": [
              45.16702651977539,
              560.990478515625,
              217.731,
              19.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "周六 9月19日 14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              20.647969052224372,
              676.6295210166178,
              365.46228239845266,
              99.37047898338221
            ],
            "actual_bounds": [
              20.647968292236328,
              676.6295166015625,
              365.4622802734375,
              99.37047576904297
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              42.75009671179884,
              683.2441055718475,
              67.62720309477756,
              67.65688367546431
            ],
            "actual_bounds": [
              42.75009536743164,
              683.2440795898438,
              67.62720489501953,
              67.6568832397461
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              54.12340425531915,
              697.6566177908113,
              44.88058800773694,
              42.624625610948186
            ],
            "actual_bounds": [
              54.12340545654297,
              697.6566162109375,
              44.88058853149414,
              42.62462615966797
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              128.6337330754352,
              683.2441055718475,
              67.62720309477756,
              67.65688367546431
            ],
            "actual_bounds": [
              128.63372802734375,
              683.2440795898438,
              67.62720489501953,
              67.6568832397461
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              214.51736943907153,
              683.2441055718475,
              67.62720309477756,
              67.65688367546431
            ],
            "actual_bounds": [
              214.51736450195312,
              683.2440795898438,
              67.62720489501953,
              67.6568832397461
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_1_4",
            "expected_bounds": [
              225.89067698259186,
              697.6566177908113,
              44.88058800773694,
              42.624625610948186
            ],
            "actual_bounds": [
              225.8906707763672,
              697.6566162109375,
              44.88058853149414,
              42.62462615966797
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_1_5",
            "expected_bounds": [
              300.4010058027079,
              683.2441055718475,
              67.62720309477756,
              67.65688367546431
            ],
            "actual_bounds": [
              300.4010009765625,
              683.2440795898438,
              67.62720489501953,
              67.6568832397461
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_1_6",
            "expected_bounds": [
              311.77431334622827,
              697.6566177908113,
              44.88058800773694,
              42.624625610948186
            ],
            "actual_bounds": [
              311.7743225097656,
              697.6566162109375,
              44.88058853149414,
              42.62462615966797
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_64",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              30.13093750733393,
              24.27080174392627,
              108.31809877641967,
              18.0
            ],
            "actual_bounds": [
              30.130937576293945,
              24.270801544189453,
              108.3181,
              18.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月18日 周五",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_65",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              28.358742639560255,
              58.9828619242932,
              90.82234313650027,
              30.0
            ],
            "actual_bounds": [
              28.358741760253906,
              58.98286056518555,
              90.82234,
              30.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "15:26",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_78",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              41.506584192248965,
              746.5837630668599,
              37.79821578833549,
              18.5
            ],
            "actual_bounds": [
              41.50658416748047,
              746.583740234375,
              37.798214,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_79",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              132.38680509961893,
              702.9590199210677,
              35.08580770782861,
              25.0
            ],
            "actual_bounds": [
              132.38681030273438,
              702.9590454101562,
              35.085808,
              25.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "18",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_80",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              131.50120773722864,
              746.8341003637297,
              36.4609906821817,
              18.0
            ],
            "actual_bounds": [
              131.50120544433594,
              746.8341064453125,
              36.46099,
              18.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_81",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              231.14955302598827,
              746.3506835665386,
              36.456778235585794,
              18.5
            ],
            "actual_bounds": [
              231.14955139160156,
              746.3507080078125,
              36.45678,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_82",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              323.5621989218288,
              746.6553976321426,
              36.957786234606395,
              18.5
            ],
            "actual_bounds": [
              323.56219482421875,
              746.6553955078125,
              36.957787,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_69",
            "reference": [
              66.5,
              233.5,
              101.0,
              16.0
            ],
            "native": [
              66.5,
              233.5,
              101.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              240,
              246,
              243
            ],
            "native_color": [
              255,
              255,
              255
            ],
            "issues": []
          },
          {
            "id": "text_70",
            "reference": [
              239.0,
              234.5,
              98.0,
              14.5
            ],
            "native": [
              239.0,
              234.5,
              98.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              80,
              80,
              80
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_71",
            "reference": [
              60.0,
              308.0,
              127.0,
              16.0
            ],
            "native": [
              60.0,
              308.0,
              124.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              -3.0,
              0.0
            ],
            "reference_color": [
              45,
              45,
              45
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_72",
            "reference": [
              59.5,
              338.5,
              123.5,
              15.5
            ],
            "native": [
              59.5,
              338.5,
              123.5,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              202,
              137,
              78
            ],
            "native_color": [
              190,
              135,
              63
            ],
            "issues": []
          },
          {
            "id": "text_73",
            "reference": [
              61.5,
              411.0,
              126.5,
              16.0
            ],
            "native": [
              61.5,
              411.0,
              121.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              -5.5,
              0.0
            ],
            "reference_color": [
              32,
              32,
              32
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_74",
            "reference": null,
            "native": null,
            "delta": null,
            "reference_color": null,
            "native_color": null,
            "issues": [
              "reference text missing or OCR unresolved"
            ]
          },
          {
            "id": "text_77",
            "reference": [
              155.0,
              615.5,
              82.5,
              19.5
            ],
            "native": [
              155.0,
              615.5,
              82.5,
              19.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              251,
              252,
              251
            ],
            "native_color": [
              255,
              255,
              255
            ],
            "issues": []
          },
          {
            "id": "text_66",
            "reference": [
              45.5,
              136.0,
              127.0,
              19.5
            ],
            "native": [
              45.5,
              136.0,
              126.5,
              19.5
            ],
            "delta": [
              0.0,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              26,
              26,
              25
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_67",
            "reference": [
              45.5,
              178.5,
              53.5,
              17.0
            ],
            "native": [
              45.5,
              178.5,
              53.5,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              66,
              66,
              65
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_75",
            "reference": [
              43.0,
              504.5,
              150.5,
              17.5
            ],
            "native": [
              70.5,
              508.5,
              130.5,
              16.0
            ],
            "delta": [
              27.5,
              4.0,
              -20.0,
              -1.5
            ],
            "reference_color": [
              113,
              113,
              113
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink position",
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_76",
            "reference": [
              46.0,
              562.5,
              245.0,
              15.0
            ],
            "native": [
              46.0,
              562.5,
              211.0,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              -34.0,
              0.0
            ],
            "reference_color": [
              89,
              89,
              89
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_64",
            "reference": [
              31.0,
              26.0,
              101.0,
              14.0
            ],
            "native": [
              31.0,
              26.0,
              101.0,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              81,
              87,
              85
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_65",
            "reference": [
              31.5,
              61.0,
              80.5,
              26.0
            ],
            "native": [
              31.5,
              61.0,
              80.5,
              25.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              52,
              63,
              58
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_78",
            "reference": [
              43.0,
              748.0,
              30.5,
              14.5
            ],
            "native": [
              43.0,
              748.0,
              30.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              102,
              109,
              106
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_79",
            "reference": [
              135.0,
              705.0,
              25.5,
              21.0
            ],
            "native": [
              135.0,
              705.0,
              25.5,
              20.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              82,
              90,
              84
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_80",
            "reference": [
              134.5,
              748.5,
              27.5,
              14.0
            ],
            "native": [
              134.5,
              748.5,
              27.5,
              13.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              98,
              106,
              103
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_81",
            "reference": [
              232.0,
              748.0,
              29.5,
              14.5
            ],
            "native": [
              232.0,
              748.0,
              29.5,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              108,
              114,
              112
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_82",
            "reference": [
              324.5,
              748.0,
              30.0,
              14.5
            ],
            "native": [
              324.5,
              748.0,
              30.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              96,
              104,
              101
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              7.0,
              0.0,
              392.0,
              776.0
            ],
            "native": [
              7.0,
              0.0,
              392.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "installation_card",
            "reference": [
              20.647969052224372,
              109.9902248289345,
              363.9458413926499,
              561.3294232649072
            ],
            "native": [
              20.647968292236328,
              109.99022674560547,
              363.9458312988281,
              561.3294067382812
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "divider_0",
            "reference": [
              41.11992263056093,
              543.8826979472141,
              316.936170212766,
              0.7585532746823069
            ],
            "native": [
              41.11992263793945,
              543.8826904296875,
              316.9361572265625,
              0.7585532665252686
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "close",
            "reference": [
              330.76015473887816,
              125.16129032258064,
              40.94390715667312,
              40.961876832844574
            ],
            "native": [
              330.7601623535156,
              125.16129302978516,
              40.94391,
              40.961876
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "close_surface",
            "reference": [
              330.76015473887816,
              125.16129032258064,
              40.94390715667312,
              40.961876832844574
            ],
            "native": [
              330.7601623535156,
              125.16129302978516,
              40.94390869140625,
              40.961875915527344
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "close_control",
            "reference": [
              330.76015473887816,
              125.16129032258064,
              40.94390715667312,
              40.961876832844574
            ],
            "native": [
              330.7601623535156,
              125.16129302978516,
              40.94390869140625,
              40.961875915527344
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "saturday",
            "reference": [
              39.603481624758224,
              217.70478983382208,
              156.19342359767893,
              46.271749755620725
            ],
            "native": [
              39.60348129272461,
              217.7047882080078,
              156.19342,
              46.27175
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "saturday_surface",
            "reference": [
              39.603481624758224,
              217.70478983382208,
              156.19342359767893,
              46.271749755620725
            ],
            "native": [
              39.60348129272461,
              217.7047882080078,
              156.19342041015625,
              46.271751403808594
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "saturday_control",
            "reference": [
              39.603481624758224,
              217.70478983382208,
              156.19342359767893,
              46.271749755620725
            ],
            "native": [
              39.60348129272461,
              217.7047882080078,
              156.19342041015625,
              46.271751403808594
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "sunday",
            "reference": [
              214.752417794971,
              217.70478983382208,
              149.36943907156675,
              46.271749755620725
            ],
            "native": [
              214.75241088867188,
              217.7047882080078,
              149.36945,
              46.27175
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "sunday_surface",
            "reference": [
              214.752417794971,
              217.70478983382208,
              149.36943907156675,
              46.271749755620725
            ],
            "native": [
              214.75241088867188,
              217.7047882080078,
              149.36944580078125,
              46.271751403808594
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "sunday_control",
            "reference": [
              214.752417794971,
              217.70478983382208,
              149.36943907156675,
              46.271749755620725
            ],
            "native": [
              214.75241088867188,
              217.7047882080078,
              149.36944580078125,
              46.271751403808594
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "conflict_slot",
            "reference": [
              39.603481624758224,
              283.6989247311828,
              326.0348162475822,
              91.02639296187684
            ],
            "native": [
              39.60348129272461,
              283.69891357421875,
              326.03482,
              91.02639
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "conflict_slot_surface",
            "reference": [
              39.603481624758224,
              283.6989247311828,
              326.0348162475822,
              91.02639296187684
            ],
            "native": [
              39.60348129272461,
              283.69891357421875,
              326.0348205566406,
              91.0263900756836
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "conflict_slot_control",
            "reference": [
              39.603481624758224,
              283.6989247311828,
              326.0348162475822,
              91.02639296187684
            ],
            "native": [
              39.60348129272461,
              283.69891357421875,
              326.0348205566406,
              91.0263900756836
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "afternoon",
            "reference": [
              39.603481624758224,
              386.10361681329425,
              326.0348162475822,
              91.78494623655914
            ],
            "native": [
              39.60348129272461,
              386.1036071777344,
              326.03482,
              91.78494
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "afternoon_surface",
            "reference": [
              39.603481624758224,
              386.10361681329425,
              326.0348162475822,
              91.78494623655914
            ],
            "native": [
              39.60348129272461,
              386.1036071777344,
              326.0348205566406,
              91.78494262695312
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "afternoon_control",
            "reference": [
              39.603481624758224,
              386.10361681329425,
              326.0348162475822,
              91.78494623655914
            ],
            "native": [
              39.60348129272461,
              386.1036071777344,
              326.0348205566406,
              91.78494262695312
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "confirm_booking",
            "reference": [
              38.845261121856865,
              598.4985337243402,
              325.2765957446809,
              53.857282502443795
            ],
            "native": [
              38.84526062011719,
              598.49853515625,
              325.27658,
              53.85728
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "confirm_booking_surface",
            "reference": [
              38.845261121856865,
              598.4985337243402,
              325.2765957446809,
              53.857282502443795
            ],
            "native": [
              38.84526062011719,
              598.49853515625,
              325.2765808105469,
              53.85728073120117
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "confirm_booking_control",
            "reference": [
              38.845261121856865,
              598.4985337243402,
              325.2765957446809,
              53.857282502443795
            ],
            "native": [
              38.84526062011719,
              598.49853515625,
              325.2765808105469,
              53.85728073120117
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "close_icon_0",
            "reference": [
              342.13346228239845,
              137.29814271749754,
              18.197292069632496,
              18.205278592375365
            ],
            "native": [
              342.1334533691406,
              137.2981414794922,
              18.19729232788086,
              18.205278396606445
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "home_icon_1",
            "reference": [
              41.87814313346229,
              504.4379276637341,
              21.230174081237912,
              20.480938416422287
            ],
            "native": [
              41.878143310546875,
              504.43792724609375,
              21.230175018310547,
              20.480937957763672
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_0",
            "reference": [
              319.38684719535786,
              313.28250244379274,
              26.537717601547392,
              26.549364613880744
            ],
            "native": [
              319.3868408203125,
              313.2825012207031,
              26.537717819213867,
              26.54936408996582
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_1",
            "reference": [
              319.38684719535786,
              415.6871945259042,
              26.537717601547392,
              26.549364613880744
            ],
            "native": [
              319.3868408203125,
              415.68719482421875,
              26.537717819213867,
              26.54936408996582
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              20.647969052224372,
              676.6295210166178,
              365.46228239845266,
              99.37047898338221
            ],
            "native": [
              20.647968292236328,
              676.6295166015625,
              365.4622802734375,
              99.37047576904297
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              42.75009671179884,
              683.2441055718475,
              67.62720309477756,
              67.65688367546431
            ],
            "native": [
              42.75009536743164,
              683.2440795898438,
              67.62720489501953,
              67.6568832397461
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              54.12340425531915,
              697.6566177908113,
              44.88058800773694,
              42.624625610948186
            ],
            "native": [
              54.12340545654297,
              697.6566162109375,
              44.88058853149414,
              42.62462615966797
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              128.6337330754352,
              683.2441055718475,
              67.62720309477756,
              67.65688367546431
            ],
            "native": [
              128.63372802734375,
              683.2440795898438,
              67.62720489501953,
              67.6568832397461
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              214.51736943907153,
              683.2441055718475,
              67.62720309477756,
              67.65688367546431
            ],
            "native": [
              214.51736450195312,
              683.2440795898438,
              67.62720489501953,
              67.6568832397461
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              225.89067698259186,
              697.6566177908113,
              44.88058800773694,
              42.624625610948186
            ],
            "native": [
              225.8906707763672,
              697.6566162109375,
              44.88058853149414,
              42.62462615966797
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              300.4010058027079,
              683.2441055718475,
              67.62720309477756,
              67.65688367546431
            ],
            "native": [
              300.4010009765625,
              683.2440795898438,
              67.62720489501953,
              67.6568832397461
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              311.77431334622827,
              697.6566177908113,
              44.88058800773694,
              42.624625610948186
            ],
            "native": [
              311.7743225097656,
              697.6566162109375,
              44.88058853149414,
              42.62462615966797
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "installation_card",
            "second": "dock",
            "vertical_gap_reference": 5.309872922776094,
            "vertical_gap_native": 5.309883117675781,
            "left_alignment_delta": 0.0
          },
          {
            "first": "close",
            "second": "close_icon_0",
            "vertical_gap_reference": -28.825024437927674,
            "vertical_gap_native": -28.825027550292965,
            "left_alignment_delta": -1.6527895297713258e-05
          },
          {
            "first": "close_icon_0",
            "second": "saturday",
            "vertical_gap_reference": 62.20136852394917,
            "vertical_gap_native": 62.20136833190918,
            "left_alignment_delta": 8.581224221870798e-06
          },
          {
            "first": "saturday",
            "second": "sunday",
            "vertical_gap_reference": -46.271749755620725,
            "vertical_gap_native": -46.27175,
            "left_alignment_delta": -6.574265512426791e-06
          },
          {
            "first": "sunday",
            "second": "conflict_slot",
            "vertical_gap_reference": 19.722385141739984,
            "vertical_gap_native": 19.72237536621094,
            "left_alignment_delta": 6.574265512426791e-06
          },
          {
            "first": "conflict_slot",
            "second": "step_0",
            "vertical_gap_reference": -61.442815249266886,
            "vertical_gap_native": -61.44280235351563,
            "left_alignment_delta": -6.043011751444283e-06
          },
          {
            "first": "step_0",
            "second": "afternoon",
            "vertical_gap_reference": 46.271749755620775,
            "vertical_gap_native": 46.27174186706543,
            "left_alignment_delta": 6.043011751444283e-06
          },
          {
            "first": "afternoon",
            "second": "step_1",
            "vertical_gap_reference": -62.201368523949185,
            "vertical_gap_native": -62.20135235351563,
            "left_alignment_delta": -6.043011751444283e-06
          },
          {
            "first": "step_1",
            "second": "home_icon_1",
            "vertical_gap_reference": 62.20136852394917,
            "vertical_gap_native": 62.20136833190918,
            "left_alignment_delta": 6.552129946157947e-06
          },
          {
            "first": "home_icon_1",
            "second": "divider_0",
            "vertical_gap_reference": 18.963831867057667,
            "vertical_gap_native": 18.963825225830078,
            "left_alignment_delta": -1.6970606253607912e-07
          },
          {
            "first": "divider_0",
            "second": "confirm_booking",
            "vertical_gap_reference": 53.8572825024438,
            "vertical_gap_native": 53.85729146003723,
            "left_alignment_delta": -5.091182018190921e-07
          },
          {
            "first": "close_surface",
            "second": "close_control",
            "vertical_gap_reference": -40.961876832844574,
            "vertical_gap_native": -40.961875915527344,
            "left_alignment_delta": 0.0
          },
          {
            "first": "saturday_surface",
            "second": "saturday_control",
            "vertical_gap_reference": -46.271749755620725,
            "vertical_gap_native": -46.271751403808594,
            "left_alignment_delta": 0.0
          },
          {
            "first": "sunday_surface",
            "second": "sunday_control",
            "vertical_gap_reference": -46.271749755620725,
            "vertical_gap_native": -46.271751403808594,
            "left_alignment_delta": 0.0
          },
          {
            "first": "conflict_slot_surface",
            "second": "conflict_slot_control",
            "vertical_gap_reference": -91.02639296187684,
            "vertical_gap_native": -91.0263900756836,
            "left_alignment_delta": 0.0
          },
          {
            "first": "afternoon_surface",
            "second": "afternoon_control",
            "vertical_gap_reference": -91.78494623655914,
            "vertical_gap_native": -91.78494262695312,
            "left_alignment_delta": 0.0
          },
          {
            "first": "confirm_booking_surface",
            "second": "confirm_booking_control",
            "vertical_gap_reference": -53.857282502443795,
            "vertical_gap_native": -53.85728073120117,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -67.65688367546431,
            "vertical_gap_native": -67.6568832397461,
            "left_alignment_delta": -3.7037242464066367e-06
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -67.65688367546431,
            "vertical_gap_native": -67.6568832397461,
            "left_alignment_delta": 1.1097304764007276e-07
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -67.65688367546431,
            "vertical_gap_native": -67.6568832397461,
            "left_alignment_delta": 1.109729907966539e-07
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -53.24437145650052,
            "vertical_gap_native": -53.244346618652344,
            "left_alignment_delta": 6.027369238381652e-06
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -42.624625610948186,
            "vertical_gap_native": -42.62462615966797,
            "left_alignment_delta": -7.407448492813273e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -42.624625610948186,
            "vertical_gap_native": -42.62462615966797,
            "left_alignment_delta": 1.5369762024874944e-05
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-06/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-06/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-06/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-06/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-06/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-06/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/06.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-06/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-06/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-06/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-06/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 7,
      "id": "aircon-07",
      "title": "选中时段",
      "description": "选中下午时段，尚未提交预约",
      "surface": "系统桌面",
      "branch": false,
      "base": "../cards/aircon-07/",
      "reference": "../cards/aircon-07/reference.png",
      "native": "../cards/aircon-07/rounds/012/native.png",
      "latest": {
        "round": "012",
        "build_id": [
          8
        ],
        "nonce": "d83455b2e20649eaaba0a98195600f5b"
      },
      "run": {
        "id": "aircon-07",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-07",
        "round": "012",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "2b829fb58ab02b6b99e6a33bbcca9c3e1596b456ae2d5bbdb9010fecf78da5e8",
          "reference_sha256": "dc33037fe9ced305eabe991fe1a207d1b7ea6a3348365b7a2e23e786f071f99e",
          "id": "aircon-07",
          "round": "012",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "installation_card",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "divider_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "close",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "close_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "close_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "saturday",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "saturday_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "saturday_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_123",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "sunday",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "sunday_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "sunday_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_124",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "conflict_slot",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "conflict_slot_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "conflict_slot_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_125",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_126",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "afternoon",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "afternoon_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "afternoon_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_127",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_128",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "cancel_selection",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "cancel_selection_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "cancel_selection_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_131",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "confirm_booking",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "confirm_booking_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "confirm_booking_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_132",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_120",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_121",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_129",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_130",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "close_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "home_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "step_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "step_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_118",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_119",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_133",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_134",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_135",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_136",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_137",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 8.066,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "dc33037fe9ced305eabe991fe1a207d1b7ea6a3348365b7a2e23e786f071f99e",
            "native_sha256": "3096ab98adffbae0ee2c381e0ca993fa6f8a091bbe5dc10f9253072f532e5f19",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_124: text color",
          "text_125: text ink dimensions",
          "text_125: text color",
          "text_126: text color",
          "text_127: text ink dimensions",
          "text_127: text color",
          "text_128: reference text missing or OCR unresolved",
          "text_131: text color",
          "text_120: text color",
          "text_121: text color",
          "text_129: reference OCR text differs",
          "text_129: text ink position",
          "text_129: text ink dimensions",
          "text_129: text color",
          "text_130: reference OCR text differs",
          "text_130: text ink dimensions",
          "text_130: text color",
          "text_118: text color",
          "text_133: text color",
          "text_134: text color",
          "text_135: text color",
          "text_136: text color",
          "text_137: text color",
          "1 extra reference text observations need classification"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              5.5,
              0.0,
              394.5,
              776.0
            ],
            "actual_bounds": [
              5.5,
              0.0,
              394.5,
              776.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "installation_card",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              19.15576923076923,
              109.9902248289345,
              366.4298076923077,
              561.3294232649072
            ],
            "actual_bounds": [
              19.15576934814453,
              109.99022674560547,
              366.4298095703125,
              561.3294067382812
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_0",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              40.39807692307692,
              543.1241446725318,
              317.8759615384615,
              0.7585532746823069
            ],
            "actual_bounds": [
              40.398075103759766,
              543.1241455078125,
              317.8759765625,
              0.7585532665252686
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "close",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              332.4798076923077,
              125.16129032258064,
              40.96730769230769,
              40.961876832844574
            ],
            "actual_bounds": [
              332.47979736328125,
              125.16129302978516,
              40.967308,
              40.961876
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "close_surface",
            "native_id": "beauty_0_0_0_1_0",
            "expected_bounds": [
              332.4798076923077,
              125.16129032258064,
              40.96730769230769,
              40.961876832844574
            ],
            "actual_bounds": [
              332.47979736328125,
              125.16129302978516,
              40.967308044433594,
              40.961875915527344
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "close_control",
            "native_id": "beauty_0_0_0_1_1",
            "expected_bounds": [
              332.4798076923077,
              125.16129032258064,
              40.96730769230769,
              40.961876832844574
            ],
            "actual_bounds": [
              332.47979736328125,
              125.16129302978516,
              40.967308044433594,
              40.961875915527344
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "saturday",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              38.122115384615384,
              217.70478983382208,
              157.79999999999998,
              46.271749755620725
            ],
            "actual_bounds": [
              38.12211608886719,
              217.7047882080078,
              157.8,
              46.27175
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "周六 9月19日",
            "enabled": true,
            "issues": []
          },
          {
            "id": "saturday_surface",
            "native_id": "beauty_0_0_0_2_0",
            "expected_bounds": [
              38.122115384615384,
              217.70478983382208,
              157.79999999999998,
              46.271749755620725
            ],
            "actual_bounds": [
              38.12211608886719,
              217.7047882080078,
              157.8000030517578,
              46.271751403808594
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "saturday_control",
            "native_id": "beauty_0_0_0_2_1",
            "expected_bounds": [
              38.122115384615384,
              217.70478983382208,
              157.79999999999998,
              46.271749755620725
            ],
            "actual_bounds": [
              38.12211608886719,
              217.7047882080078,
              157.8000030517578,
              46.271751403808594
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_123",
            "native_id": "beauty_0_0_0_2_2",
            "expected_bounds": [
              64.86264855459777,
              231.82462377217232,
              111.19418550184363,
              20.010501757038202
            ],
            "actual_bounds": [
              64.8626480102539,
              231.8246307373047,
              111.19418,
              20.010502
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Label",
            "visible": true,
            "text": "周六 9月19日",
            "enabled": true,
            "issues": []
          },
          {
            "id": "sunday",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              213.37115384615385,
              217.70478983382208,
              151.73076923076923,
              46.271749755620725
            ],
            "actual_bounds": [
              213.37115478515625,
              217.7047882080078,
              151.73077,
              46.27175
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "周日 9月20日",
            "enabled": true,
            "issues": []
          },
          {
            "id": "sunday_surface",
            "native_id": "beauty_0_0_0_3_0",
            "expected_bounds": [
              213.37115384615385,
              217.70478983382208,
              151.73076923076923,
              46.271749755620725
            ],
            "actual_bounds": [
              213.37115478515625,
              217.7047882080078,
              151.73077392578125,
              46.271751403808594
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "sunday_control",
            "native_id": "beauty_0_0_0_3_1",
            "expected_bounds": [
              213.37115384615385,
              217.70478983382208,
              151.73076923076923,
              46.271749755620725
            ],
            "actual_bounds": [
              213.37115478515625,
              217.7047882080078,
              151.73077392578125,
              46.271751403808594
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_124",
            "native_id": "beauty_0_0_0_3_2",
            "expected_bounds": [
              237.6611684176475,
              232.54511488011346,
              108.90369524179327,
              18.5
            ],
            "actual_bounds": [
              237.66116333007812,
              232.5451202392578,
              108.903694,
              18.5
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "Label",
            "visible": true,
            "text": "周日 9月20日",
            "enabled": true,
            "issues": []
          },
          {
            "id": "conflict_slot",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              38.122115384615384,
              283.6989247311828,
              327.73846153846154,
              91.02639296187684
            ],
            "actual_bounds": [
              38.12211608886719,
              283.69891357421875,
              327.73846,
              91.02639
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "09:00-11:00",
            "enabled": false,
            "issues": []
          },
          {
            "id": "conflict_slot_surface",
            "native_id": "beauty_0_0_0_4_0",
            "expected_bounds": [
              38.122115384615384,
              283.6989247311828,
              327.73846153846154,
              91.02639296187684
            ],
            "actual_bounds": [
              38.12211608886719,
              283.69891357421875,
              327.73846435546875,
              91.0263900756836
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "conflict_slot_control",
            "native_id": "beauty_0_0_0_4_1",
            "expected_bounds": [
              38.122115384615384,
              283.6989247311828,
              327.73846153846154,
              91.02639296187684
            ],
            "actual_bounds": [
              38.12211608886719,
              283.69891357421875,
              327.73846435546875,
              91.0263900756836
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": false,
            "issues": []
          },
          {
            "id": "text_125",
            "native_id": "beauty_0_0_0_4_2",
            "expected_bounds": [
              57.62662052757479,
              306.28808904734865,
              131.75047149987455,
              20.0
            ],
            "actual_bounds": [
              57.62662124633789,
              306.2880859375,
              131.75047,
              20.0
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "Label",
            "visible": true,
            "text": "09:00-11:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_126",
            "native_id": "beauty_0_0_0_4_3",
            "expected_bounds": [
              57.19168613203572,
              337.4304819459658,
              131.28941657944875,
              19.523813747541038
            ],
            "actual_bounds": [
              57.19168472290039,
              337.43048095703125,
              131.28941,
              19.523813
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "Label",
            "visible": true,
            "text": "与项目例会冲突",
            "enabled": true,
            "issues": []
          },
          {
            "id": "afternoon",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              38.122115384615384,
              386.10361681329425,
              327.73846153846154,
              91.02639296187684
            ],
            "actual_bounds": [
              38.12211608886719,
              386.1036071777344,
              327.73846,
              91.02639
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "afternoon_surface",
            "native_id": "beauty_0_0_0_5_0",
            "expected_bounds": [
              38.122115384615384,
              386.10361681329425,
              327.73846153846154,
              91.02639296187684
            ],
            "actual_bounds": [
              38.12211608886719,
              386.1036071777344,
              327.73846435546875,
              91.0263900756836
            ],
            "parent": "beauty_0_0_0_5",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "afternoon_control",
            "native_id": "beauty_0_0_0_5_1",
            "expected_bounds": [
              38.122115384615384,
              386.10361681329425,
              327.73846153846154,
              91.02639296187684
            ],
            "actual_bounds": [
              38.12211608886719,
              386.1036071777344,
              327.73846435546875,
              91.0263900756836
            ],
            "parent": "beauty_0_0_0_5",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_127",
            "native_id": "beauty_0_0_0_5_2",
            "expected_bounds": [
              58.276201671618495,
              409.4564254537901,
              129.15162327412946,
              20.0
            ],
            "actual_bounds": [
              58.27620315551758,
              409.4564208984375,
              129.15163,
              20.0
            ],
            "parent": "beauty_0_0_0_5",
            "widget_type": "Label",
            "visible": true,
            "text": "14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_128",
            "native_id": "beauty_0_0_0_5_3",
            "expected_bounds": [
              52.05243870929846,
              438.40863965842175,
              85.41364031330527,
              22.826904322451842
            ],
            "actual_bounds": [
              52.05243682861328,
              438.40863037109375,
              85.41364,
              22.826904
            ],
            "parent": "beauty_0_0_0_5",
            "widget_type": "Label",
            "visible": true,
            "text": "日历空闲",
            "enabled": true,
            "issues": []
          },
          {
            "id": "cancel_selection",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              38.122115384615384,
              597.7399804496579,
              138.83365384615385,
              50.82306940371456
            ],
            "actual_bounds": [
              38.12211608886719,
              597.739990234375,
              138.83365,
              50.82307
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "取消",
            "enabled": true,
            "issues": []
          },
          {
            "id": "cancel_selection_surface",
            "native_id": "beauty_0_0_0_6_0",
            "expected_bounds": [
              38.122115384615384,
              597.7399804496579,
              138.83365384615385,
              50.82306940371456
            ],
            "actual_bounds": [
              38.12211608886719,
              597.739990234375,
              138.83364868164062,
              50.82307052612305
            ],
            "parent": "beauty_0_0_0_6",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "cancel_selection_control",
            "native_id": "beauty_0_0_0_6_1",
            "expected_bounds": [
              38.122115384615384,
              597.7399804496579,
              138.83365384615385,
              50.82306940371456
            ],
            "actual_bounds": [
              38.12211608886719,
              597.739990234375,
              138.83364868164062,
              50.82307052612305
            ],
            "parent": "beauty_0_0_0_6",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_131",
            "native_id": "beauty_0_0_0_6_2",
            "expected_bounds": [
              87.36423003000392,
              611.9209011012767,
              43.866881752674566,
              22.5
            ],
            "actual_bounds": [
              87.36422729492188,
              611.9208984375,
              43.866882,
              22.5
            ],
            "parent": "beauty_0_0_0_6",
            "widget_type": "Label",
            "visible": true,
            "text": "取消",
            "enabled": true,
            "issues": []
          },
          {
            "id": "confirm_booking",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              195.92211538461538,
              597.7399804496579,
              169.1798076923077,
              50.82306940371456
            ],
            "actual_bounds": [
              195.922119140625,
              597.739990234375,
              169.17981,
              50.82307
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "确认预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "confirm_booking_surface",
            "native_id": "beauty_0_0_0_7_0",
            "expected_bounds": [
              195.92211538461538,
              597.7399804496579,
              169.1798076923077,
              50.82306940371456
            ],
            "actual_bounds": [
              195.922119140625,
              597.739990234375,
              169.1798095703125,
              50.82307052612305
            ],
            "parent": "beauty_0_0_0_7",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "confirm_booking_control",
            "native_id": "beauty_0_0_0_7_1",
            "expected_bounds": [
              195.92211538461538,
              597.7399804496579,
              169.1798076923077,
              50.82306940371456
            ],
            "actual_bounds": [
              195.922119140625,
              597.739990234375,
              169.1798095703125,
              50.82307052612305
            ],
            "parent": "beauty_0_0_0_7",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_132",
            "native_id": "beauty_0_0_0_7_2",
            "expected_bounds": [
              238.22086310014447,
              611.8190562410954,
              89.05916220241483,
              23.0
            ],
            "actual_bounds": [
              238.22085571289062,
              611.8190307617188,
              89.059166,
              23.0
            ],
            "parent": "beauty_0_0_0_7",
            "widget_type": "Label",
            "visible": true,
            "text": "确认预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "close_icon_0",
            "native_id": "beauty_0_0_0_8",
            "expected_bounds": [
              343.8596153846154,
              137.29814271749754,
              18.207692307692305,
              18.205278592375365
            ],
            "actual_bounds": [
              343.859619140625,
              137.2981414794922,
              18.207693099975586,
              18.205278396606445
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "home_icon_1",
            "native_id": "beauty_0_0_0_9",
            "expected_bounds": [
              40.39807692307692,
              504.4379276637341,
              21.24230769230769,
              20.480938416422287
            ],
            "actual_bounds": [
              40.398075103759766,
              504.43792724609375,
              21.242307662963867,
              20.480937957763672
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_0",
            "native_id": "beauty_0_0_0_10",
            "expected_bounds": [
              319.5826923076923,
              313.28250244379274,
              26.552884615384613,
              26.549364613880744
            ],
            "actual_bounds": [
              319.58270263671875,
              313.2825012207031,
              26.552885055541992,
              26.54936408996582
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_1",
            "native_id": "beauty_0_0_0_11",
            "expected_bounds": [
              312.7548076923077,
              407.3431085043988,
              38.691346153846155,
              40.961876832844574
            ],
            "actual_bounds": [
              312.75482177734375,
              407.3431091308594,
              38.69134521484375,
              40.961875915527344
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_120",
            "native_id": "beauty_0_0_0_12",
            "expected_bounds": [
              42.93063760860344,
              134.08592355334355,
              135.46124001688858,
              23.836475868323575
            ],
            "actual_bounds": [
              42.93063735961914,
              134.08592224121094,
              135.46124,
              23.836475
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "选择安装时间",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_121",
            "native_id": "beauty_0_0_0_13",
            "expected_bounds": [
              42.43699091097026,
              176.6219365066355,
              61.6353982839981,
              21.0
            ],
            "actual_bounds": [
              42.43699264526367,
              176.62193298339844,
              61.6354,
              21.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "王师傅",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_129",
            "native_id": "beauty_0_0_0_14",
            "expected_bounds": [
              67.39073571280672,
              506.38729177052596,
              137.5081693239466,
              20.374976576250127
            ],
            "actual_bounds": [
              67.39073944091797,
              506.3872985839844,
              137.50816,
              20.374977
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "家 · 海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_130",
            "native_id": "beauty_0_0_0_15",
            "expected_bounds": [
              39.73954545067328,
              556.7109614606546,
              257.0396471646517,
              22.379299293268467
            ],
            "actual_bounds": [
              39.73954391479492,
              556.7109375,
              257.03964,
              22.3793
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "周六 9月19日 · 14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              19.15576923076923,
              676.6295210166178,
              367.94711538461536,
              99.37047898338221
            ],
            "actual_bounds": [
              19.15576934814453,
              676.6295166015625,
              367.9471130371094,
              99.37047576904297
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              41.44122596153846,
              683.2441055718475,
              68.02090384615384,
              68.01188660801564
            ],
            "actual_bounds": [
              41.441226959228516,
              683.2440795898438,
              68.02090454101562,
              68.01188659667969
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              52.82103365384615,
              697.6566177908113,
              45.261288461538456,
              42.97962854349951
            ],
            "actual_bounds": [
              52.8210334777832,
              697.6566162109375,
              45.261287689208984,
              42.97962951660156
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              127.90879807692306,
              683.2441055718475,
              68.02090384615384,
              68.01188660801564
            ],
            "actual_bounds": [
              127.90879821777344,
              683.2440795898438,
              68.02090454101562,
              68.01188659667969
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              214.3763701923077,
              683.2441055718475,
              68.02090384615384,
              68.01188660801564
            ],
            "actual_bounds": [
              214.37637329101562,
              683.2440795898438,
              68.02090454101562,
              68.01188659667969
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_1_4",
            "expected_bounds": [
              225.75617788461537,
              697.6566177908113,
              45.261288461538456,
              42.97962854349951
            ],
            "actual_bounds": [
              225.7561798095703,
              697.6566162109375,
              45.261287689208984,
              42.97962951660156
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_1_5",
            "expected_bounds": [
              300.84394230769226,
              683.2441055718475,
              68.02090384615384,
              68.01188660801564
            ],
            "actual_bounds": [
              300.84393310546875,
              683.2440795898438,
              68.02090454101562,
              68.01188659667969
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_1_6",
            "expected_bounds": [
              312.22374999999994,
              697.6566177908113,
              45.261288461538456,
              42.97962854349951
            ],
            "actual_bounds": [
              312.2237548828125,
              697.6566162109375,
              45.261287689208984,
              42.97962951660156
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_118",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              28.96198547951073,
              24.27353798026451,
              108.21889178621558,
              18.0
            ],
            "actual_bounds": [
              28.961984634399414,
              24.27353858947754,
              108.218895,
              18.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月18日 周五",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_119",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              28.116522639000927,
              58.97962122715512,
              89.96643188423731,
              30.0
            ],
            "actual_bounds": [
              28.11652183532715,
              58.97962188720703,
              89.96643,
              30.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "15:27",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_133",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              43.561596710557076,
              746.5052674214131,
              37.816476702530416,
              18.5
            ],
            "actual_bounds": [
              43.56159591674805,
              746.5052490234375,
              37.816475,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_134",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              134.04442233030815,
              702.4990394334504,
              34.43706546578379,
              25.0
            ],
            "actual_bounds": [
              134.04441833496094,
              702.4990234375,
              34.437065,
              25.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "18",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_135",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              132.6495293880454,
              746.6389467789908,
              35.92085577421766,
              18.0
            ],
            "actual_bounds": [
              132.6495361328125,
              746.6389770507812,
              35.920856,
              18.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_136",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              231.78343190513817,
              746.537255926961,
              36.56824164481208,
              18.5
            ],
            "actual_bounds": [
              231.78343200683594,
              746.5372314453125,
              36.56824,
              18.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_137",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              324.7332543473144,
              746.0209109332662,
              37.07170475762353,
              19.0
            ],
            "actual_bounds": [
              324.7332458496094,
              746.0209350585938,
              37.071705,
              19.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_123",
            "reference": [
              65.5,
              233.5,
              102.0,
              16.0
            ],
            "native": [
              65.5,
              233.5,
              102.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              245,
              250,
              247
            ],
            "native_color": [
              255,
              255,
              255
            ],
            "issues": []
          },
          {
            "id": "text_124",
            "reference": [
              238.5,
              234.5,
              99.5,
              14.5
            ],
            "native": [
              238.5,
              234.5,
              99.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              70,
              70,
              69
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_125",
            "reference": [
              59.0,
              308.0,
              127.5,
              16.0
            ],
            "native": [
              59.0,
              308.0,
              124.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              -3.5,
              0.0
            ],
            "reference_color": [
              22,
              22,
              22
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_126",
            "reference": [
              58.5,
              339.0,
              123.5,
              15.5
            ],
            "native": [
              58.5,
              339.0,
              123.5,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              205,
              142,
              83
            ],
            "native_color": [
              190,
              135,
              63
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_127",
            "reference": [
              60.0,
              411.0,
              126.0,
              16.0
            ],
            "native": [
              60.0,
              411.0,
              121.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              -5.0,
              0.0
            ],
            "reference_color": [
              33,
              35,
              33
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_128",
            "reference": null,
            "native": null,
            "delta": null,
            "reference_color": null,
            "native_color": null,
            "issues": [
              "reference text missing or OCR unresolved"
            ]
          },
          {
            "id": "text_131",
            "reference": [
              88.0,
              613.5,
              36.5,
              18.5
            ],
            "native": [
              88.0,
              613.5,
              36.5,
              17.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              94,
              108,
              99
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_132",
            "reference": [
              239.0,
              613.5,
              81.0,
              19.0
            ],
            "native": [
              239.0,
              613.5,
              81.0,
              19.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              244,
              248,
              246
            ],
            "native_color": [
              255,
              255,
              255
            ],
            "issues": []
          },
          {
            "id": "text_120",
            "reference": [
              44.0,
              136.0,
              126.5,
              19.5
            ],
            "native": [
              44.0,
              136.0,
              126.5,
              19.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              23,
              22,
              22
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_121",
            "reference": [
              43.5,
              178.5,
              54.0,
              17.0
            ],
            "native": [
              43.5,
              178.5,
              54.0,
              16.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              70,
              70,
              70
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_129",
            "reference": [
              41.0,
              504.5,
              149.5,
              17.0
            ],
            "native": [
              69.0,
              508.5,
              130.5,
              16.0
            ],
            "delta": [
              28.0,
              4.0,
              -19.0,
              -1.0
            ],
            "reference_color": [
              115,
              115,
              115
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink position",
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_130",
            "reference": [
              43.0,
              560.5,
              244.0,
              15.0
            ],
            "native": [
              40.5,
              558.5,
              251.0,
              18.0
            ],
            "delta": [
              -2.5,
              -2.0,
              7.0,
              3.0
            ],
            "reference_color": [
              84,
              85,
              85
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_118",
            "reference": [
              30.0,
              26.0,
              100.5,
              14.0
            ],
            "native": [
              30.0,
              26.0,
              100.5,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              88,
              95,
              92
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_119",
            "reference": [
              31.0,
              61.0,
              80.0,
              26.0
            ],
            "native": [
              31.0,
              61.0,
              80.0,
              25.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              52,
              64,
              59
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_133",
            "reference": [
              45.0,
              748.0,
              30.5,
              14.5
            ],
            "native": [
              45.0,
              748.0,
              30.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              108,
              115,
              111
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_134",
            "reference": [
              136.5,
              704.5,
              25.0,
              21.0
            ],
            "native": [
              136.5,
              704.5,
              25.0,
              19.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.5
            ],
            "reference_color": [
              82,
              90,
              85
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_135",
            "reference": [
              135.5,
              748.5,
              27.0,
              14.0
            ],
            "native": [
              135.5,
              748.5,
              27.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              105,
              112,
              109
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_136",
            "reference": [
              232.5,
              748.0,
              29.5,
              14.5
            ],
            "native": [
              232.5,
              748.0,
              29.5,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              104,
              111,
              109
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_137",
            "reference": [
              325.5,
              747.5,
              30.0,
              15.0
            ],
            "native": [
              325.5,
              747.5,
              30.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              106,
              112,
              110
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              5.5,
              0.0,
              394.5,
              776.0
            ],
            "native": [
              5.5,
              0.0,
              394.5,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "installation_card",
            "reference": [
              19.15576923076923,
              109.9902248289345,
              366.4298076923077,
              561.3294232649072
            ],
            "native": [
              19.15576934814453,
              109.99022674560547,
              366.4298095703125,
              561.3294067382812
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "divider_0",
            "reference": [
              40.39807692307692,
              543.1241446725318,
              317.8759615384615,
              0.7585532746823069
            ],
            "native": [
              40.398075103759766,
              543.1241455078125,
              317.8759765625,
              0.7585532665252686
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "close",
            "reference": [
              332.4798076923077,
              125.16129032258064,
              40.96730769230769,
              40.961876832844574
            ],
            "native": [
              332.47979736328125,
              125.16129302978516,
              40.967308,
              40.961876
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "close_surface",
            "reference": [
              332.4798076923077,
              125.16129032258064,
              40.96730769230769,
              40.961876832844574
            ],
            "native": [
              332.47979736328125,
              125.16129302978516,
              40.967308044433594,
              40.961875915527344
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "close_control",
            "reference": [
              332.4798076923077,
              125.16129032258064,
              40.96730769230769,
              40.961876832844574
            ],
            "native": [
              332.47979736328125,
              125.16129302978516,
              40.967308044433594,
              40.961875915527344
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "saturday",
            "reference": [
              38.122115384615384,
              217.70478983382208,
              157.79999999999998,
              46.271749755620725
            ],
            "native": [
              38.12211608886719,
              217.7047882080078,
              157.8,
              46.27175
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "saturday_surface",
            "reference": [
              38.122115384615384,
              217.70478983382208,
              157.79999999999998,
              46.271749755620725
            ],
            "native": [
              38.12211608886719,
              217.7047882080078,
              157.8000030517578,
              46.271751403808594
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "saturday_control",
            "reference": [
              38.122115384615384,
              217.70478983382208,
              157.79999999999998,
              46.271749755620725
            ],
            "native": [
              38.12211608886719,
              217.7047882080078,
              157.8000030517578,
              46.271751403808594
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "sunday",
            "reference": [
              213.37115384615385,
              217.70478983382208,
              151.73076923076923,
              46.271749755620725
            ],
            "native": [
              213.37115478515625,
              217.7047882080078,
              151.73077,
              46.27175
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "sunday_surface",
            "reference": [
              213.37115384615385,
              217.70478983382208,
              151.73076923076923,
              46.271749755620725
            ],
            "native": [
              213.37115478515625,
              217.7047882080078,
              151.73077392578125,
              46.271751403808594
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "sunday_control",
            "reference": [
              213.37115384615385,
              217.70478983382208,
              151.73076923076923,
              46.271749755620725
            ],
            "native": [
              213.37115478515625,
              217.7047882080078,
              151.73077392578125,
              46.271751403808594
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "conflict_slot",
            "reference": [
              38.122115384615384,
              283.6989247311828,
              327.73846153846154,
              91.02639296187684
            ],
            "native": [
              38.12211608886719,
              283.69891357421875,
              327.73846,
              91.02639
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "conflict_slot_surface",
            "reference": [
              38.122115384615384,
              283.6989247311828,
              327.73846153846154,
              91.02639296187684
            ],
            "native": [
              38.12211608886719,
              283.69891357421875,
              327.73846435546875,
              91.0263900756836
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "conflict_slot_control",
            "reference": [
              38.122115384615384,
              283.6989247311828,
              327.73846153846154,
              91.02639296187684
            ],
            "native": [
              38.12211608886719,
              283.69891357421875,
              327.73846435546875,
              91.0263900756836
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "afternoon",
            "reference": [
              38.122115384615384,
              386.10361681329425,
              327.73846153846154,
              91.02639296187684
            ],
            "native": [
              38.12211608886719,
              386.1036071777344,
              327.73846,
              91.02639
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "afternoon_surface",
            "reference": [
              38.122115384615384,
              386.10361681329425,
              327.73846153846154,
              91.02639296187684
            ],
            "native": [
              38.12211608886719,
              386.1036071777344,
              327.73846435546875,
              91.0263900756836
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "afternoon_control",
            "reference": [
              38.122115384615384,
              386.10361681329425,
              327.73846153846154,
              91.02639296187684
            ],
            "native": [
              38.12211608886719,
              386.1036071777344,
              327.73846435546875,
              91.0263900756836
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "cancel_selection",
            "reference": [
              38.122115384615384,
              597.7399804496579,
              138.83365384615385,
              50.82306940371456
            ],
            "native": [
              38.12211608886719,
              597.739990234375,
              138.83365,
              50.82307
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "cancel_selection_surface",
            "reference": [
              38.122115384615384,
              597.7399804496579,
              138.83365384615385,
              50.82306940371456
            ],
            "native": [
              38.12211608886719,
              597.739990234375,
              138.83364868164062,
              50.82307052612305
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "cancel_selection_control",
            "reference": [
              38.122115384615384,
              597.7399804496579,
              138.83365384615385,
              50.82306940371456
            ],
            "native": [
              38.12211608886719,
              597.739990234375,
              138.83364868164062,
              50.82307052612305
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "confirm_booking",
            "reference": [
              195.92211538461538,
              597.7399804496579,
              169.1798076923077,
              50.82306940371456
            ],
            "native": [
              195.922119140625,
              597.739990234375,
              169.17981,
              50.82307
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "confirm_booking_surface",
            "reference": [
              195.92211538461538,
              597.7399804496579,
              169.1798076923077,
              50.82306940371456
            ],
            "native": [
              195.922119140625,
              597.739990234375,
              169.1798095703125,
              50.82307052612305
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "confirm_booking_control",
            "reference": [
              195.92211538461538,
              597.7399804496579,
              169.1798076923077,
              50.82306940371456
            ],
            "native": [
              195.922119140625,
              597.739990234375,
              169.1798095703125,
              50.82307052612305
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "close_icon_0",
            "reference": [
              343.8596153846154,
              137.29814271749754,
              18.207692307692305,
              18.205278592375365
            ],
            "native": [
              343.859619140625,
              137.2981414794922,
              18.207693099975586,
              18.205278396606445
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "home_icon_1",
            "reference": [
              40.39807692307692,
              504.4379276637341,
              21.24230769230769,
              20.480938416422287
            ],
            "native": [
              40.398075103759766,
              504.43792724609375,
              21.242307662963867,
              20.480937957763672
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_0",
            "reference": [
              319.5826923076923,
              313.28250244379274,
              26.552884615384613,
              26.549364613880744
            ],
            "native": [
              319.58270263671875,
              313.2825012207031,
              26.552885055541992,
              26.54936408996582
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_1",
            "reference": [
              312.7548076923077,
              407.3431085043988,
              38.691346153846155,
              40.961876832844574
            ],
            "native": [
              312.75482177734375,
              407.3431091308594,
              38.69134521484375,
              40.961875915527344
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              19.15576923076923,
              676.6295210166178,
              367.94711538461536,
              99.37047898338221
            ],
            "native": [
              19.15576934814453,
              676.6295166015625,
              367.9471130371094,
              99.37047576904297
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              41.44122596153846,
              683.2441055718475,
              68.02090384615384,
              68.01188660801564
            ],
            "native": [
              41.441226959228516,
              683.2440795898438,
              68.02090454101562,
              68.01188659667969
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              52.82103365384615,
              697.6566177908113,
              45.261288461538456,
              42.97962854349951
            ],
            "native": [
              52.8210334777832,
              697.6566162109375,
              45.261287689208984,
              42.97962951660156
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              127.90879807692306,
              683.2441055718475,
              68.02090384615384,
              68.01188660801564
            ],
            "native": [
              127.90879821777344,
              683.2440795898438,
              68.02090454101562,
              68.01188659667969
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              214.3763701923077,
              683.2441055718475,
              68.02090384615384,
              68.01188660801564
            ],
            "native": [
              214.37637329101562,
              683.2440795898438,
              68.02090454101562,
              68.01188659667969
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              225.75617788461537,
              697.6566177908113,
              45.261288461538456,
              42.97962854349951
            ],
            "native": [
              225.7561798095703,
              697.6566162109375,
              45.261287689208984,
              42.97962951660156
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              300.84394230769226,
              683.2441055718475,
              68.02090384615384,
              68.01188660801564
            ],
            "native": [
              300.84393310546875,
              683.2440795898438,
              68.02090454101562,
              68.01188659667969
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              312.22374999999994,
              697.6566177908113,
              45.261288461538456,
              42.97962854349951
            ],
            "native": [
              312.2237548828125,
              697.6566162109375,
              45.261287689208984,
              42.97962951660156
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "installation_card",
            "second": "dock",
            "vertical_gap_reference": 5.309872922776094,
            "vertical_gap_native": 5.309883117675781,
            "left_alignment_delta": 0.0
          },
          {
            "first": "close",
            "second": "close_icon_0",
            "vertical_gap_reference": -28.825024437927674,
            "vertical_gap_native": -28.825027550292965,
            "left_alignment_delta": 1.408503607081002e-05
          },
          {
            "first": "close_icon_0",
            "second": "saturday",
            "vertical_gap_reference": 62.20136852394917,
            "vertical_gap_native": 62.20136833190918,
            "left_alignment_delta": -3.0517578011313162e-06
          },
          {
            "first": "saturday",
            "second": "sunday",
            "vertical_gap_reference": -46.271749755620725,
            "vertical_gap_native": -46.27175,
            "left_alignment_delta": 2.3475058696931228e-07
          },
          {
            "first": "sunday",
            "second": "conflict_slot",
            "vertical_gap_reference": 19.722385141739984,
            "vertical_gap_native": 19.72237536621094,
            "left_alignment_delta": -2.3475058696931228e-07
          },
          {
            "first": "conflict_slot",
            "second": "step_0",
            "vertical_gap_reference": -61.442815249266886,
            "vertical_gap_native": -61.44280235351563,
            "left_alignment_delta": 9.624774634175992e-06
          },
          {
            "first": "step_0",
            "second": "afternoon",
            "vertical_gap_reference": 46.271749755620775,
            "vertical_gap_native": 46.27174186706543,
            "left_alignment_delta": -9.624774634175992e-06
          },
          {
            "first": "afternoon",
            "second": "step_1",
            "vertical_gap_reference": -69.78690127077229,
            "vertical_gap_native": -69.786888046875,
            "left_alignment_delta": 1.3380784253058664e-05
          },
          {
            "first": "step_1",
            "second": "home_icon_1",
            "vertical_gap_reference": 56.13294232649074,
            "vertical_gap_native": 56.13294219970703,
            "left_alignment_delta": -1.5904353233509028e-05
          },
          {
            "first": "home_icon_1",
            "second": "divider_0",
            "vertical_gap_reference": 18.205278592375368,
            "vertical_gap_native": 18.205280303955078,
            "left_alignment_delta": 0.0
          },
          {
            "first": "divider_0",
            "second": "cancel_selection",
            "vertical_gap_reference": 53.8572825024438,
            "vertical_gap_native": 53.85729146003723,
            "left_alignment_delta": 2.5235689591340815e-06
          },
          {
            "first": "cancel_selection",
            "second": "confirm_booking",
            "vertical_gap_reference": -50.82306940371456,
            "vertical_gap_native": -50.82307,
            "left_alignment_delta": 3.0517578011313162e-06
          },
          {
            "first": "close_surface",
            "second": "close_control",
            "vertical_gap_reference": -40.961876832844574,
            "vertical_gap_native": -40.961875915527344,
            "left_alignment_delta": 0.0
          },
          {
            "first": "saturday_surface",
            "second": "saturday_control",
            "vertical_gap_reference": -46.271749755620725,
            "vertical_gap_native": -46.271751403808594,
            "left_alignment_delta": 0.0
          },
          {
            "first": "sunday_surface",
            "second": "sunday_control",
            "vertical_gap_reference": -46.271749755620725,
            "vertical_gap_native": -46.271751403808594,
            "left_alignment_delta": 0.0
          },
          {
            "first": "conflict_slot_surface",
            "second": "conflict_slot_control",
            "vertical_gap_reference": -91.02639296187684,
            "vertical_gap_native": -91.0263900756836,
            "left_alignment_delta": 0.0
          },
          {
            "first": "afternoon_surface",
            "second": "afternoon_control",
            "vertical_gap_reference": -91.02639296187684,
            "vertical_gap_native": -91.0263900756836,
            "left_alignment_delta": 0.0
          },
          {
            "first": "cancel_selection_surface",
            "second": "cancel_selection_control",
            "vertical_gap_reference": -50.82306940371456,
            "vertical_gap_native": -50.82307052612305,
            "left_alignment_delta": 0.0
          },
          {
            "first": "confirm_booking_surface",
            "second": "confirm_booking_control",
            "vertical_gap_reference": -50.82306940371456,
            "vertical_gap_native": -50.82307052612305,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -68.01188660801564,
            "vertical_gap_native": -68.01188659667969,
            "left_alignment_delta": -8.568396765440411e-07
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -68.01188660801564,
            "vertical_gap_native": -68.01188659667969,
            "left_alignment_delta": 2.9578575606592494e-06
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -68.01188660801564,
            "vertical_gap_native": -68.01188659667969,
            "left_alignment_delta": -1.2300931444997332e-05
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -53.599374389051846,
            "vertical_gap_native": -53.59934997558594,
            "left_alignment_delta": 9.026160569192143e-06
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -42.97962854349951,
            "vertical_gap_native": -42.97962951660156,
            "left_alignment_delta": 2.1010178841152083e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -42.97962854349951,
            "vertical_gap_native": -42.97962951660156,
            "left_alignment_delta": 2.9578576175026683e-06
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-07/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-07/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-07/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-07/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-07/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-07/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/07.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-07/rounds/012/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-07/rounds/012/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-07/rounds/012/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-07/rounds/012/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 8,
      "id": "aircon-08",
      "title": "预约与日历",
      "description": "服务方确认预约，日历已经更新",
      "surface": "系统桌面",
      "branch": false,
      "base": "../cards/aircon-08/",
      "reference": "../cards/aircon-08/reference.png",
      "native": "../cards/aircon-08/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "fdf79fc78c7848828d21239aca62d47b"
      },
      "run": {
        "id": "aircon-08",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-08",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "1fcae2910ee582d88b226ba8a5ab8dcb7cd9a89f7373536273cb79dd25817fd1",
          "reference_sha256": "26f610453b9655c399dde452abbaed26fdd491f374311ac4aa42f2396e584d4f",
          "id": "aircon-08",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "installation_booking",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "reschedule",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "reschedule_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "reschedule_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_182",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "cancel_booking",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "cancel_booking_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "cancel_booking_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_183",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "wrench_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "check_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_178",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_179",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_180",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_181",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "calendar_updated",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "acknowledge_calendar",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "acknowledge_calendar_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "acknowledge_calendar_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_188",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "undo_calendar",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "undo_calendar_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "undo_calendar_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_189",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "calendar_icon_2",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_184",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_185",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_186",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_187",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_176",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_177",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_190",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_191",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_192",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_193",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_214",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 5.04,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "26f610453b9655c399dde452abbaed26fdd491f374311ac4aa42f2396e584d4f",
            "native_sha256": "5665152635b7e285b8028f840704b4fccb753d7c30f78d1ba3c5c29b5daa4a03",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_182: text color",
          "text_183: text color",
          "text_178: text color",
          "text_179: text color",
          "text_181: reference OCR text differs",
          "text_181: text ink position",
          "text_181: text ink dimensions",
          "text_181: text color",
          "text_188: text color",
          "text_189: text color",
          "text_185: text color",
          "text_186: text color",
          "text_187: text color",
          "text_176: text color",
          "text_190: text color",
          "text_191: text color",
          "text_192: text color",
          "text_193: text color",
          "text_214: text color"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              0.0,
              62.0,
              406.0,
              651.5
            ],
            "actual_bounds": [
              0.0,
              62.0,
              406.0,
              651.5
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "installation_booking",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              17.818181818181817,
              156.162109375,
              364.0,
              229.04296875
            ],
            "actual_bounds": [
              17.81818199157715,
              156.162109375,
              364.0,
              229.04296875
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "reschedule",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              37.54545454545455,
              326.671875,
              134.9090909090909,
              40.08251953125
            ],
            "actual_bounds": [
              37.54545593261719,
              326.671875,
              134.90909,
              40.08252
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "改约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "reschedule_surface",
            "native_id": "beauty_0_0_0_0_0",
            "expected_bounds": [
              37.54545454545455,
              326.671875,
              134.9090909090909,
              40.08251953125
            ],
            "actual_bounds": [
              37.54545593261719,
              326.671875,
              134.90908813476562,
              40.08251953125
            ],
            "parent": "beauty_0_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "reschedule_control",
            "native_id": "beauty_0_0_0_0_1",
            "expected_bounds": [
              37.54545454545455,
              326.671875,
              134.9090909090909,
              40.08251953125
            ],
            "actual_bounds": [
              37.54545593261719,
              326.671875,
              134.90908813476562,
              40.08251953125
            ],
            "parent": "beauty_0_0_0_0",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_182",
            "native_id": "beauty_0_0_0_0_2",
            "expected_bounds": [
              86.10862071523007,
              337.3160839378999,
              37.60448858254913,
              18.5
            ],
            "actual_bounds": [
              86.1086196899414,
              337.3160705566406,
              37.60449,
              18.5
            ],
            "parent": "beauty_0_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "改约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "cancel_booking",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              211.9090909090909,
              326.671875,
              133.0,
              40.08251953125
            ],
            "actual_bounds": [
              211.90908813476562,
              326.671875,
              133.0,
              40.08252
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "取消预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "cancel_booking_surface",
            "native_id": "beauty_0_0_0_1_0",
            "expected_bounds": [
              211.9090909090909,
              326.671875,
              133.0,
              40.08251953125
            ],
            "actual_bounds": [
              211.90908813476562,
              326.671875,
              133.0,
              40.08251953125
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "cancel_booking_control",
            "native_id": "beauty_0_0_0_1_1",
            "expected_bounds": [
              211.9090909090909,
              326.671875,
              133.0,
              40.08251953125
            ],
            "actual_bounds": [
              211.90908813476562,
              326.671875,
              133.0,
              40.08251953125
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_183",
            "native_id": "beauty_0_0_0_1_2",
            "expected_bounds": [
              242.93960158836185,
              337.17865658190453,
              72.93824000826523,
              19.0
            ],
            "actual_bounds": [
              242.93960571289062,
              337.17864990234375,
              72.93824,
              19.0
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "取消预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "wrench_icon_0",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              38.81818181818182,
              174.61279296875,
              28.0,
              29.2666015625
            ],
            "actual_bounds": [
              38.818180084228516,
              174.61279296875,
              28.0,
              29.2666015625
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "check_icon_1",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              336.6363636363636,
              179.06640625,
              20.363636363636363,
              20.99560546875
            ],
            "actual_bounds": [
              336.6363525390625,
              179.06640625,
              20.363636016845703,
              20.99560546875
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_178",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              79.25767356402852,
              180.90409330746817,
              163.89833904827873,
              19.5
            ],
            "actual_bounds": [
              79.25767517089844,
              180.9040985107422,
              163.89835,
              19.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "安装服务 · 预约成功",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_179",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              39.447969745880364,
              223.7377850077716,
              56.29585867871857,
              19.0
            ],
            "actual_bounds": [
              39.44797134399414,
              223.73777770996094,
              56.29586,
              19.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "王师傅",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_180",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              39.2723985240781,
              255.99660093034888,
              204.9036362982466,
              18.630935669577962
            ],
            "actual_bounds": [
              39.27239990234375,
              255.99659729003906,
              204.90364,
              18.630936
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "周六 9月19日 14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_181",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              33.65093636072279,
              286.3210833049111,
              121.00630114653481,
              18.35099777227279
            ],
            "actual_bounds": [
              33.650936126708984,
              286.3210754394531,
              121.0063,
              18.350998
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "家 · 海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "calendar_updated",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              17.818181818181817,
              396.02099609375,
              364.0,
              215.68212890625
            ],
            "actual_bounds": [
              17.81818199157715,
              396.02099609375,
              364.0,
              215.68212890625
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "acknowledge_calendar",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              35.63636363636363,
              555.07861328125,
              134.9090909090909,
              40.08251953125
            ],
            "actual_bounds": [
              35.6363639831543,
              555.07861328125,
              134.90909,
              40.08252
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "KitButton",
            "visible": true,
            "text": "确认",
            "enabled": true,
            "issues": []
          },
          {
            "id": "acknowledge_calendar_surface",
            "native_id": "beauty_0_0_1_0_0",
            "expected_bounds": [
              35.63636363636363,
              555.07861328125,
              134.9090909090909,
              40.08251953125
            ],
            "actual_bounds": [
              35.6363639831543,
              555.07861328125,
              134.90908813476562,
              40.08251953125
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "acknowledge_calendar_control",
            "native_id": "beauty_0_0_1_0_1",
            "expected_bounds": [
              35.63636363636363,
              555.07861328125,
              134.9090909090909,
              40.08251953125
            ],
            "actual_bounds": [
              35.6363639831543,
              555.07861328125,
              134.90908813476562,
              40.08251953125
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_188",
            "native_id": "beauty_0_0_1_0_2",
            "expected_bounds": [
              82.25838916377816,
              566.2518238826298,
              39.34980158059098,
              19.096134646022502
            ],
            "actual_bounds": [
              82.25839233398438,
              566.2518310546875,
              39.3498,
              19.096134
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "Label",
            "visible": true,
            "text": "确认",
            "enabled": true,
            "issues": []
          },
          {
            "id": "undo_calendar",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              211.9090909090909,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "actual_bounds": [
              211.90908813476562,
              555.07861328125,
              133.0,
              40.08252
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "KitButton",
            "visible": true,
            "text": "撤销日程",
            "enabled": true,
            "issues": []
          },
          {
            "id": "undo_calendar_surface",
            "native_id": "beauty_0_0_1_1_0",
            "expected_bounds": [
              211.9090909090909,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "actual_bounds": [
              211.90908813476562,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "parent": "beauty_0_0_1_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "undo_calendar_control",
            "native_id": "beauty_0_0_1_1_1",
            "expected_bounds": [
              211.9090909090909,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "actual_bounds": [
              211.90908813476562,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "parent": "beauty_0_0_1_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_189",
            "native_id": "beauty_0_0_1_1_2",
            "expected_bounds": [
              239.30777912302332,
              566.2181839928135,
              73.07800461060535,
              19.32247140952277
            ],
            "actual_bounds": [
              239.3077850341797,
              566.2182006835938,
              73.078,
              19.322472
            ],
            "parent": "beauty_0_0_1_1",
            "widget_type": "Label",
            "visible": true,
            "text": "撤销日程",
            "enabled": true,
            "issues": []
          },
          {
            "id": "calendar_icon_2",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              36.90909090909091,
              410.654296875,
              28.0,
              29.90283203125
            ],
            "actual_bounds": [
              36.90909194946289,
              410.654296875,
              28.0,
              29.90283203125
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_184",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              75.8136878869843,
              418.32699780446677,
              104.46184965381975,
              18.0
            ],
            "actual_bounds": [
              75.81369018554688,
              418.3269958496094,
              104.46185,
              18.0
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "日历 · 已更新",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_185",
            "native_id": "beauty_0_0_1_4",
            "expected_bounds": [
              33.32885220947213,
              457.4796298577214,
              81.93001440049784,
              21.0
            ],
            "actual_bounds": [
              33.328853607177734,
              457.4796447753906,
              81.930016,
              21.0
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "空调安装",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_186",
            "native_id": "beauty_0_0_1_5",
            "expected_bounds": [
              33.68893583885091,
              489.4958165534687,
              161.9901168884311,
              18.0
            ],
            "actual_bounds": [
              33.688934326171875,
              489.4958190917969,
              161.99011,
              18.0
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "9月19日 14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_187",
            "native_id": "beauty_0_0_1_6",
            "expected_bounds": [
              33.643206326807274,
              517.4394821325419,
              108.5935650444599,
              16.5
            ],
            "actual_bounds": [
              33.64320755004883,
              517.439453125,
              108.59357,
              16.5
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "已加入家庭日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              8.272727272727273,
              623.1552734375,
              371.6363636363636,
              89.70849609375
            ],
            "actual_bounds": [
              8.272727012634277,
              623.1552734375,
              371.6363525390625,
              89.70849609375
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_2_0",
            "expected_bounds": [
              31.690909090909088,
              629.4666796875,
              66.88436363636363,
              66.8703671875
            ],
            "actual_bounds": [
              31.690908432006836,
              629.4666748046875,
              66.88436126708984,
              66.87036895751953
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_2_1",
            "expected_bounds": [
              41.236363636363635,
              641.55505859375,
              47.793454545454544,
              45.87476171875
            ],
            "actual_bounds": [
              41.23636245727539,
              641.5550537109375,
              47.793453216552734,
              45.87476348876953
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_2_2",
            "expected_bounds": [
              119.02545454545454,
              629.4666796875,
              66.88436363636363,
              66.8703671875
            ],
            "actual_bounds": [
              119.02545166015625,
              629.4666748046875,
              66.88436126708984,
              66.87036895751953
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_2_3",
            "expected_bounds": [
              206.35999999999999,
              629.4666796875,
              66.88436363636363,
              66.8703671875
            ],
            "actual_bounds": [
              206.36000061035156,
              629.4666748046875,
              66.88436126708984,
              66.87036895751953
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_2_4",
            "expected_bounds": [
              215.90545454545452,
              641.55505859375,
              47.793454545454544,
              45.87476171875
            ],
            "actual_bounds": [
              215.90545654296875,
              641.5550537109375,
              47.793453216552734,
              45.87476348876953
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_2_5",
            "expected_bounds": [
              293.6945454545454,
              629.4666796875,
              66.88436363636363,
              66.8703671875
            ],
            "actual_bounds": [
              293.6945495605469,
              629.4666748046875,
              66.88436126708984,
              66.87036895751953
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_2_6",
            "expected_bounds": [
              303.23999999999995,
              641.55505859375,
              47.793454545454544,
              45.87476171875
            ],
            "actual_bounds": [
              303.239990234375,
              641.5550537109375,
              47.793453216552734,
              45.87476348876953
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_176",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              24.48043059395049,
              81.6403824777834,
              92.44611311352706,
              16.0
            ],
            "actual_bounds": [
              24.480430603027344,
              81.640380859375,
              92.44611,
              16.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月18日 周五",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_177",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              23.086848392352273,
              111.01413681029568,
              77.02631564647598,
              26.0
            ],
            "actual_bounds": [
              23.086849212646484,
              111.0141372680664,
              77.02631,
              26.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "15:28",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_190",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              41.15849020251396,
              687.4029179908213,
              34.06379968611722,
              16.5
            ],
            "actual_bounds": [
              41.15848922729492,
              687.4028930664062,
              34.0638,
              16.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_191",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              127.50065532053497,
              650.466408065769,
              31.57544527602744,
              22.0
            ],
            "actual_bounds": [
              127.50065612792969,
              650.4664306640625,
              31.575445,
              22.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "18",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_192",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              126.18788586561179,
              688.552628897325,
              32.988845975708585,
              15.5
            ],
            "actual_bounds": [
              126.1878890991211,
              688.5526123046875,
              32.988846,
              15.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_193",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              218.13564675360428,
              687.9160454372925,
              33.20944424656538,
              16.5
            ],
            "actual_bounds": [
              218.13565063476562,
              687.916015625,
              33.209446,
              16.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_214",
            "native_id": "beauty_0_0_9",
            "expected_bounds": [
              310.47413965894026,
              687.5767485695802,
              34.54839773811133,
              17.0
            ],
            "actual_bounds": [
              310.4741516113281,
              687.5767211914062,
              34.548397,
              17.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_182",
            "reference": [
              87.0,
              339.0,
              30.0,
              14.5
            ],
            "native": [
              87.0,
              339.0,
              30.0,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              82,
              104,
              89
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_183",
            "reference": [
              243.5,
              339.0,
              65.5,
              15.0
            ],
            "native": [
              243.5,
              339.0,
              65.5,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              104,
              107,
              104
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_178",
            "reference": [
              80.5,
              183.0,
              155.5,
              15.5
            ],
            "native": [
              80.5,
              183.0,
              155.5,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              65,
              95,
              65
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_179",
            "reference": [
              40.5,
              225.5,
              49.0,
              15.0
            ],
            "native": [
              40.5,
              225.5,
              49.0,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              67,
              67,
              66
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_180",
            "reference": [
              40.0,
              258.0,
              197.5,
              14.5
            ],
            "native": [
              40.0,
              258.0,
              197.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              58,
              58,
              58
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_181",
            "reference": [
              40.0,
              288.5,
              107.0,
              13.0
            ],
            "native": [
              35.0,
              288.0,
              114.5,
              14.5
            ],
            "delta": [
              -5.0,
              -0.5,
              7.5,
              1.5
            ],
            "reference_color": [
              80,
              81,
              81
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink position",
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_188",
            "reference": [
              83.0,
              568.0,
              32.5,
              15.0
            ],
            "native": [
              83.0,
              568.0,
              32.5,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              76,
              101,
              84
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_189",
            "reference": [
              240.0,
              568.0,
              66.0,
              15.0
            ],
            "native": [
              240.0,
              568.0,
              66.0,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              118,
              118,
              118
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_184",
            "reference": [
              78.5,
              420.0,
              95.0,
              14.0
            ],
            "native": [
              78.5,
              420.0,
              95.0,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              56,
              57,
              55
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_185",
            "reference": [
              35.0,
              459.0,
              75.5,
              17.0
            ],
            "native": [
              35.0,
              459.0,
              74.0,
              16.5
            ],
            "delta": [
              0.0,
              0.0,
              -1.5,
              -0.5
            ],
            "reference_color": [
              23,
              23,
              23
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_186",
            "reference": [
              34.5,
              491.5,
              154.5,
              14.0
            ],
            "native": [
              34.5,
              491.5,
              154.5,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              69,
              69,
              70
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_187",
            "reference": [
              35.0,
              519.0,
              103.0,
              12.5
            ],
            "native": [
              35.0,
              519.0,
              101.0,
              12.5
            ],
            "delta": [
              0.0,
              0.0,
              -2.0,
              0.0
            ],
            "reference_color": [
              117,
              117,
              117
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_176",
            "reference": [
              25.0,
              83.5,
              85.5,
              12.0
            ],
            "native": [
              25.0,
              83.5,
              85.5,
              12.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              99,
              106,
              103
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_177",
            "reference": [
              25.5,
              113.0,
              67.5,
              22.0
            ],
            "native": [
              25.5,
              113.0,
              67.5,
              21.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              54,
              65,
              59
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_190",
            "reference": [
              42.5,
              689.0,
              27.0,
              12.5
            ],
            "native": [
              42.5,
              689.0,
              26.5,
              12.5
            ],
            "delta": [
              0.0,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              83,
              94,
              87
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_191",
            "reference": [
              129.5,
              652.5,
              22.5,
              18.0
            ],
            "native": [
              129.5,
              652.5,
              22.5,
              17.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              82,
              90,
              85
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_192",
            "reference": [
              128.5,
              690.0,
              25.5,
              11.5
            ],
            "native": [
              128.5,
              690.0,
              25.0,
              11.5
            ],
            "delta": [
              0.0,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              90,
              100,
              95
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_193",
            "reference": [
              219.0,
              689.0,
              27.0,
              12.5
            ],
            "native": [
              219.0,
              689.5,
              26.5,
              12.0
            ],
            "delta": [
              0.0,
              0.5,
              -0.5,
              -0.5
            ],
            "reference_color": [
              105,
              111,
              108
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_214",
            "reference": [
              311.5,
              689.0,
              27.5,
              13.0
            ],
            "native": [
              311.5,
              689.0,
              27.5,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              107,
              115,
              112
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              0.0,
              62.0,
              406.0,
              651.5
            ],
            "native": [
              0.0,
              62.0,
              406.0,
              651.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "installation_booking",
            "reference": [
              17.818181818181817,
              156.162109375,
              364.0,
              229.04296875
            ],
            "native": [
              17.81818199157715,
              156.162109375,
              364.0,
              229.04296875
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "reschedule",
            "reference": [
              37.54545454545455,
              326.671875,
              134.9090909090909,
              40.08251953125
            ],
            "native": [
              37.54545593261719,
              326.671875,
              134.90909,
              40.08252
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "reschedule_surface",
            "reference": [
              37.54545454545455,
              326.671875,
              134.9090909090909,
              40.08251953125
            ],
            "native": [
              37.54545593261719,
              326.671875,
              134.90908813476562,
              40.08251953125
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "reschedule_control",
            "reference": [
              37.54545454545455,
              326.671875,
              134.9090909090909,
              40.08251953125
            ],
            "native": [
              37.54545593261719,
              326.671875,
              134.90908813476562,
              40.08251953125
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "cancel_booking",
            "reference": [
              211.9090909090909,
              326.671875,
              133.0,
              40.08251953125
            ],
            "native": [
              211.90908813476562,
              326.671875,
              133.0,
              40.08252
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "cancel_booking_surface",
            "reference": [
              211.9090909090909,
              326.671875,
              133.0,
              40.08251953125
            ],
            "native": [
              211.90908813476562,
              326.671875,
              133.0,
              40.08251953125
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "cancel_booking_control",
            "reference": [
              211.9090909090909,
              326.671875,
              133.0,
              40.08251953125
            ],
            "native": [
              211.90908813476562,
              326.671875,
              133.0,
              40.08251953125
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "wrench_icon_0",
            "reference": [
              38.81818181818182,
              174.61279296875,
              28.0,
              29.2666015625
            ],
            "native": [
              38.818180084228516,
              174.61279296875,
              28.0,
              29.2666015625
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "check_icon_1",
            "reference": [
              336.6363636363636,
              179.06640625,
              20.363636363636363,
              20.99560546875
            ],
            "native": [
              336.6363525390625,
              179.06640625,
              20.363636016845703,
              20.99560546875
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "calendar_updated",
            "reference": [
              17.818181818181817,
              396.02099609375,
              364.0,
              215.68212890625
            ],
            "native": [
              17.81818199157715,
              396.02099609375,
              364.0,
              215.68212890625
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "acknowledge_calendar",
            "reference": [
              35.63636363636363,
              555.07861328125,
              134.9090909090909,
              40.08251953125
            ],
            "native": [
              35.6363639831543,
              555.07861328125,
              134.90909,
              40.08252
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "acknowledge_calendar_surface",
            "reference": [
              35.63636363636363,
              555.07861328125,
              134.9090909090909,
              40.08251953125
            ],
            "native": [
              35.6363639831543,
              555.07861328125,
              134.90908813476562,
              40.08251953125
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "acknowledge_calendar_control",
            "reference": [
              35.63636363636363,
              555.07861328125,
              134.9090909090909,
              40.08251953125
            ],
            "native": [
              35.6363639831543,
              555.07861328125,
              134.90908813476562,
              40.08251953125
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "undo_calendar",
            "reference": [
              211.9090909090909,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "native": [
              211.90908813476562,
              555.07861328125,
              133.0,
              40.08252
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "undo_calendar_surface",
            "reference": [
              211.9090909090909,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "native": [
              211.90908813476562,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "undo_calendar_control",
            "reference": [
              211.9090909090909,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "native": [
              211.90908813476562,
              555.07861328125,
              133.0,
              40.08251953125
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "calendar_icon_2",
            "reference": [
              36.90909090909091,
              410.654296875,
              28.0,
              29.90283203125
            ],
            "native": [
              36.90909194946289,
              410.654296875,
              28.0,
              29.90283203125
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              8.272727272727273,
              623.1552734375,
              371.6363636363636,
              89.70849609375
            ],
            "native": [
              8.272727012634277,
              623.1552734375,
              371.6363525390625,
              89.70849609375
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              31.690909090909088,
              629.4666796875,
              66.88436363636363,
              66.8703671875
            ],
            "native": [
              31.690908432006836,
              629.4666748046875,
              66.88436126708984,
              66.87036895751953
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              41.236363636363635,
              641.55505859375,
              47.793454545454544,
              45.87476171875
            ],
            "native": [
              41.23636245727539,
              641.5550537109375,
              47.793453216552734,
              45.87476348876953
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              119.02545454545454,
              629.4666796875,
              66.88436363636363,
              66.8703671875
            ],
            "native": [
              119.02545166015625,
              629.4666748046875,
              66.88436126708984,
              66.87036895751953
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              206.35999999999999,
              629.4666796875,
              66.88436363636363,
              66.8703671875
            ],
            "native": [
              206.36000061035156,
              629.4666748046875,
              66.88436126708984,
              66.87036895751953
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              215.90545454545452,
              641.55505859375,
              47.793454545454544,
              45.87476171875
            ],
            "native": [
              215.90545654296875,
              641.5550537109375,
              47.793453216552734,
              45.87476348876953
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              293.6945454545454,
              629.4666796875,
              66.88436363636363,
              66.8703671875
            ],
            "native": [
              293.6945495605469,
              629.4666748046875,
              66.88436126708984,
              66.87036895751953
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              303.23999999999995,
              641.55505859375,
              47.793454545454544,
              45.87476171875
            ],
            "native": [
              303.239990234375,
              641.5550537109375,
              47.793453216552734,
              45.87476348876953
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "installation_booking",
            "second": "calendar_updated",
            "vertical_gap_reference": 10.81591796875,
            "vertical_gap_native": 10.81591796875,
            "left_alignment_delta": 0.0
          },
          {
            "first": "calendar_updated",
            "second": "dock",
            "vertical_gap_reference": 11.4521484375,
            "vertical_gap_native": 11.4521484375,
            "left_alignment_delta": -4.3348832790002234e-07
          },
          {
            "first": "wrench_icon_0",
            "second": "check_icon_1",
            "vertical_gap_reference": -24.81298828125,
            "vertical_gap_native": -24.81298828125,
            "left_alignment_delta": -9.363347828639235e-06
          },
          {
            "first": "check_icon_1",
            "second": "reschedule",
            "vertical_gap_reference": 126.60986328125,
            "vertical_gap_native": 126.60986328125,
            "left_alignment_delta": 1.2484463752571173e-05
          },
          {
            "first": "reschedule",
            "second": "cancel_booking",
            "vertical_gap_reference": -40.08251953125,
            "vertical_gap_native": -40.08252,
            "left_alignment_delta": -4.161487936471531e-06
          },
          {
            "first": "reschedule_surface",
            "second": "reschedule_control",
            "vertical_gap_reference": -40.08251953125,
            "vertical_gap_native": -40.08251953125,
            "left_alignment_delta": 0.0
          },
          {
            "first": "cancel_booking_surface",
            "second": "cancel_booking_control",
            "vertical_gap_reference": -40.08251953125,
            "vertical_gap_native": -40.08251953125,
            "left_alignment_delta": 0.0
          },
          {
            "first": "calendar_icon_2",
            "second": "acknowledge_calendar",
            "vertical_gap_reference": 114.521484375,
            "vertical_gap_native": 114.521484375,
            "left_alignment_delta": -6.935813203767793e-07
          },
          {
            "first": "acknowledge_calendar",
            "second": "undo_calendar",
            "vertical_gap_reference": -40.08251953125,
            "vertical_gap_native": -40.08252,
            "left_alignment_delta": -3.121115952353648e-06
          },
          {
            "first": "acknowledge_calendar_surface",
            "second": "acknowledge_calendar_control",
            "vertical_gap_reference": -40.08251953125,
            "vertical_gap_native": -40.08251953125,
            "left_alignment_delta": 0.0
          },
          {
            "first": "undo_calendar_surface",
            "second": "undo_calendar_control",
            "vertical_gap_reference": -40.08251953125,
            "vertical_gap_native": -40.08251953125,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -66.8703671875,
            "vertical_gap_native": -66.87036895751953,
            "left_alignment_delta": -2.226396034643585e-06
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -66.8703671875,
            "vertical_gap_native": -66.87036895751953,
            "left_alignment_delta": 3.495649863793915e-06
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -66.8703671875,
            "vertical_gap_native": -66.87036895751953,
            "left_alignment_delta": 3.495649906426479e-06
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -54.781988281249994,
            "vertical_gap_native": -54.78199005126953,
            "left_alignment_delta": -5.285089741846605e-06
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -45.87476171875,
            "vertical_gap_native": -45.87476348876953,
            "left_alignment_delta": 3.176602490384539e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -45.87476171875,
            "vertical_gap_native": -45.87476348876953,
            "left_alignment_delta": -1.176313918449523e-05
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-08/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-08/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-08/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-08/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-08/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-08/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/08.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-08/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-08/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-08/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-08/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 9,
      "id": "aircon-09",
      "title": "撤销日历分支",
      "description": "只撤销日历记录，安装预约仍然有效",
      "surface": "系统桌面",
      "branch": true,
      "base": "../cards/aircon-09/",
      "reference": "../cards/aircon-09/reference.png",
      "native": "../cards/aircon-09/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "efdc0e3a43ab42be848141c85889d84b"
      },
      "run": {
        "id": "aircon-09",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-09",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "8383229f684e811d47f09148bea2a574c8095a241ff419234e610358c8caee3e",
          "reference_sha256": "0fe18c17de7ef2bc5cbdfbb49a7bf092c363ac52cedd0942cc879ec597c2e68f",
          "id": "aircon-09",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "installation_booking",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "reschedule",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "reschedule_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "reschedule_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_32",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "cancel_booking",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "cancel_booking_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "cancel_booking_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_33",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "wrench_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "check_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_28",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_29",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_30",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_31",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "calendar_undone",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "restore_calendar",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "restore_calendar_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "restore_calendar_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_36",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "calendar_icon_2",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_34",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_35",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_27",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_37",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_38",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_39",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_41",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_42",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_217",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 5.985,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "0fe18c17de7ef2bc5cbdfbb49a7bf092c363ac52cedd0942cc879ec597c2e68f",
            "native_sha256": "06501e10f6ed630685bbc35663ec126ad5ef9db34f76921f740d47fbd2df8ada",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_32: text color",
          "text_33: text color",
          "text_28: text color",
          "text_31: text color",
          "text_36: text color",
          "text_34: text color",
          "text_35: text color",
          "text_37: text color",
          "text_38: text color",
          "text_39: text color",
          "text_41: text color",
          "text_42: text color",
          "text_217: text color"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              3.5,
              0.0,
              398.5,
              776.0
            ],
            "actual_bounds": [
              3.5,
              0.0,
              398.5,
              776.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "installation_booking",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              17.509765625,
              99.62688064192578,
              363.4755859375,
              259.9638916750251
            ],
            "actual_bounds": [
              17.509765625,
              99.62687683105469,
              363.4755859375,
              259.9638977050781
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "reschedule",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              39.302734375,
              291.09729187562687,
              140.09765625,
              49.035105315947845
            ],
            "actual_bounds": [
              39.302734375,
              291.0972900390625,
              140.09766,
              49.035107
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "改约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "reschedule_surface",
            "native_id": "beauty_0_0_0_0_0",
            "expected_bounds": [
              39.302734375,
              291.09729187562687,
              140.09765625,
              49.035105315947845
            ],
            "actual_bounds": [
              39.302734375,
              291.0972900390625,
              140.09765625,
              49.03510665893555
            ],
            "parent": "beauty_0_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "reschedule_control",
            "native_id": "beauty_0_0_0_0_1",
            "expected_bounds": [
              39.302734375,
              291.09729187562687,
              140.09765625,
              49.035105315947845
            ],
            "actual_bounds": [
              39.302734375,
              291.0972900390625,
              140.09765625,
              49.03510665893555
            ],
            "parent": "beauty_0_0_0_0",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_32",
            "native_id": "beauty_0_0_0_0_2",
            "expected_bounds": [
              88.96683696831789,
              305.8561628089514,
              46.11900005515402,
              22.5
            ],
            "actual_bounds": [
              88.96683502197266,
              305.8561706542969,
              46.119,
              22.5
            ],
            "parent": "beauty_0_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "改约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "cancel_booking",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              214.4248046875,
              291.09729187562687,
              137.7626953125,
              49.035105315947845
            ],
            "actual_bounds": [
              214.4248046875,
              291.0972900390625,
              137.7627,
              49.035107
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "取消预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "cancel_booking_surface",
            "native_id": "beauty_0_0_0_1_0",
            "expected_bounds": [
              214.4248046875,
              291.09729187562687,
              137.7626953125,
              49.035105315947845
            ],
            "actual_bounds": [
              214.4248046875,
              291.0972900390625,
              137.7626953125,
              49.03510665893555
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "cancel_booking_control",
            "native_id": "beauty_0_0_0_1_1",
            "expected_bounds": [
              214.4248046875,
              291.09729187562687,
              137.7626953125,
              49.035105315947845
            ],
            "actual_bounds": [
              214.4248046875,
              291.0972900390625,
              137.7626953125,
              49.03510665893555
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_33",
            "native_id": "beauty_0_0_0_1_2",
            "expected_bounds": [
              243.99813156044002,
              305.7243646139056,
              81.19214515561966,
              22.0
            ],
            "actual_bounds": [
              243.99813842773438,
              305.724365234375,
              81.19215,
              22.0
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "取消预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "wrench_icon_0",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              40.0810546875,
              118.30692076228686,
              30.3544921875,
              30.35506519558676
            ],
            "actual_bounds": [
              40.0810546875,
              118.30692291259766,
              30.3544921875,
              30.355064392089844
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "check_icon_1",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              337.3994140625,
              120.641925777332,
              22.5712890625,
              24.906720160481445
            ],
            "actual_bounds": [
              337.3994140625,
              120.64192199707031,
              22.5712890625,
              24.906719207763672
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_28",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              91.85095567320145,
              121.86689716433712,
              181.50661211151245,
              21.5
            ],
            "actual_bounds": [
              91.8509521484375,
              121.86689758300781,
              181.5066,
              21.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "安装服务 · 预约成功",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_29",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              39.83454699305079,
              170.42016010499472,
              63.737811236154705,
              21.5
            ],
            "actual_bounds": [
              39.83454513549805,
              170.420166015625,
              63.737812,
              21.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "王师傅",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_30",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              40.19585531753211,
              206.94808026501525,
              232.88145809638652,
              21.410385689798144
            ],
            "actual_bounds": [
              40.19585418701172,
              206.9480743408203,
              232.88145,
              21.410385
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "周六 9月19日 14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_31",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              38.82676834982547,
              241.99553488003536,
              131.90129491555695,
              20.0
            ],
            "actual_bounds": [
              38.82676696777344,
              241.9955291748047,
              131.90129,
              20.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "家 · 海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "calendar_undone",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              17.509765625,
              379.049147442327,
              364.25390625,
              196.14042126379138
            ],
            "actual_bounds": [
              17.509765625,
              379.04913330078125,
              364.25390625,
              196.1404266357422
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "restore_calendar",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              97.6767578125,
              507.47442326980945,
              181.3486328125,
              48.2567703109328
            ],
            "actual_bounds": [
              97.6767578125,
              507.47442626953125,
              181.34863,
              48.25677
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "KitButton",
            "visible": true,
            "text": "重新加入",
            "enabled": true,
            "issues": []
          },
          {
            "id": "restore_calendar_surface",
            "native_id": "beauty_0_0_1_0_0",
            "expected_bounds": [
              97.6767578125,
              507.47442326980945,
              181.3486328125,
              48.2567703109328
            ],
            "actual_bounds": [
              97.6767578125,
              507.47442626953125,
              181.3486328125,
              48.256771087646484
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "restore_calendar_control",
            "native_id": "beauty_0_0_1_0_1",
            "expected_bounds": [
              97.6767578125,
              507.47442326980945,
              181.3486328125,
              48.2567703109328
            ],
            "actual_bounds": [
              97.6767578125,
              507.47442626953125,
              181.3486328125,
              48.256771087646484
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_36",
            "native_id": "beauty_0_0_1_0_2",
            "expected_bounds": [
              142.39313998574434,
              521.3433031223599,
              85.57417477843913,
              22.172745022777203
            ],
            "actual_bounds": [
              142.3931427001953,
              521.3433227539062,
              85.57417,
              22.172745
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "Label",
            "visible": true,
            "text": "重新加入",
            "enabled": true,
            "issues": []
          },
          {
            "id": "calendar_icon_2",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              35.4111328125,
              400.0641925777332,
              35.0244140625,
              36.581745235707125
            ],
            "actual_bounds": [
              35.4111328125,
              400.0641784667969,
              35.0244140625,
              36.58174514770508
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_34",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              81.25160119405163,
              409.10850538132445,
              150.68208684178998,
              22.52977981086041
            ],
            "actual_bounds": [
              81.25160217285156,
              409.1085205078125,
              150.68208,
              22.52978
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "日历记录已撤销",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_35",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              38.23101318387023,
              452.2616800762366,
              143.0553763404198,
              20.0
            ],
            "actual_bounds": [
              38.231014251708984,
              452.2616882324219,
              143.05537,
              20.0
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "安装预约仍然有效",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              14.396484375,
              657.6930792377132,
              376.70703125,
              117.52858575727181
            ],
            "actual_bounds": [
              14.396484375,
              657.6930541992188,
              376.70703125,
              117.5285873413086
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_2_0",
            "expected_bounds": [
              37.20126953125,
              666.3481644934805,
              69.66278125000001,
              69.6640962888666
            ],
            "actual_bounds": [
              37.201271057128906,
              666.34814453125,
              69.66278076171875,
              69.66409301757812
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_2_1",
            "expected_bounds": [
              48.87607421875,
              681.1365295887663,
              46.313171875,
              43.979041123370116
            ],
            "actual_bounds": [
              48.876075744628906,
              681.1365356445312,
              46.31317138671875,
              43.979042053222656
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_2_2",
            "expected_bounds": [
              125.72742187499999,
              666.3481644934805,
              69.66278125000001,
              69.6640962888666
            ],
            "actual_bounds": [
              125.72742462158203,
              666.34814453125,
              69.66278076171875,
              69.66409301757812
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_2_3",
            "expected_bounds": [
              214.25357421874997,
              666.3481644934805,
              69.66278125000001,
              69.6640962888666
            ],
            "actual_bounds": [
              214.25357055664062,
              666.34814453125,
              69.66278076171875,
              69.66409301757812
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_2_4",
            "expected_bounds": [
              225.92837890624997,
              681.1365295887663,
              46.313171875,
              43.979041123370116
            ],
            "actual_bounds": [
              225.92837524414062,
              681.1365356445312,
              46.31317138671875,
              43.979042053222656
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_2_5",
            "expected_bounds": [
              302.7797265625,
              666.3481644934805,
              69.66278125000001,
              69.6640962888666
            ],
            "actual_bounds": [
              302.77972412109375,
              666.34814453125,
              69.66278076171875,
              69.66409301757812
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_2_6",
            "expected_bounds": [
              314.45453125,
              681.1365295887663,
              46.313171875,
              43.979041123370116
            ],
            "actual_bounds": [
              314.45452880859375,
              681.1365356445312,
              46.31317138671875,
              43.979042053222656
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_27",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              26.691060374434578,
              51.66754035590687,
              80.89972447377401,
              26.5
            ],
            "actual_bounds": [
              26.69106101989746,
              51.66754150390625,
              80.89973,
              26.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "15:29",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_37",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              131.93084901329843,
              690.0054133743763,
              35.3446938027046,
              26.5
            ],
            "actual_bounds": [
              131.93084716796875,
              690.0054321289062,
              35.344692,
              26.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "18",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_38",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              41.99176398075604,
              736.7037811684527,
              37.261770421076086,
              19.5
            ],
            "actual_bounds": [
              41.991764068603516,
              736.7037963867188,
              37.261772,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_39",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              131.47388154502744,
              737.2533553625083,
              36.84828317368723,
              18.0
            ],
            "actual_bounds": [
              131.473876953125,
              737.2533569335938,
              36.84828,
              18.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_41",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              229.3349211848798,
              736.3184274803706,
              35.781249363059516,
              19.5
            ],
            "actual_bounds": [
              229.3349151611328,
              736.3184204101562,
              35.78125,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_42",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              322.1522081304135,
              736.2437719341871,
              37.36923493376753,
              19.5
            ],
            "actual_bounds": [
              322.1522216796875,
              736.2437744140625,
              37.369236,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_217",
            "native_id": "beauty_0_0_9",
            "expected_bounds": [
              27.401174856923497,
              22.64020097352062,
              99.32234347599798,
              17.0
            ],
            "actual_bounds": [
              27.401174545288086,
              22.640201568603516,
              99.32234,
              17.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月18日 周五",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_32",
            "reference": [
              90.5,
              307.5,
              37.0,
              18.5
            ],
            "native": [
              90.5,
              307.5,
              37.0,
              18.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              86,
              115,
              95
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_33",
            "reference": [
              245.0,
              307.5,
              73.0,
              18.0
            ],
            "native": [
              245.0,
              307.5,
              73.0,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              111,
              115,
              113
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_28",
            "reference": [
              93.5,
              124.0,
              173.0,
              17.5
            ],
            "native": [
              93.5,
              123.5,
              172.5,
              17.0
            ],
            "delta": [
              0.0,
              -0.5,
              -0.5,
              -0.5
            ],
            "reference_color": [
              74,
              97,
              82
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_29",
            "reference": [
              41.0,
              172.0,
              56.0,
              17.5
            ],
            "native": [
              41.0,
              172.0,
              56.0,
              17.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              61,
              60,
              61
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_30",
            "reference": [
              41.0,
              209.0,
              225.0,
              17.0
            ],
            "native": [
              41.0,
              209.0,
              225.0,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              62,
              61,
              62
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_31",
            "reference": [
              40.5,
              244.0,
              123.0,
              16.0
            ],
            "native": [
              40.5,
              244.0,
              123.0,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              90,
              90,
              91
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_36",
            "reference": [
              143.5,
              523.0,
              77.5,
              18.0
            ],
            "native": [
              143.5,
              523.0,
              77.5,
              18.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              94,
              111,
              100
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_34",
            "reference": [
              85.0,
              411.0,
              140.0,
              18.5
            ],
            "native": [
              85.0,
              411.0,
              140.0,
              18.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              26,
              26,
              26
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_35",
            "reference": [
              39.5,
              454.0,
              135.0,
              16.0
            ],
            "native": [
              39.5,
              454.0,
              135.0,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              81,
              81,
              82
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_27",
            "reference": [
              29.5,
              53.5,
              71.0,
              22.5
            ],
            "native": [
              29.5,
              53.5,
              71.0,
              22.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              50,
              58,
              55
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_37",
            "reference": [
              134.5,
              691.5,
              26.5,
              22.5
            ],
            "native": [
              134.5,
              691.5,
              26.5,
              20.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -2.0
            ],
            "reference_color": [
              85,
              94,
              88
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_38",
            "reference": [
              43.5,
              738.0,
              30.0,
              15.5
            ],
            "native": [
              43.5,
              738.0,
              30.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              109,
              115,
              112
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_39",
            "reference": [
              134.5,
              739.0,
              27.5,
              14.0
            ],
            "native": [
              134.5,
              739.0,
              27.5,
              13.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              105,
              112,
              109
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_41",
            "reference": [
              230.0,
              738.0,
              29.0,
              15.5
            ],
            "native": [
              230.5,
              738.0,
              28.5,
              13.5
            ],
            "delta": [
              0.5,
              0.0,
              -0.5,
              -2.0
            ],
            "reference_color": [
              119,
              123,
              121
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_42",
            "reference": [
              323.0,
              738.0,
              30.0,
              15.5
            ],
            "native": [
              323.0,
              738.0,
              30.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              107,
              112,
              110
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_217",
            "reference": [
              28.0,
              24.5,
              92.0,
              13.0
            ],
            "native": [
              28.0,
              24.5,
              92.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              104,
              109,
              107
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              3.5,
              0.0,
              398.5,
              776.0
            ],
            "native": [
              3.5,
              0.0,
              398.5,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "installation_booking",
            "reference": [
              17.509765625,
              99.62688064192578,
              363.4755859375,
              259.9638916750251
            ],
            "native": [
              17.509765625,
              99.62687683105469,
              363.4755859375,
              259.9638977050781
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "reschedule",
            "reference": [
              39.302734375,
              291.09729187562687,
              140.09765625,
              49.035105315947845
            ],
            "native": [
              39.302734375,
              291.0972900390625,
              140.09766,
              49.035107
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "reschedule_surface",
            "reference": [
              39.302734375,
              291.09729187562687,
              140.09765625,
              49.035105315947845
            ],
            "native": [
              39.302734375,
              291.0972900390625,
              140.09765625,
              49.03510665893555
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "reschedule_control",
            "reference": [
              39.302734375,
              291.09729187562687,
              140.09765625,
              49.035105315947845
            ],
            "native": [
              39.302734375,
              291.0972900390625,
              140.09765625,
              49.03510665893555
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "cancel_booking",
            "reference": [
              214.4248046875,
              291.09729187562687,
              137.7626953125,
              49.035105315947845
            ],
            "native": [
              214.4248046875,
              291.0972900390625,
              137.7627,
              49.035107
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "cancel_booking_surface",
            "reference": [
              214.4248046875,
              291.09729187562687,
              137.7626953125,
              49.035105315947845
            ],
            "native": [
              214.4248046875,
              291.0972900390625,
              137.7626953125,
              49.03510665893555
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "cancel_booking_control",
            "reference": [
              214.4248046875,
              291.09729187562687,
              137.7626953125,
              49.035105315947845
            ],
            "native": [
              214.4248046875,
              291.0972900390625,
              137.7626953125,
              49.03510665893555
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "wrench_icon_0",
            "reference": [
              40.0810546875,
              118.30692076228686,
              30.3544921875,
              30.35506519558676
            ],
            "native": [
              40.0810546875,
              118.30692291259766,
              30.3544921875,
              30.355064392089844
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "check_icon_1",
            "reference": [
              337.3994140625,
              120.641925777332,
              22.5712890625,
              24.906720160481445
            ],
            "native": [
              337.3994140625,
              120.64192199707031,
              22.5712890625,
              24.906719207763672
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "calendar_undone",
            "reference": [
              17.509765625,
              379.049147442327,
              364.25390625,
              196.14042126379138
            ],
            "native": [
              17.509765625,
              379.04913330078125,
              364.25390625,
              196.1404266357422
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "restore_calendar",
            "reference": [
              97.6767578125,
              507.47442326980945,
              181.3486328125,
              48.2567703109328
            ],
            "native": [
              97.6767578125,
              507.47442626953125,
              181.34863,
              48.25677
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "restore_calendar_surface",
            "reference": [
              97.6767578125,
              507.47442326980945,
              181.3486328125,
              48.2567703109328
            ],
            "native": [
              97.6767578125,
              507.47442626953125,
              181.3486328125,
              48.256771087646484
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "restore_calendar_control",
            "reference": [
              97.6767578125,
              507.47442326980945,
              181.3486328125,
              48.2567703109328
            ],
            "native": [
              97.6767578125,
              507.47442626953125,
              181.3486328125,
              48.256771087646484
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "calendar_icon_2",
            "reference": [
              35.4111328125,
              400.0641925777332,
              35.0244140625,
              36.581745235707125
            ],
            "native": [
              35.4111328125,
              400.0641784667969,
              35.0244140625,
              36.58174514770508
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              14.396484375,
              657.6930792377132,
              376.70703125,
              117.52858575727181
            ],
            "native": [
              14.396484375,
              657.6930541992188,
              376.70703125,
              117.5285873413086
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              37.20126953125,
              666.3481644934805,
              69.66278125000001,
              69.6640962888666
            ],
            "native": [
              37.201271057128906,
              666.34814453125,
              69.66278076171875,
              69.66409301757812
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              48.87607421875,
              681.1365295887663,
              46.313171875,
              43.979041123370116
            ],
            "native": [
              48.876075744628906,
              681.1365356445312,
              46.31317138671875,
              43.979042053222656
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              125.72742187499999,
              666.3481644934805,
              69.66278125000001,
              69.6640962888666
            ],
            "native": [
              125.72742462158203,
              666.34814453125,
              69.66278076171875,
              69.66409301757812
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              214.25357421874997,
              666.3481644934805,
              69.66278125000001,
              69.6640962888666
            ],
            "native": [
              214.25357055664062,
              666.34814453125,
              69.66278076171875,
              69.66409301757812
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              225.92837890624997,
              681.1365295887663,
              46.313171875,
              43.979041123370116
            ],
            "native": [
              225.92837524414062,
              681.1365356445312,
              46.31317138671875,
              43.979042053222656
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              302.7797265625,
              666.3481644934805,
              69.66278125000001,
              69.6640962888666
            ],
            "native": [
              302.77972412109375,
              666.34814453125,
              69.66278076171875,
              69.66409301757812
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              314.45453125,
              681.1365295887663,
              46.313171875,
              43.979041123370116
            ],
            "native": [
              314.45452880859375,
              681.1365356445312,
              46.31317138671875,
              43.979042053222656
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "installation_booking",
            "second": "calendar_undone",
            "vertical_gap_reference": 19.458375125376165,
            "vertical_gap_native": 19.458358764648438,
            "left_alignment_delta": 0.0
          },
          {
            "first": "calendar_undone",
            "second": "dock",
            "vertical_gap_reference": 82.50351053159477,
            "vertical_gap_native": 82.50349426269531,
            "left_alignment_delta": 0.0
          },
          {
            "first": "wrench_icon_0",
            "second": "check_icon_1",
            "vertical_gap_reference": -28.02006018054162,
            "vertical_gap_native": -28.020065307617188,
            "left_alignment_delta": 0.0
          },
          {
            "first": "check_icon_1",
            "second": "reschedule",
            "vertical_gap_reference": 145.5486459378134,
            "vertical_gap_native": 145.54864883422852,
            "left_alignment_delta": 0.0
          },
          {
            "first": "reschedule",
            "second": "cancel_booking",
            "vertical_gap_reference": -49.035105315947845,
            "vertical_gap_native": -49.035107,
            "left_alignment_delta": 0.0
          },
          {
            "first": "reschedule_surface",
            "second": "reschedule_control",
            "vertical_gap_reference": -49.035105315947845,
            "vertical_gap_native": -49.03510665893555,
            "left_alignment_delta": 0.0
          },
          {
            "first": "cancel_booking_surface",
            "second": "cancel_booking_control",
            "vertical_gap_reference": -49.035105315947845,
            "vertical_gap_native": -49.03510665893555,
            "left_alignment_delta": 0.0
          },
          {
            "first": "calendar_icon_2",
            "second": "restore_calendar",
            "vertical_gap_reference": 70.82848545636912,
            "vertical_gap_native": 70.8285026550293,
            "left_alignment_delta": 0.0
          },
          {
            "first": "restore_calendar_surface",
            "second": "restore_calendar_control",
            "vertical_gap_reference": -48.2567703109328,
            "vertical_gap_native": -48.256771087646484,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -69.6640962888666,
            "vertical_gap_native": -69.66409301757812,
            "left_alignment_delta": 1.2207031261368684e-06
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -69.6640962888666,
            "vertical_gap_native": -69.66409301757812,
            "left_alignment_delta": -6.408691390902277e-06
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -69.6640962888666,
            "vertical_gap_native": -69.66409301757812,
            "left_alignment_delta": 1.220703097715159e-06
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -54.875731193580776,
            "vertical_gap_native": -54.875701904296875,
            "left_alignment_delta": 3.967285152839395e-06
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -43.979041123370116,
            "vertical_gap_native": -43.979042053222656,
            "left_alignment_delta": -5.187988250554554e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -43.979041123370116,
            "vertical_gap_native": -43.979042053222656,
            "left_alignment_delta": 1.220703097715159e-06
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-09/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-09/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-09/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-09/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-09/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-09/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/09.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-09/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-09/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-09/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-09/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 10,
      "id": "aircon-10",
      "title": "师傅即将到达",
      "description": "安装服务回传师傅的到达进度",
      "surface": "系统桌面",
      "branch": false,
      "base": "../cards/aircon-10/",
      "reference": "../cards/aircon-10/reference.png",
      "native": "../cards/aircon-10/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "378a7a1fb28f4d3bb9badcf0102b5c14"
      },
      "run": {
        "id": "aircon-10",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-10",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "5cc8fe7e412e607dc6b9c384b35bc18e0272450069058f9ef42838d616b27c47",
          "reference_sha256": "af860fb2d92987ff233281408cf1d1698069e3edd5c6e8363d606f4c7c831db3",
          "id": "aircon-10",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "installation_arriving",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "technician_portrait",
              "role": "photo",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Image"
              ],
              "actual_widget": "Image",
              "issues": [],
              "repair": "Use an original or separately generated image asset with documented crop, fit and clipping."
            },
            {
              "id": "divider_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "divider_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "contact_technician",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "contact_technician_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "contact_technician_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_95",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "view_booking",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "view_booking_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "view_booking_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_96",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "wrench_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "step_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "step_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "step_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "text_86",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_87",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_88",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_89",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_90",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_91",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_93",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_94",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_84",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_85",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_97",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_98",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_99",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_100",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_101",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 6.762,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "af860fb2d92987ff233281408cf1d1698069e3edd5c6e8363d606f4c7c831db3",
            "native_sha256": "d8d7f442bea5a2424171a957e682c5b3ff1e868938f3200ce893d2d74155f5a9",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_96: text color",
          "text_87: text color",
          "text_88: text color",
          "text_90: text color",
          "text_91: text color",
          "text_93: text color",
          "text_94: text color",
          "text_84: text color",
          "text_97: text color",
          "text_98: text color",
          "text_99: text color",
          "text_100: text color",
          "text_101: text color"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              0.0,
              0.0,
              405.5,
              776.0
            ],
            "actual_bounds": [
              0.0,
              0.0,
              405.5,
              776.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "installation_arriving",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              16.344529750479847,
              99.62688064192578,
              372.03262955854126,
              491.1293881644935
            ],
            "actual_bounds": [
              16.34453010559082,
              99.62687683105469,
              372.0326232910156,
              491.12939453125
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "technician_portrait",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              37.5,
              236.0,
              124.0,
              136.0
            ],
            "actual_bounds": [
              37.5,
              236.0,
              124.0,
              136.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Image",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_0",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              79.3877159309021,
              410.96088264794383,
              105.85028790786947,
              2.3350050150451356
            ],
            "actual_bounds": [
              79.3877182006836,
              410.96087646484375,
              105.85028839111328,
              2.335005044937134
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_1",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              203.1391554702495,
              410.96088264794383,
              110.52015355086371,
              2.3350050150451356
            ],
            "actual_bounds": [
              203.13916015625,
              410.96087646484375,
              110.52015686035156,
              2.335005044937134
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "contact_technician",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              38.13723608445297,
              519.9277833500502,
              150.21401151631477,
              49.035105315947845
            ],
            "actual_bounds": [
              38.137237548828125,
              519.9277954101562,
              150.214,
              49.035107
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "联系师傅",
            "enabled": true,
            "issues": []
          },
          {
            "id": "contact_technician_surface",
            "native_id": "beauty_0_0_0_3_0",
            "expected_bounds": [
              38.13723608445297,
              519.9277833500502,
              150.21401151631477,
              49.035105315947845
            ],
            "actual_bounds": [
              38.137237548828125,
              519.9277954101562,
              150.21400451660156,
              49.03510665893555
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "contact_technician_control",
            "native_id": "beauty_0_0_0_3_1",
            "expected_bounds": [
              38.13723608445297,
              519.9277833500502,
              150.21401151631477,
              49.035105315947845
            ],
            "actual_bounds": [
              38.137237548828125,
              519.9277954101562,
              150.21400451660156,
              49.03510665893555
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_95",
            "native_id": "beauty_0_0_0_3_2",
            "expected_bounds": [
              72.97682393380903,
              533.0496970057419,
              85.85338391524684,
              22.5
            ],
            "actual_bounds": [
              72.97682189941406,
              533.0496826171875,
              85.853386,
              22.5
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "Label",
            "visible": true,
            "text": "联系师傅",
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_booking",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              214.8138195777351,
              519.1494483450351,
              146.32245681381957,
              49.81344032096289
            ],
            "actual_bounds": [
              214.81381225585938,
              519.1494750976562,
              146.32246,
              49.81344
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "查看预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_booking_surface",
            "native_id": "beauty_0_0_0_4_0",
            "expected_bounds": [
              214.8138195777351,
              519.1494483450351,
              146.32245681381957,
              49.81344032096289
            ],
            "actual_bounds": [
              214.81381225585938,
              519.1494750976562,
              146.3224639892578,
              49.813438415527344
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_booking_control",
            "native_id": "beauty_0_0_0_4_1",
            "expected_bounds": [
              214.8138195777351,
              519.1494483450351,
              146.32245681381957,
              49.81344032096289
            ],
            "actual_bounds": [
              214.81381225585938,
              519.1494750976562,
              146.3224639892578,
              49.813438415527344
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_96",
            "native_id": "beauty_0_0_0_4_2",
            "expected_bounds": [
              248.08701174834712,
              533.5173935420881,
              82.27470304618164,
              21.5
            ],
            "actual_bounds": [
              248.08700561523438,
              533.5173950195312,
              82.274704,
              21.5
            ],
            "parent": "beauty_0_0_0_4",
            "widget_type": "Label",
            "visible": true,
            "text": "查看预约",
            "enabled": true,
            "issues": []
          },
          {
            "id": "wrench_icon_0",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              39.69385796545105,
              118.30692076228686,
              30.35412667946257,
              31.133400200601805
            ],
            "actual_bounds": [
              39.6938591003418,
              118.30692291259766,
              30.3541259765625,
              31.133399963378906
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_0",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              61.48656429942418,
              403.1775325977934,
              16.344529750479847,
              17.90170511534604
            ],
            "actual_bounds": [
              61.48656463623047,
              403.1775207519531,
              16.34453010559082,
              17.901704788208008
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_1",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              183.6813819577735,
              401.6208625877633,
              20.236084452975046,
              21.01504513540622
            ],
            "actual_bounds": [
              183.68138122558594,
              401.620849609375,
              20.236083984375,
              21.015045166015625
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "step_2",
            "native_id": "beauty_0_0_0_8",
            "expected_bounds": [
              312.8809980806142,
              402.39919759277836,
              17.901151631477926,
              19.45837512537613
            ],
            "actual_bounds": [
              312.8810119628906,
              402.3992004394531,
              17.901151657104492,
              19.458375930786133
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_86",
            "native_id": "beauty_0_0_0_9",
            "expected_bounds": [
              85.48185672400216,
              122.89785345331596,
              199.7293790329939,
              21.0
            ],
            "actual_bounds": [
              85.48185729980469,
              122.8978500366211,
              199.72939,
              21.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "安装服务 · 师傅在路上",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_87",
            "native_id": "beauty_0_0_0_10",
            "expected_bounds": [
              39.348000061833375,
              173.64159164711566,
              225.02684274108665,
              31.398821473644045
            ],
            "actual_bounds": [
              39.347999572753906,
              173.64158630371094,
              225.02684,
              31.39882
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "约20分钟后到达",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_88",
            "native_id": "beauty_0_0_0_11",
            "expected_bounds": [
              184.27761572220004,
              257.7157631316194,
              68.56495054394941,
              22.5
            ],
            "actual_bounds": [
              184.27761840820312,
              257.71575927734375,
              68.56495,
              22.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "王师傅",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_89",
            "native_id": "beauty_0_0_0_12",
            "expected_bounds": [
              184.68660762353616,
              296.3939795401268,
              157.12054978617692,
              21.081135078496413
            ],
            "actual_bounds": [
              184.68661499023438,
              296.39398193359375,
              157.12054,
              21.081135
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "今天 14:00-16:00",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_90",
            "native_id": "beauty_0_0_0_13",
            "expected_bounds": [
              183.8986408389538,
              335.09665415817045,
              135.3572723792575,
              19.719638109143293
            ],
            "actual_bounds": [
              183.8986358642578,
              335.0966491699219,
              135.35727,
              19.719639
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "家 · 海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_91",
            "native_id": "beauty_0_0_0_14",
            "expected_bounds": [
              39.20886601459699,
              436.4620555401913,
              73.41498326384725,
              19.5
            ],
            "actual_bounds": [
              39.208866119384766,
              436.4620666503906,
              73.414986,
              19.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "预约成功",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_93",
            "native_id": "beauty_0_0_0_15",
            "expected_bounds": [
              161.45475018305098,
              436.2288074565052,
              75.2748204308162,
              19.5
            ],
            "actual_bounds": [
              161.4547576904297,
              436.22882080078125,
              75.27482,
              19.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "正在前往",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_94",
            "native_id": "beauty_0_0_0_16",
            "expected_bounds": [
              290.28295752202547,
              436.37544954039504,
              72.57637529694478,
              19.5
            ],
            "actual_bounds": [
              290.282958984375,
              436.3754577636719,
              72.57638,
              19.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "安装完成",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              6.226487523992322,
              656.9147442326981,
              389.15547024952014,
              118.30692076228686
            ],
            "actual_bounds": [
              6.226487636566162,
              656.9147338867188,
              389.15545654296875,
              118.30692291259766
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              29.96497120921305,
              665.6632296890672,
              71.6046065259117,
              71.60682046138416
            ],
            "actual_bounds": [
              29.9649715423584,
              665.6632080078125,
              71.60460662841797,
              71.60681915283203
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              41.63963531669865,
              680.4515947843531,
              48.2552783109405,
              45.92176529588767
            ],
            "actual_bounds": [
              41.6396369934082,
              680.4515991210938,
              48.255279541015625,
              45.9217643737793
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              121.41650671785028,
              665.6632296890672,
              71.6046065259117,
              71.60682046138416
            ],
            "actual_bounds": [
              121.41650390625,
              665.6632080078125,
              71.60460662841797,
              71.60681915283203
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              212.86804222648746,
              665.6632296890672,
              71.6046065259117,
              71.60682046138416
            ],
            "actual_bounds": [
              212.8680419921875,
              665.6632080078125,
              71.60460662841797,
              71.60681915283203
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_1_4",
            "expected_bounds": [
              224.54270633397306,
              680.4515947843531,
              48.2552783109405,
              45.92176529588767
            ],
            "actual_bounds": [
              224.54270935058594,
              680.4515991210938,
              48.255279541015625,
              45.9217643737793
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_1_5",
            "expected_bounds": [
              304.3195777351247,
              665.6632296890672,
              71.6046065259117,
              71.60682046138416
            ],
            "actual_bounds": [
              304.319580078125,
              665.6632080078125,
              71.60460662841797,
              71.60681915283203
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_1_6",
            "expected_bounds": [
              315.9942418426103,
              680.4515947843531,
              48.2552783109405,
              45.92176529588767
            ],
            "actual_bounds": [
              315.9942321777344,
              680.4515991210938,
              48.255279541015625,
              45.9217643737793
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_84",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              25.569789228447448,
              22.521626766019835,
              102.73512904980495,
              17.521378435196187
            ],
            "actual_bounds": [
              25.56978988647461,
              22.52162742614746,
              102.73513,
              17.521378
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月19日 周六",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_85",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              25.388270879864535,
              51.69809705922267,
              84.80804518819663,
              27.0
            ],
            "actual_bounds": [
              25.38827133178711,
              51.698097229003906,
              84.808044,
              27.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "13:40",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_97",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              36.072180341689545,
              739.6275049940394,
              37.26138287315359,
              19.5
            ],
            "actual_bounds": [
              36.072181701660156,
              739.6275024414062,
              37.261383,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_98",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              128.91862701045872,
              692.3915426892595,
              35.597144273552345,
              26.5
            ],
            "actual_bounds": [
              128.9186248779297,
              692.3915405273438,
              35.597145,
              26.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "19",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_99",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              128.5377577686939,
              740.2075007233096,
              36.21430372987421,
              18.0
            ],
            "actual_bounds": [
              128.53775024414062,
              740.20751953125,
              36.214302,
              18.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_100",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              228.2319412302316,
              739.3927466542991,
              36.90941689672966,
              19.0
            ],
            "actual_bounds": [
              228.23194885253906,
              739.3927612304688,
              36.909416,
              19.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_101",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              325.10362095913007,
              739.3700935648841,
              37.45057510217377,
              19.5
            ],
            "actual_bounds": [
              325.1036071777344,
              739.3701171875,
              37.450577,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_95",
            "reference": [
              74.0,
              535.0,
              78.0,
              18.5
            ],
            "native": [
              74.0,
              535.0,
              78.0,
              18.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              241,
              246,
              243
            ],
            "native_color": [
              255,
              255,
              255
            ],
            "issues": []
          },
          {
            "id": "text_96",
            "reference": [
              249.0,
              535.5,
              74.0,
              17.5
            ],
            "native": [
              249.0,
              535.5,
              74.0,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              84,
              107,
              91
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_86",
            "reference": [
              87.0,
              124.5,
              191.5,
              17.0
            ],
            "native": [
              87.0,
              124.5,
              191.5,
              16.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              51,
              51,
              51
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_87",
            "reference": [
              40.5,
              175.5,
              217.0,
              27.0
            ],
            "native": [
              40.5,
              175.5,
              216.5,
              27.0
            ],
            "delta": [
              0.0,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              27,
              26,
              26
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_88",
            "reference": [
              185.5,
              259.5,
              60.5,
              18.5
            ],
            "native": [
              185.5,
              259.5,
              60.5,
              18.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              29,
              29,
              29
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_89",
            "reference": [
              185.5,
              298.0,
              149.5,
              17.0
            ],
            "native": [
              186.0,
              298.0,
              149.0,
              17.0
            ],
            "delta": [
              0.5,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              65,
              66,
              66
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_90",
            "reference": [
              185.5,
              337.0,
              126.5,
              15.5
            ],
            "native": [
              185.5,
              337.0,
              126.5,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              90,
              89,
              90
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_91",
            "reference": [
              40.0,
              438.0,
              66.0,
              15.5
            ],
            "native": [
              40.0,
              438.0,
              66.0,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              79,
              79,
              78
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_93",
            "reference": [
              162.5,
              438.0,
              67.5,
              15.5
            ],
            "native": [
              162.5,
              438.0,
              67.5,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              72,
              110,
              78
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_94",
            "reference": [
              291.5,
              438.0,
              65.0,
              15.5
            ],
            "native": [
              291.5,
              438.0,
              65.0,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              88,
              88,
              89
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_84",
            "reference": [
              26.5,
              24.5,
              95.5,
              13.5
            ],
            "native": [
              26.5,
              24.5,
              95.5,
              13.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              102,
              107,
              105
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_85",
            "reference": [
              28.0,
              53.5,
              75.0,
              23.0
            ],
            "native": [
              28.0,
              53.5,
              75.0,
              23.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              49,
              59,
              55
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_97",
            "reference": [
              37.5,
              741.0,
              30.0,
              15.5
            ],
            "native": [
              37.5,
              741.0,
              30.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              112,
              118,
              116
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_98",
            "reference": [
              131.5,
              694.0,
              26.5,
              22.5
            ],
            "native": [
              131.5,
              694.0,
              26.5,
              20.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -2.0
            ],
            "reference_color": [
              82,
              91,
              85
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_99",
            "reference": [
              131.5,
              742.0,
              27.0,
              14.0
            ],
            "native": [
              131.5,
              742.0,
              27.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              91,
              98,
              95
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_100",
            "reference": [
              229.0,
              741.0,
              29.5,
              15.0
            ],
            "native": [
              229.0,
              741.0,
              29.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              114,
              118,
              116
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_101",
            "reference": [
              326.0,
              741.0,
              30.5,
              15.5
            ],
            "native": [
              326.0,
              741.0,
              30.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              128,
              133,
              131
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              0.0,
              0.0,
              405.5,
              776.0
            ],
            "native": [
              0.0,
              0.0,
              405.5,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "installation_arriving",
            "reference": [
              16.344529750479847,
              99.62688064192578,
              372.03262955854126,
              491.1293881644935
            ],
            "native": [
              16.34453010559082,
              99.62687683105469,
              372.0326232910156,
              491.12939453125
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "technician_portrait",
            "reference": [
              37.5,
              236.0,
              124.0,
              136.0
            ],
            "native": [
              37.5,
              236.0,
              124.0,
              136.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "divider_0",
            "reference": [
              79.3877159309021,
              410.96088264794383,
              105.85028790786947,
              2.3350050150451356
            ],
            "native": [
              79.3877182006836,
              410.96087646484375,
              105.85028839111328,
              2.335005044937134
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "divider_1",
            "reference": [
              203.1391554702495,
              410.96088264794383,
              110.52015355086371,
              2.3350050150451356
            ],
            "native": [
              203.13916015625,
              410.96087646484375,
              110.52015686035156,
              2.335005044937134
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "contact_technician",
            "reference": [
              38.13723608445297,
              519.9277833500502,
              150.21401151631477,
              49.035105315947845
            ],
            "native": [
              38.137237548828125,
              519.9277954101562,
              150.214,
              49.035107
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "contact_technician_surface",
            "reference": [
              38.13723608445297,
              519.9277833500502,
              150.21401151631477,
              49.035105315947845
            ],
            "native": [
              38.137237548828125,
              519.9277954101562,
              150.21400451660156,
              49.03510665893555
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "contact_technician_control",
            "reference": [
              38.13723608445297,
              519.9277833500502,
              150.21401151631477,
              49.035105315947845
            ],
            "native": [
              38.137237548828125,
              519.9277954101562,
              150.21400451660156,
              49.03510665893555
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "view_booking",
            "reference": [
              214.8138195777351,
              519.1494483450351,
              146.32245681381957,
              49.81344032096289
            ],
            "native": [
              214.81381225585938,
              519.1494750976562,
              146.32246,
              49.81344
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "view_booking_surface",
            "reference": [
              214.8138195777351,
              519.1494483450351,
              146.32245681381957,
              49.81344032096289
            ],
            "native": [
              214.81381225585938,
              519.1494750976562,
              146.3224639892578,
              49.813438415527344
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "view_booking_control",
            "reference": [
              214.8138195777351,
              519.1494483450351,
              146.32245681381957,
              49.81344032096289
            ],
            "native": [
              214.81381225585938,
              519.1494750976562,
              146.3224639892578,
              49.813438415527344
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "wrench_icon_0",
            "reference": [
              39.69385796545105,
              118.30692076228686,
              30.35412667946257,
              31.133400200601805
            ],
            "native": [
              39.6938591003418,
              118.30692291259766,
              30.3541259765625,
              31.133399963378906
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_0",
            "reference": [
              61.48656429942418,
              403.1775325977934,
              16.344529750479847,
              17.90170511534604
            ],
            "native": [
              61.48656463623047,
              403.1775207519531,
              16.34453010559082,
              17.901704788208008
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "step_1",
            "reference": [
              183.6813819577735,
              401.6208625877633,
              20.236084452975046,
              21.01504513540622
            ],
            "native": [
              183.68138122558594,
              401.620849609375,
              20.236083984375,
              21.015045166015625
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "step_2",
            "reference": [
              312.8809980806142,
              402.39919759277836,
              17.901151631477926,
              19.45837512537613
            ],
            "native": [
              312.8810119628906,
              402.3992004394531,
              17.901151657104492,
              19.458375930786133
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              6.226487523992322,
              656.9147442326981,
              389.15547024952014,
              118.30692076228686
            ],
            "native": [
              6.226487636566162,
              656.9147338867188,
              389.15545654296875,
              118.30692291259766
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              29.96497120921305,
              665.6632296890672,
              71.6046065259117,
              71.60682046138416
            ],
            "native": [
              29.9649715423584,
              665.6632080078125,
              71.60460662841797,
              71.60681915283203
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              41.63963531669865,
              680.4515947843531,
              48.2552783109405,
              45.92176529588767
            ],
            "native": [
              41.6396369934082,
              680.4515991210938,
              48.255279541015625,
              45.9217643737793
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              121.41650671785028,
              665.6632296890672,
              71.6046065259117,
              71.60682046138416
            ],
            "native": [
              121.41650390625,
              665.6632080078125,
              71.60460662841797,
              71.60681915283203
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              212.86804222648746,
              665.6632296890672,
              71.6046065259117,
              71.60682046138416
            ],
            "native": [
              212.8680419921875,
              665.6632080078125,
              71.60460662841797,
              71.60681915283203
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              224.54270633397306,
              680.4515947843531,
              48.2552783109405,
              45.92176529588767
            ],
            "native": [
              224.54270935058594,
              680.4515991210938,
              48.255279541015625,
              45.9217643737793
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              304.3195777351247,
              665.6632296890672,
              71.6046065259117,
              71.60682046138416
            ],
            "native": [
              304.319580078125,
              665.6632080078125,
              71.60460662841797,
              71.60681915283203
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              315.9942418426103,
              680.4515947843531,
              48.2552783109405,
              45.92176529588767
            ],
            "native": [
              315.9942321777344,
              680.4515991210938,
              48.255279541015625,
              45.9217643737793
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "installation_arriving",
            "second": "dock",
            "vertical_gap_reference": 66.15847542627881,
            "vertical_gap_native": 66.15846252441406,
            "left_alignment_delta": -2.4253713348798556e-07
          },
          {
            "first": "wrench_icon_0",
            "second": "technician_portrait",
            "vertical_gap_reference": 86.55967903711132,
            "vertical_gap_native": 86.55967712402344,
            "left_alignment_delta": -1.1348907449360013e-06
          },
          {
            "first": "technician_portrait",
            "second": "step_1",
            "vertical_gap_reference": 29.620862587763327,
            "vertical_gap_native": 29.620849609375,
            "left_alignment_delta": -7.321875727939187e-07
          },
          {
            "first": "step_1",
            "second": "step_2",
            "vertical_gap_reference": -20.23671013039118,
            "vertical_gap_native": -20.2366943359375,
            "left_alignment_delta": 1.4614464021178719e-05
          },
          {
            "first": "step_2",
            "second": "step_0",
            "vertical_gap_reference": -18.68004012036109,
            "vertical_gap_native": -18.680055618286133,
            "left_alignment_delta": -1.3545470153530914e-05
          },
          {
            "first": "step_0",
            "second": "divider_0",
            "vertical_gap_reference": -10.118355065195608,
            "vertical_gap_native": -10.118349075317383,
            "left_alignment_delta": 1.9329752021235436e-06
          },
          {
            "first": "divider_0",
            "second": "divider_1",
            "vertical_gap_reference": -2.3350050150451356,
            "vertical_gap_native": -2.335005044937134,
            "left_alignment_delta": 2.4162190044307863e-06
          },
          {
            "first": "divider_1",
            "second": "view_booking",
            "vertical_gap_reference": 105.85356068204615,
            "vertical_gap_native": 105.85359358787537,
            "left_alignment_delta": -1.2007876222241975e-05
          },
          {
            "first": "view_booking",
            "second": "contact_technician",
            "vertical_gap_reference": -49.03510531594785,
            "vertical_gap_native": -49.0351196875,
            "left_alignment_delta": 8.786250873527024e-06
          },
          {
            "first": "contact_technician_surface",
            "second": "contact_technician_control",
            "vertical_gap_reference": -49.035105315947845,
            "vertical_gap_native": -49.03510665893555,
            "left_alignment_delta": 0.0
          },
          {
            "first": "view_booking_surface",
            "second": "view_booking_control",
            "vertical_gap_reference": -49.81344032096289,
            "vertical_gap_native": -49.813438415527344,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -71.60682046138416,
            "vertical_gap_native": -71.60681915283203,
            "left_alignment_delta": -3.1447456336763935e-06
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -71.60682046138416,
            "vertical_gap_native": -71.60681915283203,
            "left_alignment_delta": 2.5773003216045254e-06
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -71.60682046138416,
            "vertical_gap_native": -71.60681915283203,
            "left_alignment_delta": 2.577300250550252e-06
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -56.81845536609822,
            "vertical_gap_native": -56.81842803955078,
            "left_alignment_delta": -6.662907594545686e-07
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -45.92176529588767,
            "vertical_gap_native": -45.9217643737793,
            "left_alignment_delta": 1.339903320740632e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -45.92176529588767,
            "vertical_gap_native": -45.9217643737793,
            "left_alignment_delta": -1.2681488783528039e-05
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-10/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-10/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-10/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-10/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-10/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-10/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/10.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-10/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-10/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-10/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-10/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 11,
      "id": "aircon-11",
      "title": "材料费待支付",
      "description": "根据安装服务单呈现支付卡，尚未扣款",
      "surface": "系统桌面",
      "branch": false,
      "base": "../cards/aircon-11/",
      "reference": "../cards/aircon-11/reference.png",
      "native": "../cards/aircon-11/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "f9a71ba4132644599b7c8106197b28e3"
      },
      "run": {
        "id": "aircon-11",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-11",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "1661addf1e25c9a5445efd34d1d481ca4a57f4e33baaf88390dc6777f68581d4",
          "reference_sha256": "e1549e4ad205c4376b7ee0ff77e6ba3f5c39b9ce61fa8f0e30f989503afd5c1a",
          "id": "aircon-11",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "payment_due",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "divider_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "source_service_order",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "source_service_order_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "source_service_order_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_146",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "pay_materials",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "pay_materials_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "pay_materials_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_148",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "withdraw_payment_request",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "withdraw_payment_request_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "withdraw_payment_request_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_149",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "wallet_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_141",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_142",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_143",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_144",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_145",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_147",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "installation_complete",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "report_installation_issue",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "report_installation_issue_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "report_installation_issue_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_152",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "wrench_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_150",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_151",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_139",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_140",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_153",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_154",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_155",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_157",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_158",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 7.714,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "e1549e4ad205c4376b7ee0ff77e6ba3f5c39b9ce61fa8f0e30f989503afd5c1a",
            "native_sha256": "e30eaf7a431b587582a5aaeb25fcb5e629b5d7667f3f5874dd107b7fde986e61",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_146: text color",
          "text_149: reference text missing or OCR unresolved",
          "text_142: text color",
          "text_143: text ink dimensions",
          "text_143: text color",
          "text_144: text color",
          "text_145: reference OCR text differs",
          "text_145: text ink position",
          "text_145: text ink dimensions",
          "text_145: text color",
          "text_147: text color",
          "text_152: text color",
          "text_151: reference OCR text differs",
          "text_151: text ink position",
          "text_151: text ink dimensions",
          "text_151: text color",
          "text_139: text color",
          "text_153: text color",
          "text_154: text color",
          "text_155: text color",
          "text_157: text color",
          "text_158: text color",
          "1 extra reference text observations need classification"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              2.5,
              0.0,
              400.5,
              776.0
            ],
            "actual_bounds": [
              2.5,
              0.0,
              400.5,
              776.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "payment_due",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              16.498058252427185,
              97.97194388777555,
              356.95048543689325,
              356.8977955911824
            ],
            "actual_bounds": [
              16.498058319091797,
              97.9719467163086,
              356.95050048828125,
              356.8977966308594
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_0",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              39.050485436893204,
              265.14629258517033,
              311.06796116504853,
              0.7775551102204409
            ],
            "actual_bounds": [
              39.05048370361328,
              265.14630126953125,
              311.0679626464844,
              0.7775551080703735
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "source_service_order",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              35.93980582524272,
              350.67735470941886,
              98.76407766990292,
              26.43687374749499
            ],
            "actual_bounds": [
              35.93980407714844,
              350.6773681640625,
              98.76408,
              26.436874
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "安装服务单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "source_service_order_surface",
            "native_id": "beauty_0_0_0_1_0",
            "expected_bounds": [
              35.93980582524272,
              350.67735470941886,
              98.76407766990292,
              26.43687374749499
            ],
            "actual_bounds": [
              35.93980407714844,
              350.6773681640625,
              98.76408,
              26.436874
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "source_service_order_control",
            "native_id": "beauty_0_0_0_1_1",
            "expected_bounds": [
              35.93980582524272,
              350.67735470941886,
              98.76407766990292,
              26.43687374749499
            ],
            "actual_bounds": [
              35.93980407714844,
              350.6773681640625,
              98.76407623291016,
              26.436874389648438
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_146",
            "native_id": "beauty_0_0_0_1_2",
            "expected_bounds": [
              38.30259765182331,
              354.5633177006692,
              93.11975763474443,
              19.783169732148284
            ],
            "actual_bounds": [
              38.30259704589844,
              354.5633239746094,
              93.11976,
              19.783169
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "安装服务单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "pay_materials",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              35.1621359223301,
              390.3326653306613,
              168.75436893203883,
              45.875751503006015
            ],
            "actual_bounds": [
              35.16213607788086,
              390.3326721191406,
              168.75436,
              45.87575
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "支付 ¥130",
            "enabled": true,
            "issues": []
          },
          {
            "id": "pay_materials_surface",
            "native_id": "beauty_0_0_0_2_0",
            "expected_bounds": [
              35.1621359223301,
              390.3326653306613,
              168.75436893203883,
              45.875751503006015
            ],
            "actual_bounds": [
              35.16213607788086,
              390.3326721191406,
              168.75436401367188,
              45.87575149536133
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "pay_materials_control",
            "native_id": "beauty_0_0_0_2_1",
            "expected_bounds": [
              35.1621359223301,
              390.3326653306613,
              168.75436893203883,
              45.875751503006015
            ],
            "actual_bounds": [
              35.16213607788086,
              390.3326721191406,
              168.75436401367188,
              45.87575149536133
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_148",
            "native_id": "beauty_0_0_0_2_2",
            "expected_bounds": [
              71.06501600047615,
              402.905450839493,
              94.41889724768603,
              21.5
            ],
            "actual_bounds": [
              71.06501770019531,
              402.90545654296875,
              94.4189,
              21.5
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Label",
            "visible": true,
            "text": "支付 ¥130",
            "enabled": true,
            "issues": []
          },
          {
            "id": "withdraw_payment_request",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              224.1359223300971,
              389.5551102204409,
              131.426213592233,
              45.875751503006015
            ],
            "actual_bounds": [
              224.13592529296875,
              389.55511474609375,
              131.42621,
              45.87575
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "撤销",
            "enabled": true,
            "issues": []
          },
          {
            "id": "withdraw_payment_request_surface",
            "native_id": "beauty_0_0_0_3_0",
            "expected_bounds": [
              224.1359223300971,
              389.5551102204409,
              131.426213592233,
              45.875751503006015
            ],
            "actual_bounds": [
              224.13592529296875,
              389.55511474609375,
              131.42620849609375,
              45.87575149536133
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "withdraw_payment_request_control",
            "native_id": "beauty_0_0_0_3_1",
            "expected_bounds": [
              224.1359223300971,
              389.5551102204409,
              131.426213592233,
              45.875751503006015
            ],
            "actual_bounds": [
              224.13592529296875,
              389.55511474609375,
              131.42620849609375,
              45.87575149536133
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_149",
            "native_id": "beauty_0_0_0_3_2",
            "expected_bounds": [
              263.20205070992233,
              402.2303633403552,
              48.7637376538389,
              24.79275614020817
            ],
            "actual_bounds": [
              263.2020568847656,
              402.2303771972656,
              48.763737,
              24.792757
            ],
            "parent": "beauty_0_0_0_3",
            "widget_type": "Label",
            "visible": true,
            "text": "撤销",
            "enabled": true,
            "issues": []
          },
          {
            "id": "wallet_icon_0",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              39.828155339805825,
              115.85571142284569,
              34.21747572815534,
              31.879759519038075
            ],
            "actual_bounds": [
              39.828155517578125,
              115.855712890625,
              34.21747589111328,
              31.879758834838867
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_141",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              90.68387359988026,
              121.91826134723608,
              119.45370744069909,
              21.5
            ],
            "actual_bounds": [
              90.68387603759766,
              121.91825866699219,
              119.453705,
              21.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付 · 待付款",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_142",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              38.76734450892006,
              170.0456650030288,
              176.0658356128433,
              26.000810484334245
            ],
            "actual_bounds": [
              38.7673454284668,
              170.04566955566406,
              176.06584,
              26.00081
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "空调安装材料费",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_143",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              41.561116585017494,
              213.76278201206077,
              103.20344839203044,
              36.0
            ],
            "actual_bounds": [
              41.56111526489258,
              213.76278686523438,
              103.203445,
              36.0
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "¥130",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_144",
            "native_id": "beauty_0_0_0_8",
            "expected_bounds": [
              38.83363601508717,
              279.5312118574727,
              109.96688220069765,
              20.5
            ],
            "actual_bounds": [
              38.83363723754883,
              279.5312194824219,
              109.96688,
              20.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "加长铜管 2米",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_145",
            "native_id": "beauty_0_0_0_9",
            "expected_bounds": [
              32.46124586817716,
              322.1216452731917,
              189.12769066394827,
              21.235388000813582
            ],
            "actual_bounds": [
              32.461246490478516,
              322.12164306640625,
              189.12769,
              21.235388
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "收款方：安装服务团队",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_147",
            "native_id": "beauty_0_0_0_10",
            "expected_bounds": [
              303.72033967970435,
              281.83885193135814,
              49.04118494517118,
              17.5
            ],
            "actual_bounds": [
              303.7203369140625,
              281.8388671875,
              49.041183,
              17.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "¥130",
            "enabled": true,
            "issues": []
          },
          {
            "id": "installation_complete",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              16.498058252427185,
              468.86573146292585,
              356.95048543689325,
              171.06212424849699
            ],
            "actual_bounds": [
              16.498058319091797,
              468.86572265625,
              356.95050048828125,
              171.06211853027344
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "report_installation_issue",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              103.59708737864078,
              571.503006012024,
              177.30873786407767,
              45.098196392785574
            ],
            "actual_bounds": [
              103.59708404541016,
              571.5029907226562,
              177.30873,
              45.098198
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "KitButton",
            "visible": true,
            "text": "反馈问题",
            "enabled": true,
            "issues": []
          },
          {
            "id": "report_installation_issue_surface",
            "native_id": "beauty_0_0_1_0_0",
            "expected_bounds": [
              103.59708737864078,
              571.503006012024,
              177.30873786407767,
              45.098196392785574
            ],
            "actual_bounds": [
              103.59708404541016,
              571.5029907226562,
              177.30873107910156,
              45.09819793701172
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "report_installation_issue_control",
            "native_id": "beauty_0_0_1_0_1",
            "expected_bounds": [
              103.59708737864078,
              571.503006012024,
              177.30873786407767,
              45.098196392785574
            ],
            "actual_bounds": [
              103.59708404541016,
              571.5029907226562,
              177.30873107910156,
              45.09819793701172
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_152",
            "native_id": "beauty_0_0_1_0_2",
            "expected_bounds": [
              148.68765012025264,
              585.3721686482476,
              84.66625560338338,
              21.0
            ],
            "actual_bounds": [
              148.68765258789062,
              585.3721923828125,
              84.66625,
              21.0
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "Label",
            "visible": true,
            "text": "反馈问题",
            "enabled": true,
            "issues": []
          },
          {
            "id": "wrench_icon_1",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              36.71747572815534,
              489.85971943887773,
              29.55145631067961,
              31.879759519038075
            ],
            "actual_bounds": [
              36.71747589111328,
              489.8597106933594,
              29.551456451416016,
              31.879758834838867
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_150",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              88.06974980034023,
              495.09936486938693,
              200.55014708559645,
              21.5
            ],
            "actual_bounds": [
              88.06974792480469,
              495.099365234375,
              200.55014,
              21.5
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "安装服务 · 安装已完成",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_151",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              32.50059452253676,
              535.2726836007225,
              139.04410913395708,
              20.563361890338477
            ],
            "actual_bounds": [
              32.50059509277344,
              535.272705078125,
              139.04411,
              20.563362
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "家 · 海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              12.609708737864079,
              658.5891783567134,
              378.7252427184466,
              115.85571142284569
            ],
            "actual_bounds": [
              12.609708786010742,
              658.5891723632812,
              378.7252502441406,
              115.855712890625
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_2_0",
            "expected_bounds": [
              35.570412621359225,
              667.0489779559118,
              69.96851650485436,
              69.9581883767535
            ],
            "actual_bounds": [
              35.570411682128906,
              667.0489501953125,
              69.96851348876953,
              69.95819091796875
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_2_1",
            "expected_bounds": [
              47.23546116504854,
              681.8225250501002,
              46.638419417475724,
              44.29886973947895
            ],
            "actual_bounds": [
              47.2354621887207,
              681.822509765625,
              46.63842010498047,
              44.29887008666992
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_2_2",
            "expected_bounds": [
              124.57084466019418,
              667.0489779559118,
              69.96851650485436,
              69.9581883767535
            ],
            "actual_bounds": [
              124.57084655761719,
              667.0489501953125,
              69.96851348876953,
              69.95819091796875
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_2_3",
            "expected_bounds": [
              213.5712766990291,
              667.0489779559118,
              69.96851650485436,
              69.9581883767535
            ],
            "actual_bounds": [
              213.57127380371094,
              667.0489501953125,
              69.96851348876953,
              69.95819091796875
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_2_4",
            "expected_bounds": [
              225.23632524271844,
              681.8225250501002,
              46.638419417475724,
              44.29886973947895
            ],
            "actual_bounds": [
              225.236328125,
              681.822509765625,
              46.63842010498047,
              44.29887008666992
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_2_5",
            "expected_bounds": [
              302.57170873786407,
              667.0489779559118,
              69.96851650485436,
              69.9581883767535
            ],
            "actual_bounds": [
              302.57171630859375,
              667.0489501953125,
              69.96851348876953,
              69.95819091796875
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_2_6",
            "expected_bounds": [
              314.23675728155337,
              681.8225250501002,
              46.638419417475724,
              44.29886973947895
            ],
            "actual_bounds": [
              314.23675537109375,
              681.822509765625,
              46.63842010498047,
              44.29887008666992
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_139",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              31.170185151088088,
              24.187642064553334,
              99.65725170626096,
              17.0
            ],
            "actual_bounds": [
              31.170185089111328,
              24.187641143798828,
              99.65725,
              17.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月19日 周六",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_140",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              29.166694484590465,
              52.541732165772856,
              82.85337653071157,
              28.0
            ],
            "actual_bounds": [
              29.16669464111328,
              52.54173278808594,
              82.85338,
              28.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "16:10",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_153",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              131.51790443581447,
              693.0504664826026,
              35.14133349094046,
              26.5
            ],
            "actual_bounds": [
              131.5178985595703,
              693.0504760742188,
              35.141335,
              26.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "19",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_154",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              40.60671361753211,
              739.4146597791347,
              37.82212281119602,
              19.5
            ],
            "actual_bounds": [
              40.606712341308594,
              739.4146728515625,
              37.822124,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_155",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              131.15269300979136,
              740.430800306785,
              35.700294781443375,
              18.0
            ],
            "actual_bounds": [
              131.15269470214844,
              740.4307861328125,
              35.700294,
              18.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_157",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              230.35041743461053,
              739.6298189651394,
              35.90377472413016,
              19.5
            ],
            "actual_bounds": [
              230.3504180908203,
              739.6298217773438,
              35.903774,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_158",
            "native_id": "beauty_0_0_9",
            "expected_bounds": [
              324.5197590030103,
              739.380253898003,
              37.34258498650412,
              19.5
            ],
            "actual_bounds": [
              324.5197448730469,
              739.3802490234375,
              37.342587,
              19.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_146",
            "reference": [
              39.5,
              356.5,
              85.0,
              15.5
            ],
            "native": [
              39.5,
              356.5,
              85.0,
              15.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              86,
              86,
              86
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_148",
            "reference": [
              72.0,
              404.5,
              87.0,
              17.5
            ],
            "native": [
              72.0,
              404.5,
              87.0,
              17.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              243,
              247,
              245
            ],
            "native_color": [
              255,
              255,
              255
            ],
            "issues": []
          },
          {
            "id": "text_149",
            "reference": null,
            "native": null,
            "delta": null,
            "reference_color": null,
            "native_color": null,
            "issues": [
              "reference text missing or OCR unresolved"
            ]
          },
          {
            "id": "text_141",
            "reference": [
              91.5,
              123.5,
              112.0,
              17.5
            ],
            "native": [
              91.5,
              123.5,
              112.0,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.5
            ],
            "reference_color": [
              54,
              53,
              54
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_142",
            "reference": [
              40.5,
              172.0,
              167.0,
              21.5
            ],
            "native": [
              40.5,
              172.0,
              167.0,
              21.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              25,
              25,
              24
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_143",
            "reference": [
              43.0,
              215.5,
              101.5,
              32.0
            ],
            "native": [
              43.0,
              215.5,
              94.5,
              32.0
            ],
            "delta": [
              0.0,
              0.0,
              -7.0,
              0.0
            ],
            "reference_color": [
              43,
              43,
              41
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_144",
            "reference": [
              39.5,
              281.5,
              102.5,
              16.5
            ],
            "native": [
              39.5,
              281.5,
              102.5,
              16.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              82,
              81,
              82
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_145",
            "reference": [
              40.0,
              324.5,
              176.5,
              15.5
            ],
            "native": [
              34.0,
              324.0,
              182.5,
              17.0
            ],
            "delta": [
              -6.0,
              -0.5,
              6.0,
              1.5
            ],
            "reference_color": [
              84,
              84,
              84
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink position",
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_147",
            "reference": [
              304.5,
              283.5,
              42.0,
              13.5
            ],
            "native": [
              304.5,
              283.5,
              42.0,
              13.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              87,
              87,
              87
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_152",
            "reference": [
              150.0,
              587.0,
              77.0,
              17.0
            ],
            "native": [
              150.0,
              587.0,
              77.0,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              83,
              104,
              89
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_150",
            "reference": [
              89.5,
              497.0,
              192.5,
              17.5
            ],
            "native": [
              89.5,
              497.0,
              192.5,
              17.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              63,
              63,
              63
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_151",
            "reference": [
              37.5,
              537.0,
              128.0,
              16.0
            ],
            "native": [
              34.0,
              537.0,
              132.0,
              16.5
            ],
            "delta": [
              -3.5,
              0.0,
              4.0,
              0.5
            ],
            "reference_color": [
              90,
              90,
              90
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink position",
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_139",
            "reference": [
              32.0,
              26.0,
              92.5,
              13.0
            ],
            "native": [
              32.0,
              26.0,
              92.5,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              104,
              109,
              108
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_140",
            "reference": [
              32.0,
              54.5,
              73.0,
              24.0
            ],
            "native": [
              32.0,
              54.5,
              73.0,
              23.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              54,
              63,
              59
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_153",
            "reference": [
              134.0,
              694.5,
              26.5,
              22.5
            ],
            "native": [
              134.0,
              694.5,
              26.5,
              20.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -2.0
            ],
            "reference_color": [
              76,
              84,
              79
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_154",
            "reference": [
              42.0,
              741.0,
              30.5,
              15.5
            ],
            "native": [
              42.0,
              741.0,
              30.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              98,
              105,
              103
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_155",
            "reference": [
              134.0,
              742.0,
              27.0,
              14.0
            ],
            "native": [
              134.0,
              742.0,
              27.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              104,
              111,
              108
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_157",
            "reference": [
              231.0,
              741.0,
              29.5,
              15.5
            ],
            "native": [
              231.5,
              741.0,
              29.0,
              14.0
            ],
            "delta": [
              0.5,
              0.0,
              -0.5,
              -1.5
            ],
            "reference_color": [
              124,
              128,
              126
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_158",
            "reference": [
              325.5,
              741.0,
              30.0,
              15.5
            ],
            "native": [
              325.5,
              741.0,
              30.0,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              111,
              115,
              113
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              2.5,
              0.0,
              400.5,
              776.0
            ],
            "native": [
              2.5,
              0.0,
              400.5,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "payment_due",
            "reference": [
              16.498058252427185,
              97.97194388777555,
              356.95048543689325,
              356.8977955911824
            ],
            "native": [
              16.498058319091797,
              97.9719467163086,
              356.95050048828125,
              356.8977966308594
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "divider_0",
            "reference": [
              39.050485436893204,
              265.14629258517033,
              311.06796116504853,
              0.7775551102204409
            ],
            "native": [
              39.05048370361328,
              265.14630126953125,
              311.0679626464844,
              0.7775551080703735
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "source_service_order",
            "reference": [
              35.93980582524272,
              350.67735470941886,
              98.76407766990292,
              26.43687374749499
            ],
            "native": [
              35.93980407714844,
              350.6773681640625,
              98.76408,
              26.436874
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "source_service_order_surface",
            "reference": [
              35.93980582524272,
              350.67735470941886,
              98.76407766990292,
              26.43687374749499
            ],
            "native": [
              35.93980407714844,
              350.6773681640625,
              98.76408,
              26.436874
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "source_service_order_control",
            "reference": [
              35.93980582524272,
              350.67735470941886,
              98.76407766990292,
              26.43687374749499
            ],
            "native": [
              35.93980407714844,
              350.6773681640625,
              98.76407623291016,
              26.436874389648438
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "pay_materials",
            "reference": [
              35.1621359223301,
              390.3326653306613,
              168.75436893203883,
              45.875751503006015
            ],
            "native": [
              35.16213607788086,
              390.3326721191406,
              168.75436,
              45.87575
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "pay_materials_surface",
            "reference": [
              35.1621359223301,
              390.3326653306613,
              168.75436893203883,
              45.875751503006015
            ],
            "native": [
              35.16213607788086,
              390.3326721191406,
              168.75436401367188,
              45.87575149536133
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "pay_materials_control",
            "reference": [
              35.1621359223301,
              390.3326653306613,
              168.75436893203883,
              45.875751503006015
            ],
            "native": [
              35.16213607788086,
              390.3326721191406,
              168.75436401367188,
              45.87575149536133
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "withdraw_payment_request",
            "reference": [
              224.1359223300971,
              389.5551102204409,
              131.426213592233,
              45.875751503006015
            ],
            "native": [
              224.13592529296875,
              389.55511474609375,
              131.42621,
              45.87575
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "withdraw_payment_request_surface",
            "reference": [
              224.1359223300971,
              389.5551102204409,
              131.426213592233,
              45.875751503006015
            ],
            "native": [
              224.13592529296875,
              389.55511474609375,
              131.42620849609375,
              45.87575149536133
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "withdraw_payment_request_control",
            "reference": [
              224.1359223300971,
              389.5551102204409,
              131.426213592233,
              45.875751503006015
            ],
            "native": [
              224.13592529296875,
              389.55511474609375,
              131.42620849609375,
              45.87575149536133
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "wallet_icon_0",
            "reference": [
              39.828155339805825,
              115.85571142284569,
              34.21747572815534,
              31.879759519038075
            ],
            "native": [
              39.828155517578125,
              115.855712890625,
              34.21747589111328,
              31.879758834838867
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "installation_complete",
            "reference": [
              16.498058252427185,
              468.86573146292585,
              356.95048543689325,
              171.06212424849699
            ],
            "native": [
              16.498058319091797,
              468.86572265625,
              356.95050048828125,
              171.06211853027344
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "report_installation_issue",
            "reference": [
              103.59708737864078,
              571.503006012024,
              177.30873786407767,
              45.098196392785574
            ],
            "native": [
              103.59708404541016,
              571.5029907226562,
              177.30873,
              45.098198
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "report_installation_issue_surface",
            "reference": [
              103.59708737864078,
              571.503006012024,
              177.30873786407767,
              45.098196392785574
            ],
            "native": [
              103.59708404541016,
              571.5029907226562,
              177.30873107910156,
              45.09819793701172
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "report_installation_issue_control",
            "reference": [
              103.59708737864078,
              571.503006012024,
              177.30873786407767,
              45.098196392785574
            ],
            "native": [
              103.59708404541016,
              571.5029907226562,
              177.30873107910156,
              45.09819793701172
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "wrench_icon_1",
            "reference": [
              36.71747572815534,
              489.85971943887773,
              29.55145631067961,
              31.879759519038075
            ],
            "native": [
              36.71747589111328,
              489.8597106933594,
              29.551456451416016,
              31.879758834838867
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              12.609708737864079,
              658.5891783567134,
              378.7252427184466,
              115.85571142284569
            ],
            "native": [
              12.609708786010742,
              658.5891723632812,
              378.7252502441406,
              115.855712890625
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              35.570412621359225,
              667.0489779559118,
              69.96851650485436,
              69.9581883767535
            ],
            "native": [
              35.570411682128906,
              667.0489501953125,
              69.96851348876953,
              69.95819091796875
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              47.23546116504854,
              681.8225250501002,
              46.638419417475724,
              44.29886973947895
            ],
            "native": [
              47.2354621887207,
              681.822509765625,
              46.63842010498047,
              44.29887008666992
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              124.57084466019418,
              667.0489779559118,
              69.96851650485436,
              69.9581883767535
            ],
            "native": [
              124.57084655761719,
              667.0489501953125,
              69.96851348876953,
              69.95819091796875
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              213.5712766990291,
              667.0489779559118,
              69.96851650485436,
              69.9581883767535
            ],
            "native": [
              213.57127380371094,
              667.0489501953125,
              69.96851348876953,
              69.95819091796875
            ],
            "delta": [
              -0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              225.23632524271844,
              681.8225250501002,
              46.638419417475724,
              44.29886973947895
            ],
            "native": [
              225.236328125,
              681.822509765625,
              46.63842010498047,
              44.29887008666992
            ],
            "delta": [
              0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              302.57170873786407,
              667.0489779559118,
              69.96851650485436,
              69.9581883767535
            ],
            "native": [
              302.57171630859375,
              667.0489501953125,
              69.96851348876953,
              69.95819091796875
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              314.23675728155337,
              681.8225250501002,
              46.638419417475724,
              44.29886973947895
            ],
            "native": [
              314.23675537109375,
              681.822509765625,
              46.63842010498047,
              44.29887008666992
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "payment_due",
            "second": "installation_complete",
            "vertical_gap_reference": 13.99599198396794,
            "vertical_gap_native": 13.995979309082031,
            "left_alignment_delta": 0.0
          },
          {
            "first": "installation_complete",
            "second": "dock",
            "vertical_gap_reference": 18.661322645290596,
            "vertical_gap_native": 18.661331176757812,
            "left_alignment_delta": -1.8517948063845324e-08
          },
          {
            "first": "wallet_icon_0",
            "second": "divider_0",
            "vertical_gap_reference": 117.41082164328658,
            "vertical_gap_native": 117.41082954406738,
            "left_alignment_delta": -1.911052223135812e-06
          },
          {
            "first": "divider_0",
            "second": "source_service_order",
            "vertical_gap_reference": 84.75350701402809,
            "vertical_gap_native": 84.75351178646088,
            "left_alignment_delta": -1.4814361293247202e-08
          },
          {
            "first": "source_service_order",
            "second": "withdraw_payment_request",
            "vertical_gap_reference": 12.440881763527042,
            "vertical_gap_native": 12.44087258203125,
            "left_alignment_delta": 4.710965953336199e-06
          },
          {
            "first": "withdraw_payment_request",
            "second": "pay_materials",
            "vertical_gap_reference": -45.098196392785596,
            "vertical_gap_native": -45.09819262695312,
            "left_alignment_delta": -2.8073208966361562e-06
          },
          {
            "first": "source_service_order_surface",
            "second": "source_service_order_control",
            "vertical_gap_reference": -26.43687374749499,
            "vertical_gap_native": -26.436874,
            "left_alignment_delta": 0.0
          },
          {
            "first": "pay_materials_surface",
            "second": "pay_materials_control",
            "vertical_gap_reference": -45.875751503006015,
            "vertical_gap_native": -45.87575149536133,
            "left_alignment_delta": 0.0
          },
          {
            "first": "withdraw_payment_request_surface",
            "second": "withdraw_payment_request_control",
            "vertical_gap_reference": -45.875751503006015,
            "vertical_gap_native": -45.87575149536133,
            "left_alignment_delta": 0.0
          },
          {
            "first": "wrench_icon_1",
            "second": "report_installation_issue",
            "vertical_gap_reference": 49.763527054108195,
            "vertical_gap_native": 49.76352119445801,
            "left_alignment_delta": -3.496188554663604e-06
          },
          {
            "first": "report_installation_issue_surface",
            "second": "report_installation_issue_control",
            "vertical_gap_reference": -45.098196392785574,
            "vertical_gap_native": -45.09819793701172,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -69.9581883767535,
            "vertical_gap_native": -69.95819091796875,
            "left_alignment_delta": 2.8366533229018387e-06
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -69.9581883767535,
            "vertical_gap_native": -69.95819091796875,
            "left_alignment_delta": -4.792741179926452e-06
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -69.9581883767535,
            "vertical_gap_native": -69.95819091796875,
            "left_alignment_delta": 1.0466047854151839e-05
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -55.18464128256508,
            "vertical_gap_native": -55.18463134765625,
            "left_alignment_delta": -6.547057523675903e-06
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -44.29886973947895,
            "vertical_gap_native": -44.29887008666992,
            "left_alignment_delta": 1.8586094086003868e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -44.29886973947895,
            "vertical_gap_native": -44.29887008666992,
            "left_alignment_delta": -4.792741179926452e-06
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-11/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-11/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-11/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-11/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-11/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-11/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/11.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-11/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-11/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-11/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-11/rounds/002/interactions.json",
          "available": true
        }
      }
    },
    {
      "number": 12,
      "id": "aircon-12",
      "title": "付款完成",
      "description": "支付和安装服务分别显示完成记录",
      "surface": "系统桌面",
      "branch": false,
      "base": "../cards/aircon-12/",
      "reference": "../cards/aircon-12/reference.png",
      "native": "../cards/aircon-12/rounds/002/native.png",
      "latest": {
        "round": "002",
        "build_id": [
          8
        ],
        "nonce": "2a563a0c601e436e9b7b70c0014bd09d"
      },
      "run": {
        "id": "aircon-12",
        "status": "failed",
        "scope": "fixed_artboard_parity",
        "accepted": false,
        "stages": [
          {
            "stage": "gate",
            "pass": false
          }
        ],
        "errors": [],
        "current_stage": "gate"
      },
      "gate": {
        "schema_version": 1,
        "id": "aircon-12",
        "round": "002",
        "build_id": [
          8
        ],
        "tolerances": {
          "native_geometry_px": 1.0,
          "image_position_px": 3.0,
          "image_dimension_px": 3.0,
          "text_ink_position_px": 3.0,
          "text_ink_dimension_px": 3.0,
          "clipping_px": 1.0,
          "color_channel": 16
        },
        "native_structure_pass": true,
        "image_structure_pass": false,
        "semantic_mapping_pass": true,
        "semantic_errors": [],
        "semantic_mapping": {
          "schema_version": 1,
          "policy_version": "1.1.0",
          "policy_sha256": "d502a7c4f7dcc52ada37cfbbaf6bd9289afdcab90e30c504de96e8f8f39ff153",
          "evaluator_sha256": "35d4dfa6e986e0f4c6acbf9cd7e10a7c148e30fe3f9e31be930d53b15eeef9d3",
          "manifest_sha256": "4ff4763c677e7bf950dacce6862e7befb1b10cbd3ee62d98b19a298c97233d7f",
          "reference_sha256": "640ad7f395aa1a5b7f5d5438d6ffee5661a69cc64a19250f09aa69abaec247c7",
          "id": "aircon-12",
          "round": "002",
          "phase": "inspection",
          "pass": true,
          "errors": [],
          "elements": [
            {
              "id": "page",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "screen",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "payment_complete",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "divider_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "source_service_order",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "source_service_order_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "source_service_order_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_203",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "view_payment_receipt",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "view_payment_receipt_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "view_payment_receipt_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_204",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "wallet_icon_0",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "check_icon_1",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_197",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_198",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_199",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_200",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_201",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_202",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_215",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "installation_complete",
              "role": "card",
              "basis": "Service-owned card surface with native child widgets",
              "expected_widgets": [
                "View",
                "TaskplanProjectCard",
                "CamoTrackRow"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Reuse the matching kit component, or compose and name a new reusable component from native children."
            },
            {
              "id": "view_service_order",
              "role": "button",
              "basis": "authored KitButton composition",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "KitButton",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "view_service_order_surface",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "view_service_order_control",
              "role": "button",
              "basis": "authored button node",
              "expected_widgets": [
                "Button",
                "KitButton"
              ],
              "actual_widget": "Button",
              "issues": [],
              "repair": "Use a native control and verify its declared action."
            },
            {
              "id": "text_207",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "wrench_icon_2",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_205",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_206",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "dock",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_0",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_mail",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_1",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_tile_2",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_bag",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "dock_tile_3",
              "role": "layout",
              "basis": "authored stack node",
              "expected_widgets": [
                "View"
              ],
              "actual_widget": "View",
              "issues": [],
              "repair": "Compose layout containers with explicit spacing, sizing and clipping."
            },
            {
              "id": "dock_wallet",
              "role": "icon",
              "basis": "Visual source-region review and explicit native renderer ownership",
              "expected_widgets": [
                "Svg",
                "Icon",
                "Image"
              ],
              "actual_widget": "Svg",
              "issues": [],
              "repair": "Use a matching kit icon or reference-derived SVG. A source crop requires a recorded visual feature that cannot be reproduced faithfully with the available vector renderer."
            },
            {
              "id": "text_195",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_196",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_208",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_209",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_210",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_211",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            },
            {
              "id": "text_216",
              "role": "text",
              "basis": "authored text node",
              "expected_widgets": [
                "Label",
                "TextFlow"
              ],
              "actual_widget": "Label",
              "issues": [],
              "repair": "Use native text with a bundled font, exact copy and measured line layout."
            }
          ],
          "scope": "Semantic mapping checks only; geometry, visual fidelity and complete app workflows remain separate."
        },
        "accepted": false,
        "visual_review": {
          "status": "repair",
          "rgb_mae": 5.457,
          "note": "Diagnostic only. Typography, graphics, color and effects still need side-by-side review.",
          "review": {
            "reference_sha256": "640ad7f395aa1a5b7f5d5438d6ffee5661a69cc64a19250f09aa69abaec247c7",
            "native_sha256": "b47ae8bd815737384bc582173007cd96e38ca5be7437e8123a9dae9e3d86f899",
            "reviewer": "Codex visual inspection of the original atlas and each actual Studio viewport capture",
            "verdict": "repair",
            "criteria": {
              "typography": false,
              "colors": false,
              "imagery": false,
              "effects": false
            },
            "findings": [
              {
                "area": "overall",
                "status": "repair",
                "detail": "All 12 final captures visually inspected. Native card hierarchy, readable labels, actions and service ownership are present. Measured font sizing improved and confirmation check is legible. Exact raster-reference parity remains unmet.",
                "remaining_differences": "Noto glyphs and dark sage text differ from the generated gray type; reconstructed line icons and desktop dock retain different proportions and shapes; native panels omit source soft shadows and abstract wallpaper. Source wording corrections are intentional and documented; source photos are retained as artwork-only crops."
              }
            ]
          },
          "receipt_current": true
        },
        "native_errors": [],
        "image_errors": [
          "text_203: text color",
          "text_204: text color",
          "text_197: text color",
          "text_198: text color",
          "text_199: text ink dimensions",
          "text_199: text color",
          "text_200: text color",
          "text_201: text color",
          "text_202: reference OCR text differs",
          "text_202: text color",
          "text_215: text color",
          "text_207: text color",
          "text_206: reference OCR text differs",
          "text_206: text ink position",
          "text_206: text ink dimensions",
          "text_206: text color",
          "text_195: text color",
          "text_208: text color",
          "text_209: text color",
          "text_210: text color",
          "text_211: text color",
          "text_216: text color"
        ],
        "elements": [
          {
            "id": "page",
            "native_id": "beauty_0",
            "expected_bounds": [
              0,
              0,
              406,
              776
            ],
            "actual_bounds": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "parent": "host",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "screen",
            "native_id": "beauty_0_0",
            "expected_bounds": [
              0.0,
              69.5,
              406.0,
              637.0
            ],
            "actual_bounds": [
              0.0,
              69.5,
              406.0,
              637.0
            ],
            "parent": "beauty_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "payment_complete",
            "native_id": "beauty_0_0_0",
            "expected_bounds": [
              14.0,
              150.95454545454544,
              358.9090909090909,
              296.54545454545456
            ],
            "actual_bounds": [
              14.0,
              150.9545440673828,
              358.9090881347656,
              296.5454406738281
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "divider_0",
            "native_id": "beauty_0_0_0_0",
            "expected_bounds": [
              33.72727272727273,
              294.77272727272725,
              311.8181818181818,
              0.6363636363636364
            ],
            "actual_bounds": [
              33.727272033691406,
              294.7727355957031,
              311.81817626953125,
              0.6363636255264282
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "source_service_order",
            "native_id": "beauty_0_0_0_1",
            "expected_bounds": [
              31.18181818181818,
              363.5,
              80.81818181818181,
              22.272727272727273
            ],
            "actual_bounds": [
              31.18181800842285,
              363.5,
              80.818184,
              22.272728
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "安装服务单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "source_service_order_surface",
            "native_id": "beauty_0_0_0_1_0",
            "expected_bounds": [
              31.18181818181818,
              363.5,
              80.81818181818181,
              22.272727272727273
            ],
            "actual_bounds": [
              31.18181800842285,
              363.5,
              80.818184,
              22.272728
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "source_service_order_control",
            "native_id": "beauty_0_0_0_1_1",
            "expected_bounds": [
              31.18181818181818,
              363.5,
              80.81818181818181,
              22.272727272727273
            ],
            "actual_bounds": [
              31.18181800842285,
              363.5,
              80.81818389892578,
              22.272727966308594
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_203",
            "native_id": "beauty_0_0_0_1_2",
            "expected_bounds": [
              34.44058628336092,
              365.78625680194097,
              80.4756258252873,
              17.0
            ],
            "actual_bounds": [
              34.44058609008789,
              365.7862548828125,
              80.475624,
              17.0
            ],
            "parent": "beauty_0_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "安装服务单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_payment_receipt",
            "native_id": "beauty_0_0_0_2",
            "expected_bounds": [
              35.0,
              395.95454545454544,
              211.9090909090909,
              38.18181818181818
            ],
            "actual_bounds": [
              35.0,
              395.9545593261719,
              211.90909,
              38.18182
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "KitButton",
            "visible": true,
            "text": "查看凭证",
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_payment_receipt_surface",
            "native_id": "beauty_0_0_0_2_0",
            "expected_bounds": [
              35.0,
              395.95454545454544,
              211.9090909090909,
              38.18181818181818
            ],
            "actual_bounds": [
              35.0,
              395.9545593261719,
              211.90908813476562,
              38.181819915771484
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_payment_receipt_control",
            "native_id": "beauty_0_0_0_2_1",
            "expected_bounds": [
              35.0,
              395.95454545454544,
              211.9090909090909,
              38.18181818181818
            ],
            "actual_bounds": [
              35.0,
              395.9545593261719,
              211.90908813476562,
              38.181819915771484
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_204",
            "native_id": "beauty_0_0_0_2_2",
            "expected_bounds": [
              105.89015723075715,
              405.8602084537482,
              74.13811202687319,
              19.0
            ],
            "actual_bounds": [
              105.8901596069336,
              405.8601989746094,
              74.138115,
              19.0
            ],
            "parent": "beauty_0_0_0_2",
            "widget_type": "Label",
            "visible": true,
            "text": "查看凭证",
            "enabled": true,
            "issues": []
          },
          {
            "id": "wallet_icon_0",
            "native_id": "beauty_0_0_0_3",
            "expected_bounds": [
              33.09090909090909,
              167.5,
              30.545454545454547,
              27.363636363636363
            ],
            "actual_bounds": [
              33.09090805053711,
              167.5,
              30.545454025268555,
              27.363636016845703
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "check_icon_1",
            "native_id": "beauty_0_0_0_4",
            "expected_bounds": [
              318.1818181818182,
              172.5909090909091,
              21.0,
              21.636363636363637
            ],
            "actual_bounds": [
              318.18182373046875,
              172.59091186523438,
              21.0,
              21.636363983154297
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_197",
            "native_id": "beauty_0_0_0_5",
            "expected_bounds": [
              77.6186434070083,
              173.7329472121005,
              102.24952675228171,
              18.5
            ],
            "actual_bounds": [
              77.61864471435547,
              173.73294067382812,
              102.24953,
              18.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付 · 已完成",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_198",
            "native_id": "beauty_0_0_0_6",
            "expected_bounds": [
              32.63252877447193,
              211.89555105572788,
              150.33816226407754,
              22.869462423227578
            ],
            "actual_bounds": [
              32.632530212402344,
              211.8955535888672,
              150.33817,
              22.869463
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "空调安装材料费",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_199",
            "native_id": "beauty_0_0_0_7",
            "expected_bounds": [
              35.232779253342514,
              249.12632269902826,
              87.87935616527135,
              30.5
            ],
            "actual_bounds": [
              35.23278045654297,
              249.12632751464844,
              87.87936,
              30.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "¥130",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_200",
            "native_id": "beauty_0_0_0_8",
            "expected_bounds": [
              149.17195447301492,
              258.73013433213265,
              55.61335078481991,
              19.5
            ],
            "actual_bounds": [
              149.1719512939453,
              258.7301330566406,
              55.61335,
              19.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "已支付",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_201",
            "native_id": "beauty_0_0_0_9",
            "expected_bounds": [
              34.22621461354197,
              307.5719194664619,
              102.12810999903577,
              18.09581161057193
            ],
            "actual_bounds": [
              34.22621536254883,
              307.5719299316406,
              102.12811,
              18.095812
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "加长铜管 2米",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_202",
            "native_id": "beauty_0_0_0_10",
            "expected_bounds": [
              31.729135288399828,
              339.6469799079231,
              158.71229389850083,
              18.403714561950423
            ],
            "actual_bounds": [
              31.729135513305664,
              339.64697265625,
              158.7123,
              18.403715
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "收款方：安装服务团队",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_215",
            "native_id": "beauty_0_0_0_11",
            "expected_bounds": [
              300.6293897340993,
              310.03673010576557,
              43.066302517270366,
              15.5
            ],
            "actual_bounds": [
              300.62939453125,
              310.0367431640625,
              43.066303,
              15.5
            ],
            "parent": "beauty_0_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "¥130",
            "enabled": true,
            "issues": []
          },
          {
            "id": "installation_complete",
            "native_id": "beauty_0_0_1",
            "expected_bounds": [
              13.363636363636363,
              457.6818181818182,
              359.54545454545456,
              141.27272727272728
            ],
            "actual_bounds": [
              13.363636016845703,
              457.68182373046875,
              359.5454406738281,
              141.27272033691406
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_service_order",
            "native_id": "beauty_0_0_1_0",
            "expected_bounds": [
              90.36363636363636,
              545.5,
              158.45454545454544,
              37.54545454545455
            ],
            "actual_bounds": [
              90.36363983154297,
              545.5,
              158.45454,
              37.545456
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "KitButton",
            "visible": true,
            "text": "查看服务单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_service_order_surface",
            "native_id": "beauty_0_0_1_0_0",
            "expected_bounds": [
              90.36363636363636,
              545.5,
              158.45454545454544,
              37.54545454545455
            ],
            "actual_bounds": [
              90.36363983154297,
              545.5,
              158.4545440673828,
              37.54545593261719
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "view_service_order_control",
            "native_id": "beauty_0_0_1_0_1",
            "expected_bounds": [
              90.36363636363636,
              545.5,
              158.45454545454544,
              37.54545454545455
            ],
            "actual_bounds": [
              90.36363983154297,
              545.5,
              158.4545440673828,
              37.54545593261719
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "Button",
            "visible": true,
            "text": "",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_207",
            "native_id": "beauty_0_0_1_0_2",
            "expected_bounds": [
              122.51858683021435,
              555.4771355861163,
              89.4265585810467,
              18.96877271406122
            ],
            "actual_bounds": [
              122.51858520507812,
              555.4771118164062,
              89.42656,
              18.968773
            ],
            "parent": "beauty_0_0_1_0",
            "widget_type": "Label",
            "visible": true,
            "text": "查看服务单",
            "enabled": true,
            "issues": []
          },
          {
            "id": "wrench_icon_2",
            "native_id": "beauty_0_0_1_1",
            "expected_bounds": [
              33.09090909090909,
              477.4090909090909,
              26.09090909090909,
              25.454545454545453
            ],
            "actual_bounds": [
              33.09090805053711,
              477.4090881347656,
              26.090909957885742,
              25.454545974731445
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_205",
            "native_id": "beauty_0_0_1_2",
            "expected_bounds": [
              77.11114028871755,
              480.035465929761,
              180.4227297018214,
              18.896809776923035
            ],
            "actual_bounds": [
              77.11113739013672,
              480.03546142578125,
              180.42273,
              18.89681
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "安装服务 · 安装已完成",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_206",
            "native_id": "beauty_0_0_1_3",
            "expected_bounds": [
              28.472810427209655,
              511.77846124376856,
              121.13344943017097,
              19.27182948266786
            ],
            "actual_bounds": [
              28.472810745239258,
              511.7784729003906,
              121.133446,
              19.27183
            ],
            "parent": "beauty_0_0_1",
            "widget_type": "Label",
            "visible": true,
            "text": "家．海棠路18号",
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock",
            "native_id": "beauty_0_0_2",
            "expected_bounds": [
              8.272727272727273,
              610.4090909090909,
              371.6363636363636,
              95.45454545454545
            ],
            "actual_bounds": [
              8.272727012634277,
              610.4091186523438,
              371.6363525390625,
              95.45454406738281
            ],
            "parent": "beauty_0_0",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "native_id": "beauty_0_0_2_0",
            "expected_bounds": [
              31.690909090909088,
              617.4090909090909,
              66.88436363636363,
              66.88436363636363
            ],
            "actual_bounds": [
              31.690908432006836,
              617.4091186523438,
              66.88436126708984,
              66.88436126708984
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_mail",
            "native_id": "beauty_0_0_2_1",
            "expected_bounds": [
              41.236363636363635,
              629.5,
              47.793454545454544,
              45.88436363636364
            ],
            "actual_bounds": [
              41.23636245727539,
              629.5,
              47.793453216552734,
              45.88436508178711
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "native_id": "beauty_0_0_2_2",
            "expected_bounds": [
              119.02545454545454,
              617.4090909090909,
              66.88436363636363,
              66.88436363636363
            ],
            "actual_bounds": [
              119.02545166015625,
              617.4091186523438,
              66.88436126708984,
              66.88436126708984
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "native_id": "beauty_0_0_2_3",
            "expected_bounds": [
              206.35999999999999,
              617.4090909090909,
              66.88436363636363,
              66.88436363636363
            ],
            "actual_bounds": [
              206.36000061035156,
              617.4091186523438,
              66.88436126708984,
              66.88436126708984
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_bag",
            "native_id": "beauty_0_0_2_4",
            "expected_bounds": [
              215.90545454545452,
              629.5,
              47.793454545454544,
              45.88436363636364
            ],
            "actual_bounds": [
              215.90545654296875,
              629.5,
              47.793453216552734,
              45.88436508178711
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "native_id": "beauty_0_0_2_5",
            "expected_bounds": [
              293.6945454545454,
              617.4090909090909,
              66.88436363636363,
              66.88436363636363
            ],
            "actual_bounds": [
              293.6945495605469,
              617.4091186523438,
              66.88436126708984,
              66.88436126708984
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "View",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "dock_wallet",
            "native_id": "beauty_0_0_2_6",
            "expected_bounds": [
              303.23999999999995,
              629.5,
              47.793454545454544,
              45.88436363636364
            ],
            "actual_bounds": [
              303.239990234375,
              629.5,
              47.793453216552734,
              45.88436508178711
            ],
            "parent": "beauty_0_0_2",
            "widget_type": "Svg",
            "visible": true,
            "text": null,
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_195",
            "native_id": "beauty_0_0_3",
            "expected_bounds": [
              24.879833940927462,
              90.13896625023352,
              83.54134952047593,
              14.5
            ],
            "actual_bounds": [
              24.879833221435547,
              90.13896942138672,
              83.54135,
              14.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "9月19日 周六",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_196",
            "native_id": "beauty_0_0_4",
            "expected_bounds": [
              24.012745650992226,
              113.6848972807492,
              73.09111303255341,
              24.0
            ],
            "actual_bounds": [
              24.012744903564453,
              113.68489837646484,
              73.09111,
              24.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "16:12",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_208",
            "native_id": "beauty_0_0_5",
            "expected_bounds": [
              125.80683460356806,
              638.0885171964965,
              32.35279332022158,
              22.5
            ],
            "actual_bounds": [
              125.80683135986328,
              638.0885009765625,
              32.352795,
              22.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "19",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_209",
            "native_id": "beauty_0_0_6",
            "expected_bounds": [
              37.221067276651375,
              676.4790554748926,
              34.06380178214427,
              16.5
            ],
            "actual_bounds": [
              37.221065521240234,
              676.4790649414062,
              34.0638,
              16.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "邮件",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_210",
            "native_id": "beauty_0_0_7",
            "expected_bounds": [
              123.76033674666373,
              676.9924109925619,
              34.281839279000266,
              16.0
            ],
            "actual_bounds": [
              123.76033782958984,
              676.992431640625,
              34.281837,
              16.0
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "日历",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_211",
            "native_id": "beauty_0_0_8",
            "expected_bounds": [
              217.30056367863577,
              676.4997093595694,
              33.92033476605116,
              16.5
            ],
            "actual_bounds": [
              217.30056762695312,
              676.4996948242188,
              33.920334,
              16.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "购物",
            "enabled": true,
            "issues": []
          },
          {
            "id": "text_216",
            "native_id": "beauty_0_0_9",
            "expected_bounds": [
              309.96204536852224,
              676.5071451383672,
              33.931100316713184,
              16.5
            ],
            "actual_bounds": [
              309.9620361328125,
              676.5071411132812,
              33.9311,
              16.5
            ],
            "parent": "beauty_0_0",
            "widget_type": "Label",
            "visible": true,
            "text": "支付",
            "enabled": true,
            "issues": []
          }
        ],
        "text_differences": [
          {
            "id": "text_203",
            "reference": [
              35.5,
              367.5,
              73.0,
              13.0
            ],
            "native": [
              35.5,
              367.5,
              73.0,
              13.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              98,
              98,
              99
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_204",
            "reference": [
              107.0,
              407.5,
              66.5,
              15.0
            ],
            "native": [
              107.0,
              407.5,
              66.5,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              78,
              98,
              85
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_197",
            "reference": [
              78.5,
              175.5,
              95.0,
              14.5
            ],
            "native": [
              78.5,
              175.5,
              95.0,
              13.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -1.0
            ],
            "reference_color": [
              71,
              99,
              75
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_198",
            "reference": [
              34.5,
              214.0,
              141.5,
              18.5
            ],
            "native": [
              34.5,
              213.5,
              141.5,
              19.0
            ],
            "delta": [
              0.0,
              -0.5,
              0.0,
              0.5
            ],
            "reference_color": [
              25,
              24,
              24
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_199",
            "reference": [
              36.5,
              251.0,
              87.0,
              26.5
            ],
            "native": [
              36.5,
              251.0,
              79.5,
              26.5
            ],
            "delta": [
              0.0,
              0.0,
              -7.5,
              0.0
            ],
            "reference_color": [
              47,
              47,
              45
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_200",
            "reference": [
              151.0,
              260.5,
              47.0,
              15.5
            ],
            "native": [
              151.0,
              260.5,
              47.0,
              15.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              66,
              106,
              71
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_201",
            "reference": [
              35.0,
              309.5,
              95.0,
              14.0
            ],
            "native": [
              35.0,
              309.5,
              95.0,
              14.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              80,
              81,
              81
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_202",
            "reference": [
              35.5,
              342.0,
              151.0,
              12.5
            ],
            "native": [
              33.0,
              341.5,
              152.5,
              14.0
            ],
            "delta": [
              -2.5,
              -0.5,
              1.5,
              1.5
            ],
            "reference_color": [
              83,
              83,
              84
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text color"
            ]
          },
          {
            "id": "text_215",
            "reference": [
              301.5,
              311.5,
              36.5,
              11.5
            ],
            "native": [
              301.5,
              311.5,
              36.5,
              11.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              80,
              80,
              80
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_207",
            "reference": [
              123.5,
              557.5,
              81.5,
              14.5
            ],
            "native": [
              123.5,
              557.5,
              81.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              84,
              105,
              90
            ],
            "native_color": [
              96,
              133,
              112
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_205",
            "reference": [
              78.5,
              482.0,
              172.5,
              14.5
            ],
            "native": [
              78.5,
              482.0,
              172.5,
              14.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              61,
              62,
              62
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_206",
            "reference": [
              35.0,
              514.5,
              108.0,
              13.0
            ],
            "native": [
              30.0,
              513.5,
              114.5,
              15.0
            ],
            "delta": [
              -5.0,
              -1.0,
              6.5,
              2.0
            ],
            "reference_color": [
              86,
              86,
              86
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "reference OCR text differs",
              "text ink position",
              "text ink dimensions",
              "text color"
            ]
          },
          {
            "id": "text_195",
            "reference": [
              25.5,
              92.0,
              77.0,
              10.5
            ],
            "native": [
              25.5,
              92.0,
              77.0,
              10.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              101,
              106,
              104
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_196",
            "reference": [
              26.5,
              115.5,
              63.5,
              20.0
            ],
            "native": [
              26.5,
              115.5,
              63.5,
              20.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              61,
              71,
              66
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": []
          },
          {
            "id": "text_208",
            "reference": [
              128.0,
              640.0,
              23.5,
              18.5
            ],
            "native": [
              128.0,
              640.0,
              23.5,
              18.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              -0.5
            ],
            "reference_color": [
              77,
              86,
              80
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_209",
            "reference": [
              38.5,
              678.0,
              27.5,
              12.5
            ],
            "native": [
              38.5,
              678.0,
              27.0,
              12.5
            ],
            "delta": [
              0.0,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              102,
              108,
              105
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_210",
            "reference": [
              126.5,
              678.5,
              26.0,
              12.0
            ],
            "native": [
              126.5,
              678.5,
              25.5,
              12.0
            ],
            "delta": [
              0.0,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              111,
              118,
              115
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_211",
            "reference": [
              218.0,
              678.0,
              27.0,
              12.5
            ],
            "native": [
              218.0,
              678.0,
              27.0,
              12.5
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "reference_color": [
              114,
              118,
              116
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          },
          {
            "id": "text_216",
            "reference": [
              310.5,
              678.0,
              27.5,
              12.5
            ],
            "native": [
              311.0,
              678.0,
              27.0,
              12.5
            ],
            "delta": [
              0.5,
              0.0,
              -0.5,
              0.0
            ],
            "reference_color": [
              95,
              103,
              99
            ],
            "native_color": [
              49,
              65,
              60
            ],
            "issues": [
              "text color"
            ]
          }
        ],
        "geometry_differences": [
          {
            "id": "page",
            "reference": [
              0,
              0,
              406,
              776
            ],
            "native": [
              0.0,
              0.0,
              406.0,
              776.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "screen",
            "reference": [
              0.0,
              69.5,
              406.0,
              637.0
            ],
            "native": [
              0.0,
              69.5,
              406.0,
              637.0
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "payment_complete",
            "reference": [
              14.0,
              150.95454545454544,
              358.9090909090909,
              296.54545454545456
            ],
            "native": [
              14.0,
              150.9545440673828,
              358.9090881347656,
              296.5454406738281
            ],
            "delta": [
              0.0,
              -0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "divider_0",
            "reference": [
              33.72727272727273,
              294.77272727272725,
              311.8181818181818,
              0.6363636363636364
            ],
            "native": [
              33.727272033691406,
              294.7727355957031,
              311.81817626953125,
              0.6363636255264282
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "source_service_order",
            "reference": [
              31.18181818181818,
              363.5,
              80.81818181818181,
              22.272727272727273
            ],
            "native": [
              31.18181800842285,
              363.5,
              80.818184,
              22.272728
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "source_service_order_surface",
            "reference": [
              31.18181818181818,
              363.5,
              80.81818181818181,
              22.272727272727273
            ],
            "native": [
              31.18181800842285,
              363.5,
              80.818184,
              22.272728
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "source_service_order_control",
            "reference": [
              31.18181818181818,
              363.5,
              80.81818181818181,
              22.272727272727273
            ],
            "native": [
              31.18181800842285,
              363.5,
              80.81818389892578,
              22.272727966308594
            ],
            "delta": [
              -0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "view_payment_receipt",
            "reference": [
              35.0,
              395.95454545454544,
              211.9090909090909,
              38.18181818181818
            ],
            "native": [
              35.0,
              395.9545593261719,
              211.90909,
              38.18182
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "view_payment_receipt_surface",
            "reference": [
              35.0,
              395.95454545454544,
              211.9090909090909,
              38.18181818181818
            ],
            "native": [
              35.0,
              395.9545593261719,
              211.90908813476562,
              38.181819915771484
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "view_payment_receipt_control",
            "reference": [
              35.0,
              395.95454545454544,
              211.9090909090909,
              38.18181818181818
            ],
            "native": [
              35.0,
              395.9545593261719,
              211.90908813476562,
              38.181819915771484
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "wallet_icon_0",
            "reference": [
              33.09090909090909,
              167.5,
              30.545454545454547,
              27.363636363636363
            ],
            "native": [
              33.09090805053711,
              167.5,
              30.545454025268555,
              27.363636016845703
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "check_icon_1",
            "reference": [
              318.1818181818182,
              172.5909090909091,
              21.0,
              21.636363636363637
            ],
            "native": [
              318.18182373046875,
              172.59091186523438,
              21.0,
              21.636363983154297
            ],
            "delta": [
              0.0,
              0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "installation_complete",
            "reference": [
              13.363636363636363,
              457.6818181818182,
              359.54545454545456,
              141.27272727272728
            ],
            "native": [
              13.363636016845703,
              457.68182373046875,
              359.5454406738281,
              141.27272033691406
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "view_service_order",
            "reference": [
              90.36363636363636,
              545.5,
              158.45454545454544,
              37.54545454545455
            ],
            "native": [
              90.36363983154297,
              545.5,
              158.45454,
              37.545456
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "view_service_order_surface",
            "reference": [
              90.36363636363636,
              545.5,
              158.45454545454544,
              37.54545454545455
            ],
            "native": [
              90.36363983154297,
              545.5,
              158.4545440673828,
              37.54545593261719
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "view_service_order_control",
            "reference": [
              90.36363636363636,
              545.5,
              158.45454545454544,
              37.54545454545455
            ],
            "native": [
              90.36363983154297,
              545.5,
              158.4545440673828,
              37.54545593261719
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "wrench_icon_2",
            "reference": [
              33.09090909090909,
              477.4090909090909,
              26.09090909090909,
              25.454545454545453
            ],
            "native": [
              33.09090805053711,
              477.4090881347656,
              26.090909957885742,
              25.454545974731445
            ],
            "delta": [
              -0.0,
              -0.0,
              0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock",
            "reference": [
              8.272727272727273,
              610.4090909090909,
              371.6363636363636,
              95.45454545454545
            ],
            "native": [
              8.272727012634277,
              610.4091186523438,
              371.6363525390625,
              95.45454406738281
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_0",
            "reference": [
              31.690909090909088,
              617.4090909090909,
              66.88436363636363,
              66.88436363636363
            ],
            "native": [
              31.690908432006836,
              617.4091186523438,
              66.88436126708984,
              66.88436126708984
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_mail",
            "reference": [
              41.236363636363635,
              629.5,
              47.793454545454544,
              45.88436363636364
            ],
            "native": [
              41.23636245727539,
              629.5,
              47.793453216552734,
              45.88436508178711
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_1",
            "reference": [
              119.02545454545454,
              617.4090909090909,
              66.88436363636363,
              66.88436363636363
            ],
            "native": [
              119.02545166015625,
              617.4091186523438,
              66.88436126708984,
              66.88436126708984
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_2",
            "reference": [
              206.35999999999999,
              617.4090909090909,
              66.88436363636363,
              66.88436363636363
            ],
            "native": [
              206.36000061035156,
              617.4091186523438,
              66.88436126708984,
              66.88436126708984
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_bag",
            "reference": [
              215.90545454545452,
              629.5,
              47.793454545454544,
              45.88436363636364
            ],
            "native": [
              215.90545654296875,
              629.5,
              47.793453216552734,
              45.88436508178711
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          },
          {
            "id": "dock_tile_3",
            "reference": [
              293.6945454545454,
              617.4090909090909,
              66.88436363636363,
              66.88436363636363
            ],
            "native": [
              293.6945495605469,
              617.4091186523438,
              66.88436126708984,
              66.88436126708984
            ],
            "delta": [
              0.0,
              0.0,
              -0.0,
              -0.0
            ],
            "issues": []
          },
          {
            "id": "dock_wallet",
            "reference": [
              303.23999999999995,
              629.5,
              47.793454545454544,
              45.88436363636364
            ],
            "native": [
              303.239990234375,
              629.5,
              47.793453216552734,
              45.88436508178711
            ],
            "delta": [
              -0.0,
              0.0,
              -0.0,
              0.0
            ],
            "issues": []
          }
        ],
        "relations": [
          {
            "first": "payment_complete",
            "second": "installation_complete",
            "vertical_gap_reference": 10.181818181818187,
            "vertical_gap_native": 10.181838989257812,
            "left_alignment_delta": -3.4679066018838967e-07
          },
          {
            "first": "installation_complete",
            "second": "dock",
            "vertical_gap_reference": 11.45454545454541,
            "vertical_gap_native": 11.454574584960938,
            "left_alignment_delta": 8.6697664158919e-08
          },
          {
            "first": "wallet_icon_0",
            "second": "check_icon_1",
            "vertical_gap_reference": -22.27272727272727,
            "vertical_gap_native": -22.272724151611328,
            "left_alignment_delta": 6.589022518710408e-06
          },
          {
            "first": "check_icon_1",
            "second": "divider_0",
            "vertical_gap_reference": 100.54545454545452,
            "vertical_gap_native": 100.54545974731445,
            "left_alignment_delta": -6.242231904707296e-06
          },
          {
            "first": "divider_0",
            "second": "source_service_order",
            "vertical_gap_reference": 68.09090909090911,
            "vertical_gap_native": 68.09090077877045,
            "left_alignment_delta": 5.201859920589413e-07
          },
          {
            "first": "source_service_order",
            "second": "view_payment_receipt",
            "vertical_gap_reference": 10.181818181818166,
            "vertical_gap_native": 10.181831326171874,
            "left_alignment_delta": 1.73395328317838e-07
          },
          {
            "first": "source_service_order_surface",
            "second": "source_service_order_control",
            "vertical_gap_reference": -22.272727272727273,
            "vertical_gap_native": -22.272728,
            "left_alignment_delta": 0.0
          },
          {
            "first": "view_payment_receipt_surface",
            "second": "view_payment_receipt_control",
            "vertical_gap_reference": -38.18181818181818,
            "vertical_gap_native": -38.181819915771484,
            "left_alignment_delta": 0.0
          },
          {
            "first": "wrench_icon_2",
            "second": "view_service_order",
            "vertical_gap_reference": 42.63636363636367,
            "vertical_gap_native": 42.63636589050293,
            "left_alignment_delta": 4.508278593107207e-06
          },
          {
            "first": "view_service_order_surface",
            "second": "view_service_order_control",
            "vertical_gap_reference": -37.54545454545455,
            "vertical_gap_native": -37.54545593261719,
            "left_alignment_delta": 0.0
          },
          {
            "first": "dock_tile_0",
            "second": "dock_tile_1",
            "vertical_gap_reference": -66.88436363636363,
            "vertical_gap_native": -66.88436126708984,
            "left_alignment_delta": -2.226396034643585e-06
          },
          {
            "first": "dock_tile_1",
            "second": "dock_tile_2",
            "vertical_gap_reference": -66.88436363636363,
            "vertical_gap_native": -66.88436126708984,
            "left_alignment_delta": 3.495649863793915e-06
          },
          {
            "first": "dock_tile_2",
            "second": "dock_tile_3",
            "vertical_gap_reference": -66.88436363636363,
            "vertical_gap_native": -66.88436126708984,
            "left_alignment_delta": 3.495649906426479e-06
          },
          {
            "first": "dock_tile_3",
            "second": "dock_mail",
            "vertical_gap_reference": -54.79345454545451,
            "vertical_gap_native": -54.793479919433594,
            "left_alignment_delta": -5.285089741846605e-06
          },
          {
            "first": "dock_mail",
            "second": "dock_bag",
            "vertical_gap_reference": -45.88436363636364,
            "vertical_gap_native": -45.88436508178711,
            "left_alignment_delta": 3.176602490384539e-06
          },
          {
            "first": "dock_bag",
            "second": "dock_wallet",
            "vertical_gap_reference": -45.88436363636364,
            "vertical_gap_native": -45.88436508178711,
            "left_alignment_delta": -1.176313918449523e-05
          }
        ],
        "interaction_scope": "native activation and declared fixture state/data probes; no live feeds or complete app navigation"
      },
      "files": {
        "card": {
          "label": ".card 源码",
          "url": "../cards/aircon-12/page.card",
          "available": true
        },
        "kit": {
          "label": "组件 kit",
          "url": "../cards/aircon-12/kit/native/light/kit.json",
          "available": true
        },
        "components": {
          "label": "原生组件",
          "url": "../cards/aircon-12/kit/native/light/components.l0",
          "available": true
        },
        "actions": {
          "label": "服务动作",
          "url": "../cards/aircon-12/service-actions.json",
          "available": true
        },
        "mapped": {
          "label": "组件树",
          "url": "../cards/aircon-12/mapped.json",
          "available": true
        },
        "run": {
          "label": "Pipeline",
          "url": "../cards/aircon-12/pipeline-run.json",
          "available": true
        },
        "data": {
          "label": "服务状态",
          "url": "../service/fixtures/12.view.json",
          "available": true
        },
        "gate": {
          "label": "验收 gate",
          "url": "../cards/aircon-12/rounds/002/gate.json",
          "available": true
        },
        "tree": {
          "label": "Studio 控件树",
          "url": "../cards/aircon-12/rounds/002/tree.json",
          "available": true
        },
        "provenance": {
          "label": "截图来源",
          "url": "../cards/aircon-12/rounds/002/provenance.json",
          "available": true
        },
        "interactions": {
          "label": "原生输入证据",
          "url": "../cards/aircon-12/rounds/002/interactions.json",
          "available": true
        }
      }
    }
  ],
  "note": "Only latest.json selects a native capture. Missing or failed evidence is never replaced with reference imagery."
};
