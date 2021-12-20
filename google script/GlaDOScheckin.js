function glaSign() {
    var cookies = '用户获取到的cookie'; //可通过浏览器采集
    var checkinUrl = 'https://glados.rocks/api/user/checkin';
    var token = 'pushplus token'; //自己获取
    var pushUrl = 'http://www.pushplus.plus/send';
    var signData = {
      'token': 'glados_network'  
    }
    var options = {
      'method': 'post',
      'contentType': 'application/json; charset=UTF-8',
      'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37',
        'cookie': cookies,
      },
      'payload': JSON.stringify(signData)
    }
    var res = UrlFetchApp.fetch(checkinUrl, options);
    var obj = JSON.parse(res)
    if (obj['code'] == 0) {
      var status = '成功'
    } else {
      var status = '失败'
    }
    var data = {
      'token': token,
      'title': 'GlaDOS 签到',
      'content': {
        '签到情况：': status,
        '签到次数：': obj['list'].length,
        '剩余天数：': parseInt(obj['list'][0]['balance'])
      },
      'template': 'json'
    }
    UrlFetchApp.fetch(pushUrl, {
      'method': 'post',
      'contentType': 'application/json; charset=UTF-8',
      'payload': JSON.stringify(data)
    })
}