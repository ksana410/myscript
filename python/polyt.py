# -*- coding: utf-8 -*-

# polyt 平台自动购买工具
# 输入所需购买的演出项目名，自动购买添加到用户的订单中
# 查询响应
# {
# 	"code":"200",
# 	"data":{
# 		"countId":null,
# 		"current":0,
# 		"hitCount":false,
# 		"maxLimit":null,
# 		"optimizeCountSql":true,
# 		"orders":[],
# 		"pages":1,
# 		"records":[
# 			{
# 				"calendar":false,
# 				"categoryName":"音乐剧",
# 				"cityName":"无锡市",
# 				"couponsLabel":false,
# 				"cultureCouponLabel":false,
# 				"cuss":true,
# 				"flash":false,
# 				"horizontalPictureUrl":"",
# 				"id":"4957400_platform",
# 				"imgList":[],
# 				"invoicing":false,
# 				"linkInfo":null,
# 				"linkType":null,
# 				"maxPrice":1080.0,
# 				"minPrice":180.0,
# 				"openShop":false,
# 				"openTicket":true,
# 				"placeAddress":"无锡市滨湖区大剧院路1号",
# 				"placeCname":"无锡大剧院",
# 				"plat":true,
# 				"previewNum":null,
# 				"productAnnouncement":null,
# 				"productDesc":"<p style=\"white-space: normal;\"><strong style=\"font-size: 20px; color: rgb(235, 0, 59); font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; letter-spacing: 1.5px; widows: 1;\"><span style=\"color: rgb(255, 0, 0); margin: 0px; padding: 0px; outline: 0px; max-width: 100%; box-sizing: border-box !important; overflow-wrap: break-word !important;\">温馨提示：<strong><span style=\"margin: 0px; padding: 0px; outline: 0px; max-width: 100%; box-sizing: border-box !important; overflow-wrap: break-word !important;\">因院线票务系统升级，演出票单次购买数量不可超过6张，望您理解。</span></strong></span></strong></p><p style=\"margin-top: 0px; margin-bottom: 0px; white-space: normal; padding: 0px; outline: 0px; max-width: 100%; clear: both; min-height: 1em; color: rgb(235, 0, 59); font-size: 16px; letter-spacing: 1.5px; widows: 1; vertical-align: inherit; line-height: 2em; font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; box-sizing: border-box !important; overflow-wrap: break-word !important;\"><span style=\"font-size: 20px;\"><strong><span style=\"color: rgb(255, 0, 0); margin: 0px; padding: 0px; outline: 0px; max-width: 100%; box-sizing: border-box !important; overflow-wrap: break-word !important;\">1、本场演出可使用会员折扣，每个ID限购6张。</span></strong></span></p><p style=\"margin-top: 0px; margin-bottom: 0px; white-space: normal; padding: 0px; outline: 0px; max-width: 100%; clear: both; min-height: 1em; color: rgb(235, 0, 59); font-size: 16px; letter-spacing: 1.5px; widows: 1; vertical-align: inherit; line-height: 2em; font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; box-sizing: border-box !important; overflow-wrap: break-word !important;\"><span style=\"font-size: 20px;\"><strong><span style=\"color: rgb(255, 0, 0); margin: 0px; padding: 0px; outline: 0px; max-width: 100%; box-sizing: border-box !important; overflow-wrap: break-word !important;\">&nbsp; &nbsp; &nbsp;演出票是进入剧场的唯一凭证，请妥善保管，遗失不补。<br style=\"margin: 0px; padding: 0px; outline: 0px; max-width: 100%; box-sizing: border-box !important; overflow-wrap: break-word !important;\"/>2、该场演出1米以下儿童谢绝入场。<br style=\"margin: 0px; padding: 0px; outline: 0px; max-width: 100%; box-sizing: border-box !important; overflow-wrap: break-word !important;\"/>3、本剧院楼层不互通，建议同行观演人购买同一楼层座位。</span></strong></span></p><p style=\"margin-top: 0px; margin-bottom: 0px; white-space: normal; padding: 0px; outline: 0px; max-width: 100%; clear: both; min-height: 1em; color: rgb(235, 0, 59); font-size: 16px; letter-spacing: 1.5px; widows: 1; vertical-align: inherit; line-height: 2em; font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; box-sizing: border-box !important; overflow-wrap: break-word !important;\"><span style=\"font-size: 20px;\"><strong><span style=\"color: rgb(255, 0, 0); margin: 0px; padding: 0px; outline: 0px; max-width: 100%; box-sizing: border-box !important; overflow-wrap: break-word !important;\">4、由于演出票存在时效性，属于特殊商品，一经售出不退不换。</span></strong></span></p><p style=\"margin-top: 0px; margin-bottom: 0px; white-space: normal; padding: 0px; outline: 0px; max-width: 100%; color: rgb(235, 0, 59); font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 16px; letter-spacing: 1.5px; widows: 1; caret-color: rgb(255, 0, 0); text-indent: 2em; line-height: 3em; box-sizing: border-box !important; overflow-wrap: break-word !important;\"><span style=\"font-size: 20px;\"><strong><span style=\"color: rgb(255, 0, 0); margin: 0px; padding: 0px; outline: 0px; max-width: 100%; box-sizing: border-box !important; overflow-wrap: break-word !important;\">*请观演人务必于售票中心取得纸质票后方可于观众入口处入场。</span></strong></span></p><p style=\"text-align: center;\"><br/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/e712c809-506b-4a2b-a58e-0838fe62cc34.jpg\" title=\"1673499924334051470.jpg\" alt=\"1.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><br/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/91bdf3ec-fba4-4042-8dee-547c0cc842e9.jpg\" title=\"1673499942505006852.jpg\" alt=\"2.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/5ea8eab7-76b7-4f73-9609-f3f814fae552.jpg\" title=\"1673499936120088266.jpg\" alt=\"白夜行.jpg\" style=\"max-width: 864px; text-align: center; white-space: normal;\"/><img src=\"https://cdn.polyt.cn/uploadImg/f4e8a74e-75a3-45e2-b3b8-866518039d1f.jpg\" title=\"1673499950877008084.jpg\" alt=\"3.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/d4be6e9c-633b-4e79-ac45-32cb275b3351.jpg\" title=\"1673499987202079273.jpg\" alt=\"4.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/f841ba4e-2bc2-4a84-9727-70cc172cfa30.jpg\" title=\"1673499993926090287.jpg\" alt=\"5.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/d319009b-9dca-4c76-b46e-dcdbb193bac7.jpg\" title=\"1673500000798026958.jpg\" alt=\"6.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/8acde538-a7f9-449e-a018-9c828b784a92.jpg\" title=\"1673500007640056074.jpg\" alt=\"7.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/ba83b51b-d140-48e8-aebd-1c6e86ac7bb0.jpg\" title=\"1673500014713065661.jpg\" alt=\"8.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/ee984d7d-3d44-4803-9054-991cafd5724f.jpg\" title=\"1673500021060027835.jpg\" alt=\"9.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/8790461a-9e6a-4392-9b3f-c789664aa57d.jpg\" title=\"1673500027805040344.jpg\" alt=\"10.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/84007364-d9ac-4693-9dfb-79759afc6487.jpg\" title=\"1673500035610092944.jpg\" alt=\"11.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/a3076886-d1c7-41c4-a0b3-abe591783a71.jpg\" title=\"1673500042054052512.jpg\" alt=\"12.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/8a7c649f-2b93-4337-90e8-902f25aaacf7.jpg\" title=\"1673500049337015490.jpg\" alt=\"13.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><img src=\"https://cdn.polyt.cn/uploadImg/2854ef9f-ba24-4b41-9192-a33ee50636aa.jpg\" title=\"1673500059225064691.jpg\" alt=\"14.jpg\" style=\"max-width:864px\"/></p><p style=\"text-align: center;\"><br/></p><p style=\"margin-top: 0px; margin-bottom: 0px; white-space: normal; padding: 0px; outline: 0px; max-width: 100%; clear: both; min-height: 1em; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; letter-spacing: 0.544px; background-color: rgb(255, 255, 255); vertical-align: inherit; font-size: 16px; line-height: 2em; text-align: center; box-sizing: border-box !important; overflow-wrap: break-word !important;\"><span style=\"margin: 0px; padding: 0px; outline: 0px; max-width: 100%; letter-spacing: 0.544px; font-size: 15px; box-sizing: border-box !important; overflow-wrap: break-word !important;\">＊演出相关信息均由演出团提供</span></p><p><section style=\"white-space: normal; margin: 0px; padding: 0px; outline: 0px; max-width: 100%; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; letter-spacing: 0.544px; background-color: rgb(255, 255, 255); font-size: 16px; min-height: 1em; line-height: 2em; text-align: center; box-sizing: border-box !important; overflow-wrap: break-word !important;\"><span style=\"margin: 0px; padding: 0px; outline: 0px; max-width: 100%; letter-spacing: 0.544px; font-size: 15px; box-sizing: border-box !important; overflow-wrap: break-word !important;\">具体演出信息以演出当日为准</span></section></p><p style=\"white-space: normal;\"><br/></p><p style=\"margin-top: 7px; margin-right: 24px; margin-bottom: 7px; font-variant-numeric: normal; font-variant-east-asian: normal; white-space: normal; background: none 0% 0% / auto repeat scroll padding-box border-box rgb(255, 255, 255); color: rgb(0, 0, 152); font-family: Arial, Helvetica, sans-serif; font-size: 12px; line-height: 30px; padding: 0px; text-indent: 26px; text-align: center;\"><strong style=\"padding: 0px;\"><span style=\"padding: 0px;\"><span style=\"color: rgb(255, 0, 0); font-family: 微软雅黑; font-size: 24px; letter-spacing: 0px; line-height: 60px; padding: 0px;\"><img src=\"https://cdn.polyt.cn/uploadImg/5b20b92f-0dbb-4d8f-8667-250959687c20.jpg\" title=\"1637893519282073752.jpg\" alt=\"16.jpg\" style=\"max-width: 864px;\"/></span></span></strong></p><p style=\"margin-top: 7px; margin-right: 24px; margin-bottom: 7px; font-variant-numeric: normal; font-variant-east-asian: normal; white-space: normal; background: none 0% 0% / auto repeat scroll padding-box border-box rgb(255, 255, 255); color: rgb(0, 0, 152); font-family: Arial, Helvetica, sans-serif; font-size: 12px; line-height: 30px; padding: 0px; text-indent: 26px; text-align: center;\"><strong style=\"padding: 0px;\"><span style=\"padding: 0px;\"><span style=\"color: rgb(255, 0, 0); font-family: 微软雅黑; font-size: 24px; letter-spacing: 0px; line-height: 60px; padding: 0px;\"><img src=\"https://cdn.polyt.cn/uploadImg/2aeddf91-1ab1-4d65-aa9c-1d2925d373f1.jpg\" title=\"1637893524398040535.jpg\" alt=\"17.jpg\" style=\"max-width: 864px;\"/></span></span></strong></p><p style=\"margin-top: 7px; margin-right: 24px; margin-bottom: 7px; font-variant-numeric: normal; font-variant-east-asian: normal; white-space: normal; background: none 0% 0% / auto repeat scroll padding-box border-box rgb(255, 255, 255); color: rgb(0, 0, 152); font-family: Arial, Helvetica, sans-serif; font-size: 12px; line-height: 30px; padding: 0px; text-indent: 26px; text-align: center;\"><strong style=\"padding: 0px;\"><span style=\"padding: 0px;\"><span style=\"color: rgb(255, 0, 0); font-family: 微软雅黑; font-size: 24px; letter-spacing: 0px; line-height: 60px; padding: 0px;\"><img src=\"https://cdn.polyt.cn/uploadImg/9c662718-9072-4f66-8bc9-89deb26e81b1.jpg\" title=\"1637893529469062903.jpg\" alt=\"18.jpg\" style=\"max-width: 864px;\"/></span></span></strong></p><p style=\"text-align: center;\"><br/></p>",
# 				"productId":"4957400",
# 				"productImg":"https://cdn.polyt.cn/uploadImg/77457b3a-d71c-4d59-9c6e-b4ddaf8eb37e.webp",
# 				"productLabel":null,
# 				"productNameShort":"韩雪、刘令飞主演——音乐剧《白夜行》（无锡站2023）",
# 				"productShowTime":"2023.04.05-2023.06.10",
# 				"productSource":"POLY",
# 				"projectId":"812335767057178624",
# 				"recommendLabel":null,
# 				"showDesc":null,
# 				"showLasts":"",
# 				"subCategoryName":"音乐剧",
# 				"theaterId":1130,
# 				"ticketAgent":false,
# 				"tour":false,
# 				"tourId":null,
# 				"tourSubTitle":null,
# 				"verticalPictureUrl":"https://cdn.polyt.cn/uploadImg/77457b3a-d71c-4d59-9c6e-b4ddaf8eb37e.webp",
# 				"video":null,
# 				"videoImg":null
# 			}
# 		],
# 		"searchCount":true,
# 		"size":20,
# 		"total":1
# 	},
# 	"errors":null,
# 	"ext":{},
# 	"state":"SUCCESS",
# 	"success":true
# }

# [{'address': '无锡市滨湖区大剧院路1号',
#   'cdnPath': None,
#   'checkMode': '0',
#   'childCode': '此场演出1米以下儿童谢绝入场',
#   'cityId': '0042019200000000215',
#   'cityName': '无锡市',
#   'cultureCouponIds': None,
#   'express': None,
#   'footage': '',
#   'happenTime': 1686310200000,
#   'hasMemberDiscount': True,
#   'invoiceNotice': '凭订单信息至前台登记开具',
#   'memberDiscount': [{'applyTime': 1671605520000,
#                       'discount': 80.0,
#                       'distription': '八折会员80折',
#                       'endTime': 1686313800000,
#                       'levelRankId': '10140000000000058'},
#                      {'applyTime': 1671605520000,
#                       'discount': 70.0,
#                       'distription': '七折会员70折',
#                       'endTime': 1686313800000,
#                       'levelRankId': '10140000000000061'},
#                      {'applyTime': 1671605520000,
#                       'discount': 60.0,
#                       'distription': '六折会员60折',
#                       'endTime': 1686313800000,
#                       'levelRankId': '10140000000000064'},
#                      {'applyTime': 1671605520000,
#                       'discount': 50.0,
#                       'distription': '五折会员50折',
#                       'endTime': 1686313800000,
#                       'levelRankId': '11140000000000066'},
#                      {'applyTime': 1671605520000,
#                       'discount': 100.0,
#                       'distription': '普通会员100折',
#                       'endTime': 1686313800000,
#                       'levelRankId': '18140000000000022'}],
#   'pickUp': None,
#   'pickUpType': '01,02',
#   'placeCname': '无锡大剧院',
#   'placeId': 97,
#   'platShelfStatus': '02',
#   'realNamePricePricelevel': 'A,B,C,D,E,F,G,H,J,K,M,N',
#   'saleBeginTime': 1673582280000,
#   'saleBeginTimeStr': '2023.01.13 星期五 11:58',
#   'saleEndTime': 1686313800000,
#   'score': 1,
#   'sectionId': '8029600',
#   'sectionNum': 1,
#   'shelfStatus': '02',
#   'showId': 8033900,
#   'showNameLabel': None,
#   'showNotices': [{'noticeRemarks': '演出票一经售出，恕不退换。',
#                    'noticeTitle': '退/换票说明',
#                    'number': 2},
#                   {'noticeRemarks': '单场次限购6张票',
#                    'noticeTitle': '限购说明',
#                    'number': 3},
#                   {'noticeRemarks': '此场演出1米以下儿童谢绝入场',
#                    'noticeTitle': '儿童入场说明',
#                    'number': 4},
#                   {'noticeRemarks': '为避免快递配送不能及时送达，演出开场前5天不提供【快递配送】服务，请您谅解；您可以选择在线支付后上门自取纸质票',
#                    'noticeTitle': '配送说明',
#                    'number': 5},
#                   {'noticeRemarks': '以现场为准',
#                    'noticeTitle': '入场时间',
#                    'number': 6},
#                   {'noticeRemarks': '以现场为准',
#                    'noticeTitle': '演出时长',
#                    'number': 7},
#                   {'noticeRemarks': '部分银行支付可能有一定限额，请提前检查银行卡的限额，或可充值至电子钱包进行支付',
#                    'noticeTitle': '支付限额',
#                    'number': 9},
#                   {'noticeRemarks': '凭订单信息至前台登记开具',
#                    'noticeTitle': '发票说明',
#                    'number': 10},
#                   {'noticeRemarks': '购票下单成功后需在15分钟内完成支付，未支付成功的订单，将在下单15分钟后系统自动取消，所选座位将自动释放后重新点亮，大家可及时刷新购票页面进行购买。',
#                    'noticeTitle': '支付时效提醒',
#                    'number': 11}],
#   'showRestriction': 6,
#   'showStatusName': '售票中',
#   'showTime': '2023.06.09 星期五 19:30',
#   'site': 1,
#   'status': '05',
#   'theaterId': '1130',
#   'thirdShowSetting': None,
#   'ticketPriceList': [{'actuallyPrice': 1080.0,
#                        'applyTime': 1671605520000,
#                        'basisPrice': 1080.0,
#                        'discount': 100.0,
#                        'endTime': 1686313800000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 1080.0,
#                        'priceId': 424539,
#                        'priceWay': '',
#                        'reservedCount': 177,
#                        'saleclassId': 983856,
#                        'saleclassLevelId': 3722953,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 1080.0},
#                       {'actuallyPrice': 880.0,
#                        'applyTime': 1671605520000,
#                        'basisPrice': 880.0,
#                        'discount': 100.0,
#                        'endTime': 1686313800000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 880.0,
#                        'priceId': 424540,
#                        'priceWay': '',
#                        'reservedCount': 108,
#                        'saleclassId': 983856,
#                        'saleclassLevelId': 3722954,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 880.0},
#                       {'actuallyPrice': 680.0,
#                        'applyTime': 1671605520000,
#                        'basisPrice': 680.0,
#                        'discount': 100.0,
#                        'endTime': 1686313800000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 680.0,
#                        'priceId': 424541,
#                        'priceWay': '',
#                        'reservedCount': 185,
#                        'saleclassId': 983856,
#                        'saleclassLevelId': 3722955,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 680.0},
#                       {'actuallyPrice': 480.0,
#                        'applyTime': 1671605520000,
#                        'basisPrice': 480.0,
#                        'discount': 100.0,
#                        'endTime': 1686313800000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 480.0,
#                        'priceId': 424542,
#                        'priceWay': '',
#                        'reservedCount': 101,
#                        'saleclassId': 983856,
#                        'saleclassLevelId': 3722956,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 480.0},
#                       {'actuallyPrice': 280.0,
#                        'applyTime': 1671605520000,
#                        'basisPrice': 280.0,
#                        'discount': 100.0,
#                        'endTime': 1686313800000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 280.0,
#                        'priceId': 424543,
#                        'priceWay': '',
#                        'reservedCount': 0,
#                        'saleclassId': 983856,
#                        'saleclassLevelId': 3722957,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 280.0},
#                       {'actuallyPrice': 180.0,
#                        'applyTime': 1671605520000,
#                        'basisPrice': 180.0,
#                        'discount': 100.0,
#                        'endTime': 1686313800000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 180.0,
#                        'priceId': 424544,
#                        'priceWay': '',
#                        'reservedCount': 0,
#                        'saleclassId': 983856,
#                        'saleclassLevelId': 3722958,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 180.0}],
#   'userAvailableCount': 6,
#   'userRegType': '1',
#   'venueId': 161,
#   'venueName': '无锡大剧院歌剧厅'},
#  {'address': '无锡市滨湖区大剧院路1号',
#   'cdnPath': None,
#   'checkMode': '0',
#   'childCode': '此场演出1米以下儿童谢绝入场',
#   'cityId': '0042019200000000215',
#   'cityName': '无锡市',
#   'cultureCouponIds': None,
#   'express': None,
#   'footage': '',
#   'happenTime': 1686396600000,
#   'hasMemberDiscount': True,
#   'invoiceNotice': '凭订单信息至前台登记开具',
#   'memberDiscount': [{'applyTime': 1673345638000,
#                       'discount': 80.0,
#                       'distription': '八折会员80折',
#                       'endTime': 1686407400000,
#                       'levelRankId': '10140000000000058'},
#                      {'applyTime': 1673345638000,
#                       'discount': 70.0,
#                       'distription': '七折会员70折',
#                       'endTime': 1686407400000,
#                       'levelRankId': '10140000000000061'},
#                      {'applyTime': 1673345638000,
#                       'discount': 60.0,
#                       'distription': '六折会员60折',
#                       'endTime': 1686407400000,
#                       'levelRankId': '10140000000000064'},
#                      {'applyTime': 1673345638000,
#                       'discount': 50.0,
#                       'distription': '五折会员50折',
#                       'endTime': 1686407400000,
#                       'levelRankId': '11140000000000066'},
#                      {'applyTime': 1673345638000,
#                       'discount': 100.0,
#                       'distription': '普通会员100折',
#                       'endTime': 1686407400000,
#                       'levelRankId': '18140000000000022'}],
#   'pickUp': None,
#   'pickUpType': '01,02',
#   'placeCname': '无锡大剧院',
#   'placeId': 97,
#   'platShelfStatus': '02',
#   'realNamePricePricelevel': 'A,B,C,D,E,F,G,H,J,K,M,N',
#   'saleBeginTime': 1673582280000,
#   'saleBeginTimeStr': '2023.01.13 星期五 11:58',
#   'saleEndTime': 1686400200000,
#   'score': 1,
#   'sectionId': '8140300',
#   'sectionNum': 1,
#   'shelfStatus': '02',
#   'showId': 8144500,
#   'showNameLabel': None,
#   'showNotices': [{'noticeRemarks': '演出票一经售出，恕不退换。',
#                    'noticeTitle': '退/换票说明',
#                    'number': 2},
#                   {'noticeRemarks': '单场次限购6张票',
#                    'noticeTitle': '限购说明',
#                    'number': 3},
#                   {'noticeRemarks': '此场演出1米以下儿童谢绝入场',
#                    'noticeTitle': '儿童入场说明',
#                    'number': 4},
#                   {'noticeRemarks': '为避免快递配送不能及时送达，演出开场前5天不提供【快递配送】服务，请您谅解；您可以选择在线支付后上门自取纸质票',
#                    'noticeTitle': '配送说明',
#                    'number': 5},
#                   {'noticeRemarks': '以现场为准',
#                    'noticeTitle': '入场时间',
#                    'number': 6},
#                   {'noticeRemarks': '以现场为准',
#                    'noticeTitle': '演出时长',
#                    'number': 7},
#                   {'noticeRemarks': '部分银行支付可能有一定限额，请提前检查银行卡的限额，或可充值至电子钱包进行支付',
#                    'noticeTitle': '支付限额',
#                    'number': 9},
#                   {'noticeRemarks': '凭订单信息至前台登记开具',
#                    'noticeTitle': '发票说明',
#                    'number': 10},
#                   {'noticeRemarks': '购票下单成功后需在15分钟内完成支付，未支付成功的订单，将在下单15分钟后系统自动取消，所选座位将自动释放后重新点亮，大家可及时刷新购票页面进行购买。',
#                    'noticeTitle': '支付时效提醒',
#                    'number': 11}],
#   'showRestriction': 6,
#   'showStatusName': '售票中',
#   'showTime': '2023.06.10 星期六 19:30',
#   'site': 1,
#   'status': '05',
#   'theaterId': '1130',
#   'thirdShowSetting': None,
#   'ticketPriceList': [{'actuallyPrice': 1080.0,
#                        'applyTime': 1673345638000,
#                        'basisPrice': 1080.0,
#                        'discount': 100.0,
#                        'endTime': 1686407400000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 1080.0,
#                        'priceId': 430695,
#                        'priceWay': '',
#                        'reservedCount': 138,
#                        'saleclassId': 999968,
#                        'saleclassLevelId': 3780978,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 1080.0},
#                       {'actuallyPrice': 880.0,
#                        'applyTime': 1673345638000,
#                        'basisPrice': 880.0,
#                        'discount': 100.0,
#                        'endTime': 1686407400000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 880.0,
#                        'priceId': 430696,
#                        'priceWay': '',
#                        'reservedCount': 86,
#                        'saleclassId': 999968,
#                        'saleclassLevelId': 3780979,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 880.0},
#                       {'actuallyPrice': 680.0,
#                        'applyTime': 1673345638000,
#                        'basisPrice': 680.0,
#                        'discount': 100.0,
#                        'endTime': 1686407400000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 680.0,
#                        'priceId': 430697,
#                        'priceWay': '',
#                        'reservedCount': 147,
#                        'saleclassId': 999968,
#                        'saleclassLevelId': 3780980,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 680.0},
#                       {'actuallyPrice': 480.0,
#                        'applyTime': 1673345638000,
#                        'basisPrice': 480.0,
#                        'discount': 100.0,
#                        'endTime': 1686407400000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 480.0,
#                        'priceId': 430698,
#                        'priceWay': '',
#                        'reservedCount': 81,
#                        'saleclassId': 999968,
#                        'saleclassLevelId': 3780981,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 480.0},
#                       {'actuallyPrice': 280.0,
#                        'applyTime': 1673345638000,
#                        'basisPrice': 280.0,
#                        'discount': 100.0,
#                        'endTime': 1686407400000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 280.0,
#                        'priceId': 430699,
#                        'priceWay': '',
#                        'reservedCount': 0,
#                        'saleclassId': 999968,
#                        'saleclassLevelId': 3780982,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 280.0},
#                       {'actuallyPrice': 180.0,
#                        'applyTime': 1673345638000,
#                        'basisPrice': 180.0,
#                        'discount': 100.0,
#                        'endTime': 1686407400000,
#                        'giftAmount': 0,
#                        'giveAwayTicket': '',
#                        'isShowSign': None,
#                        'lackRecord': False,
#                        'policyType': '01',
#                        'price': 180.0,
#                        'priceId': 430700,
#                        'priceWay': '',
#                        'reservedCount': 0,
#                        'saleclassId': 999968,
#                        'saleclassLevelId': 3780983,
#                        'sign': None,
#                        'ticketCount': 1,
#                        'totalPrices': 180.0}],
#   'userAvailableCount': 6,
#   'userRegType': '1',
#   'venueId': 161,
#   'venueName': '无锡大剧院歌剧厅'}]

import requests
from pprint import pprint
import urllib.parse
import time
import json
import re

url = "https://m.polyt.cn/platform-backend/good/search-products-data"
search_url = "https://m.polyt.cn/platform-backend/good/search-lenovo/"
check_url = "https://m.polyt.cn/platform-backend/good/shows/"
section_url = "https://m.polyt.cn/platform-backend/good/show/section/"
available_url = "https://m.polyt.cn/platform-backend/good/seats/"
price_url = "https://m.polyt.cn/platform-backend/good/show/price/"
lock_url = "https://m.polyt.cn/platform-backend/order/lock-seat-choose"
order_url = "https://m.polyt.cn/platform-backend/order/order"
viewers_url = "https://m.polyt.cn/platform-backend/member/viewers"
discount_url = "https://m.polyt.cn/platform-backend/order/discount-amt"
cookie = ""
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 Edg/112.0.1722.34',
    'Referer': 'https://m.polyt.cn/',
    'Authorization': '',
    'Content-Type': 'application/json',
    'Channel': 'plat_h5',
    'Connection': 'keep-alive',
    'Cookie': cookie
}

def aplyt_auto(keyword, city = '无锡'):
    session = requests.session()
    session.headers.update(headers)
    # 基于输入的关键字进行粗略查找，同时这也可以测试网络情况，如果网络不通则退出，后续可以加入循环进行多次重试
    try:
        get_productName = session.get(search_url + urllib.parse.quote(keyword))
    except Exception as e:
        pprint(e)
        exit()
    #pprint(get_productName.status_code)
    #pprint(get_productName.json())
    if get_productName.json()['success']:
        get_productId = session.post(url, json = {'keyword': keyword})
        #pprint(get_productId.json())
        if get_productId.json()['success']:
            #print(get_productId.json())
            product_records = get_productId.json()['data']['records']
            #productId = get_productId.json()['data']['records'][0]['productId']
            #pprint(product_records)
            for record in product_records:
                if city in record['cityName']:
                    productId = record['productId']
                    print(productId)
                    break
            if productId:
                # 此处可以获得场次时间，座位价格等
                get_productDetail = session.get(check_url + productId)
                #pprint(get_productDetail.json()['data']['showInfoDetailList'])
                # 基于产品号查找节点号 sectionId，此节点号将用于获取可选座位信息，考虑到演出的场次不同，需要增加一个选择参数，即选择哪个时间点的场次进行操作，演出时间由 showTime 输出，所有场次信息保存在
                # ['data']['showTimes'] 中，时间戳需要除以1000，场次显示格式 2023.06.09 星期五 19:30，需要注意，有些场次并不是单纯的时间显示，showTime 对应 showInfoDetailList 中的 happenTime
                # 优先进行场次选择，后续再进行价格选择
                DetailList = get_productDetail.json()['data']['showInfoDetailList']
                pprint(dict(zip(range(len(DetailList)), [j['showTime'] for j in DetailList])))
                DetailIndex = int(input('请输入演出编号：')) # 需要考虑用户输入的编号是否超出范围
                showId = str(DetailList[DetailIndex]['showId'])
                sectionId = DetailList[DetailIndex]['sectionId']
                price_dict = dict(zip([str(int(price['price'])) for price in DetailList[DetailIndex]['ticketPriceList'] if price['reservedCount'] != 0], [str(priceId['priceId']) for priceId in DetailList[DetailIndex]['ticketPriceList'] ])) # 建立价位和价格id的索引关系
                get_section = session.get(section_url + showId).json()
                get_seatsUrl = get_section['data']['showSectionDtos'][0]['webCdnPath']
                # categoryId = get_section['data']['categoryId']
                get_seatsInfo = json.loads(re.findall(r"jsonpCallback\((.*?)\)", session.get(get_seatsUrl).text)[0])['data'] # 座位信息列表，配合下面的可选座位列表进行选择
                seats_status = session.get(available_url + productId + '/' + showId + '/' + sectionId + '/' + 'available').json()['data'] # 可选座位列表，可选的值为1
                # 基于上述所获取的可选座位信息，建立索引关系
                seats_available = []
                for index in range(len(seats_status)):
                    if seats_status[index] == 1:
                        seats_available.append(get_seatsInfo[index])
                seats_dict = {}
                for item in seats_available:  # 遍历列表，基于价格id建立对应座位的座位id字典，字典中的key为价格id，value为座位id列表
                    if str(item['p']) not in seats_dict:
                        seats_dict[str(item['p'])] = [str(item['sid'])]
                    else:
                        seats_dict[str(item['p'])].append(str(item['sid']))
                price_list = [key for key in price_dict.keys()]
                while 1:
                    price_sel = input(f"在如下价格中选择你需要的价位{price_list}：")
                    if price_sel in price_list:
                        break
                    else:
                        print(f"找不到价格为{price_sel}的票，请重试！")
                # 基于用户所选的价位选择对应的座位id列表，一般情况下列表数值越小，座位越好，一般取前面几个作为候选
                price_id = price_dict[price_sel]
                # 需要注意所选的价格是否还有座位，如果没有，则不能选择
                seatId_selList = [str(i) for i in seats_dict[price_id][0:3]]
                lock_seats = session.post(lock_url, json={'productId': productId, 'showId': showId, 'sectionId': sectionId, 'seatList': seatId_selList}).json()
                uuid = lock_seats['data']
                # 获取折扣信息，此为必选项，必须将所选座位的uuid提交至系统才能在后续订单提交的过程中获得响应
                get_discount = session.post(discount_url, json = {'uuid': uuid})
                # discountAmt = get_discount.json()['data']['discountAmt']
                # 获取所有观演人对应的身份信息id，这个主要用于实名制
                get_id = session.get(viewers_url).json()['data']
                viewerIdList = [ viewer['id'] for viewer in get_id ]
                name = "邹峰"
                phone_number = "13915303588"
                # make_explain = session.post("https://m.polyt.cn/platform-backend/member/integral/explain", json = {'actuallyPrice': int(discountAmt), 'showId': showId})
                submit_order = session.post(order_url, json = {"deliveryWay": "01", "uuid": uuid, "viewerIdList": viewerIdList, "consignee": name, "consigneePhone": phone_number}).json()
                if submit_order['success']:
                    print("订单已提交，请及时支付以免失效！")
                else:
                    print("失败")
                    print(submit_order)
                # url = section_url + showId, 获取到选择地址保存在['data']['showSectionDtos']['webCdnPath'] 中，地址类似于 https://cdn.polyt.cn/seats/POLY/80255/1678154150651/all_web.json
                # 获取到的单个座位信息：{"b":"","d":"1楼A区1排17座","i":8,"k":0,"n":"","p":424539,"sid":232839437,"t":1,"x":31,"y":7} {"b":"","d":"1楼A区1排32座","i":32,"k":0,"n":"","p":424540,"sid":232839461,"t":1,"x":57,"y":7} {"b":"","d":"1楼A区19排6座","i":677,"k":0,"n":"","p":424541,"sid":232840106,"t":1,"x":42,"y":26}
                # 座位信息中 p 所显示的id 即为 priceId，可以增加一个价位字典，自动购买指定价格范围内的票，亦或是首次执行时先指定价位和场次，然后再执行循环操作
                # 可选座位的信息报错在 https://m.polyt.cn/platform-backend/good/seats/4957400/8033900/8029600/available 地址中，productId 为 4957400，sectionId 为 8029600，showId 为 8033900，
                # pprint(session.get("https://m.polyt.cn/platform-backend/good/seats/4957400/8033900/8029600/available").json())
                # 选座请求地址 https://m.polyt.cn/platform-backend/order/lock-seat-choose post中需要携带 {"productId": "4957400", "seatList": ["232839437"],"sectionId": 8029600,"showId": 8033900 } seatList中所包含的是座位的 sid，可多选，响应信息中的data需要记录
                # https://m.polyt.cn/platform-backend/order/advance/8a7a2575-0fa0-4ec1-b638-9e2ff9fa1975 8a7a2575-0fa0-4ec1-b638-9e2ff9fa1975 对应的就是上述的 data
                # 订单请求 post 中需要携带 { "deliveryWay": "01", "uuid": "6e479227-cd7e-4950-88f4-9f035d6b517c", "viewerIdList": [ "1645636805202669569" ], "consignee": "邹峰", "consigneePhone": "13358153869"}，
                # 请求地址 https://m.polyt.cn/platform-backend/order/order ，consignee 和 consigneePhone 必填，手动指定接受人和手机号即可，viewerIdList 中的id 在https://m.polyt.cn/platform-backend/member/viewers
                # 请求['data']获得，建议身份证号进行筛选，基于credentialsCode，获得用户的id
                # 手动添加观演用户使用如下地址 https://m.polyt.cn/platform-backend/member/viewer，post {"credentialsCode": "320281199705143779", "cardTypeEnum": "ID_CERT","name": "张亮", "id": "", "top": 0}，
                # 删除观演人使用 DELETE https://m.polyt.cn/platform-backend/member/view/1646433646266707970, 对应观演人id即可
                # 按照格式添加即可
                # { 
                #     "code":"200",
                #     "data":{
                #         "categoryId":"1099120000000000004",
                #         "certificateMaxCountLimit":1,
                #         "cityCode":"320200",
                #         "cityName":"无锡市",
                #         "exchangePoints":null,
                #         "invoiceNotice":"凭订单信息至前台登记开具",
                #         "isGiftCard":false,
                #         "maxViewerNum":1,
                #         "minViewerNum":1,
                #         "myPickUpTypeList":null,
                #         "payWallet":true,
                #         "pickUpType":"01,02",
                #         "placeName":"无锡大剧院",
                #         "productId":"4957400",
                #         "productImg":"https://cdn.polyt.cn/uploadImg/77457b3a-d71c-4d59-9c6e-b4ddaf8eb37e.webp",
                #         "productName":"韩雪、刘令飞主演——音乐剧《白夜行》（无锡站2023）",
                #         "productSourceEnum":"POLY",
                #         "realNameEnum":"TICKET_ONE_CARD",
                #         "realNamePricePricelevel":"A,B,C,D,E,F,G,H,J,K,M,N",
                #         "seat":true,
                #         "seatInfoList":[
                #             {
                #                 "num":1,
                #                 "price":"1080.0",
                #                 "pricelevel":"A",
                #                 "seatName":"歌剧厅1楼A区1排17座"
                #             }
                #         ],
                #         "showBefore":5,
                #         "showId":8033900,
                #         "showNameLabel":null,
                #         "showTime":"2023-06-09 星期五 19:30",
                #         "theaterId":"1130",
                #         "thirdCouponId":null
                #     },
                #     "errors":null,
                #     "ext":{},
                #     "state":"SUCCESS",
                #     "success":true
                # }
                # 订单提交地址 https://m.polyt.cn/platform-backend/order/order post信息 {"deliveryWay": "01","uuid": "8a7a2575-0fa0-4ec1-b638-9e2ff9fa1975", "viewerIdList": ["1645636805202669569"],"consignee": "邹峰","consigneePhone": "13358153869"} 其中 uuid 对应 data viewerIdList 中对应观演人id，可通过https://m.polyt.cn/platform-backend/member/viewers
                # 获得
    else:
        print(get_productName.json()['errors'])


if __name__ == '__main__':
    # 关键字
    keyword = '阿波罗'
    city = '厦门'
    # 基于输入的关键字进行粗略查找
    aplyt_auto(keyword)
    
    
    
