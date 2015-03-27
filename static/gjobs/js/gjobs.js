$(document).ready(function(){
    function ajaxtable(){
        $.ajax({
            url:"/gjobs/jobsjson",
            dataType:"json",
            type:"GET",
            success:function(result,stats,ahx){
                freshtbody(result)
            }
        })
    }

    function ajaxtable(posturl){
        var jsonStr =$form.serialize();
        $.ajax({
            url:posturl,
            type:"post",
            data:jsonStr,
            success:function(result){
                $form.children("input[name='xx']").val(result);
            }
        })
    }

    function freshtbody(result){
        $.each(result,function(jobsid,jobsct){
            var obj = $("tbody>tr#"+jobsid)
            if(obj.length>0){ //attention judge the obj exist by judge obj.length not obj
                freshrow(jobsid,jobsct)
            }else{
                addrow(jobsid,jobsct)
            }
        })
    }

    function freshrow(jobsid,jobsct){
        var existrow = $("#"+jobsid) //find exist jobs then replace rd, this method will avoid blink when ajax fresh
        $.each(jobsct,function(j,n){
            existrow.children("#"+j).find(".il").html(n)
        })
    }

    function addrow(jobsid,jobsct){
        var clonrow = $("#tr-tmplate").clone()
        $.each(jobsct,function(j,n){
            clonrow.children("#"+j).find(".il").html(n)
        })
        clonrow.attr("id",jobsid) //replace id "tr-tmplate" to jobsid
        $("tbody").append(clonrow)
        clonrow.fadeIn("slow")
    }

    function refreshontime(){
        setInterval(function(){
            ajaxtable()
        },1000)   //set interval time 1000ms
    }

    // refreshontime()

    function select(){
        $(".selectall").click(function(){
            $(this).parent().parent().find(":checkbox").prop("checked",true);
        })
        $(".unselect").click(function(){
            $(this).parent().parent().find(":checkbox").prop("checked",false);
        })
        $(".reverse").click(function(){
            $(this).parent().parent().find(":checkbox").each(function(){
                // alert($(this).attr("checked"))
                $(this).prop("checked",!$(this).prop("checked"));
                // $(this).attr("checked",false);
            })
        })
    }
    select()

    // function foldhis(){
    //     $("tbody > tr").click(function(){
    //         $(".fold").hide()
    //         var slug = $(this).attr('id')
    //         var sel_his = $(this).parent().find("."+slug)
    //         sel_his.addClass("fold")
    //         sel_his.show()
    //         // $(this).parent().find("."+slug).toggle()
    //     })
    // }  

    function foldhis(){
        $("tbody > tr >td").not("#select,#Operate").click(function(){
            var slug = $(this).parent().attr('id')
            $(this).parent().parent().find("."+slug).toggle()
        })
    }

    foldhis()

    function delhis(){
        $(".hisdel").click(function(){
        $(this).parent().parent().remove()
        })
    }

    delhis()
    function getckbox(){
        var cklist = []
        $("input:checkbox").each(function(){
            if($(this).prop("checked")==true){
                var ids = $(this).parent().parent().attr("id")
                cklist.push(ids)
            }
        })
        return cklist
    }
    function rmvslt(){
        $("#rmvslt").click(function(){
            var rmvlist = getckbox()
            var yes  = confirm(rmvlist)
            if(yes==true){
                for(i in rmvlist){
                    $("#"+rmvlist[i]).remove()
                }
            }
        })
    }
    rmvslt()   
    $("#addfile").click(function (){ 
    var fileInput = document.getElementById("fileInput");//
    fileInput.click();//
    }); 
 
    function inputFileOnChange(){
        var path = $("#my-file").val()
        $("#catpath").html(path)
    }
})                         
