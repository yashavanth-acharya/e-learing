
localStorage.removeItem("edittopicicon")
function editcourse(id){
    $.ajax({
        url:"edittopic",
        method:"GET",
        data:{"topicid":id},
        success:function(data){
            if(data.error==0){
              
               $("#editname").val(data.data.topicname)
                $("#editdescriptions").val(data.data.topic_description)
                $("#editmq").val(data.data.marks_for_pre_question)
                $("#editpassingmark").val(data.data.minimum_mark)
                $("#editduration").val(data.data.duration)
                $("#editcoursename").val(data.data.coursename)
              if(data.data.icon){
                localStorage.setItem("edittopicicon",data.data.icon)
              }
            }
        }
    })
} 




$("#updatetopic").click(function () {

    $("#updatetopic").attr("disabled",true)
    $("#updatetopic").html('<i class="fa fa-spinner fa-spin"></i> Loading...')
    $("#errormsg2").empty()
    let name=$("#editname").val()
    let descriptions=$("#editdescriptions").val()
    let mq=$("#editmq").val()
    let passingmark=$("#editpassingmark").val()
    let duration=$("#editduration").val()
    let coursename=$("#editcoursename").val()
    
    
    let icon=$('#editimage')[0].files;
    let error1=0,error2=0,error3=0,error4=0,error5=0,error6=0,error7=0;
    
    if(coursename.length==0)
    {
    
        $("#editcoursename-error").html("Course name is required *")
        $("#editcoursename").addClass("errorborder")
        $("#editcoursename-error").addClass("errorlable")
        error7=1
    
    }else{
    
        $("#editcoursename-error").html(" ")
        $("#editcoursename").removeClass("errorborder")
        $("#editcoursename-error").removeClass("errorlable")
        error7=0
    
    }
    
    
    if(name.length==0)
    {
    
        $("#edittopicname-error").html("Topic name is required *")
        $("#editname").addClass("errorborder")
        $("#editname-error").addClass("errorlable")
        error1=1
    
    }else{
    
        $("#edittopicname-error").html(" ")
        $("#editname").removeClass("errorborder")
        $("#editname-error").removeClass("errorlable")
        error1=0
    
    }
    
    
    if(mq.length==0){
    
        $("#edittopicmq-error").html("Topic name is required *")
        $("#editmq").addClass("errorborder")
        $("#editmq-error").addClass("errorlable")
        error4=1
    
    }else{
    
        $("#edittopicmq-error").html(" ")
        $("#editmq").removeClass("errorborder")
        $("#editmq-error").removeClass("errorlable")
        error4=0
    
    }
        
    if(passingmark.length==0)
    {
    
        $("#edittopicpassingmark-error").html("Passing making is required *")
        $("#editpassingmark").addClass("errorborder")
        $("#editpassingmark-error").addClass("errorlable")
        error5=1
    
    }else{
    
        $("#edittopicpassingmark-error").html(" ")
        $("#editpassingmark").removeClass("errorborder")
        $("#editpassingmark-error").removeClass("errorlable")
        error5=0
    
    }
    
    if(duration.length==0)
    {
    
        $("#edittopicduration-error").html("Durations is required *")
        $("#editduration").addClass("errorborder")
        $("#editduration-error").addClass("errorlable")
        error6=1
    
    }else{
    
        $("#edittopicduration-error").html(" ")
        $("#editduration").removeClass("errorborder")
        $("#editduration-error").removeClass("errorlable")
        error6=0
    
    }
    
    
    if(descriptions.length==0){
    
    $("#editcourse-description-error").html("Topic descriptions is required *")
    $("#editdescriptions").addClass("errorborder")
    $("#editdescriptions-error").addClass("errorlable")
    error2=1
    
    }else{
    
    $("#edittopic-description-error").html(" ")
    $("#editdescriptions").removeClass("errorborder")
    $("#editdescriptions-error").removeClass("errorlable")
    error2=0
    
    }
    
    
    if(icon.length!=0)
        {
            let fileExtension = ['jpeg', 'jpg', 'png', 'gif'];
            if ($.inArray(String(icon[0].name).split('.').pop().toLowerCase(), fileExtension) == -1) {
                $("#editiconerror").html("<p style='color:red'>Only formats are allowed : "+fileExtension.join(', ')+"*</p>");
                error3=1
            }
            else{
                if(icon[0].size>1083743){
                    $("#editiconerror").html("Image size should be less than 1MB*")
                    $("#editimageUploaded").addClass("errorborder")
                    $("#editicon-error").addClass("errorlable")
                    error3=1
                }else{
                    $("#editiconerror").html(" ")
                    $("#editimageUploaded").removeClass("errorborder")
                    $("#editicon-error").removeClass("errorlable")
                    error3=0
                }
                
            }
            iconimage=localStorage.getItem("edittopicicon")        
        }else{
            iconimage=localStorage.getItem("edittopicicon")
        }
    
    if(error1==0 && error2==0 && error3==0 && error4==0 && error5==0 && error6==0,error7==0){
        data={
            "course":coursename,
            "name":name,
            "descriptions":descriptions,
            "icons":iconimage,
            "duration":duration,
            "marks_for_pre_question":mq,
            "minimum_mark":passingmark
        }

        $.ajax({
            method:"POST",
            url:"edittopic",
            data:data,
            success: function(data){
                if(data.error==0){
                    echo=`<div class="alert alert-success alert-dismissible fade show" role="alert">
                        <strong>Done</strong> `+data.msg+`.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                      </div>`
                      tables.ajax.reload();
                      $('#modal2').modal('toggle');
                      $("form").trigger('reset');
                      $("#msg").append(echo)
                }else{
                    echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                        <strong>Done</strong> `+data.msg+`.
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                      </div>`
                      $("#errormsg2").append(echo)
                }
                $("#updatetopic").attr("disabled",false)
                $("#updatetopic").html('Update')
            },
            error: function(message){
                echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                    <strong>Done</strong> `+data.msg+`.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>`
                  $("#errormsg1").append(echo)
                  $("#updatetopic").attr("disabled",false)
                $("#updatetopic").html('Update')
            }
        })
    }
     })
    


     