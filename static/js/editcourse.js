
function editcourse(id){
    $("#editname").val("Loading....")
    $("#editdescriptions").val("Loading....")
    $.ajax({
        url:"editcourse",
        method:"GET",
        data:{"couserid":id},
        success:function(data){
            if(data.error==0){
              $("#editname").val(data.data.coursename)
              $("#editdescriptions").val(data.data.course_description)
              if(data.data.icon){
                localStorage.setItem("editcourseicon",data.data.icon)
              }

            }
        }
    })
} 




$("#updatecourse").click(function () {

$("#updatecourse").attr("disabled",true)
$("#updatecourse").html('<i class="fa fa-spinner fa-spin"></i> Loading...')

$("#errormsg2").empty()
$("#msg").empty()
let name=$("#editname").val()
let descriptions=$("#editdescriptions").val()
let icon=$('#editimage')[0].files;
let error1=0,error2=0,error3=0

if(name.length==0){
$("#editcoursename-error").html("Course name is required *")
$("#editname").addClass("errorborder")
$("#editname-error").addClass("errorlable")
error1=1
}else{
$("#editcoursename-error").html(" ")
$("#editname").removeClass("errorborder")
$("#editname-error").removeClass("errorlable")
error1=0
}

if(descriptions.length==0){
$("#editcourse-description-error").html("Course descriptions is required *")
$("#editdescriptions").addClass("errorborder")
$("#editdescriptions-error").addClass("errorlable")
error2=1
}else{
    $("#editcourse-description-error").html(" ")
    $("#editdescriptions").removeClass("errorborder")
    $("#editdescriptions-error").removeClass("errorlable")
    error2=0
}



if(icon.length!=0){

let fileExtension = ['jpeg', 'jpg', 'png', 'gif'];
if ($.inArray(String(icon[0].name).split('.').pop().toLowerCase(), fileExtension) == -1) {
    $("#editiconerror").html("<p style='color:red'>Only formats are allowed : "+fileExtension.join(', ')+"*</p>");
    error3=1
}
else
{
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

    iconimage=localStorage.getItem("editcourseicon");
}
}
}else{
    iconimage=localStorage.getItem("editcourseicon");
}
 



if(error1==0 && error2==0 && error3==0){
   
    $.ajax({
        method: "POST",
        url:"editcourse",
        data:{"name":name,"descriptions":descriptions,"icons":iconimage},
        success: function(data){
            
            if(data.error==0){
                echo=`<div class="alert alert-success alert-dismissible fade show" role="alert">
                    <strong>Done</strong> `+data.msg+`.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div>`
                  
                  localStorage.removeItem("editcourseicon")
                  $('#example').DataTable().ajax.reload();
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
            
            $("#updatecourse").attr("disabled",false)
                  $("#updatecourse").html('Update')
           

        },
        error: function(message){
            echo=`<div class="alert alert-danger alert-dismissible fade show" role="alert">
                <strong>Done</strong> `+data.msg+`.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>`
              $("#errormsg2").append(echo)
              $("#updatecourse").attr("disabled",false)
                  $("#updatecourse").html('Update')
        }
    })
}
 })
