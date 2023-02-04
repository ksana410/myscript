function smzdm_checkin() {
    var checkin_url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin';
    var status_url = 'https://zhiyou.smzdm.com/user/info/jsonp_get_current';
    var token = ''; // pushplustoken
    var pushUrl = 'http://www.pushplus.plus/send';
    var cookie = ''; // smzdm cookie
    var d = new Date();
    let rd = '';
    for(let i=0;i<20;i++) {
      rd += Math.floor(Math.random()*10);
    };
    var params = { 
      'headers': {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        'Accept': "*\/*",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9,zh-TW;q=0.8",
        'Referer': "https://www.smzdm.com/",
        'cookie': cookie,
      },
      'method': "get"    
    };
    var status = JSON.parse(UrlFetchApp.fetch(status_url + '?' + encodeURIComponent({
      'callback': 'jQuery' + rd + '_' + d.getTime(),
      '_': d.getTime()
    }), params));
    if (status['checkin']['has_checkin']) {
      var checkin_num = parseInt(status['checkin']['daily_checkin_num']);
      var check_status = '已由其它客户端签到！'
    } else {
      var checkin_status = JSON.parse(UrlFetchApp.fetch(checkin_url + '?' + encodeURIComponent({
        'callback': 'jQuery' + rd + '_' + d.getTime(),
        '_': d.getTime()
      }), params));
      var checkin_num = checkin_status['data']['checkin_num']
      var check_status = '自动签到成功！'
    };
    var data = {
      'token': token,
      'title': '什么值得买签到',
      'content': {
        '签到情况：': check_status,
        '签到次数：': checkin_num,
        '签到账户：': status['nickname'],
        '执行时间：': Utilities.formatDate(new Date(), "GMT+8", "yyyy-MM-dd HH:mm:ss")
      },
      'template': 'json'
    };
    UrlFetchApp.fetch(pushUrl, {
      'method': 'post',
      'contentType': 'application/json; charset=UTF-8',
      'payload': JSON.stringify(data)
    })
  }