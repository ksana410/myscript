/*
需要先在 google 表格中新建一个表格文件，在 A1 处填入获取到的 refresh_token 值，如果有多个账号，则依次向下填写即可

Index.html 模版文件基本结构如下：

<!DOCTYPE html>
<html>
  <head>
    <base target="_top">
  </head>
  <body>
    <ol>
      <? for (var [title, info] of Object.entries(data)) { ?>
        <li><?= title ?></li>
          <ul>
            <? for (var [key, value] of Object.entries(info)) { ?>
              <li><?= key + ":" + value ?></li>
            <? } ?>
          </ul>
      <? } ?>
    </ol>
  </body>
</html>
之后在扩展程序——Apps脚本，写入如下代码：
*/

const accesssTokenURL = "https://auth.aliyundrive.com/v2/account/token";
const siginURL = "https://member.aliyundrive.com/v1/activity/sign_in_list";

function aliyunCheckin() {
    // 从 google 表格中获取 refresh_token 列表
    var sheet = SpreadsheetApp.getActiveSheet();
    var range = sheet.getRange(1,1,sheet.getLastRow()).getValues();
    var refreshTokenList = range.map(function(i) {return i[0];});
    var message = {};
    for (var index in refreshTokenList) {
      try {
        var queryBody = {
          'grant_type': 'refresh_token',
          'refresh_token': refreshTokenList[index]
        };
        // 使用 refresh_token 获取 access_token
        var accessRep = UrlFetchApp.fetch(accesssTokenURL, {
          'method': 'POST',
          'contentType': 'application/json; charset=UTF-8',
          'payload': JSON.stringify(queryBody)
        });
        var accessToken = JSON.parse(accessRep).access_token;
        var nickName = JSON.parse(accessRep).nick_name;
        // 签到
        try {
          var checkRep = UrlFetchApp.fetch(siginURL, {
            'method': 'POST',
            'contentType': 'application/json; charset=UTF-8',
            'payload': JSON.stringify(queryBody),
            'headers': {
              'Authorization': 'Bearer '+ accessToken
            }
          });
          var {signInLogs, signInCount} = JSON.parse(checkRep).result;
          var signInArray = signInLogs.filter(function(day) {
            return day.status === 'normal';
          }); //获取当月签到的记录
          var currentSignIn = signInArray[signInCount - 1];
          if (currentSignIn.isReward) {
            var signInReward = currentSignIn.reward.name + currentSignIn.reward.description;
          } else {
            var signInReward = '空气'
          };
          message['账号： ' + nickName] = {
            '本月已签到': signInCount,
            '签到奖励': signInReward
          };
        } catch(e) {
          message['账号： ' + nickName] = {
            '签到失败，错误信息': e
          };
          break;
        };
      } catch(e) {
        message['账号编号： ' + String(index + 1)] = {
          '获取 access_token 失败，错误信息': e
        };
        break;
      };
    };
    // 将签到的信息发送至邮箱
    var email = Session.getActiveUser().getEmail();
    var htmlTemplate = HtmlService.createTemplateFromFile('Index');
    htmlTemplate.data = message;
    var htmlBody = htmlTemplate.evaluate().getContent();
    var subject = '阿里云盘签到——' +  Utilities.formatDate(new Date(), "GMT+8", "yyyy-MM-dd")
    GmailApp.sendEmail(email, subject, '', {
      htmlBody: htmlBody
    })
  }
