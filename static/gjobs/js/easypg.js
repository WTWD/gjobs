$(document).ready(function (){
  $('#send_ajax').click(function (){
     var params=$('input').serialize(); //序列化表单的值
     $.ajax({
       url:'/gjobs/testjson', //后台处理程序
       type:'post',         //数据发送方式
       dataType:'json',     //接受数据格式
       data:params,         //要传递的数据
       success:update_page //回传函数(这里是函数名)
     });
   });

//$.post()方式：
$('#test_post').click(function (){
    $.post(
      '/gjobs/testjson',
      {
        username:$('#input1').val(),
        age:$('#input2').val(),
        sex:$('#input3').val(),
        job:$('#input4').val()
      },
      function (data) //回传函数
      {
        var myjson='';
        eval('myjson=' + data + ';');
        $('#result').html("姓名:" + myjson.username + "<br/>工作:" + myjson['job']);
      }
    );
   });

//$.get()方式：
$('#test_get').click(function (){
    $.get(
      '/gjobs/testjson',
      {
        username:$("#input1").val(),
        age:$("#input2").val(),
        sex:$("#input3").val(),
        job:$("#input4").val()
      },
      function(data) //回传函数
      {
        var myjson='';
        eval("myjson=" + data + ";");
        alert(myjson.username)
        // $("#result").html(data);
        $("#result").html(myjson.job);
      }
    );
});
});

function update_page (json) //回传函数实体，参数为XMLhttpRequest.responseText
{
    var str="姓名:"+json.username+"<br />";
    str+="年龄:"+json.age+"<br />";
    str+="性别:"+json.sex+"<br />";
    str+="工作:"+json.job+"<br />";
    str+="追加测试:"+json.append;
    $("#result").html(str);
}
