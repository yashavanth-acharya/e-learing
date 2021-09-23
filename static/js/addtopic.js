
let tables=$('#example').DataTable({"processing": true,"pageLength": 10,ajax: 'gettopic',});





$("#addtopic").click(function () {


$("#addtopic").attr("disabled",true)
$("#addtopic").html('<i class="fa fa-spinner fa-spin"></i> Loading...')
$("#errormsg1").empty()

let name=$("#name").val()
let descriptions=$("#descriptions").val()
let mq=$("#mq").val()
let passingmark=$("#passingmark").val()
let duration=$("#duration").val()
let coursename=$("#coursename").val()


let icon=$('#image')[0].files;
let error1=0,error2=0,error3=0,error4=0,error5=0,error6=0,error7=0;

if(coursename.length==0)
{

    $("#coursename-error").html("Course name is required *")
    $("#coursename").addClass("errorborder")
    $("#coursename-error").addClass("errorlable")
    error7=1

}else{

    $("#coursename-error").html(" ")
    $("#coursename").removeClass("errorborder")
    $("#coursename-error").removeClass("errorlable")
    error7=0

}


if(name.length==0)
{

    $("#topicname-error").html("Topic name is required *")
    $("#name").addClass("errorborder")
    $("#name-error").addClass("errorlable")
    error1=1

}else{

    $("#topicname-error").html(" ")
    $("#name").removeClass("errorborder")
    $("#name-error").removeClass("errorlable")
    error1=0

}


if(mq.length==0){

    $("#topicmq-error").html("Topic name is required *")
    $("#mq").addClass("errorborder")
    $("#mq-error").addClass("errorlable")
    error4=1

}else{

    $("#topicmq-error").html(" ")
    $("#mq").removeClass("errorborder")
    $("#mq-error").removeClass("errorlable")
    error4=0

}
    
if(passingmark.length==0)
{

    $("#topicpassingmark-error").html("Passing making is required *")
    $("#passingmark").addClass("errorborder")
    $("#passingmark-error").addClass("errorlable")
    error5=1

}else{

    $("#topicpassingmark-error").html(" ")
    $("#passingmark").removeClass("errorborder")
    $("#passingmark-error").removeClass("errorlable")
    error5=0

}

if(duration.length==0)
{

    $("#topicduration-error").html("Durations is required *")
    $("#duration").addClass("errorborder")
    $("#duration-error").addClass("errorlable")
    error6=1

}else{

    $("#topicduration-error").html(" ")
    $("#duration").removeClass("errorborder")
    $("#duration-error").removeClass("errorlable")
    error6=0

}


if(descriptions.length==0){

$("#course-description-error").html("Topic descriptions is required *")
$("#descriptions").addClass("errorborder")
$("#descriptions-error").addClass("errorlable")
error2=1

}else{

$("#topic-description-error").html(" ")
$("#descriptions").removeClass("errorborder")
$("#descriptions-error").removeClass("errorlable")
error2=0

}
if(icon.length==0){
    $("#iconerror").html("Course icon is required *")
    $("#imageUploaded").addClass("errorborder")
    $("#icon-error").addClass("errorlable")
    error3=1
    }else{

        let fileExtension = ['jpeg', 'jpg', 'png', 'gif'];
        if ($.inArray(String(icon[0].name).split('.').pop().toLowerCase(), fileExtension) == -1) {
            $("#iconerror").html("<p style='color:red'>Only formats are allowed : "+fileExtension.join(', ')+"*</p>");
        }
        else{
            if(icon[0].size>1083743){
                $("#iconerror").html("Image size should be less than 1MB*")
                $("#imageUploaded").addClass("errorborder")
                $("#icon-error").addClass("errorlable")
                error3=1
            }else{
                $("#iconerror").html(" ")
                $("#imageUploaded").removeClass("errorborder")
                $("#icon-error").removeClass("errorlable")
                error3=0
            }
            
        }
                
    }

if(error1==0 && error2==0 && error3==0 && error4==0 && error5==0 && error6==0,error7==0){
    data={
        "course":coursename,
        "name":name,
        "descriptions":descriptions,
        "icons":localStorage.getItem("topicicons"),
        "duration":duration,
        "marks_for_pre_question":mq,
        "minimum_mark":passingmark
    }

    $.ajax({
        method: "POST",
        url:"addtopic",
        data:data,
        success: function(data){
            if(data.error==0){
                echo=`<div class="alert alert-success alert-dismissible fade show" role="alert">
                    <strong>Done</strong> `+data.msg+`.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>`
                  localStorage.removeItem("topicicons")
                  tables.ajax.reload();
                  $('#modal1').modal('toggle');
                  $("form").trigger('reset');
                  $("#msg").append(echo)
            }else{
                echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                    <strong>Done</strong> `+data.msg+`.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>`
                  $("#errormsg1").append(echo)

            }
            
            $("#addtopic").attr("disabled",false)
            $("#addtopic").html('Add')
           

        },
        error: function(message){
            echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                <strong>Done</strong> `+data.msg+`.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>`
              $("#errormsg1").append(echo)
              $("#addtopic").attr("disabled",false)
              $("#addtopic").html('Add')
        }
    })
}
 })
