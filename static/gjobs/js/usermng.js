$(document).ready(function() {
   function addproj(){
        $('.proj-add-bar').click(function (){
            $(".add-box").toggle()
        })

        $('.add-yes').click(function (){
            var newproj_name = $("#add-proj-input").val()
            var username = $(".username").text()
            var yes = confirm(username+"确定要新建工程"+newproj_name+"吗？")
            if (yes == true){
                $.get(    
                    '/gjobs/projmanage',
                    {
                        projname:newproj_name,
                        crtuser:username,
                    },
                    function(data) //回传函数
                    {
                        var myjson='';
                        eval("myjson=" + data + ";");
                        npname = myjson.npname
                        npslug = myjson.npslug
                        // $("#result").html(data);
                        var new_proj = '<a href="/gjobs/user/'+username+'/'+npslug+'"><div class="proj-bar"> <p>'+npname+' </p> </div></a>'
                        $(".proj-list").append(new_proj);
                    }
                );
                $(".add-box").toggle()
            }else{
            }
        })      
    }
    addproj()        
})
